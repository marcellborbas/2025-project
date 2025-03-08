import os
import pandas as pd
import datetime
from collections import OrderedDict

"""
1. minden file-t meg kell nyitni és a tartalmát dataframe-ben kell, hogy megkapjam
2. a dataframe segítségével meg kellene állapítani az oszlopok típusait
3. az oszlopok megléte után generálni kellene egy insert és egy create utasítást, file-ba kiírni ezeket a scripteket
4. a create utasítást le kellene futtatni

"""

# "Speciális változó" - Konstans - Constans -> az értéke nem fog változni
FOLDER_PATH = r"C:\2025-project\data"


def get_data_from_csv(file_path):
    return pd.read_csv(file_path)

def get_files_from_folder():
    return os.listdir(FOLDER_PATH)

def generate_columns_with_data_types(df: pd.DataFrame):
    columns = OrderedDict()
    data_type = None
    dtypes = df.dtypes.to_dict()
    
    for col, dtype in dtypes.items():
        if dtype == 'int64':
            data_type = "int"
        elif dtype == 'float64':
            data_type = "float"
        elif dtype == 'object':
            try:
                pd.to_datetime(df[col], format='%Y-%m-%d', errors="raise")
                data_type = "date"
            except Exception as e:
                # print(df[col].str.len().max())
                data_type = "text"
        else:
            # print(df[col].str.len().max())
            data_type = "text"

        columns[col] = data_type

    return columns
    

def generate_create_script(columns: OrderedDict, table_name: str):
    create_script = f"create table project.{table_name} ("

    cnt = 0
    for col, dtype in columns.items():
        cnt += 1
        create_script += f"{col} {dtype},\n" if len(columns) != cnt else f"{col} {dtype})"

    return create_script


def generate_insert_script(columns: OrderedDict, table_name: str):
    insert_script_begin = f"insert into project.{table_name} ("
    insert_script_values = f" values ("
    final_insert = None

    cnt = 0
    for col in columns:
        cnt += 1
        insert_script_begin += f"{col}, " if len(columns) != cnt else f"{col})"
        insert_script_values += f":{col}, " if len(columns) != cnt else f":{col})"
    
    final_insert = insert_script_begin + insert_script_values

    return final_insert

def write_sql_to_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data)

def run_sql(sql_script: str, csv_data = []):
    from sqlalchemy import create_engine, text

    engine = create_engine('postgresql://postgres:Asdf123456789/@localhost:5432/postgres')

    with engine.connect() as conn:
        conn.execute(text(sql_script), csv_data)
        conn.commit()

def create_tables_flow():
    files = get_files_from_folder()

    for file in files:
        file_path = f"{FOLDER_PATH}\\{file}"
        # file_name = file.replace('.csv', '')
        file_name = file[0:-4]
        # data -> pandas DataFrame -> OOP object
        data = get_data_from_csv(file_path)

        """
            Pandas int64 - Python int
            Pandas float64 - Python float
            Pandas object - Python string
        """

        columns_dt = generate_columns_with_data_types(data)
        create = generate_create_script(columns_dt, file_name)
        insert = generate_insert_script(columns_dt, file_name)

        create_path = rf"C:\2025-project\sql_scripts\create_{file_name}.sql"
        insert_path = rf"C:\2025-project\sql_scripts\insert_{file_name}.sql"

        write_sql_to_file(create_path, create)
        write_sql_to_file(insert_path, insert)

        run_sql(create)


def insert_into_quick():
    files = get_files_from_folder()

    for file in files:
        file_path = f"{FOLDER_PATH}\\{file}"
        # file_name = file.replace('.csv', '')
        file_name = file[0:-4]
        # data -> pandas DataFrame -> OOP object
        data = get_data_from_csv(file_path)
        final_data = data.to_dict(orient="records")

        insert = generate_insert_script(data.columns, file_name)
        
        run_sql(insert, final_data)

if __name__ == '__main__':
    # create_tables_flow()
    insert_into_quick()