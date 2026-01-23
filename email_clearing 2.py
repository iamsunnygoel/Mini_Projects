import imaplib
import email
from email.header import decode_header

# Your credentials
EMAIL = "sunny.dtu@gmail.com"
PASSWORD = "ymlq hnrf wkbw rqhz"  # Use app password if 2FA enabled
SENDER_EMAIL = "newsletters-noreply@linkedin.com"  # Email ID you want to delete from

# Connect to Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)

# Select the mailbox you want to delete from (use "INBOX")
mail.select("inbox")

# Search for emails from the specific sender
status, messages = mail.search(None, f'FROM "{SENDER_EMAIL}"')

if status == "OK":
    email_ids = messages[0].split()
    print(f"Found {len(email_ids)} emails from {SENDER_EMAIL}")

    for eid in email_ids:
        # Mark email for deletion
        mail.store(eid, "+FLAGS", "\\Deleted")

    # Permanently delete marked emails
    mail.expunge()
    print("Deleted all emails from", SENDER_EMAIL)
else:
    print("Error searching emails.")

# Logout
mail.logout()
