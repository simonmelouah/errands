from django.test import TestCase, Client

class TestTasks(TestCase):

    def test_sign_in_get(self):
        response = self.client.get('/tasks/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
