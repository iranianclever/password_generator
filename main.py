from curses import newpad
import random
import hashlib
import uuid


class PasswordManager:

    def __init__():
        '''Initialize'''
        pass

    def create_password(self):
        '''Create password simple'''
        for i in range(22):
            num = random.randint(0, len(self.charactors))
            self.password += self.charactors[num]
        return self.password

    def write_password(self):
        '''Write passowrd in password.txt'''
        with open('password.txt', 'w') as f:
            f.write(self.password)

    def convert_to_hash(self):
        '''Convert password to hash'''
        salt = 'abc'
        self.password = hashlib.sha512(self.password.encode(
            'utf-8') + salt.encode('utf-8')).hexdigest()

    def __init__(self):
        '''Initialize'''
        self.password = ''
        self.charactors = '1234567890abcdefghijklmnopqrsvutwxyz!@#$%^&*'


if __name__ == '__main__':
    pm = PasswordManager()
    gusserNumber = pm.create_password()
    pm.write_password()
    print(gusserNumber)
