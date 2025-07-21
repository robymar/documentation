import requests
import smtplib
from email.mime.text import MIMEText

def get_xrp_price():
    """Fetches the current price of XRP in USD from the CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data["ripple"]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching XRP price: {e}")
        return None

def send_email(price):
    """Sends an email with the XRP price."""
    sender_email = "YOUR_EMAIL@example.com"
    receiver_email = "YOUR_EMAIL@example.com"
    password = "YOUR_EMAIL_PASSWORD"  # Or an app-specific password
    smtp_server = "smtp.yourprovider.com"
    smtp_port = 587

    if price is None:
        subject = "Error Fetching XRP Price"
        body = "There was an error fetching the XRP price. Please check the script."
    else:
        subject = f"XRP Price Update: ${price}"
        body = f"The current price of XRP is ${price}."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    xrp_price = get_xrp_price()
    send_email(xrp_price)
