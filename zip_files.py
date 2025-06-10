import pyzipper
import secrets
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def create_zip(files, zip_filename, password):
    with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password)
        for file in files:
            zf.write(file, arcname=file)

def main():
    files_to_zip = ['test_file.csv','test_file_2.csv'] 
    zip_filename = 'zipped_files.zip'
    random_password = generate_password(5)
    password_file = 'zip_passwords.txt'

    with open(password_file, 'w') as f:
        f.write(zip_filename + " " + random_password + '\n')


    print(f"Creating zip file: {zip_filename}")
    # Create the encrypted zip file
    create_zip(files_to_zip, zip_filename, random_password)
    print(f"Created {zip_filename} with AES encryption.")
    

if __name__ == '__main__':
    main()