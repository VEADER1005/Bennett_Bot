import telepot
BennettBot = telepot.Bot('1687936397:AAGRc4Xv1gR8pt_dhX7QjXPC5Ha_i1mtxZg')
def timetableday(first_chat_id):
    from datetime import date
    import pandas as pd
    tdate = date.today()
    df = pd.read_excel('Academic-Calendar-OddSemester_2020-21_First-Year-Students.xlsx')
    (df)
    for n in(df['Date']):
        if n.date() == tdate :
            x = (df[df.Date == n]['Type1'].sum())
            if x == 0 or (x == "Holiday" or x == "Vacation"):
                ev = (df[df.Date==n]['Event'].sum())
                if ev == 0:
                    return BennettBot.sendMessage(first_chat_id, 'Holiday')
                else:
                    return BennettBot.sendMessage(first_chat_id,['a holiday for',ev])
            elif x == "Examination":
                ev = (df[df.Date==n]['Event'].sum())
                print(ev)
            else:
                #finding what day it is
                today= date.today()
                today1 = today.strftime('%d %m %Y')
                import datetime 
                import calendar   
                def findDay(date): 
                    born = datetime.datetime.strptime(today1, '%d %m %Y').weekday() 
                    return (calendar.day_name[born]) 
                tday =(findDay(today1))
                # finding the timetable according to the day
                from datetime import datetime
                import pandas as pd
                df = pd.read_excel('EB09-TT.xlsx')
                (df)
                for n in(df['Days']):    
                    if str(n) == tday :
                        x = (df[df.Days==tday]['TT'].sum())
                        if tday == "Saturday" or tday=="Sunday":
                            print(x)
                        else:
                            image_store=(df[df.Days==tday]['Image'].sum())
                            return BennettBot.sendPhoto(first_chat_id,photo=open(image_store,'rb'))

