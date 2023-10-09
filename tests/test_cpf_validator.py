import unittest
from flask_testing import TestCase
from app.cpf_validator import app, valida_cpf

class TestCPFValidator(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_valida_cpf_valid(self):
        self.assertTrue(valida_cpf('39053344705'))  # Exemplo de CPF válido

    def test_valida_cpf_invalid(self):
        self.assertFalse(valida_cpf('39053344706'))  # Exemplo de CPF inválido

    def test_valida_cpf_non_numeric(self):
        self.assertFalse(valida_cpf('invalid_cpf'))  # Exemplo de CPF não numérico

    def test_valida_cpf_length(self):
        self.assertFalse(valida_cpf('123'))  # Exemplo de CPF com comprimento inválido

    def test_valida_cpf_web_service(self):
        response = self.client.post('/valida_cpf', json={'cpf': '39053344705'})
        self.assert200(response)
        self.assertTrue(response.json['valido'])

if __name__ == '__main__':
    unittest.main()

