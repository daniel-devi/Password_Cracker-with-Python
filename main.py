'''
Password Cracker
-------------------------------------------------------------
'''

import secrets
import string
import time

# Fuunction to Generate Password
def create_pw(pw_length):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        alphabet = letters + digits + special_chars
        pwd = ''
    
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

            '''
            if (any(char in special_chars for char in pwd) and
                    sum(char in digits for char in pwd) >= 2):
                pw_strong = True
                '''

        return pwd


# Function to Crack Password
def crack_password(password):   
    startTime = time.time()

    tryPassword = create_pw(len(password))
    
    attempts = 1
    totalTime = 0
    filePath = "password.txt"
    
    allGeneratedPassword = ["\n PASSWORD GENERATED: \n", ]
    
    # Open the file in read mode ('r')
    def check_string_in_file(file_path, search_string):
        with open(file_path, 'r') as file:
            for line in file:
                if search_string in line:
                    return True
                
        return False
    
    if check_string_in_file(filePath, password):
        print("Password Succesfuly Cracked")
        print("PASSWORD IS A COMMON PASSWORD")
    else:
        while tryPassword != password:
            attempts+= 1
            tryPassword = create_pw(len(password))
            allGeneratedPassword.append(tryPassword)
            cracking_code = "............\n"
            print(cracking_code)
            time.sleep(2)
    
    
    endTime = time.time()
    totalTime = endTime - startTime

    # Open the file in write mode ('w')
    with open("passwordtried.txt", mode="w") as file:
        file.write("\n".join(allGeneratedPassword))
       
    print(f"Password Succesfuly Cracked\n After {attempts} attempts\n In {totalTime+0.25:.4f}Seconds")

   
    
print("Hello Welcome to my Penetration Test")
print("\nLets Test how strong your Password is")
input("Press an Key to Continue:\n")
password = input("What is your Password: \n")

test =  "Daniekjs" #create_pw(8)

print(crack_password(password))
print(f"Your Password was {password}")