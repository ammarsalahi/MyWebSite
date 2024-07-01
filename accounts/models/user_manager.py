from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string


def get_unique_username()->str:
    return format(get_random_string(length=15)) 

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, is_superuser, is_staff, first_name, last_name=None, password=None):
        if not username:
            raise ValueError("username is required!")
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.is_verified=True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        return self.create_user(
            username=username,
            email=email,
            is_superuser=True,
            is_staff=True,
            first_name="",
            last_name="",
            password=password
        )

    def create_staffuser(self, username, email, first_name, last_name, password=None):
        return self.create_user(
            username=username,
            email=email,
            is_superuser=False,
            is_staff=True,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

    def create_publicuser(self, email, first_name, last_name=None, username=None,password=None):
        return self.create_user(
            username= get_unique_username() if username is None else username,
            email=email,
            is_superuser=False,
            is_staff=False,
            first_name=first_name,
            last_name=last_name,
            password=password
        )