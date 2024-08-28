import random


class randomGenerate():
#return email after adding random 3 integers on last
    @staticmethod
    def add_random_numbers_to_email(email, num_digits=3):
        # Split the email address into local part and domain
        local_part, domain = email.split('@')
        # Generate random digits
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
        # Add "+1" followed by random digits to the local part and recombine
        new_email = f"{local_part}+{random_digits}@{domain}"
        return new_email
    @staticmethod
    def generate_random_phone_number():
        area_code = 201  # Generate a random 3-digit area code
        prefix = 234  # Generate a random 3-digit prefix
        line_number = random.randint(1000, 9999)  # Generate a random 4-digit line number
        phone_number = f"{area_code}{prefix}{line_number}"  # Format the phone number
        return phone_number

#generate random 5 digit for postal code
    @staticmethod
    def generate_random_postal():
        line_number = random.randint(10000, 99999)  # Generate a random 4-digit line number
        phone_number = f"{line_number}"  # Format the phone number
        return phone_number


