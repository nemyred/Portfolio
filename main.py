import datetime
import os
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
import smtplib

my_email = "ndiwechi1@gmail.com"
password = os.environ.get('PASSWORD')


app = Flask(__name__)

bootstrap = Bootstrap5(app)

current_year = datetime.datetime.now().year


@app.route('/')
def home():
    return render_template('layout.html', year=current_year)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=False)


