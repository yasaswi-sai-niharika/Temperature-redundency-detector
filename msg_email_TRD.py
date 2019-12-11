import confi
from boltiot import Sms,Email,Bolt
import json,time

minimum_limit=300
maximum_limit=600

mybolt=Bolt(confi.API_KEY,confI.DEVICE_ID)

sms=Sms(confi.SID,confi.AUTH_TOKEN,confi.TO_NUMBER,confi.FROM_NUMBER)
mailer=Email(confi.MAILGUN_API_KEY,confi.SANDBOX_URL,confi.SENDER_EMAIL,confi.RECIPIENT_EMAIL)

while True:
    print ("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print("Sensor value is:"+str(data['value']))
    try:
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to mailgun and twilio to send an email and a message")
            response1 = sms.send_sms("the current temperature sensor value is"+str(sensor_value))
            response2 = mailer.send_email("Alert","the current sensor value is "+str(sensor_value))
            print("response recived from twilio is:"+str(response1))
            response_text = json.loads(response2.text)
            print("Status of SMS at Twilio is:"+str(response1.status))
            print("response recieved from Mailgun is:"+str(response-text[message]))
        except Exception as e:
            print("Error occured:Below are the reasons")
            print(e)
        time.sleep(10)
