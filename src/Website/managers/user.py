"""
User Mangager.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "11.5.2020" 

from django.contrib.auth.base_user import BaseUserManager
import secrets
import hashlib

def _generateUserID(email):
    """
    Generate userID.
    
    :param email: User email.
    :type email: str

    :return: UserID as string.
    :rtype: str
    """
    
    # compose email an random token
    magicStr = email + secrets.token_hex(32)
    
    # hash the result using sha512
    return hashlib.sha512(magicStr.encode('utf-8')).hexdigest()

class UserManager(BaseUserManager):
    """
    User modele manager.
    """
    def create_user(self, email, password, **args):
        """
        Create new User.
        """
        
        # check if email, password and so on are valid
        if not email:
            raise ValueError('Email is a required field for the user.')
            
        if not password:
            raise ValueError('Pasword must not be empty for the user.')
        
        # Create new user and set password
        user = self.model(email=self.normalize_email(email),
                          userID=_generateUserID(email),
                          **args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **args):
        """
        Create a SuperUser with the given email and password.
        """
        
        # set  admin privilages
        args.setdefault('is_staff', True)
        args.setdefault('is_superuser', True)
        args.setdefault('is_active', True)

        # verify whether values are correct before we call the function to create the user
        if args.get('is_staff') is not True:
           raise ValueError('Superuser must have is_staff=True.')
       
        if args.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **args) 
