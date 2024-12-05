import re

def check_password_strength(password):
    # Criteria for password strength:
    # 1. Password must be at least 8 characters long
    length_criteria = len(password) >= 8
    
    # 2. Password must contain at least one uppercase letter
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    
    # 3. Password must contain at least one lowercase letter
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    
    # 4. Password must contain at least one number
    number_criteria = bool(re.search(r'[0-9]', password))
    
    # 5. Password must contain at least one special character from the defined set
    special_character_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Count the number of criteria met (this is used to determine password strength)
    criteria_met = sum([  # Summing boolean values; True counts as 1, False as 0
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_character_criteria
    ])
    
    # Determine password strength based on the number of criteria met
    if criteria_met == 5:
        return "Strong"  
    elif 3 <= criteria_met < 5:
        return "Moderate"  
    else:
        return "Weak"  

def analyze_passwords(file_name):
    try:
        # Attempt to open the file containing passwords
        with open(file_name, 'r') as file:
            passwords = file.readlines()  # Read all passwords from the file
        
        # Iterate through the passwords, starting from index 1 for user-friendly numbering
        for index, password in enumerate(passwords, start=1):
            password = password.strip()  # Remove leading/trailing whitespace
            if password:  # Skip empty lines
                strength = check_password_strength(password)  # Get the strength of the current password
                # Print password strength result
                print(f"Password {index}: {password} - Strength: {strength}")
    except FileNotFoundError:
        # Handle case where the file is not found
        print(f"File {file_name} not found.")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {e}")

# Analyze passwords from the file
file_name = "passwords.demo.txt"  
analyze_passwords(file_name)  
