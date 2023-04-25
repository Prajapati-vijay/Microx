
from django.contrib.auth.base_user import BaseUserManager


class Usermanager(BaseUserManager):
    use_in_migrations=True


    def create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError("username is required ")

        
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("wrong superuser")

        return self.create_user(username,password,**extra_fields)

