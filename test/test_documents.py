import unittest
import document

class Document_Test(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = document.directories, document.documents

    def test_document_owner(self, test_value = '11-2'):
        ownership = document.document_owner(test_value)
        self.assertNotIn('Ошибка', ownership)

    def test_document_deletion(self, test_value = '5400 028765'):
        self.assertNotIn(test_value, document.doc_delete(test_value))

    def test_document_addition(self, test_type = 'Passport',
                               test_number = '34325,', test_name = "Nemo",
                               test_shelf = '2'):
        new_paper = document.add_document(test_type, test_number, test_name, test_shelf)
        self.assertIn(test_type, new_paper)
        self.assertIn(test_number, new_paper)
        self.assertIn(test_name, new_paper)
        self.assertIn(test_shelf, new_paper)
        self.assertNotIn('Ошибка', new_paper)

    def test_negative_owner(self, test_value = '!@#$%^&*()'):
        ownership = document.document_owner(test_value)
        self.assertIn('Ошибка', ownership)

    def test_negative_deletion(self, test_value = '23489987654'):
        self.assertIn('Ошибка', document.doc_delete(test_value))


