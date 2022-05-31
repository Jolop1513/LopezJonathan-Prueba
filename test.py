import todoapp
import unittest

# Create class for testing


class TesttodoApp(unittest.TestCase):

    # Set up method
    def setUp(self):
        todoapp.app.testing = True
        self.app = todoapp.app.test_client()

    # Test index route
    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    # Test \enviar route
    def test_enviar(self):
        result = self.app.post('/enviar', data=dict(registro_id='1',
                               registro_name='Jonathan Lopez', registro_telephone='0980137673', registro_priority='Normal'))
        self.assertEqual(result.status_code, 302)
