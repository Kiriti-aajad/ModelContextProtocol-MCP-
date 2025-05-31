class ResponseFormatter:
    def __init__(self):
        pass

    def format(self, raw_response):
        """
        Takes raw LLM or engine response and converts it to a structured output.
        For now, it's just a pass-through or simple cleanup.

        You can expand this later to extract SQL queries, table names, or other structured info.
        """
        if isinstance(raw_response, str):
            return {"response": raw_response.strip()}
        elif isinstance(raw_response, dict):
            return raw_response
        else:
            return {"response": str(raw_response)}
