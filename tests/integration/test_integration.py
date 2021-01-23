import json
import os
import tempfile
from my_app.main import app, Person, db
import unittest
import variables as var


class PersonTestCase(unittest.TestCase):
    def setUp(self):
        print('\n# RUN SETUP - BEFORE EACH')
        app.config['TESTING'] = True

        var.client = app.test_client()

    @classmethod
    def setUpClass(cls):
        print('\n# RUN SETUPALL - BEFORE ALL')
        Person.query.delete()
        db.session.commit()

    def test_1(self):
        result = var.client.get('/api/person')
        json_data = result.get_json()
        print('#1. GET_EMPTY')
        print(result.status_code)
        print(json_data)
        self.assertEqual(json_data['objects'], [])

    def test_2(self):
        newperson = {'first_name': 'Roberto', 'last_name': 'Santos'}
        headers = {'Content-Type': 'application/json'}

        result = var.client.post('/api/person', data=json.dumps(newperson), headers=headers)
        json_data = result.get_json()
        print('#2. INSERT')
        print(result.status_code)
        print(json_data)
        var.id = json_data['id']
        self.assertEqual(result.status_code, 201)

    def test_3(self):
        endpoint = '/api/person/'+str(var.id)
        result = var.client.get(endpoint)
        json_data = result.get_json()
        print('#3. GET_BY_ID')
        print(result.status_code)
        print(json_data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json_data['id'], var.id)

    def test_4(self):
        endpoint = '/api/person/'+str(var.id)
        newperson = {'first_name': 'Roberto', 'last_name': 'Silva'}
        headers = {'Content-Type': 'application/json'}

        result = var.client.put(endpoint, data=json.dumps(newperson), headers=headers)
        json_data = result.get_json()
        print('#4. EDIT_BY_ID')
        print(result.status_code)
        print(json_data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json_data['last_name'], 'Silva')

    def test_5(self):
        endpoint = '/api/person/'+str(var.id)
        result = var.client.delete(endpoint)
        print('#5. DELETE_BY_ID')
        print(result.status_code)
        self.assertEqual(result.status_code, 204)

    def endTest(self):
        print('\n# RUN TEARDOWN')

    @classmethod
    def tearDownClass(cls):
        cls.endTest(cls)


# python -m unittest discover -s tests/integration
