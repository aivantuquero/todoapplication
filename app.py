from __future__ import print_function
from mimetypes import init
import string
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import random

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'
otp = 0
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "OTP Code"
sender = {"name":"Pogi si Aivan","email":"login@activity5.com"}
html_content = ""




list = []
isLoggedIn = True

while(True):
    choice = input("Enter a choice\n[1] - Login\n[2] - Register\n")

    if choice == '1':
        print("===LOGIN===")
        email = input("Enter email: ")
        password = input("Enter password: ")

        for obj in list:
            if obj.email == email and obj.password == password:
                otp = random.randint(1000,9999)
                html_content = "<html><body><h1>YOUT OTP CODE IS </h1><h2>"+str(otp)+"</h2></body></html>"
                #success
                try:
                    to = [{"email":email}]
                    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)
                    api_response = api_instance.send_transac_email(send_smtp_email)
                    print("Otp has been sent, Please WAIT and CHECK your email")
                    
                except ApiException as e:
                    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
                userOtp=input("Please input the OTP, that had been sent to your email: ")
                if userOtp == str(otp):
                    print("YOU ARE NOW LOGGED IN")
                    input("Press any key to logout")
                    continue
                else:
                    print("invalid otp exiting the system...")
                    exit()
            else:
                print("user not found...")
                continue

    if choice == '2':
        print("===REGISTER===")
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        list.append( User(name, email, password))
    else:
        print("invalid input")
