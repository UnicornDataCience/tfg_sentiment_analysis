import unittest
import re

class TestRemoveEmoji(unittest.TestCase):
    def remove_emoji(self, text):
        """
        La funcion remove_emoji elimina los emoticonos de un texto.
        Argumentos:
        text: El texto del que se quieren eliminar los emoticonos.
        Retorna:
        El texto sin emoticonos.
        """
        
        emoji_regex = re.compile("["
                                u"\U0001F600-\U0001F64F"  
                                u"\U0001F300-\U0001F5FF"  
                                u"\U0001F680-\U0001F6FF"  
                                u"\U0001F900-\U0001F9FF"  
                                u"\U0001FA00-\U0001FA6F"  
                                u"\U0001FA70-\U0001FAFF"  
                                u"\U0001F000-\U0001F0FF" 
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                "]+", flags=re.UNICODE)
        return emoji_regex.sub('', text)

    def test_remove_emoji(self):
        # Test case 1: No hay emojis en el texto
        text = "This is a test without emojis"
        expected_output = "This is a test without emojis"
        assert self.remove_emoji(text) == expected_output

        # Test case 2: Texto con emojis
        text = "I love ❤️ coding! 😃👍"
        expected_output = "I love  coding! "
        assert self.remove_emoji(text) == expected_output

        # Test case 3: Texto sólo con emojis
        text = "😃👍"
        expected_output = ""
        assert self.remove_emoji(text) == expected_output

        # Test case 4: Texto con emojis y otros caracteres
        text = "I ❤️ coding! 🚀👍 #python"
        expected_output = "I  coding!  #python"
        assert self.remove_emoji(text) == expected_output

        # Test case 5: Texto con emojis y menciones
        text = "I ❤️ coding! 🚀👍 @github"
        expected_output = "I  coding!  @github"
        assert self.remove_emoji(text) == expected_output

        print("All test cases pass")

unittest.main()
