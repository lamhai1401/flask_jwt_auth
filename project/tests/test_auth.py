import unittest
import json
from project.server.app import db
from project.server.models import User
from project.tests.base import BaseTestCase


class TestAuthBlueprint(BaseTestCase):

    def test_registration(self):
        with self.client:
            resp = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    email='joe@gmail.com',
                    password='123456'
                )),
                content_type='application/json'
            )

            print(resp)
            data = json.loads(resp.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 201)


if __name__ == '__main__':
    unittest.main()
