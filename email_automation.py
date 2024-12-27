import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    from_address = 'marieltrinidad1234@gmail.com'
    password = 'cfnjlmaitvalglcs'

    # Create the email message
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    try:
        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
            print(f"Email sent to {to_address} successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_email('marielanntrinidad16@gmail.com', 'Test Subject', 'This is a test email.')








