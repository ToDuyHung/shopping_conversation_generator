import pandas as pd
import csv

df_175 = pd.read_csv('175.csv')

# new_df = df['Request']['id_product'].dropna(axis =0)
# df1 = df[['Request', 'ID_product']].dropna(axis = 0)
# print(df1.head(5))

# df_ID_product = pd.concat([ele[['Request', 'ID_product']].dropna(axis=0) for ele in [df_175]])
# normalized_ls_ID_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_ID_product['Request'])]
# print([[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_ID_product]])


# df_ID_product = pd.concat([ele[['Request', 'ID_product', 'size_product']] for ele in [df_175]])
# # print(df_ID_product.head(10))
# # normalized_ls_ID_product = [ele[ele.index(':')+2:] if ':' in ele else ele for ele in list(df_ID_product['Request'])]
# # print([[ele[1:-1] if '"' in ele else ele for ele in normalized_ls_ID_product]])

# # print(df_ID_product['Request'])

# df_ID_product.fillna("", inplace = True)
# df_ID_product = df_ID_product[df_ID_product['Request'] != '']
# # print(df_ID_product.head(20))

# ls_Request = list(df_ID_product['Request'])
# ls_ID_product = list(df_ID_product['ID_product'])
# ls_size_product = list(df_ID_product['size_product'])
# print(ls_Request[-1])
# print(ls_ID_product[-1])
# print(ls_size_product[-1])


# df_ID_product.fillna("", inplace = True)
# df_ID_product = df_ID_product[df_ID_product['Request'] != '']
# # print(df_ID_product.head(20))

# ls_Request = list(df_ID_product['Request'])
# ls_ID_product = list(df_ID_product['ID_product'])
# ls_size_product = list(df_ID_product['size_product'])
# print(ls_Request[-1])
# print(ls_ID_product[-1])
# print(ls_size_product[-1])

df_text_summary = pd.concat([ele[['text', 'Id member', 'phone member','addr member']] for ele in [df_175]])
df_text_summary.fillna('', inplace = True)
df_text_summary = df_text_summary[df_text_summary['phone member'] != '' or df_text_summary['addr member'] != '']

print(df_text_summary)