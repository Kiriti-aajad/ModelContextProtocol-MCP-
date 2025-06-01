import os

schema_dir = r"C:\Github\ModelContextProtocol-MCP-\data\Tables"
files = os.listdir(schema_dir)
json_files = [f for f in files if f.endswith('.json')]
print("JSON files found in Tables folder:")
for jf in json_files:
    print(jf)
