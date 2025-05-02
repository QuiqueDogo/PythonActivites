import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'Buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'Buen Dia') #primer param - como viene # segundo param, como deberia venir


if __name__ == '__main__':
    unittest.main()