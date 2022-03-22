from ast import Try
from curses import newpad
import random
import hashlib
from turtle import goto
import uuid


class PasswordManager:

    def __init__(self):
        '''Initialize'''
        self.password = ''
        self.charactors = '1234567890abcdefghijklmnopqrsvutwxyz!@#$%^&*'

    def create_password(self, range_length):
        '''Create password simple'''
        for i in range(range_length):
            num = random.randint(0, len(self.charactors))
            self.password += self.charactors[num]
        return self.password

    def write_password(self):
        '''Write passowrd in password.txt'''
        with open('password.txt', 'w') as f:
            f.write(self.password)

    def convert_to_hash(self):
        '''Convert password to hash'''
        # Incomplete
        salt = 'abc'
        self.password = hashlib.sha512(self.password.encode(
            'utf-8') + salt.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    pm = PasswordManager()
    password = ''
    while (True):
        try:
            # Get number of charactors
            num = int(input('How many charactors do you want for password: '))
            # Check count of number
            if num < 8:
                raise Exception('Password must be at least 8 charactors')
            # Create password
            password = pm.create_password(num)
            # Write password to file
            pm.write_password()
            break
        except ValueError:
            print('Please enter a number')
            continue
        except Exception as e:
            print(e)
            continue

    print(password)
