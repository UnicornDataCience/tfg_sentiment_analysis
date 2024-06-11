import nltk
import unittest

def format_sentence(sent):
    '''
    la funcion format_sentence recibe una oración y la convierte en un diccionario de palabras
    parametros:
    -sent: oración
    retorna:
    -diccionario de palabras tokenizadas
    '''
    return({word: True for word in nltk.word_tokenize(sent)})

class TestFormatSentence(unittest.TestCase):
    def test_format_sentence(self):
        # Test case 1: frase básica
        sentence = "This is a test sentence"
        expected_output = {'This': True, 'is': True, 'a': True, 'test': True, 'sentence': True}
        self.assertEqual(format_sentence(sentence), expected_output)
        
    print("Todos los casos de prueba han pasado")
    
unittest.main()
