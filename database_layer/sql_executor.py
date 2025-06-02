import json
from database_layer.db_connector import connect_to_mssql

def get_table_description(table_name):
    """
    Fetch detailed columns info of the specified table.
    Returns a list of dicts with keys: column_name, data_type, is_nullable, max_length,
    default, numeric_precision, numeric_scale, datetime_precision, is_identity, is_primary_key
    """
    conn = connect_to_mssql()
    if not conn:
        print("No database connection available.")
        return None

    query = """
    SELECT
        c.COLUMN_NAME,
        c.DATA_TYPE,
        c.IS_NULLABLE,
        c.CHARACTER_MAXIMUM_LENGTH,
        c.COLUMN_DEFAULT,
        c.NUMERIC_PRECISION,
        c.NUMERIC_SCALE,
        c.DATETIME_PRECISION,
        c.CHARACTER_OCTET_LENGTH,
        COLUMNPROPERTY(object_id(c.TABLE_SCHEMA + '.' + c.TABLE_NAME), c.COLUMN_NAME, 'IsIdentity') AS IsIdentity,
        CASE WHEN kcu.COLUMN_NAME IS NOT NULL THEN 'YES' ELSE 'NO' END AS IsPrimaryKey
    FROM INFORMATION_SCHEMA.COLUMNS c
    LEFT JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc 
        ON c.TABLE_NAME = tc.TABLE_NAME
        AND tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
    LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
        ON tc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
        AND c.COLUMN_NAME = kcu.COLUMN_NAME
    WHERE c.TABLE_NAME = ?
    ORDER BY c.ORDINAL_POSITION
    """

    try:
        cursor = conn.cursor()
        cursor.execute(query, (table_name,))
        rows = cursor.fetchall()

        description = []
        for row in rows:
            description.append({
                "column_name": row.COLUMN_NAME,
                "data_type": row.DATA_TYPE,
                "is_nullable": row.IS_NULLABLE,
                "max_length": row.CHARACTER_MAXIMUM_LENGTH,
                "default": row.COLUMN_DEFAULT,
                "numeric_precision": row.NUMERIC_PRECISION,
                "numeric_scale": row.NUMERIC_SCALE,
                "datetime_precision": row.DATETIME_PRECISION,
                "char_octet_length": row.CHARACTER_OCTET_LENGTH,
                "is_identity": bool(row.IsIdentity),
                "is_primary_key": row.IsPrimaryKey
            })

        cursor.close()
        conn.close()
        return description

    except Exception as e:
        print(f"Error fetching table description for {table_name}:")
        print(e)
        return None
 



if __name__ == "__main__":
    table_name = "tblCounterParty"  
    description = get_table_description(table_name)
    if description:
        # Save to JSON file
        output_file = f"{table_name}_description.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(description, f, indent=4)
        print(f"Table description saved to {output_file}")
    else:
        print("Failed to fetch table description.")
