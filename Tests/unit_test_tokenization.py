import re
import unittest

class TestTokenization(unittest.TestCase):
    def tokenization(self, text):
        '''
        la función tokenization tokeniza el texto de los tweets
        parámetros:
        -text: texto que contiene los textos de los tweets
        retorna:
        -texto tokenizado
        '''
        
        text = re.split('\W+', text)
        if text == ['']:
            return []
        # si el texto contiene simbolos especiales, se eliminan
        if text != []:
            if text[0] == '':
                text.pop(0)
            if text[-1] == '':
                text.pop(-1)
        return text

    def test_tokenization(self):
        # Caso de prueba 1: Texto vacío
        text = ''
        expected_output = []
        assert self.tokenization(text) == expected_output

        # Caso de prueba 2: Texto con solo una palabra
        text = 'Hello'
        expected_output = ['Hello']
        assert self.tokenization(text) == expected_output

        # Caso de prueba 3: Texto con múltiples palabras
        text = 'Hello, world! This is a test.'
        expected_output = ['Hello', 'world', 'This', 'is', 'a', 'test']
        assert self.tokenization(text) == expected_output

        # Caso de prueba 4: Texto con caracteres especiales
        text = 'Hello, world! @username #hashtag'
        expected_output = ['Hello', 'world', 'username', 'hashtag']
        assert self.tokenization(text) == expected_output

        # Caso de prueba 5: Texto con números
        text = 'I have 10 apples and 5 oranges.'
        expected_output = ['I', 'have', '10', 'apples', 'and', '5', 'oranges']
        assert self.tokenization(text) == expected_output

        print("Todos los casos de prueba han pasado")

# Esto permite ejecutar los tests si este archivo se ejecuta como script
if __name__ == '__main__':
    unittest.main()
