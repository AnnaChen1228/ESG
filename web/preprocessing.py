def pre_rule(text):#return dict
    temp={}
    text=text.strip()
    if text!='0':
        temp['answer']=text[text.find('回')+5:text.find('參')-1].strip()
        if len(text[text.find('參')+5:text.find('參',text.find('參')+5)-1].strip())!=0:
            temp['ref']='參考'+text[text.find('參')+5:text.find('參',text.find('參')+5)-1].strip()+' '+text[text.find('Q'):text.find('Q')+2].strip()+''
    elif text==1:
        temp['answer']="無法獲得回應"
    else:
        temp['answer']="抱歉，這些問題我無法幫助你。"

    return temp
