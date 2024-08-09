import os
import pandas as pd
# import glob

carpeta = 'C:/Users/CHINALCO/Downloads/fatiga'

retirarc = ['Fecha y Hora de Llegada', 'Tipo Evento', 'Sede', 'Flota', 'Compañía',
            'Velocidad (km/h)', 'Referencia', 'Conductor', 'Duración de Evento ']

valor_filtrar = ['SEN-CONDUCTOR - FATIGADO',
                 'SEN-CONDUCTOR - DISTRAÍDO', 'SEN-CONDUCTOR - BOSTEZO']

Orden_columns = ['Fecha', 'Descripción Evento',
                 'Código Externo', 'Placa', 'Hora', 'Ubicación']

archivos = [archivo for archivo in os.listdir(
    carpeta) if archivo.endswith('.xlsx')]

dfs = []

for archivo in archivos:
    ruta_archivo = os.path.join(carpeta, archivo)
    df = pd.read_excel(ruta_archivo, skiprows=2)
    df = df.drop(columns=retirarc, errors='ignore')
    agregarc = df['Fecha y Hora de Suceso'].str.split(expand=True)
    agregarc.columns = ['Fecha', 'Hora']
    df = pd.concat([df, agregarc], axis=1)
    df.drop(columns=['Fecha y Hora de Suceso'], inplace=True)
    df = df[df['Descripción Evento'].isin(valor_filtrar)]
    df = df[Orden_columns]
    df = df.sort_values(by='Hora', ascending=True)
    dfs.append(df)

resultado = pd.concat(dfs, ignore_index=True)

resultado.to_excel(
    'C:/Users/CHINALCO/Downloads/fatiga/fatigas.xlsx', index=False)
