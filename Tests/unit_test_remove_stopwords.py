# se eliminan las stopwords del texto de los tweets en español
import unittest
import re
import nltk

stopword = nltk.corpus.stopwords.words('spanish')

class RemoveStopwordsTestCase(unittest.TestCase):
    def remove_stopwords(self,text):
        '''
        la función remove_stopwords elimina las stopwords del texto de los tweets
        param:
        -text: texto que contiene los textos de los tweets
        return:
        -texto sin stopwords
        '''
        
        text = [word for word in text if word not in stopword]
        return text

    def test_empty_text(self):
        # caso de prueba para tweet vacío
        text = []
        expected_output = []
        self.assertEqual(self.remove_stopwords(text), expected_output)

    def test_text_with_stopwords(self):
        # Caso de prueba para texto con palabras vacías
        text = ['esto', 'es', 'un', 'texto', 'prueba']
        expected_output = ['texto', 'prueba']
        self.assertEqual(self.remove_stopwords(text), expected_output)

    def test_text_without_stopwords(self):
        # Caso de prueba para texto sin palabras vacías
        text = ['texto', 'prueba']
        expected_output = ['texto', 'prueba']
        self.assertEqual(self.remove_stopwords(text), expected_output)
        
    print("Todos los casos de prueba han pasado")

if __name__ == '__main__':
    unittest.main()
