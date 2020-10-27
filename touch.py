import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import json,urllib.request
import datetime

def check(s,d,dd,incoming_msg,states,states_confirmed,states_recovered,l1,l2,l3,months,b):
    Tasks = [s,d,dd]
    my_labels = 'Confirmed','Deaths','Recovered'
    my_colors = ['red','green','blue']
    my_explode = (0, 0.1, 0)
    fig = plt.figure()
    # plot it
    fig = plt.figure(figsize=(15,15))
    ax0 = plt.subplot2grid((8,12), (0, 0), colspan=3,rowspan=3)
    ax0.pie(Tasks, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow = True, colors=my_colors, explode=my_explode,radius=1.4)
    ax0.set_title('COMPARISON OF TOTAL CASES \n TOTAL DEATHS AND TOTAL RECOVERED',fontsize=8)
    ax0.axis('equal')
    ax1=plt.subplot2grid((8,12),(0,4),colspan=3,rowspan=3)
    ax1.set_facecolor=("yellow")
    ax1.bar(my_labels,Tasks,color=("yellow"))
    ax1.set_title("VIEW OF THE WHOLE COUNTRY",fontsize=8)
    ax1.tick_params(axis='x', rotation=45,labelsize=8)
    ax2=plt.subplot2grid((8,12),(4,0),colspan=3,rowspan=3)
    ax2.bar(states,states_confirmed,color=("black"))
    ax2.set_title("CONFIRMED STATES REPORT OF THE MOST EFFECTED STATES",fontsize=8)
    ax2.tick_params(axis='x', rotation=45,labelsize=6)
    ax3=plt.subplot2grid((8,12),(4,4),colspan=3,rowspan=3)
    ax3.bar(states,states_recovered,color=("purple"))
    ax3.set_title("RECOVERY RATES OF THE MOST EFFECTED STATES",fontsize=8)
    ax3.tick_params(axis='x', rotation=45,labelsize=6)
    ax4=plt.subplot2grid((8,12),(0,8),colspan=4,rowspan=7)
    ax4.plot(months,l1,color='red',marker='o',label="CONFIRMED")
    for x,y in zip(months,l1):
        label = "{}".format(y)
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center')
    ax4.plot(months,l2,color='green',marker='*',label="DEATHS")
    for x,y in zip(months,l2):
        label = "{}".format(y)
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center')
    ax4.plot(months,l3,color='black',marker='.',label="recovered")
    for x,y in zip(months,l3):
        label = "{}".format(y)
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center')
    ax4.set_title("LIVE STATS(LAST 4 MONTHS)",fontsize=12)
    ax4.legend()
    fig.tight_layout(pad=2.0)
    plt.savefig('/home/frosted/test1/to.png')
    plt.clf()
