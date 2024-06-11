import re
import string
import nltk
import unittest

class TweetProcessor(unittest.TestCase):
    stopword = ['the', 'and', 'is', 'in', 'to', 'of']

    def process_tweets_texts(self, tweet):
        '''
        la función process_tweets_texts aplica todas las funciones de preprocesado a un texto
        parámetros:
        - tweet: texto de un tweet
        retorna:
        - tweet preprocesado
        '''
        text = re.sub(r'@\w+|#\w+', '', tweet)
        # se eliminan los signos de puntuación de cada tweet
        text = "".join([char for char in text if char not in string.punctuation])
        # se eliminan los digitos numéricos de cada tweet
        text = re.sub('[0-9]+', '', text)
        emojis = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticonos
                                u"\U0001F300-\U0001F5FF"  # símbolos y emoticonos
                                u"\U0001F680-\U0001F6FF"  # emoticonos suplementarios
                                u"\U0001F900-\U0001F9FF"  # emoticonos ideográficos
                                u"\U0001FA00-\U0001FA6F"  # emoticonos de símbolos diversos
                                u"\U0001FA70-\U0001FAFF"  # emoticonos de transporte y objetos
                                u"\U0001F000-\U0001F0FF"  
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                "]+", flags=re.UNICODE)
        text = emojis.sub('', text)
        # se eliminan las URL que empiezan por http
        text = re.sub(r'http\S+', '', text)
        # se eliminan las URL que empiezan por www
        text = re.sub(r'www\S+', '', text)
        # se eliminan las URL que empiezan por https
        text = re.sub(r'https\S+', '', text)
        text = re.split('\W+', text)
        text = [word for word in text if word.isalnum()]
        text = [word for word in text if word not in self.stopword]
        # se invoca la función de lematización de la librería nltk
        WNL = nltk.WordNetLemmatizer()
        # se lematiza el texto de los tweets
        text = [WNL.lemmatize(word) for word in text]
        return text

    def test_process_tweets_texts(self):
        # Test case 1: Tweet básico sin caracteres especiales
        tweet = "This is a test tweet"
        expected_output = ['This', 'a', 'test', 'tweet']
        assert self.process_tweets_texts(tweet) == expected_output

        # Test case 2: Tweet con menciones y hashtags
        tweet = "Hello @user1, check out this #awesome tweet!"
        expected_output = ['Hello', 'check', 'out', 'this', 'tweet']
        assert self.process_tweets_texts(tweet) == expected_output

        # Test case 3: Tweet con emojis
        tweet = "I feel 😊 today!"
        expected_output = ['I', 'feel', 'today']
        assert self.process_tweets_texts(tweet) == expected_output

        # Test case 4: Tweet con URLs
        tweet = "Check out this cool website: https://example.com"
        expected_output = ['Check', 'out', 'this', 'cool', 'website']
        assert self.process_tweets_texts(tweet) == expected_output

        # Test case 5: Tweet vací
        tweet = ""
        expected_output = []
        assert self.process_tweets_texts(tweet) == expected_output

        print("Todos los casos de pruebas han pasado")

unittest.main()