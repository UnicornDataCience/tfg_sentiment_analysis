import pandas as pd
import unittest

def data_preprocessed_segmented(df, columna):
    '''
    la función data_preprocessed_segmented recibe un dataframe y segmenta los datos por sentimiento
    parámetros:
    - df: conjunto de datos
    retorna:
    - texto_positivo: subgrupo con sentimiento positivo
    - texto_negativo: subgrupo con sentimiento negativo
    - texto_neutral: subgrupo con sentimiento neutral
    '''
    df_positivo = df[df['Sentimiento'] == 'Positivo']
    df_neutral = df[df['Sentimiento'] == 'Neutral']
    df_negativo = df[df['Sentimiento'] == 'Negativo']
    # extraer tokens de la columna texto_token
    texto_positivo = " ".join(str(review) for review in df_positivo[columna].tolist())
    texto_negativo = " ".join(str(review) for review in df_negativo[columna].tolist())
    texto_neutral = " ".join(str(review) for review in df_neutral[columna].tolist())
    return texto_positivo, texto_negativo, texto_neutral

class TestDataPreprocessedSegmented(unittest.TestCase):
    def test_data_preprocessed_segmented(self):
        # Test case 1: Dataframe vacío
        df_empty = pd.DataFrame(columns=['Sentimiento', 'Texto'])
        assert data_preprocessed_segmented(df_empty, 'Texto') == ('', '', '')

        # Test case 2: Solo sentimientos positivos
        df_positive = pd.DataFrame({'Sentimiento': ['Positivo', 'Positivo'],
                                    'Texto': ['Great product', 'Excellent service']})
        assert data_preprocessed_segmented(df_positive, 'Texto') == ('Great product Excellent service', '', '')

        # Test case 3: Solo sentimientos negativos
        df_negative = pd.DataFrame({'Sentimiento': ['Negativo', 'Negativo'],
                                    'Texto': ['Poor quality', 'Bad experience']})
        assert data_preprocessed_segmented(df_negative, 'Texto') == ('', 'Poor quality Bad experience', '')

        # Test case 4: Solo sentimiento neutrales
        df_neutral = pd.DataFrame({'Sentimiento': ['Neutral', 'Neutral'],
                                   'Texto': ['Average performance', 'No opinion']})
        assert data_preprocessed_segmented(df_neutral, 'Texto') == ('', '', 'Average performance No opinion')

        # Test case 5: Sentimientos mezclados
        df_mixed = pd.DataFrame({'Sentimiento': ['Positivo', 'Neutral', 'Negativo'],
                                 'Texto': ['Good job', 'Okay product', 'Terrible service']})
        assert data_preprocessed_segmented(df_mixed, 'Texto') == ('Good job', 'Terrible service', 'Okay product')

        print("Todos los casos de prueba han pasado")

unittest.main()

