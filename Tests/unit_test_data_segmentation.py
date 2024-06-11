import pandas as pd
import unittest
import re

class TestDataSegmentation(unittest.TestCase):
    # Segmentación de los datos por sentimiento
    def data_segmentation(self, df, columna):
        '''
        la función data_segmentation recibe un dataframe y segmenta los datos por sentimiento
        parámetros:
        - df: conjunto de datos
        retorna:
        - texto_positivo: subgrupo con sentimiento positivo
        - texto_negativo: subgrupo con sentimiento negativo
        - texto_neutral: subgrupo con sentimiento neutral
        '''
        df_positivo = df[df['Sentimiento'] == 'Positivo'] 
        df_negativo = df[df['Sentimiento'] == 'Negativo']
        df_neutral = df[df['Sentimiento'] == 'Neutral']
        texto_positivo = " ".join(str(review) for review in df_positivo[columna])
        texto_negativo = " ".join(str(review) for review in df_negativo[columna])
        texto_neutral = " ".join(str(review) for review in df_neutral[columna])
        return texto_positivo, texto_negativo, texto_neutral

    def test_data_segmentation(self):
        # Test case 1: Dataframe vacío
        df_empty = pd.DataFrame(columns=['Sentimiento', 'Review'])
        assert self.data_segmentation(df_empty, 'Review') == ('', '', '')

        # Test case 2: Solo sentimiento positivo
        df_positive = pd.DataFrame({'Sentimiento': ['Positivo', 'Positivo'],
                                    'Review': ['Great product', 'Excellent service']})
        assert self.data_segmentation(df_positive, 'Review') == ('Great product Excellent service', '', '')

        # Test case 3: Solo sentimiento negativo
        df_negative = pd.DataFrame({'Sentimiento': ['Negativo', 'Negativo'],
                                    'Review': ['Poor quality', 'Bad experience']})
        assert self.data_segmentation(df_negative, 'Review') == ('', 'Poor quality Bad experience', '')

        # Test case 4: Solo sentimiento neutral
        df_neutral = pd.DataFrame({'Sentimiento': ['Neutral', 'Neutral'],
                                   'Review': ['Average performance', 'No opinion']})
        assert self.data_segmentation(df_neutral, 'Review') == ('', '', 'Average performance No opinion')

        # Test case 5: Sentimientos mezclados
        df_mixed = pd.DataFrame({'Sentimiento': ['Positivo', 'Negativo', 'Neutral'],
                                 'Review': ['Great product', 'Poor quality', 'Average performance']})
        assert self.data_segmentation(df_mixed, 'Review') == ('Great product', 'Poor quality', 'Average performance')

        print("Todos los casos de prueba han pasado")

if __name__ == '__main__':
    unittest.main()
