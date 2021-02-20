import telepot
def upcoming():
    striL=[]
    BennettBot = telepot.Bot('1687936397:AAGRc4Xv1gR8pt_dhX7QjXPC5Ha_i1mtxZg')
    from datetime import date
    import pandas as pd
    tdate = date.today()
    cls = False
    df = pd.read_excel('Academic-Calendar-OddSemester_2020-21_First-Year-Students.xlsx')
    (df)
    for n in(df['Date']):
        if n.date() == tdate :
            x = (df[df.Date == n]['Type1'].sum())
            if x == 0 or (x == "Holiday" or x == "Vacation"):
                ev = (df[df.Date==n]['Event'].sum())
                if ev == 0:
                    return BennettBot.sendMessage(first_chat_id, "Holiday")
                else:
                    string = "a holiday for"+" " + ev
                    return BennettBot.sendMessage(first_chat_id, string)
            elif x == "Examination":
                ev = (df[df.Date==n]['Event'].sum())
                return BennettBot.sendMessage(first_chat_id, ev)
            else:
                print("working day")
                #finding what day it is
                today= date.today()
                today1 = today.strftime('%d %m %Y')
                import datetime 
                import calendar   
                def findDay(date): 
                    born = datetime.datetime.strptime(today1, '%d %m %Y').weekday() 
                    return (calendar.day_name[born]) 
                tday =(findDay(today1))
                print(tday)
                # finding the timetable according to the day
                from datetime import datetime
                df = pd.read_excel('EB09-TT.xlsx')
                (df)
                for n in(df['Days']):    
                    if str(n) == tday :
                        x = (df[df.Days==tday]['TT'].sum())
                        if tday == "Saturday" or tday=="Sunday":
                            break
                        else:
                            df = pd.read_excel(x)
                            for n in (df['SUBJECT_CODE']):
                                print(n)
                                checkf = (df[df.SUBJECT_CODE== n]['START_TIME'].sum())
                                '''
                                if checkf == 0:
                                    break
                                '''
                                print(type(checkf))
                                checkt = (df[df.SUBJECT_CODE== n]['END_TIME'].sum())
                                print(type(checkt))
                                tn = datetime.now()
                                c_time = tn.time()
                                if c_time>=checkf and c_time<=checkt:
                                    chekf = checkf.strftime('%H:%M:%S')
                                    chekt = checkt.strftime('%H:%M:%S')
                                    stri = "Current Class for " + n + ": from " + chekf + " to " + chekt
                                    striL.append(stri)  
                                elif c_time>=checkf and c_time>=checkt:
                                    pass
                                elif c_time<=checkf and c_time<=checkt:
                                    chekf = checkf.strftime('%H:%M:%S')
                                    chekt = checkt.strftime('%H:%M:%S')
                                    stri = "Upcoming Class for " + n + ": from " + chekf + " to " + chekt
                                    striL.append(stri)
                    return striL
                                    
#based on days 
