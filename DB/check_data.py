import read_data

def get_company_index_name(data):#儲存各公司指標名稱
    index_name=[]
    index=0
    for company in data:
        index_name.append([])
        for data in company:
            index_name[index].append(data[2])
        index+=1
    return index_name

def get_same_part(company_data,company_index_data):#輸出ESG共同部分 company_data用來輸出其在E/S/G
    #  將第一個子列表轉換為集合
    common_elements = [item for item in company_index_data[0] if all(item in sublist for sublist in company_index_data[1:])]

    # 找出不同的元素
    common_elements = [item for item in company_index_data[0] if all(item in sublist for sublist in company_index_data[1:])]

    # 找出不再共同元素的獨特元素
    unique_elements = []
    for i, sublist in enumerate(company_index_data):
        unique = [item for item in sublist if item not in common_elements]
        unique_elements.append((f"List {i + 1}", unique))  
    # print(common_elements)
    index_name=[]
    for item in company_data:
        index_name.append(item[2])

    E_data={}
    S_data={}
    G_data={}
    start=0
    #分別列吃三個共有部分
    for item in common_elements:
        site=index_name.index(item,start)
        if company_data[site][0]=="環境":
            if company_data[site][1] not in E_data:
                E_data[company_data[site][1]]=[]
            E_data[company_data[site][1]].append(item)
        elif company_data[site][0]=="社會":
            if company_data[site][1] not in S_data:
                S_data[company_data[site][1]]=[]
            S_data[company_data[site][1]].append(item)
        elif company_data[site][0]=='治理':
            if company_data[site][1] not in G_data:
                G_data[company_data[site][1]]=[]
            G_data[company_data[site][1]].append(item)
        start+=1
    # print(f"E_data:{E_data}\nlength:{len(E_data)}")
    # print(f"S_data:{S_data}\nlength:{len(S_data)}")
    # print(f"G_data:{G_data}\nlength:{len(G_data)}")
    return E_data,S_data,G_data

def check(company_list):
    company_data = read_data.read_company_data(company_list)
    company_index_name = get_company_index_name(company_data)
    return get_same_part(company_data[0],company_index_name)

company_list = ['2330 - 台積電', '3711 - 日月光投控', '2454 - 聯發科', '2303 - 聯電', '2379 - 瑞昱']
company_data = read_data.read_company_data(company_list)
company_index_name = get_company_index_name(company_data)
E_data,S_data,G_data= get_same_part(company_data[0],company_index_name)