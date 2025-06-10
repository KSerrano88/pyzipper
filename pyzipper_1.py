import os
import pyzipper_1
import secrets
import string

def generate_password(length=5):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def create_protected_zip(files, zip_filename, password):
    with pyzipper_1.AESZipFile(zip_filename, 'w', compression=pyzipper_1.ZIP_LZMA, encryption=pyzipper_1.WZ_AES) as zf:
        zf.setpassword(password.encode())
        for file in files:
            zf.write(file, os.path.basename(file))

def main():
    files_to_zip = ['test_file.csv']  # Replace with your files
    zip_filename = 'protected_archive.zip'
    password_file = 'zip_password.txt'

    password = generate_password()
    print(f"Generated password: {password}")
    #create_protected_zip(files_to_zip, zip_filename, password)

    #with open(password_file, 'w') as f:
    #    f.write(password)

    #print(f"Created {zip_filename} with password stored in {password_file}")

if __name__ == '__main__':
    main()