# coding=utf-8
import pandas as pd
import csv
import random
import sys
df_172 = pd.read_csv('172.csv')
df_173 = pd.read_csv('173.csv')
df_174 = pd.read_csv('174.csv')

ls_of_ls = []

# 1. "text"
# Get text of shop (the text without 'Khach X:' ) and text of customer (the other)
df_text = pd.concat([ele['text'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
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

df_hello = pd.concat([ele['Hello'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_hello = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_hello)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_hello]]
# print(normalized_ls_hello)

# 3. "Done"
df_done = pd.concat([ele['Done'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_done = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_done)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_done]]


# 4. "Connect"
df_connect = pd.concat([ele['Connect'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_connect = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_connect)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_connect]]

# 5. "Order"
df_order = pd.concat([ele['Order'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_order = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_order)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_order]]
# print(normalized_ls_order)

# 6. "Changing"
df_changing = pd.concat([ele['Changing'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_changing = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_changing)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_changing]]

# 7. "Return"
df_return = pd.concat([ele['Return'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_return = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_return)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_return]]

# 8. "Other"
df_other = pd.concat([ele['Other'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_other = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_other)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_other]]

# 9. "Inform"
df_inform = pd.concat([ele['Inform'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_inform = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_inform)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_inform]]

# 10. "Request"
df_request = pd.concat([ele['Request'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_request = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_request)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_request]]

# 11. "ID_product"
df_ID_product = pd.concat([ele['ID_product'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_ID_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_ID_product)]
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_ID_product]]

# 12. "size_product"
df_size_product = pd.concat([ele['size_product'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_size = list(df_size_product)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_size]]
# print(normalized_ls_size_product)

# 13. "color_product"
df_color_product = pd.concat([ele['color_product'].dropna(axis=0) for ele in [df_172, df_173, df_174]])
normalized_ls_color = list(df_color_product)
ls_of_ls += [[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_color]]
# print(normalized_ls_color)

# 14. "material_product"
# 15. "cost_product"
# 16. "amount_product"
# 17. "name_promotion"
# 18. "content_promotion"
# 19. "Id member"
# 20. "phone member"
# 21. "level member"
# 22. "benefit member"
# 23. "feedback"
# 24. "shiping fee"
# 25. "size customer"
# 26. "height customer"
# 27. "weight customer"
# 28. "addr store"
# 29. "phone store"
# 30. "addr member"

rule = sys.argv[1:]
# print(rule)


with open('result.rtf', 'w') as file:
    # ls_column = list(df_172.columns)
    # id_init = 1662000
    writer = csv.writer(file)
    # writer.writerow(ls_column)
    # len_hello = len(normalized_ls_hello)
    # len_order = len(normalized_ls_order)
    # len_size = len(normalized_ls_size)
    # len_color = len(normalized_ls_color)
    # len_text = len(normalized_ls_text)

    for i in range(10):
        # ls_result = ['' for _ in ls_column]
        writer.writerow(['Conversation: ' + str(i)])
        
        for ele in rule:
            num_rule = int(ele)
            tmp = random.choice(range(len(ls_of_ls[num_rule])))
            # print(tmp)
            if num_rule != 0:
                writer.writerow(['Khach ' + str(i) + ': ' + ls_of_ls[num_rule][tmp]])
            else:
                writer.writerow(['Shop: ' + ls_of_ls[num_rule][tmp]])
        writer.writerow([])

