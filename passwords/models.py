from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from password_manager.settings import KEY_PASS

KEY = KEY_PASS

cipher_suite = Fernet(KEY)

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()

    def set_password(self, password):
        self.encrypted_password = cipher_suite.encrypt(password.encode())

    def get_password(self):
        return cipher_suite.decrypt(self.encrypted_password).decode()