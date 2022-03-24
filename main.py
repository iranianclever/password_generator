import random
import hashlib


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
        '''Write password in password.txt'''
        with open('password.txt', 'w') as f:
            # Encode password
            hash = self.encode(self.password)
            # Write password to file
            f.write(hash)

    def encode(self, password):
        '''Convert password to hash'''
        salt = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return salt


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
