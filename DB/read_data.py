import csv
def read_company_data(list):#儲存公司所有有效數據
    data=[]
    index=0
    for company in list:
        path='org_csv\\'+company+'.csv'
        data.append([])
        file=open(path,'r',newline='')
        reader = csv.reader(file)  # 建立 CSV 讀取器 只讀符合部分
        for row in reader:
            if row and(row[0]=='環境' or row[0]=='社會' or row[0]=='治理'):
                data[index].append(row)
        index+=1
    return data