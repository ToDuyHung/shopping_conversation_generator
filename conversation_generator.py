# coding=utf-8
import json
import random

import pandas as pd
import csv
import random
import sys
# df_172 = pd.read_csv('172.csv')
# df_173 = pd.read_csv('173.csv')
# df_174 = pd.read_csv('174.csv')
df_175 = pd.read_csv('175.csv')


def FilterListText(ls_text):
    return [ele[ele.index(':')+2:] if ':' in ele else ele for ele in ls_text]

ls_of_ls = []

# 1. "text"
# Get text of shop (the text without 'Khach X:' ) and text of customer (the other)
df_text = pd.concat([ele['text'].dropna(axis=0) for ele in [df_175]])
normalized_ls_shop = []
normalized_ls_customer = []
for ele in list(df_text):
    if 'Khách' not in ele:
        if '"' in ele:
            normalized_ls_shop += [ele[1:-1]]
        else:
            normalized_ls_shop += [ele]
    else:
        # skip text like 'onversation ...: Khách ...'
        if 'onversation' not in ele:
            if ':' in ele:
                normalized_ls_customer += [ele[ele.index(':') + 2:]]
            # print(ele)
            else:
                normalized_ls_shop += [ele]
        

# print(normalized_ls_shop)
ls_of_ls += [normalized_ls_shop]
# print(normalized_ls_customer[:10])
ls_of_ls += [normalized_ls_customer]


# 2. "Hello"

df_hello = pd.concat([ele['Hello'].dropna(axis=0) for ele in [df_175]])
normalized_ls_hello = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_hello)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_hello]]
# print(normalized_ls_hello)

# 3. "Done"
df_done = pd.concat([ele['Done'].dropna(axis=0) for ele in [df_175]])
normalized_ls_done = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_done)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_done]]


# 4. "Connect"
df_connect = pd.concat([ele['Connect'].dropna(axis=0) for ele in [df_175]])
normalized_ls_connect = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_connect)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_connect]]

# 5. "Order"
df_order = pd.concat([ele['Order'].dropna(axis=0) for ele in [df_175]])
normalized_ls_order = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_order)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_order]]
# print(normalized_ls_order)

# 6. "Changing"
df_changing = pd.concat([ele['Changing'].dropna(axis=0) for ele in [df_175]])
normalized_ls_changing = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_changing)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_changing]]

# 7. "Return"
df_return = pd.concat([ele['Return'].dropna(axis=0) for ele in [df_175]])
normalized_ls_return = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_return)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_return]]

# 8. "Other"
df_other = pd.concat([ele['Other'].dropna(axis=0) for ele in [df_175]])
normalized_ls_other = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_other)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_other]]

# 9. "Inform"
df_inform = pd.concat([ele['Inform'].dropna(axis=0) for ele in [df_175]])
normalized_ls_inform = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_inform)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_inform]]

# 10. "Request"
df_request = pd.concat([ele['Request'].dropna(axis=0) for ele in [df_175]])
normalized_ls_request = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_request)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_request]]

# 11. "ID_product":

df_ID_product = pd.concat([ele['ID_product'].dropna(axis=0) for ele in [df_175]])
normalized_ls_ID_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_ID_product)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_ID_product]]


# 12. "size_product"
df_size_product = pd.concat([ele['size_product'].dropna(axis=0) for ele in [df_175]])
normalized_ls_size = list(df_size_product)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_size]]
# print(normalized_ls_size_product)

# 13. "color_product"
df_color_product = pd.concat([ele['color_product'].dropna(axis=0) for ele in [df_175]])
normalized_ls_color = list(df_color_product)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_color]]
# print(normalized_ls_color)

# 14. "amount_product"
df_amount_product = pd.concat([ele['amount_product'].dropna(axis=0) for ele in [df_175]])
normalized_ls_amount = list(df_amount_product)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_amount]]
# print(normalized_ls_color)


# 15 "Id member"
df_Id_member = pd.concat([ele['Id member'].dropna(axis=0) for ele in [df_175]])
normalized_ls_Id_mem = list(df_Id_member)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_Id_mem]]



# 16 "phone member"
df_phone_member = pd.concat([ele['phone member'].dropna(axis=0) for ele in [df_175]])
normalized_ls_phone_mem = list(df_phone_member)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_phone_mem]]

#  17 "addr member"
df_addr_member = pd.concat([ele['addr member'].dropna(axis=0) for ele in [df_175]])
normalized_ls_addr_mem = list(df_addr_member)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_addr_mem]]


# Get request cover Id_product
df_request_id_product = pd.concat([ele[['Request', 'ID_product']].dropna(axis=0) for ele in [df_175]])
normalized_ls_request_id_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_request_id_product['Request'])]
ls_request_id_product = [ele[1:-1] if '"' in ele else ele for ele in normalized_ls_request_id_product]



df_Order_summary = pd.concat([ele[['Request', 'ID_product', 'size_product','color_product','amount_product']] for ele in [df_175]])
df_Order_summary.fillna('', inplace = True)
df_Order_summary = df_Order_summary[df_Order_summary['Request'] != '']
# print(df_ID_product.head(20))


ls_Request = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_Order_summary['Request'])]
ls_ID_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_Order_summary['ID_product'])]
ls_size_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_Order_summary['size_product'])]
ls_color_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_Order_summary['color_product'])]
ls_amount_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_Order_summary['amount_product'])]
# print(len(ls_Request))
# print(len(ls_ID_product))
# print(len(ls_amount_product))
# print(ls_Request[-1])
# print(ls_ID_product[-1])
# print(ls_amount_product[-1])



df_InfoMember_summary = pd.concat([ele[['Inform', 'Id member', 'phone member','addr member']] for ele in [df_175]])
df_InfoMember_summary.fillna('', inplace = True)
df_InfoMember_summary = df_InfoMember_summary[df_InfoMember_summary['Inform'] != '']



ls_InfoMember = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_InfoMember_summary['Inform'])]
ls_ID_member = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_InfoMember_summary['Id member'])]
ls_phone_member = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_InfoMember_summary['phone member'])]
ls_addr_member = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_InfoMember_summary['addr member'])]


def find_first_state(start):
    if start == 'user_image':
        return ['inform_img']
    elif start == 'info_product':
        return ['hello', 'request']
    elif start == 'chat_emp':
        return ['hello', 'connect', 'end']
    elif start == 'order_':
        return ['hello', 'order']

def sentence_generator(state):
    ls = []
    if state == 'inform_img':
        # print('Customer: [Hinh anh san pham]')
        ls = ['Customer: [Hinh anh san pham]']
    elif state == 'id_product':
        ls = ls_request_id_product
        # print('Shop: San pham [id_product] nay phai khong a ?')
    elif state == 'hello':
        ls = ls_of_ls[2]
    elif state == 'done':
        ls = ls_of_ls[3]
    elif state == 'connect':
        ls = ls_of_ls[4]
    elif state == 'request':
        ls = ls_of_ls[10]
    elif state == 'order':
        ls = ls_Request
    elif state == 'ok_1':
        ls = ls_InfoMember
    elif state == 'ok_2':
        ls = ['Cam on ban da dat hang', 'Shop xin cam on. Chuc ban mot ngay tot lanh', 'Cam on quy khach']
    else:
        # print('----', state)
        ls = [state]
    return ls

with open('rule.json', 'rb') as json_data:
    rules = json.loads(json_data.read())
    
    start = ''
    # state = 'user_image'
    

    with open('order_conversation.rtf', 'w') as file:
        writer = csv.writer(file)

        for i in range(500):
            
            state = 'order_'

            writer.writerow(['Conversation: ' + str(i)])

            while(True):
                
                if state in rules:
                    start = state
                    state = find_first_state(start)
                    # print("hi")
                    if len(state) == 1:
                        state = state[0]
                    else:
                        state = random.choice(state)


                if state == "end":
                    break
                
                list_sentence = sentence_generator(state)
                

                if state == 'order':
                    tmp = random.choice(range(len(list_sentence)))
                    id_pro = ls_ID_product[tmp]
                    size_pro = ls_size_product[tmp]
                    color_pro = ls_color_product[tmp]
                    amount_pro = ls_amount_product[tmp]
                    writer.writerow(['Khach: ' + list_sentence[tmp]])
                    # print('Khach: ' + list_sentence[tmp])
                    if id_pro == '':
                        writer.writerow(['Shop: Da ban muon lay san pham gi a ?'])
                        # print('Shop: Da ban muon lay san pham gi a ?')
                        id_pro = random.choice(ls_of_ls[11])
                        writer.writerow(['Khach: ' + id_pro])
                        # print('Khach: ' + id_pro)
                    if size_pro == '':
                        writer.writerow(['Shop: Da ban muon lay size gi a ?'])
                        # print('Shop: Da ban muon lay size gi a ?')
                        size_pro = random.choice(ls_of_ls[12])
                        writer.writerow(['Khach: ' + size_pro])
                        # print('Khach: ' + size_pro)
                    if color_pro == '':
                        writer.writerow(['Shop: Da ban muon lay mau gi a ?'])
                        # print('Shop: Da ban muon lay mau gi a ?')
                        color_pro = random.choice(ls_of_ls[13])
                        writer.writerow(['Khach: ' + color_pro])
                        # print('Khach: ' + color_pro)
                    if amount_pro == '':
                        writer.writerow(['Shop: Da ban muon lay so luong nhu the nao a ?'])
                        # print('Shop: Da ban muon lay so luong nhu the nao a ?')
                        amount_pro = random.choice(ls_of_ls[14])
                        writer.writerow(['Khach: ' + amount_pro])
                        # print('Khach: ' + amount_pro)

                    ########### shop confirm ##########
                    writer.writerow(['Shop: Da, cua khach la: ' + id_pro + ' ' + size_pro + ' ' +  color_pro])
                    # print('Shop: Da, cua khach la: ' + id_pro + ' ' + size_pro + ' ' +  color_pro)

                elif state == 'ok_1':
                    tmp = random.choice(range(len(list_sentence)))
                    id_mem = ls_ID_member[tmp]
                    phone_mem = ls_phone_member[tmp]
                    addr_mem = ls_addr_member[tmp]

                    inform = list_sentence[tmp]
                    if id_mem in inform or phone_mem in inform or addr_mem in inform:
                        writer.writerow(['Khach: ' + inform])
                        # print('Khach: ' + inform)
                    if id_mem == '':
                        writer.writerow(['Shop: Cho shop xin ten khach hang voi a ?'])
                        # print('Shop: Cho shop xin ten khach hang voi a ?')
                        id_mem = random.choice(ls_of_ls[15])
                        writer.writerow(['Khach: ' + id_mem])
                        # print('Khach: ' + id_mem)
                    if phone_mem == '':
                        writer.writerow(['Shop: Cho shop xin sdt voi a ?'])
                        # print('Shop: Cho shop xin sdt voi a ?')
                        phone_mem = random.choice(ls_of_ls[16])
                        writer.writerow(['Khach: ' + phone_mem])
                        # print('Khach: ' + phone_mem)
                    if addr_mem == '':
                        writer.writerow(['Shop: Cho shop xin dia chi giao hang voi a ?'])
                        # print('Shop: Cho shop xin dia chi giao hang voi a ?')
                        addr_mem = random.choice(ls_of_ls[17])
                        writer.writerow(['Khach: ' + addr_mem])
                        # print('Khach: ' + addr_mem)
                    

                    ########### shop confirm ##########
                    writer.writerow(['Shop: Chot don'])
                    # print('Shop: Chot don')
                else:
                    writer.writerow(['Khach: ' + random.choice(list_sentence)])
                    # print('Khach: ' + random.choice(list_sentence))
                
                state = rules[start][state]
                # print(state)
        
                if state == "end":
                    break
                if len(state) == 1:
                    state = state[0]
                else:
                    state = random.choice(state)

                # print(state)
                if state == "end":
                    break
                