import unittest

def label_to_labels(label):
    '''
    la funcion label_to_labels recibe una etiqueta y la convierte en un valor numérico según la siguiente relación:
    parámetros:
    - label: etiqueta a convertir
    return:
    - valor numérico de la etiqueta
    '''
    if label == 'NEUTRAL':
        return 2
    elif label == 'FAVOR':
        return 1
    else:
        return 0

class TestLabelToLabels(unittest.TestCase):
    def test_label_to_labels(self):
        label = 'NEUTRAL'
        expected_output = 2
        actual_output = label_to_labels(label)
        self.assertEqual(actual_output, expected_output)
        
        label = 'FAVOR'
        expected_output = 1
        self.assertEqual(label_to_labels(label), expected_output)
        
        label = 'AGAINST'
        expected_output = 0
        self.assertEqual(label_to_labels(label), expected_output)
        
if __name__ == '__main__':
    unittest.main()