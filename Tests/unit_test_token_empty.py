import unittest

class TestTokenEmpty(unittest.TestCase):
    def token_empty(self, text):
        '''
        la función token_empty elimina los tokens vacíos de los tweets
        parámetros:
        -text: texto que contiene los textos de los tweets
        retorna:
        -texto sin tokens vacíos
        '''
        
        text = [word for word in text if word.isalnum()]
        return text

    def test_token_empty(self):
        # Caso de prueba 1: Texto vacío
        text = []
        expected_output = []
        assert self.token_empty(text) == expected_output

        # Caso de prueba 2: Texto con solo tokens vacíos
        text = ['', '', '']
        expected_output = []
        assert self.token_empty(text) == expected_output

        # Caso de prueba 3: Texto con tokens alfanuméricos
        text = ['hello', 'world', '123', 'abc']
        expected_output = ['hello', 'world', '123', 'abc']
        assert self.token_empty(text) == expected_output

        # Caso de prueba 4: Texto con tokens alfanuméricos y vacíos
        text = ['hello', '', 'world', '123', '', 'abc', '']
        expected_output = ['hello', 'world', '123', 'abc']
        assert self.token_empty(text) == expected_output

        # Caso de prueba 5: Texto con caracteres especiales
        text = ['hello', '!', 'world', '@', '123', '#', 'abc', '$']
        expected_output = ['hello', 'world', '123', 'abc']
        assert self.token_empty(text) == expected_output

        print("Todos los casos de prueba han pasado")

unittest.main()
