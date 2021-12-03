__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020"

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **args):
        # check if email, password are valid
        if not email:
            raise ValueError('Email is a required field for the user.')

        if not password:
            raise ValueError('Pasword must not be empty for the user.')

        user = self.model(email=self.normalize_email(email), **args)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **args):        
        # set admin privilages
        args.setdefault('is_staff', True)
        args.setdefault('is_superuser', True)
        args.setdefault('is_active', True)

        # verify whether values are correct before creating the user
        if args.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if args.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **args) 
