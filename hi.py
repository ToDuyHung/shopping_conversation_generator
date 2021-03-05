with open('test.rtf', 'w') as file:
    # ls_column = list(df_172.columns)
    # id_init = 1662000
    writer = csv.writer(file)
    # writer.writerow(ls_column)
    len_hello = len(normalized_ls_hello)
    len_order = len(normalized_ls_order)
    len_size = len(normalized_ls_size)
    len_color = len(normalized_ls_color)
    len_text = len(normalized_ls_text)

    for i in range(300):
        # ls_result = ['' for _ in ls_column]
        writer.writerow(['Conversation: ' + str(i)])
        
        tmp = random.choice(range(len_hello))
        # print(tmp)
        writer.writerow(['Khach ' + str(i) + ': ' + normalized_ls_hello[tmp]])

        tmp = random.choice(range(len_order))
        # print(tmp)

        writer.writerow(['Khach ' + str(i) + ': ' + normalized_ls_order[tmp]])

        if i < 100:
            tmp = random.choice(range(len_color))
            # print(tmp)
            writer.writerow(['Khach ' + str(i) + ': ' + normalized_ls_color[tmp]])
        elif i < 200:
            tmp = random.choice(range(len_size))
            # print(tmp)
            writer.writerow(['Khach ' + str(i) + ': ' + normalized_ls_size[tmp]])

        tmp = random.choice(range(len_text))
        writer.writerow(['Shop: ' + normalized_ls_text[tmp]])

        writer.writerow([])