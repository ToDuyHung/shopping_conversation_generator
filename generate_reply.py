import pandas as pd
df_172 = pd.read_csv('172.csv')
df_173 = pd.read_csv('173.csv')
df_174 = pd.read_csv('174.csv')


df_text = pd.concat([ele['text'].dropna(axis=0) for ele in [df_172, df_173, df_174]])

# print(df_hello.describe())


# df_order = pd.concat([ele['Order'].dropna(axis=0) for ele in [df_172, df_173, df_174]])

# df_size_product = pd.concat([ele['size_product'].dropna(axis=0) for ele in [df_172, df_173, df_174]])

# print(df_size_product.describe())

# df_color_product = pd.concat([ele['color_product'].dropna(axis=0) for ele in [df_172, df_173, df_174]])


import csv
with open('test_reply.csv', 'w') as file:
    ls_column = list(df_172.columns)
    id_init = 1662000
    writer = csv.writer(file)
    writer.writerow(ls_column)

    for i in range(300):
        ls_result = ['' for _ in ls_column]
        ls_result[0] = id_init + i
        while True:
            hihi = str(df_text.sample().to_string().encode('utf-8'))
            if ':' not in hihi:
                # print(df_text.sample().to_string().encode('utf-8'))
                ls_result[ls_column.index('text')] = hihi
                break
        # ls_result[ls_column.index('Order')] = df_order.sample().to_string().encode('utf-8')
        # if i < 100:
        #     ls_result[ls_column.index('size_product')] = df_size_product.sample().to_string().encode('utf-8')
        # elif i < 200:
        #     ls_result[ls_column.index('color_product')] = df_color_product.sample().to_string().encode('utf-8')
        writer.writerow(ls_result)