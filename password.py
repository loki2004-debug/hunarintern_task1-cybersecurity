Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def password_strength(password):
...     score = 0
...     
...     # Length check
...     if len(password) >= 8:
...         score += 1
...         
...     # Uppercase and lowercase check
...     if re.search("[a-z]", password) and re.search("[A-Z]", password):
...         score += 1
... 
...     
...     # Digit check
...     if re.search("[0-9]", password):
...         score += 1
...     
...     # Special character check
...     if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
...         score += 1
...     
...     # Evaluate strength
...     if score == 1:
...         return "Weak"
...     elif score == 2:
...         return "Moderate"
...     elif score == 3:
...         return "Strong"
...     elif score == 4:
...         return "Very Strong"
...     else:
...         return "Very Weak"
... 
... # Example usage
... password = input("Enter a password: ")
... print(f"Password strength: {password_strength(password)}")
>>> [DEBUG ON]
>>> [DEBUG OFF]
