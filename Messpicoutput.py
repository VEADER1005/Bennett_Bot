import telepot
from datetime import date
import pandas as pd
BennettBot = telepot.Bot('1687936397:AAGRc4Xv1gR8pt_dhX7QjXPC5Ha_i1mtxZg')
def timetableday(first_chat_id):
    today = date.today()
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
            image_store =(df[df.Days==tday]['Mess'].sum())
            return BennettBot.sendPhoto(first_chat_id,photo=open(image_store,'rb'))

