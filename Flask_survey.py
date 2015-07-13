#!/usr/bin/env python

'''
This is all still very much a work in progress and is not yet completed. I am working through the thought process of the program and still working out a few pesky Python syntax errors.
This is a Flask app which just allows development server and a debugger. Flask website-(http://flask.pocoo.org/)
Created by: Stephen Tornetta
'''

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

admin_list = {
   "+16109089405": "Stephen Tornetta",
}

user_list = []

Call = False
   
@app.route("/", methods=['GET', 'POST'])
def survey():
    #Checks the 'From ID' which is the caller's number and see if it has been recorded.
    from_number = request.values.get('From')
    
    #I think this is an optional feature and I'm not sure if we want it included but I thought I would leave it in and see if we could make any use of it.
    if from_number in admin_list:
        message = admin_list[from_number] + ',Thank you for messaging the Easter Out Reach Program. Admin settings will be messaged too you.'
        
    else:
            #message is what is sent to the user via SMS
            message = "It seems this is the first time you have contacted us. Enter your name so we can record your data."
            #Works the same as 'From' but instead retrieves the body of the SMS message
            user = request.values.get('Body')
            user_name = str(user)
            message = "Is ",user_name, "Correct?"
            if request.values.get("Body") == "yes":
                message = "Next Step"
            else:
                message = "Error"
            
            user.append(user_name)
            #print user
 
    resp = twilio.twiml.Response()
    resp.message(message) 
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)