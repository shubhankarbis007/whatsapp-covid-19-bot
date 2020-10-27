from flask import Flask, request
import requests
import json,urllib.request
from twilio.twiml.messaging_response import MessagingResponse
from touch import check
from flask import send_from_directory
import datetime
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    data = urllib.request.urlopen("https://covid19.mathdro.id/api/countries/"+incoming_msg).read()
    output = json.loads(data)
    s=output["confirmed"]["value"]
    d=output["deaths"]["value"]
    dd=output["recovered"]["value"]
    data1=urllib.request.urlopen("https://covid19.mathdro.id/api/countries/{}/confirmed".format(incoming_msg)).read()
    output1=json.loads(data1)
    states_confirmed=[]
    states=[]
    states_recovered=[]
    for i in range(0,5):
        states.append(output1[i]["provinceState"])
        states_confirmed.append(output1[i]["confirmed"])
        states_recovered.append(output1[i]["recovered"])
    current_time = datetime.datetime.now()
    a=current_time.day
    b=current_time.month
    l1=[]
    l2=[]
    l3=[]
    months=[b-4,b-3,b-2,b-1]
    for j in range(b-4,b):
        c=0
        d=0
        z=0
        if j<10:
            j="0"+str(j)
        data2=urllib.request.urlopen("https://covid-api.com/api/reports?date=2020-{}-28&region_name={}".format(j,incoming_msg)).read()
        output3=json.loads(data2)
        for i in range(len(output3["data"])):
            c=c+output3["data"][i]["confirmed"]
            d=d+output3["data"][i]["deaths"]
            z=z+output3["data"][i]["recovered"]
        l1.append(c)
        l2.append(d)
        l3.append(z)
    check(s,d,dd,incoming_msg,states,states_confirmed,states_recovered,l1,l2,l3,months,b)
    '''msg.media('https://e10e44bde524.ngrok.io/uploads/to.png')'''
    msg.body("LIVE CORONAVIRUS STATS CLICK ON THE LINK TO GET A VISUAL GRAPH\n  https://515b902dc287.ngrok.io/to.png")
    return str(resp)

'''@app.route('/uploads/to.png', methods=['GET', 'POST'])
def uploaded_file():
    return send_from_directory("/home/frosted/","to.png")'''
if __name__ == '__main__':
    app.run()
