#!/usr/bin/env python

#!/usr/bin/env python

'''
This is all still very much a work in progress and is not yet completed. I am working through the thought process of the program and still working out a few pesky Python syntax errors.
This is a Flask app which just allows development server and a debugger. Flask website-(http://flask.pocoo.org/)
Created by: Stephen Tornetta
'''

from flask import Flask
#from flask import redirect
from flask import request
import twilio.twiml
app = Flask(__name__)

admin_list = {
   "+16109089405": "Stephen Tornetta",
   "+16105258676": "Vicki Tornetta",
}

user_list = []
user_info = []
print("This program is working.")
   
@app.route("/", methods=['GET', 'POST'])  
def survey():
    response = twilio.twiml.Response()
    body = request.form['Body']
    Call = True
    user_name = ' '
    
    #Checks the 'From ID' which is the caller's number and see if it has been recorded.
    from_Number = str(request.form['From'])
    user_info.append(from_Number)
    
    from_City = str(request.form['FromCity'])
    user_info.append(from_City)
    
    from_Country = str(request.form['FromCountry'])
    user_info.append(from_Country)
    
    from_State = str(request.form['FromState'])
    user_info.append(from_State)
    
    from_Zip = str(request.form['FromZip'])
    user_info.append(from_Zip)
    
    print user_info
     
    #I think this is an optional feature and I'm not sure if we want it included but I thought I would leave it in and see if we could make any use of it.
    if from_Number in admin_list:
        message = admin_list[from_number] + ',Thank you for messaging the Easter Out Reach Program. Admin settings will be messaged too you.'
        
    elif user_name == ' ': 
        if Call == True:
            message1 = "It seems this is the first time you have contacted us."
            response.message(message1)
            #message is what is sent to the user via SMS
        if user_name not in user_list:
            message2 = "Enter your name so we can record your data."
            response.message(message2)
            #Works the same as 'From' but instead retrieves the body of the SMS message
            user = request.form['Body']
            user_name = str(user)
            user_list.append(user_name)
            print user_name
            print user_list
            Call = True
            

    return str(response) 

if __name__ == "__main__":
    app.run(debug=True)
    