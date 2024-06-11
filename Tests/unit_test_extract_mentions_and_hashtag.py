import unittest
import re

class TestExtractMentionsHashtags(unittest.TestCase):
    def extract_mentions_hashtags(self, text):
        # filtrar palabras que comienzan con @
        mentions = re.findall(r'@\w+', text)
        # filtrar palabras que comienzan con #
        hashtags = re.findall(r'#\w+', text)
        return mentions, hashtags

    def test_extract_mentions_hashtags(self):
        # caso de prueba 1
        text = "This is a sample text"
        expected_mentions = []
        expected_hashtags = []
        mentions, hashtags = self.extract_mentions_hashtags(text)
        assert mentions == expected_mentions
        assert hashtags == expected_hashtags
        # caso de prueba 2
        text = "Hello @user1, how are you doing? @user2"
        expected_mentions = ["@user1", "@user2"]
        expected_hashtags = []
        mentions, hashtags = self.extract_mentions_hashtags(text)
        assert mentions == expected_mentions
        assert hashtags == expected_hashtags
        # caso de prueba 3
        text = "I love #programming and #coding"
        expected_mentions = []
        expected_hashtags = ["#programming", "#coding"]
        mentions, hashtags = self.extract_mentions_hashtags(text)
        assert mentions == expected_mentions
        assert hashtags == expected_hashtags
        #caso de prueba 4
        text = "Hey @user3, check out this cool #project"
        expected_mentions = ["@user3"]
        expected_hashtags = ["#project"]
        mentions, hashtags = self.extract_mentions_hashtags(text)
        assert mentions == expected_mentions
        assert hashtags == expected_hashtags
    
    print("Todos los casos de prueba han pasado")

unittest.main()