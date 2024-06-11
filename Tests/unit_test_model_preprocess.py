from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('spanish'))
def preprocess_text(text):
    '''
    la funcion preprocess_text recibe un texto y realiza las siguientes operaciones:
    - Tokeniza el texto
            - Elimina stopwords
            - Une los tokens filtrados en un solo texto
            parámetros:
            - text: texto a preprocesar
            return:
            - preprocessed_text: texto preprocesado
            '''
            # Tokenización
    tokens = word_tokenize(text)
            # Eliminación de stopwords
    filtered_tokens = [token for token in tokens if token not in stop_words]
            # Unir los tokens filtrados en un solo texto
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text

import unittest

class TestPreprocessText(unittest.TestCase):
    def test_preprocess_text(self):
        text = "Este es un texto de prueba para el preprocesamiento de texto."
        expected_output = "Este texto prueba preprocesamiento texto ."
        
        # Call the function to preprocess the text
        actual_output = preprocess_text(text)
        
        # Check if the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)
        
if __name__ == '__main__':
    unittest.main()
print(preprocess_text(''))