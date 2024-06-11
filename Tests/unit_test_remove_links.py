import unittest
import re


class RemoveLinksTestCase(unittest.TestCase):
    def remove_links(self, text):
        '''
        la función remove_links elimina los enlaces web de los tweets
        parámetros:
        -text: texto que contiene los textos de los tweets
        retorna:
        -texto sin enlaces web
        '''
        
        # se eliminan las URL que empiezan por http
        text = re.sub(r'http\S+', '', text)
        # se eliminan las URL que empiezan por www
        text = re.sub(r'www\S+', '', text)
        # se eliminan las URL que empiezan por https
        text = re.sub(r'https\S+', '', text)
        return text

    def test_remove_links(self):
        text_with_links = "Check out this website: https://www.example.com"
        expected_output = "Check out this website: "
        self.assertEqual(self.remove_links(text_with_links), expected_output)

        text_with_multiple_links = "Visit our website at www.example.com or check out our blog at http://blog.example.com"
        expected_output = "Visit our website at  or check out our blog at "
        self.assertEqual(self.remove_links(text_with_multiple_links), expected_output)

        text_without_links = "This is a tweet without any links"
        expected_output = "This is a tweet without any links"
        self.assertEqual(self.remove_links(text_without_links), expected_output)

        text_with_mixed_content = "Check out this website: https://www.example.com and follow us on Twitter @example"
        expected_output = "Check out this website:  and follow us on Twitter @example"
        self.assertEqual(self.remove_links(text_with_mixed_content), expected_output)


if __name__ == '__main__':
    unittest.main()
