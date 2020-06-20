### I made this program for studying oop :) ###

from line_notify import LineNotify # To send notification through line
from time import localtime # To get present time
from socket import gethostname # To get hostname(It's maybe not necessary but it's awesome)
import cv2 # To access camera
from requests import get # To get ip public address
from sys import exit # To kill process of running
from time import sleep # awaiting connection

class compsecure:
    '''Am using class because i just want to study about Object-Orient Programming concept'''
    token = "put your line notify token here"  # line notify token visit "https://notify-bot.line.me/" to get your
    notify = LineNotify(token) # use token to identify account
    def __init__(self):
        self.ip_addr = get('https://checkip.amazonaws.com').text.strip() ### get ipv4
        self.now = list(localtime()) ### get local time

    def getlocation(self):
        ip_req = get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_req.json()['ip']  ### Temp ipv6
        geo_req = f'https://get.geojs.io/v1/ip/geo/{my_ip}.json'
        geo_request = get(geo_req)
        return geo_request.json() # information in dict
    '''
    it's is an old version i improved it to run faster :)
    def getpic(self,num):
        # capture from webcam and saved
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(f"capture{num}.png", image)
        camera.release()
        return f"capture{num}.png"
    '''

    def takepic(self, time):
        # capture from webcam and saved
        lst = []
        for num in range(1,time+1):
            # use open cv to access webcam
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            # save picture
            cv2.imwrite(f"capture{num}.png", image)
            lst.append(f"capture{num}.png") # list that contain pic file name
            camera.release()
        #print(lst)
        #
        return lst

    def data(self):
        name = gethostname() # get this machine hostname
        time = self.now # get time in list
        present_date = f"{time[2]}/{time[1]}/{time[0]}" # date format dd/mm/yy
        present_time = f"{time[3]}:{time[4]}:{time[5]}" # time format hh/mm/ss
        ipv4 = self.ip_addr # ipv4
        country = self.getlocation()["country"] # country
        province = self.getlocation()["region"] # region, province
        city = self.getlocation()["city"] # city
        latitude = self.getlocation()["latitude"] #latitude
        longitude = self.getlocation()["longitude"] #longitude
        org = self.getlocation()["organization"] # Internet distributor organization
        return f"\n\nLogin : {name}" \
               f"\nDate : {present_date}" \
               f"\nTime : {present_time}" \
               f"\nIPv4: {ipv4}" \
               f"\nOrg : {org}" \
               f"\nLocation : " \
               f"\n    |-Country : {country}" \
               f"\n    |-Region : {province}" \
               f"\n    |-City : {city}" \
               f"\n    |-Latitude : {latitude}" \
               f"\n    |-Longitude : {longitude}\n " # return data

    def sendtxt(self, message):
        self.notify.send(message)

    def sendpic(self, txt, path_lst):
        for path in path_lst:
            self.notify.send(f"\n{txt}", image_path = path) # send picture

    def run(self):
        self.sendtxt(self.data()) # send login data
        pic_file = self.takepic(2) # number of captured picture
        self.sendpic("Captured : ", pic_file) # send picture

def internet_connection():
    ### waiting for connection establish ###
    ### using recursive function ###
    try:
        ### connection to google ###
        ### 200 it's mean successful ###
        get("https://www.google.com/").status_code
    except:
        ### not connected to internet ###
        sleep(3)
        ### waiting for 3 seconds ###
        ### try connection by using recursive method ###
        internet_connection()
    ### connection successful ###
    return True

### waiting for internet connection ###
if internet_connection():
    start = compsecure()
    start.run()

### kill program process ###
exit()
#end of program #





