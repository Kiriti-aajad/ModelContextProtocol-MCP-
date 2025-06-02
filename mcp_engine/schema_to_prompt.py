import json
from database_layer.schema_loader import load_table_schema

def build_prompt(schema: list, question: str) -> str:
    prompt = "Given the following database schema:\n"
    # We replace dynamic fields with your exact columns for tblCounterParty
    # Assuming the table name is 'tblCounterParty'
    prompt += "Table: tblCounterParty\n"
    columns = [
        "CTPT_ID", "CounterPartyName", "UniqueID", "CTPT_GUID", "FaxNumber", "BusinessUnit", 
        "LegalTypeFlag", "LT_ID", "CPT_ID", "DomicileCountry", "Industry", "IncoporationDate", 
        "BirthDate", "BR_ID", "Confidential_Indicator", "AS_ID", "DC_ID", "ControlState", 
        "InProcess", "UserDefinedFields", "WebsiteAddress", "CustomerSince", "CBEconomicSectorCode", 
        "BaselEntityType", "MRAScore", "MRARatingGrade", "IsProsprective", "CBRBClassificationID", 
        "IsBoardMember", "ExistingRiskRate", "CreatedOn", "CreatedBy", "ModifiedOn", "ModifiedBy", 
        "IsAppCreated", "SalesTurnOver", "INC_CountryID", "BU_ID", "PrimaryAliasID", "SecBestRating", 
        "LegalName", "ListingStatus", "EfilingStatus", "AuthCapital", "PaidupCapital", 
        "CustomerCategory", "DateOfCompanyFetch", "DateOfDirectorsFetch", "DateOfChargesFetch", 
        "Promoters", "ForeignBodiesCorporate", "Banks", "IsExposureForeign", "BookingUnit", 
        "CustomerSize", "EnterpriseSector", "InvestmentEquipment", "UWSDeviationsSecurityNetWorth", 
        "ExemptQCR", "MarketCap", "RatingFrom", "MonitoringStatus", "Actionable", "ReasonForStress", 
        "IncorpInASTAR", "ASTARClassification", "IRACStatus", "Customer_Style", "MCA_Old_Name", 
        "MCA_PAN", "MCA_Email_Id", "MCA_Company_Category", "MCA_Company_Sub_Category", "MCA_Industry", 
        "MCA_Sector", "MCA_Date_of_Balance_Sheet", "MCA_RoC_Code", "MCA_Number_of_Members", 
        "MCA_Classification", "MCA_last_agm_date", "CTPT_XML"
    ]
    # For simplicity, all fields are treated as string type in the prompt
    for col in columns:
        prompt += f"- {col} (string)\n"
    prompt += "\n"
    prompt += f"Write an SQL query to answer: {question}\nSQL Query:"
    return prompt

def generate_sql_from_question(question: str) -> str:
    schema = load_table_schema(json_path=r"C:\Github\ModelContextProtocol-MCP-\tblCounterParty_description.json")
    print("DEBUG SCHEMA:", schema)
    if schema is None:
        raise ValueError("Failed to load database schema.")
    prompt = build_prompt(schema, question)
    print("DEBUG PROMPT:\n", prompt)
    
    def query_llm(prompt: str) -> str:
        # Placeholder: Replace with actual LLM API call
        # For example purpose, just return a sample query matching your question
        return "SELECT CounterPartyName, MCA_PAN FROM tblCounterParty WHERE DomicileCountry = 'India' AND BusinessUnit = 'Mumbai';"

    sql = query_llm(prompt)
    return sql.strip()

if __name__ == "__main__":
    question = "Find Name and PAN of all counterparties in Mumbai"
    result = generate_sql_from_question(question)
    print("Generated SQL:\n", result)
