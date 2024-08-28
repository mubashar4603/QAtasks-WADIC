import imaplib
import re
# from bs4 import BeautifulSoup
class getLink:
    @staticmethod
    def access_email(username, password):
        # Replace 'imap.example.com' with your IMAP server address
        with imaplib.IMAP4_SSL('imap.gmail.com') as server:
            server.login(username, password)
            server.select('INBOX')

            # Search for emails based on criteria
            key = 'FROM'
            value = 'info@metutors.com'
            server.search(None, key, value)

            # Get the list of email IDs
            response, email_ids = server.search(None, key, value)
            email_ids = email_ids[0].split()
            ids = len(email_ids)
            # print(len(email_ids))
            req = ids-1
            # print(req)

            # Fetch the email data for a specific ID
            email_id = email_ids[req]
            response, email_data = server.fetch(email_id, '(RFC822)')

            # Process the email data
            email_message = email_data[0][1].decode('utf-8')
            # print(email_message)
            otp_pattern = r'\b\d{5}\b'  # Assumes the OTP is a 5-digit number
            match = re.findall(otp_pattern, email_message)
            required_digit = len(match)-1
            print(match[required_digit])


        return match[required_digit]

# access_email(username = 'mubashar4603@gmail.com', password = 'lfst wacj qiwp wclj')