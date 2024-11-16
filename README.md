# Password Strength Checker

## Objective
The purpose of this project is to create a Python script that evaluates the strength of a password based on predefined security criteria. This tool helps users understand how secure their passwords are and provides feedback to encourage stronger password practices.

### Skills Learned

- Regex (Regular Expressions): Learned to apply regex patterns to validate specific conditions like detecting uppercase letters, numbers, and special characters.
- Python Functions: Gained experience in defining and using reusable functions.
- Conditional Logic: Improved understanding of implementing conditional statements to determine outcomes based on criteria.
- User Input Handling: Practiced collecting user input and providing dynamic feedback.
  
### Tools Used

- Python 3.x: The primary programming language used to develop the script.
- Regex Module (re): Utilized to perform pattern matching for password validation.
- Command Line/Terminal: Used for testing and running the script interactively.

## Steps
#### 1. Import the re Module

- Import Python's built-in re module for regex functionality
<img width="68" alt="image" src="https://github.com/user-attachments/assets/1c0057c1-6a8c-43d4-a60e-d8520bcdef7f">


#### 2. Define the Password Strength Criteria

- Length of at least 8 characters
- At least one uppercase letter.
- At least one lowercase letter.
- At least one numeric digit.
- At least one special character (e.g., **!@#$%^&*()**)
<img width="502" alt="image" src="https://github.com/user-attachments/assets/e69c14df-e678-4c12-8539-c2266b4e06ae">


#### 3. Implement the Validation Logic

- Use the **re.search()** method to detect if a password meets each criterion.
- Create Boolean variables to store results for each condition.

#### 4. Count the Criteria Met

- Use a **sum()** function to count the number of conditions the password satisfies
<img width="191" alt="image" src="https://github.com/user-attachments/assets/0c207258-5d09-48bd-bcec-0c49b67ed71d">


#### 5. Classify Password Strength

- Categorize the password strength as:
  - Strong: Meets all 5 criteria.
  - Moderate: Meets 3 or 4 criteria.
  - Weak: Meets fewer than 3 criteria.
 
#### 6. Collect User Input

- Prompt the user to input a password using the **input()** function.
 
#### 7. Display Results

- Call the **check_password_strength()** function and print the result to the console.

#### 8. Test the Script

- Run the script and test various passwords to ensure correct classification.
