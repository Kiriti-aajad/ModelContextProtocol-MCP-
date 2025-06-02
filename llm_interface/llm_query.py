import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load env variables if needed (e.g. for local path or others)
load_dotenv()

# Local path to your downloaded model directory
LOCAL_MODEL_PATH = "./models/sqlcoder-7b-2"  # Adjust path to where your model is stored locally

# Load tokenizer and model from local path
tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(LOCAL_MODEL_PATH, torch_dtype=torch.float16)
model.eval()

if torch.cuda.is_available():
    model = model.to("cuda")

def get_counterparty_schema():
    fields = [
        "CTPT_ID", "CounterPartyName", "UniqueID", "CTPT_GUID", "FaxNumber", "BusinessUnit", "LegalTypeFlag", "LT_ID",
        "CPT_ID", "DomicileCountry", "Industry", "IncoporationDate", "BirthDate", "BR_ID", "Confidential_Indicator",
        "AS_ID", "DC_ID", "ControlState", "InProcess", "UserDefinedFields", "WebsiteAddress", "CustomerSince",
        "CBEconomicSectorCode", "BaselEntityType", "MRAScore", "MRARatingGrade", "IsProsprective",
        "CBRBClassificationID", "IsBoardMember", "ExistingRiskRate", "CreatedOn", "CreatedBy", "ModifiedOn",
        "ModifiedBy", "IsAppCreated", "SalesTurnOver", "INC_CountryID", "BU_ID", "PrimaryAliasID", "SecBestRating",
        "LegalName", "ListingStatus", "EfilingStatus", "AuthCapital", "PaidupCapital", "CustomerCategory",
        "DateOfCompanyFetch", "DateOfDirectorsFetch", "DateOfChargesFetch", "Promoters", "ForeignBodiesCorporate",
        "Banks", "IsExposureForeign", "BookingUnit", "CustomerSize", "EnterpriseSector", "InvestmentEquipment",
        "UWSDeviationsSecurityNetWorth", "ExemptQCR", "MarketCap", "RatingFrom", "MonitoringStatus", "Actionable",
        "ReasonForStress", "IncorpInASTAR", "ASTARClassification", "IRACStatus", "Customer_Style", "MCA_Old_Name",
        "MCA_PAN", "MCA_Email_Id", "MCA_Company_Category", "MCA_Company_Sub_Category", "MCA_Industry", "MCA_Sector",
        "MCA_Date_of_Balance_Sheet", "MCA_RoC_Code", "MCA_Number_of_Members", "MCA_Classification", "MCA_last_agm_date",
        "CTPT_XML"
    ]
    return [{
        "table_name": "tblCounterParty",
        "fields": [{"name": field, "type": "TEXT"} for field in fields]
    }]

def build_prompt(schema: list, question: str) -> str:
    prompt = "Given the following database schema:\n"
    for table in schema:
        table_name = table.get("table_name", "UnknownTable")
        fields = table.get("fields", [])
        prompt += f"Table: {table_name}\n"
        for field in fields:
            field_name = field.get("name", "UnknownField")
            field_type = field.get("type", "UnknownType")
            prompt += f"- {field_name} ({field_type})\n"
        prompt += "\n"
    prompt += f"Write an SQL query to answer: {question}\nSQL Query:"
    return prompt

def query_llm_local(prompt: str, max_new_tokens=256) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,  # deterministic output
            pad_token_id=tokenizer.eos_token_id
        )
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Remove prompt from generated text to get only generated SQL query
    return generated[len(prompt):].strip()

def generate_sql_from_question(question: str) -> str:
    schema = get_counterparty_schema()
    prompt = build_prompt(schema, question)
    print("DEBUG PROMPT:\n", prompt)
    sql = query_llm_local(prompt)
    return sql

if __name__ == "__main__":
    question = "Find Name and PAN of all counterparties in Mumbai"
    result = generate_sql_from_question(question)
    print("Generated SQL:\n", result)
