from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
bootstrap = Bootstrap5(app)
my_email = "iqdev7@gmail.com"
my_password = os.environ.get("MAIL_PASSWORD")



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        email_message = f"Subject:Users Contact Info\n\n{name}\n{email}\n{phone}\n{message}"
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="qprioleau7jw@gmail.com",
                                msg=email_message)
        return render_template('index.html')


    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)