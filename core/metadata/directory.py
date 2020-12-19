import os


class PathDataRaw:
    """
    class generated for reading data
    """
    
    data = 'data'
    data_abreviacion = os.path.join(data, 'abreviacion_estados.csv')
    

class PathOutput:
    """
    class generated for output data
    """
    output = 'output'
    
    output_EDA_tables = os.path.join(output, 'tables_EDA')
    output_data_core = os.path.join(output, 'data_core')
    output_map = os.path.join(output, 'maps')
