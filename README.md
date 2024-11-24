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

#### 2. Define the Function to Check Password Strength
- Create a function named **check_password_strength(password)**
<img width="226" alt="image" src="https://github.com/user-attachments/assets/a7d03c80-59fa-49e0-8a91-b9fb03ba561c">

#### 3. Define Criteria for Password Strength
- Inside the function, define the following criteria:
  - Password length 
  - Presence of uppercase letters (
  - Presence of lowercase letters 
  - Presence of numbers 
  - Presence of special characters
<img width="483" alt="image" src="https://github.com/user-attachments/assets/785615d6-f775-4627-b6cd-7f082ac5faaf">

#### 4. Count the Number of Criteria Met
- Use the **sum()** function to count the True values for all criteria
<img width="196" alt="image" src="https://github.com/user-attachments/assets/3224bea5-d585-4bad-9d3f-13fa91f9e35b">

#### 5. Determine Password Strength
- Use conditional statements to classify the password strength:
  - Strong: All 5 criteria are met.
  - Moderate: 3 or 4 criteria are met.
  - Weak: Fewer than 3 criteria are met.
<img width="176" alt="image" src="https://github.com/user-attachments/assets/22f12488-e78b-4d08-b806-0211c14d84dd">

#### 6. Get User Input
- Prompt the user to enter a password using the **input()** function:
<img width="360" alt="image" src="https://github.com/user-attachments/assets/86f0f21a-78ff-4622-9b8b-d9f105fdf8a3">

#### 7. Call the Function
- Call the **check_password_strength()** function with the user-provided password
<img width="262" alt="image" src="https://github.com/user-attachments/assets/948389f8-ed92-493c-a058-9b2258be566b">

#### 9. Display Results
- Print the result obtained
<img width="229" alt="image" src="https://github.com/user-attachments/assets/03e3f191-3d04-4539-8599-48d686246515">

#### 10. Test Case Results
- Testing to see if script works and the respective results
<img width="293" alt="image" src="https://github.com/user-attachments/assets/fd55b3c2-2509-4bf1-8893-cd23c3e0f3ae">





