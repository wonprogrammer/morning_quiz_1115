from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.


# 1. 회원정보 테스트 코드 및 setUp code
class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username":"testuser",
            "fullname":"tester",
            "email":"test@test.com",
            "password":"1234",
        }
        response = self.client.post(url, user_data)
        self.assertEqual('가입 완료!!', response.json()['message'])

