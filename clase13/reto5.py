import pandas as pd

rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split('.')[-1] == 'csv?raw=true': #Si es un archivo csv
        try:
            df = pd.read_csv(rutaFileCsv)
            sub_df = df[['Country','Language', 'Gross Earnings']]
            final_table = sub_df.pivot_table(index=['Country','Language'])
            return final_table.head(10)
        except:
            print("Error al leer el archivo de datos.")
    else:
        print('Extensión inválida.')
    

print(listaPeliculas(rutaFileCsv))