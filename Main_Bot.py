import requests
import telegram
import datetime
import telepot
import imageoutput
import Messpicoutput
import Dynamic_Table
import Dynamic_Mess
import faculty_email
import Class_for_faculty
import upcoming_class
BennettBot = telepot.Bot('1687936397:AAGRc4Xv1gR8pt_dhX7QjXPC5Ha_i1mtxZg')

#list to check strings
weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
date_req = list(range(1,32))
email_sym = ["email","mail","mail-id","email-id",]

#all def statements
def day_c(I):
    for i in I:
        if i in weekdays:
            return True
def day_r(I):
    for i in I:
        if i in weekdays:
            return i
def date_c(I):
    for i in I:
        if i in str(date_req):
            return True
def date_r(I):
    for i in I:
        if i in str(date_req):
            return i
class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

#url = "https://api.telegram.org/bot<token>/"
    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
    
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update

token = '1687936397:AAGRc4Xv1gR8pt_dhX7QjXPC5Ha_i1mtxZg' #Token of your bot
Bennett_Bot = BotHandler(token) #Your bot's name



def main():
    logi=0
    login = 0
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=Bennett_Bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"
#Dynamic Output
                I = first_chat_text
                I = I.lower()
                I = I.split()
                
                if  ("/start" in I) or (("help" in I) or ("about" in I)):
                    BennettBot.sendPhoto(first_chat_id, photo = open('start.jpeg', 'rb'))
                    new_offset = first_update_id + 1
#Normal Chat
                elif ("hello" in I) or ("hi" in I) :
                    Bennett_Bot.send_message(first_chat_id,"Hi Welcome to Bennett Bot. How may I Help You?")
                    new_offset = first_update_id + 1
                elif ("bot" in I):
                    Bennett_Bot.send_message(first_chat_id,"Yes I am")
                    new_offset = first_update_id + 1
                elif ("thankyou" in I) or (("thank" in I) or ("thanks" in I)) :
                    Bennett_Bot.send_message(first_chat_id,"It was my pleasure to assist you")
                    new_offset = first_update_id + 1

                elif ("time" in I)and (("library" in I) and (("close" in I)or ("close?" in I)or("closing" in I))):
                    Bennett_Bot.send_message(first_chat_id,"The Library closes at 11 pm ")
                    new_offset = first_update_id + 1
                elif ("time" in I)and (("library" in I) and (("open" in I)or ("open?" in I))):
                    Bennett_Bot.send_message(first_chat_id,"The Library open's at 11 pm ")
                    new_offset = first_update_id + 1
                elif ("time" in I)and (("canteen" in I) and (("close" in I)or ("close?" in I))):
                    Bennett_Bot.send_message(first_chat_id,"The Canteen closes at 11 pm ")
                    new_offset = first_update_id + 1
                elif ("time" in I)and (("canteen" in I) and (("open" in I)or ("open?" in I))):
                    Bennett_Bot.send_message(first_chat_id,"The Canteen open's at 11 pm ")
                    new_offset = first_update_id + 1
                elif (("time" in I)and ("lunch" in I)) or ("lunch?" in I):
                    Bennett_Bot.send_message(first_chat_id,"Lunch is form 12 noon to 2:00pm ")
                    new_offset = first_update_id + 1
                elif (("time" in I)and ("breakfast" in I)) or ("breakfast?" in I):
                    Bennett_Bot.send_message(first_chat_id,"Breakfast is form 7:00am to 9:30am ")
                    new_offset = first_update_id + 1
                elif (("time" in I)and ("snacks" in I)) or ("snacks?" in I):
                    Bennett_Bot.send_message(first_chat_id,"Evening Snacks is form 5:30pm to 7:00pm ")
                    new_offset = first_update_id + 1
                elif (("time" in I)and ("dinner" in I)) or ("dinner?" in I):
                    Bennett_Bot.send_message(first_chat_id,"Dinner is form 8:00pm to 10:00pm ")
                    new_offset = first_update_id + 1
                elif((("lecture" in I) or ("class" in I)) and (("today" in I) and ("do" in I))) and ("what" not in I):
                    Class_for_faculty.class_fac(first_chat_id,I)
                    new_offset = first_update_id + 1
                elif(("lecture" in I) or ("class" in I)) and ((("tomorrow" in I) or ("kal" in I)) and (("do" in I) or ("hai" in I))):
                    Class_for_faculty.class_fac(first_chat_id,I)
                    new_offset = first_update_id + 1
#Time Table
                elif day_c(I) and (("class" in I) or (("lecture" in I) or ("timetable" in I))):
                    T_T = day_r(I)
                    Dynamic_Table.output_todisplay(first_chat_id,T_T)
                    new_offset = first_update_id + 1
                elif date_c(I) and (("class" in I) or (("lecture" in I) or ("timetable" in I))):
                    D_R= date_r(I)
                    Dynamic_Table.output_todisplayday(first_chat_id,D_R)
                    new_offset = first_update_id + 1
                elif ("today" in I) and (("class" in I) or (("lecture" in I) or ("timetable" in I))):
                    imageoutput.timetableday(first_chat_id)
                    new_offset = first_update_id + 1
                elif ("tomorrow" in I) and (("class" in I) or (("lecture" in I) or ("timetable" in I))):
                    today = datetime.date.today()
                    tomorrow = today + datetime.timedelta(days=1)
                    today1 = tomorrow.strftime('%d %m %Y')
                    import calendar   
                    def findDay(date): 
                        born = datetime.datetime.strptime(today1, '%d %m %Y').weekday() 
                        return (calendar.day_name[born]) 
                    tday =(findDay(today1))
                    print(tday)
                    Dynamic_Table.output_todisplay(first_chat_id,tday.lower())
                    new_offset = first_update_id + 1

#Mess Menu
                elif first_chat_text == 'M':
                      Messpicoutput.timetableday(first_chat_id)
                      new_offset = first_update_id + 1
                elif day_c(I) and (("food" in I) or (("menu" in I) or ("breakfast" in I))):
                    T_T = day_r(I)
                    Dynamic_Mess.output_todisplay(first_chat_id,T_T)
                    new_offset = first_update_id + 1
                elif date_c(I) and (("food" in I) or (("lunch" in I) or ("breakfast" in I))):
                    D_R = date_r(I)
                    Dynamic_Mess.output_todisplayday(first_chat_id,D_R)
                    new_offset = first_update_id + 1
                elif ("today" in I) and ((("food" in I) or ("mess" in I)) or ((("lunch" in I) or ("dinner" in I)) or (("breakfast" in I) or ("snacks" in I)))):
                    Messpicoutput.timetableday(first_chat_id)
                    new_offset = first_update_id + 1
                elif ("tomorrow" in I) and ((("food" in I) or ("mess" in I))or ((("lunch" in I) or ("dinner" in I)) or (("breakfast" in I) or ("snacks" in I)))):
                    today = datetime.date.today()
                    tomorrow = today + datetime.timedelta(days=1)
                    today1 = tomorrow.strftime('%d %m %Y')
                    import calendar   
                    def findDay(date): 
                        born = datetime.datetime.strptime(today1, '%d %m %Y').weekday() 
                        return (calendar.day_name[born]) 
                    tday =(findDay(today1))
                    print(tday)
                    Dynamic_Mess.output_todisplay(first_chat_id,tday.lower())
                    new_offset = first_update_id + 1
#Emergency Contacts
                elif("medical" in I)and ("emergency" in I):
                     Bennett_Bot.send_message(first_chat_id,"Contact No:120-7199494")
                     new_offset = first_update_id + 1
#faculty email ID    
                elif any(word in I for word in email_sym):
                    topri = faculty_email.output_email(first_chat_id,I)
                    if type(topri) == list:
                        for i in range(len(topri)):
                            Bennett_Bot.send_message(first_chat_id,topri[i])
                    else:
                        Bennett_Bot.send_message(first_chat_id,topri)
                    new_offset = first_update_id + 1
                elif ("reception" in I) or (("board" in I) and ("reception" in I)):
                    Bennett_Bot.send_message(first_chat_id,"The number for Reception Board is: 0120-7199300. ")
                    new_offset = first_update_id + 1
                elif (("main" in I) and ("gate" in I)) or (("maingate" in I) and ("security" in I)):
                    Bennett_Bot.send_message(first_chat_id,"The number for Main Gate Security is: 1000/0120-7199389. ")
                    new_offset = first_update_id + 1
                elif (("counselling" in I) and ("services" in I)) and (("contact" in I) or ("number" in I)):
                    Bennett_Bot.send_message(first_chat_id,"The contact number for Counselling Services is: 0120-7199500. ")
                    new_offset = first_update_id + 1
                elif ("dean" in I) and ("who" in I):
                    Bennett_Bot.send_message(first_chat_id,"The Name of our Dean is Dr.Milind Padalkar. Email-id: dsa@bennett.edu.in.\n Contact no.: 0120-7199341. ")
                    new_offset = first_update_id + 1
                elif (("student" in I) and ("welfare" in I)) or ("officer" in I):
                    Bennett_Bot.send_message(first_chat_id,"Manisha Shukla is the Student Welfare Officer. Email-id: manisha.shukla@bennett.edu.in.\n Contact no.: 0120-7199360 ")
                    new_offset = first_update_id + 1
                elif (("student" in I) and ("library" in I)) or ("coordinator" in I):
                    Bennett_Bot.send_message(first_chat_id,"Fraz Mallik is the name of the Student Welfare Coordinator.  Email-id: fraz.malik@bennett.edu.in.\n Contact no.: 0120-7199360 ")
                    new_offset = first_update_id + 1
                elif ("time" in I) and (("laundry" in I) and (("open" in I)or ("open?" in I))):
                    Bennett_Bot.send_message(first_chat_id,"The Laundry open's at 9:00 am ")
                    new_offset = first_update_id + 1
#Clubs 
                elif (("club" in I) and ("advaita" in I)) or ("advaita" in I):
                    Bennett_Bot.send_message(first_chat_id,"Advaita is the Music Society of Bennett University. https://www.instagram.com/advaita.bu/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('advaita.bu-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("nomads" in I)) or ("nomads" in I):
                    Bennett_Bot.send_message(first_chat_id,"Nomads is the travel club of Bennett. https://www.instagram.com/nomads.bennettuniversity/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('Nomads_New_lols'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("silhouette" in I)) or ("silhouette" in I):
                    Bennett_Bot.send_message(first_chat_id,"Silhouette is the Creative Society of Bennett University. https://www.instagram.com/silhouette_bu/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('Silhouette new'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("isac" in I)) or ("isac" in I):
                    Bennett_Bot.send_message(first_chat_id,"Isac is the Photography Club of Bennett University. https://www.instagram.com/isac.bu/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('isac.bu-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("astronomy" in I)) or ("astronomy" in I):
                    Bennett_Bot.send_message(first_chat_id,"Astronomy is the Astronomy Club of Bennett University. https://www.instagram.com/astronomy_bu/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('astronomy_bu-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("spark" in I)) or ("spark" in I):
                    Bennett_Bot.send_message(first_chat_id,"Spark is the Entrepreneurship Club of Bennett University. https://instagram.com/getsparked.bu?igshid=15optru8kfz0g ")
                    BennettBot.sendVideo(first_chat_id, video = open('Spark new'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("alexis" in I)) or ("alexis" in I):
                    Bennett_Bot.send_message(first_chat_id,"Alexis is the Social Work Club of Bennett University. https://instagram.com/goalexisbu?igshid=1ca6cqoup6xi3 ")
                    BennettBot.sendVideo(first_chat_id, video = open('Alexis_New'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("techtonix" in I)) or ("techtonix" in I):
                    Bennett_Bot.send_message(first_chat_id,"Techtonix is the Robotics Club of Bennett University. https://instagram.com/technotix_bennett?igshid=3t8k2qvuyfh2 ")
                    BennettBot.sendVideo(first_chat_id, video = open('technotix_bennett-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("pulse" in I)) or ("pulse" in I):
                    Bennett_Bot.send_message(first_chat_id,"Pulse is the Adventure Club of Bennett University. https://instagram.com/pulse_bu?igshid=xnz925rb1jpw ")
                    BennettBot.sendVideo(first_chat_id, video = open('pulse_bu-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("rivaaz" in I)) or ("rivaaz" in I):
                    Bennett_Bot.send_message(first_chat_id,"Rivaaz is the Indian Cultural Society of Bennett University. https://instagram.com/rivaaz_bu?igshid=psbf8aanoc7q ")
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("verve" in I)) or ("verve" in I):
                    Bennett_Bot.send_message(first_chat_id,"Verve is the Western Dance Club of Bennett University. https://instagram.com/verve_bu?igshid=1q5migjt07qf2 ")
                    BennettBot.sendVideo(first_chat_id, video = open('verve_bu-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("ansh" in I)) or ("ansh" in I):
                    Bennett_Bot.send_message(first_chat_id,"Ansh is the Dramatics Club of Bennett University. https://instagram.com/ansh.bu?igshid=lg3gzg0oecv5 ")
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("bugamers" in I)) or (("bu" in I) and ("gamers" in I)):
                    Bennett_Bot.send_message(first_chat_id,"BUGamers is the Gaming Club of Bennett University. https://www.instagram.com/bu.gamers/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('bu.gamers-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("panache" in I)) or ("panache" in I):
                    Bennett_Bot.send_message(first_chat_id,"Panache is the Fashion Club of Bennett University. https://www.instagram.com/panache.bu/ ")
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("bumun" in I)) or ("bumun" in I):
                    Bennett_Bot.send_message(first_chat_id,"BUMUN is the Modern United Nations Club of Bennett University. https://www.instagram.com/bumunclub/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('bumunclub-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("cerebrum" in I)) or ("cerebrum" in I):
                    Bennett_Bot.send_message(first_chat_id,"Cerebrum is a Club of Bennett University. https://www.instagram.com/cerebrumbennett/ ")
                    new_offset = first_update_id + 1
                elif (("club" in I) and ("enactus" in I)) or ("enactus" in I):
                    Bennett_Bot.send_message(first_chat_id,"Enactus is a Club of Bennett University. https://www.instagram.com/enactus.bu/ ")
                    BennettBot.sendVideo(first_chat_id, video = open('enactus.bu-20210210-0001'+ '.mp4', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
#Day/Night Pass
                elif ((("day" in I ) and ("pass" in I)) or (("night" in I ) and ("pass" in I))) or ("pass" in I):
                    BennettBot.sendPhoto(first_chat_id, photo = open('Pass.jpeg', 'rb'))
                    new_offset = first_update_id + 1
                    
                elif ("location" in I) or (("where" in I) and (("bu"in I) or ("bennett" in I))):
                    Bennett_Bot.send_message(first_chat_id,"https://goo.gl/maps/GVKfed6RYEhzx6zF9")
                    new_offset = first_update_id + 1
#C0D3X
                elif ("c0d3x" in I):
                    Bennett_Bot.send_message(first_chat_id,"C0D3X,the team behind creating this Bot")
                    Bennett_Bot.send_message(first_chat_id,"It comprises of: Rithwik Arthur William, Riya Jain, Sahil Jain, Tanya Gupta,Yash Saxena")
                    Bennett_Bot.send_message(first_chat_id,"Hope you liked it!!")
                    Bennett_Bot.send_message(first_chat_id,"send your reviwes at: bennettbot.suggestions@gmail.com")
                    BennettBot.sendVideo(first_chat_id, video = open('c0d3x'+ '.gif', 'rb'),supports_streaming = True)
                    new_offset = first_update_id + 1
#Static Output
                elif first_chat_text == 'L' or first_chat_text == 'l':
                    Bennett_Bot.send_message(first_chat_id,"Enter your roll number")
                    logi = 1
                    new_offset = first_update_id + 1
                
                elif logi == 1:
                    list1 = []
                    file = open("rn.txt","r")
                    for i in range(100):
                            line = file.readline()
                            if not line:
                                    break
                            line = line.lower()
                            list1.append(line.strip())
                    if first_chat_text.lower() in list1:
                        Bennett_Bot.send_message(first_chat_id,'You have successfully logged in')
                        Bennett_Bot.send_message(first_chat_id,'What do you want to look up?')
                        Bennett_Bot.send_message(first_chat_id,'T- Timetable , U- Upcoming classes , M- Mess Menu')
                        new_offset = first_update_id + 1
                        login = 1
                        logi = 0
                elif login == 1:

                    if first_chat_text == 'T' or first_chat_text == 't' :
                      imageoutput.timetableday(first_chat_id)
                      new_offset = first_update_id + 1
                    elif first_chat_text == 'U' or first_chat_text == 'u':
                      topri = upcoming_class.upcoming()
                      if len(topri) >= 1:
                        for i in range(len(topri)):
                            Bennett_Bot.send_message(first_chat_id,topri[i])
                      else:
                            Bennett_Bot.send_message(first_chat_id,"No more Classes today")
                      new_offset = first_update_id + 1
                    else:
                      BennettBot.sendSticker(first_chat_id, sticker = open('Oops! Command not Found!.WEBP', 'rb'))
                      new_offset = first_update_id + 1
                else:
                    BennettBot.sendSticker(first_chat_id, sticker = open('Oops! Command not Found!.WEBP', 'rb'))
                    new_offset = first_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    
