import os


class PathDataRaw:
    
    data = 'data'
    
    data_abreviacion = os.path.join(data, 'abreviacion_estados.csv')
    

class PathOutput:
    
    output = 'output'
    
    output_EDA_tables = os.path.join(output, 'tables_EDA')
    output_map = os.path.join(output, 'maps')
    