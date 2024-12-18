# Password Strength Checker

## Objective
The purpose of this project is to create a Python script that evaluates the strength of a password based on predefined security criteria. This tool helps users understand how secure their passwords are and provides feedback to encourage stronger password practices.

### Skills Learned

- Regex (Regular Expressions): Learned to apply regex patterns to validate specific conditions like detecting uppercase letters, numbers, and special characters.
- Python Functions: Gained experience in defining and using reusable functions.
- Conditional Logic: Improved understanding of implementing conditional statements to determine outcomes based on criteria.
- File Handling: Learned to read from files, process file content line by line, and handle file-related errors such as missing files.
- Error Handling: Developed ability to manage exceptions (FileNotFoundError, general exceptions) to ensure robust code execution.
  
### Tools Used

- Python 3.x: The primary programming language used to develop the script.
- Regex Module (re): Utilized to perform pattern matching for password validation.
- Text Files: Used to store and test multiple passwords for analysis.
- Command Line/Terminal: Employed for running the script and displaying password strength results interactively.

## Steps
#### 1. Import the re Module

- Import Python's built-in re module for regex functionality
<div>
<img width="68" alt="image" src="https://github.com/user-attachments/assets/1c0057c1-6a8c-43d4-a60e-d8520bcdef7f">
<div>
  
#### 2. Define the Function to Check Password Strength
- Create a function named **check_password_strength(password)**
<div>
<img width="226" alt="image" src="https://github.com/user-attachments/assets/a7d03c80-59fa-49e0-8a91-b9fb03ba561c">
<div>
  
#### 3. Define Criteria for Password Strength
- Inside the function, define the following criteria:
  - Password length 
  - Presence of uppercase letters (
  - Presence of lowercase letters 
  - Presence of numbers 
  - Presence of special characters
<div>
<img width="483" alt="image" src="https://github.com/user-attachments/assets/785615d6-f775-4627-b6cd-7f082ac5faaf">
<div>
  
#### 4. Count the Number of Criteria Met
- Use the **sum()** function to count the True values for all criteria
<div>
<img width="196" alt="image" src="https://github.com/user-attachments/assets/3224bea5-d585-4bad-9d3f-13fa91f9e35b">
<div>
  
#### 5. Determine Password Strength
- Use conditional statements to classify the password strength:
  - Strong: All 5 criteria are met.
  - Moderate: 3 or 4 criteria are met.
  - Weak: Fewer than 3 criteria are met.
<div>
<img width="176" alt="image" src="https://github.com/user-attachments/assets/22f12488-e78b-4d08-b806-0211c14d84dd">
<div>
  
#### 6. Define the Function to Analyze Passwords
Create a function named **analyze_passwords(file_name)** to process multiple passwords from a file.
<div>
<img width="191" alt="image" src="https://github.com/user-attachments/assets/6fdba2c6-2515-4c95-9fbb-c122525e0b80">
<div>
  
#### 7. Read and Process Passwords from File
Open the specified file, read each password line by line, and remove unnecessary whitespace.
<div>
<img width="506" alt="image" src="https://github.com/user-attachments/assets/44671942-ebb0-444b-ab85-861000818504">
<div>
  
#### 8. Check Password Strength for Each Password and Display Results
Call the **check_password_strength()** function for each password to evaluate its strength.
<div>
<img width="536" alt="image" src="https://github.com/user-attachments/assets/f85f985a-86e4-4a7d-aae5-ba57b32d89e8">
<div>
  
#### 9. Handle Errors
Manage file-related issues like FileNotFoundError and handle other unexpected exceptions.
<div>
<img width="273" alt="image" src="https://github.com/user-attachments/assets/00e54d03-2eae-4321-8a85-916ae3e8c77e">
<div>
  
#### 10. Set the File Name and Call the Function
Specify the file name (e.g., passwords.demo.txt) and call the **analyze_passwords()** function to analyze the passwords.
<div>
<img width="203" alt="image" src="https://github.com/user-attachments/assets/647ac7b8-58b7-468b-836a-f02317c708d9">
<div>
  
#### 11. Test the Script
Run the script to confirm it correctly analyzes passwords and displays expected results.
<div>
<img width="481" alt="image" src="https://github.com/user-attachments/assets/c4a1272f-2cab-46cc-94e3-f6f5ebcb86ad">
<div>











