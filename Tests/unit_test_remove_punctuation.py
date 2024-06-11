import string
import re
import unittest

class TestRemovePunctuation(unittest.TestCase):
    def remove_punctuation(self, text):
        '''
        la función remove_punctuation elimina los signos de puntuación de un texto y los números
        parámetros:
        -text: texto que contiene los textos de los tweets
        retorna:
        -texto sin signos de puntuación
        '''
        
        # se eliminan los signos de puntuación de cada tweet
        text = "".join([char for char in text if char not in string.punctuation])
        # se eliminan los digitos numéricos de cada tweet
        text = re.sub('[0-9]+', '', text)
        return text

    def test_remove_punctuation(self):
        # Test case 1: Texto con puntuación y números
        text = "Hello, world! 123"
        expected_output = "Hello world "
        self.assertEqual(self.remove_punctuation(text), expected_output)

        # Test case 2: Texto con solo puntuación
        text = "!@#$%^&*()_+"
        expected_output = ""
        self.assertEqual(self.remove_punctuation(text), expected_output)

        # Test case 3: Texto con sólo números
        text = "1234567890"
        expected_output = ""
        self.assertEqual(self.remove_punctuation(text), expected_output)

        # Test case 4: Texto sin puntuaciones o números
        text = "Hello world"
        expected_output = "Hello world"
        self.assertEqual(self.remove_punctuation(text), expected_output)

        # Test case 5: Texto con caractéres mezclados
        text = "Hello, 123 world!"
        expected_output = "Hello  world"
        self.assertEqual(self.remove_punctuation(text), expected_output)

        print("Todos los casos de prueba han pasado")

if __name__ == '__main__':
    unittest.main()
