import pandas as pd

datos = pd.read_csv("accidentalidad.csv")


tabla = "CREATE TABLE if not exists ACCIDENTES(\n"

for column in datos.columns:
    column_name = column.replace(" ", "").replace("/", "").replace("(", "").replace(")", "").replace(":", "_")   
    tabla += column_name + " TEXT,\n"
tabla = tabla[:-2]  
tabla += ");\n"

print(tabla)


insert = "INSERT INTO ACCIDENTES("
for column in datos.columns:
    column_name = column.replace(" ", "").replace("/", "").replace("(", "").replace(")", "").replace(":", "_")     
    insert += column_name + ", "
insert = insert[:-2] 
insert += ") VALUES\n"

for index, row in datos.iterrows():
    insert += "("
    for column in datos.columns:
        insert += "'" + str(row[column]) + "', "
    insert = insert[:-2]  
    insert += "),\n"

insert = insert[:-2]  
insert += ";\n"

print(insert)


with open("sql.sql", "w", encoding="UTF-8") as f:
    f.write(insert)
