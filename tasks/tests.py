from django.test import TestCase

class TestTasks(TestCase):

    def test_sign_in_get(self):
        response = self.client.get('/tasks/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/login.html')

    def test_sign_in_post(self):
        response = self.client.post('/tasks/', {'username': 'simon', 'password': 'abc123abc123'})
        self.assertInHTML("Error", response)
        self.assertTemplateUsed(response, 'tasks/index.html')

