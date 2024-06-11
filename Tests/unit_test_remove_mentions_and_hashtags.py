import unittest
import re

# crear una función que elimine las menciones  y los hastags con regex
def remove_mentions_and_hastags(tweet):
    '''
    la funcion remove_mentions_and_hashtags elimina las menciones y los hastags de los textos de tweets
    parámentros:
    - tweet: texto de un tweet
    retorna:
    - texto de tweet sin menciones y hastags
    '''
    # debe conservar los espacios en blanco que hay delante de la hastag o mención eleminada
    tweet = re.sub(r'@\w+|#\w+', '', tweet)
    return re.sub(r'@\w+|#\w+', '', tweet)

class TestRemoveMentionsAndHashtags(unittest.TestCase):

    def test_remove_mentions_and_hashtags(self):
        # Caso de prueba con una mención y un hashtag
        tweet = "Hola @usuario, este es un tweet de prueba #ejemplo"
        expected_result = "Hola , este es un tweet de prueba "
        self.assertEqual(remove_mentions_and_hastags(tweet), expected_result)

        # Caso de prueba solo con menciones
        tweet = "@usuario1 @usuario2 Esto es un tweet con varias menciones"
        expected_result = "  Esto es un tweet con varias menciones"
        self.assertEqual(remove_mentions_and_hastags(tweet), expected_result)

        # Caso de prueba solo con hashtags
        tweet = "Este tweet tiene varios #hashtags #ejemplo #prueba"
        expected_result = "Este tweet tiene varios   "
        self.assertEqual(remove_mentions_and_hastags(tweet), expected_result)

        # Caso de prueba sin menciones ni hashtags
        tweet = "Este tweet no tiene menciones ni hashtags"
        expected_result = "Este tweet no tiene menciones ni hashtags"
        self.assertEqual(remove_mentions_and_hastags(tweet), expected_result)
    print("Todos los casos de prueba han pasado")
# Esto permite ejecutar los tests si este archivo se ejecuta como script
if __name__ == '__main__':
    unittest.main()
