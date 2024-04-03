from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    error_msg = ""

    # NAME
    if 'name' not in request.form or not request.form['name']:
        error_msg = "Name is required "
    else:
        name = request.form['name']

    # EMAIL
    if 'email' not in request.form or not request.form['email']:
        error_msg += "Email is required "
    else:
        email = request.form['email']

    # SUBJECT
    if 'subject' not in request.form or not request.form['subject']:
        error_msg += "Subject is required "
    else:
        subject = request.form['subject']

    # MESSAGE
    if 'message' not in request.form or not request.form['message']:
        error_msg += "Message is required "
    else:
        message = request.form['message']

    email_to = "bibliophilebargain@gmail.com"
    subject_line = "New Message Received"

    # prepare email body text
    body = ""
    body += "Name: " + name + "\n"
    body += "Email: " + email + "\n"
    body += "Subject: " + subject + "\n"
    body += "Message: " + message + "\n"

    # send email
    sender_email = "your_email@example.com"
    receiver_email = email_to
    sender_email(subject_line, body, sender_email, receiver_email)

    # Return success or error message
    if not error_msg:
        return "success"
    else:
        return error_msg
    
if __name__ == '__main__':
    app.run(debug=True)
