import random
import hashlib


class PasswordManager:

    def __init__(self):
        '''Initialize'''
        self.password = ''
        self.characters = '1234567890abcdefghijklmnopqrsvutwxyz!@#$%^&*'

    def create_password(self, range_length):
        '''Create password simple'''
        self.password = ''
        for i in range(range_length):
            num = random.randint(0, (len(self.characters) - 1))
            self.password += self.characters[num]
        return self.password

    def write_password(self):
        '''Write password in password.txt'''
        with open('password.txt', 'w') as f:
            # Encode password
            hash = self.convert_to_sha256(self.password)
            # Write password to file
            f.write(hash)

    def convert_to_sha256(self, password):
        '''Convert password to hash'''
        salt = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return salt

    def convert_to_md5(self, password):
        '''Convert password to md5'''
        salt = hashlib.md5(password.encode('utf-8')).hexdigest()
        return salt



if __name__ == '__main__':
    pm = PasswordManager()
    password = ''
    while (True):
        try:
            print('Enter your sign to choose the type of password creation. (n) -> normal password, (m) -> password with md5, (s) -> password with sha256, (e) -> exit.')
            sign = input('What\'s your sign: ')
            if sign == 'n':
                # Get number of characters
                num = int(input('How many characters do you want for password: '))
                # Create password
                password = pm.create_password(num)
                print(password)
            elif sign == 'm':
                # Get number of characters
                num = int(input('How many characters do you want for password: '))
                # Create password
                raw_password = pm.create_password(num)
                # Convert password to md5
                password = pm.convert_to_md5(raw_password)
                print('Raw: ' + raw_password)
                print('Md5: ' + password)
            elif sign == 's':
                # Get number of characters
                num = int(input('How many characters do you want for password: '))
                # Create password
                raw_password = pm.create_password(num)
                # Convert password to sha256
                password = pm.convert_to_sha256(raw_password)
                print('Raw: ' + raw_password)
                print('Sha256: ' + password)
            elif sign == 'e':
                break
            continue
        except ValueError:
            print('Please enter a number')
            continue
        except Exception as e:
            print(e)
            continue

    print('Bye')
