from ..embeddings.vector_store import VectorStore
from ..llm.Client import LLMClient
from .schema_loader import load_schema_snippets

class QueryEngine:
    def __init__(self, faiss_index_path, embedding_dim, snippets_path):
        # Load snippets correctly
        self.snippets = load_schema_snippets(snippets_path)
        
        self.vector_store = VectorStore(
            faiss_index_path=faiss_index_path,
            snippets=self.snippets,
            embedding_dim=embedding_dim
        )
        self.llm = LLMClient()

    def embed_query(self, query):
        from openai import OpenAI
        client = OpenAI(api_key=self.llm.client.api_key)
        response = client.embeddings.create(
            input=query,
            model="text-embedding-3-large"
        )
        return response.data[0].embedding

    def get_relevant_snippets(self, query_embedding, top_k=5):
        indices, distances = self.vector_store.query(query_embedding, top_k=top_k)
        return [self.snippets[i] for i in indices]

    def generate_sql(self, user_query):
        query_embedding = self.embed_query(user_query)
        relevant_snippets = self.get_relevant_snippets(query_embedding)

        prompt = self.build_prompt(user_query, relevant_snippets)
        sql = self.llm.generate(prompt)
        return sql

    def build_prompt(self, user_query, snippets):
        schema_text = "\n\n".join(
            [f"Table: {snip['table_name']}\nColumns: {', '.join(snip['columns'])}" for snip in snippets]
        )
        prompt = (
            f"You are an AI assistant generating SQL queries.\n\nRelevant schema:\n{schema_text}\n\n"
            f"User Query: {user_query}\n\nGenerate SQL query:"
        )
        return prompt
