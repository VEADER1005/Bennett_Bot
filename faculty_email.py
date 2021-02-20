def output_email(first_chat_id,I):
    S_lst = []
    out_lst = []
    loop = 0
    import pandas as pd
    df = pd.read_excel('faculty.xlsx')
    (df)
    temp = []
    for n in(df['Name']):
        if str(n.lower()) in I:
            x = (df[df.Name==n]['Email Id'].sum())
            out = ("The Professor's Email Id is "+x)
            return out
            break
    for n in(df['Surname']):
        S_lst.append(n.lower())
    for n in(df['Surname']):
        if str(n.lower()) in I:
            cou = S_lst.count(n.lower())
            if cou == 1:    
                x = (df[df.Surname==n]['Email Id'].sum())
                out = ("The Professor's Email id is "+x)
                return out
                break
            elif loop == 0:
                temp1=(df[df.Surname==n]['Email Id'].sum())
                tempn=(df[df.Surname==n]['Full Name'].sum())
                temp2 = temp1.split(".in")
                tempn = tempn.split("@")
                for i in range(len(temp2)):
                    if temp2[i] == "":
                        break
                    else:
                        temp3 = temp2[i]+".in"
                    out_lst.append("Email id of "+tempn[i]+" is "+temp3)
                return out_lst 
                loop+=1
  
        
            
