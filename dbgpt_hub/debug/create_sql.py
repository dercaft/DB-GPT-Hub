import os
import json

def generate_sql(db_content):
    for db_entry in db_content:
        db_id = db_entry['db_id']
        tables = db_entry['tables']
        
        # Create directory if it doesn't exist
        if not os.path.exists("database/"+db_id):
            os.makedirs("database/"+db_id)
        
        schema_sql = f"{db_id}/schema.sql"
        
        # Generate schema and data SQL
        with open("database/"+schema_sql, 'w') as schema_file:
            for table_name, table_info in tables.items():
                schema_file.write(f"CREATE TABLE `{table_name}` (\n")
                for i, column in enumerate(table_info['header']):
                    column_name = f"`{column}`"  # Add single quotes to column name
                    column_type = "TEXT"
                    if table_info['type'][i] == 'time':
                        column_type = "TEXT"  # Assuming time will be stored as string
                    elif table_info['type'][i] == 'number':
                        column_type = "INTEGER"  # Assuming number will be stored as integer
                    schema_file.write(f"    {column_name} {column_type}")
                    if i < len(table_info['header']) - 1:
                        schema_file.write(",")
                    schema_file.write("\n")
                schema_file.write(");\n\n")
                
                for row in table_info['cell']:
                    values = ", ".join(f"'{value}'" if isinstance(value, str) else str(value) for value in row)
                    schema_file.write(f"INSERT INTO `{table_name}` VALUES ({values});\n")
                schema_file.write("\n")
                
            print(f"Generated SQL file for {db_id}.")

if __name__ == "__main__":
    os.chdir('../')
    with open('db_content.json', 'r') as file:
        db_content = json.load(file)
    generate_sql(db_content)
