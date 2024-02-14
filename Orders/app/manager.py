from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
 
    def create_user(self, phonenumber, password=None, **extra_fields):
        if not phonenumber:
            raise ValueError('Phone number is required')
        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phonenumber, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phonenumber, password, **extra_fields)