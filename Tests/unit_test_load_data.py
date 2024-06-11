import unittest

class DataLoader(unittest.TestCase):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        '''
        la funcion load_data verifica que el archivo que se va a cargar sea un csv
        retorna:
        - TypeError si el archivo no es un csv
        '''
        # the last 4 letters even on a File path with multiple dots (e.g. data.file.csv)
        if self.file_path[-4:] != ".csv":
            raise TypeError("El fichero no tiene el formato correcto. Debe ser un csv")

def test_load_data():
    # Test case 1: Fichero CSV válido
    file_path = "data.csv"
    try:
        data_loader = DataLoader(file_path)
        data_loader.load_data()
        print("Test case 1 ha pasado")
    except TypeError as e:
        print("Test case 1 ha fallado:", str(e))

    # Test case 2: Formato de fichero invalido
    file_path = "data.txt"
    try:
        data_loader = DataLoader(file_path)
        data_loader.load_data()
        print("Test case 2 ha fallado")
    except TypeError as e:
        expected_error = "El fichero no tiene el formato correcto. Debe ser un csv"
        if str(e) == expected_error:
            print("Test case 2 ha pasado")
        else:
            print("Test case 2 ha fallado:", str(e))

    # Test case 3: El directorio del fichero lleva múltiples puntos
    file_path = "data.file.csv"
    try:
        data_loader = DataLoader(file_path)
        data_loader.load_data()
        print("Test case 3 ha pasado") 
    except TypeError as e:
        print("Test case 3 ha fallado:", str(e))

test_load_data()