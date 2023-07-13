def remove_from_list_item(item_list, removable):
    for i in item_list:
        if removable in i:
            item_list.remove(i)
    freshed_list = list(filter(('|').__ne__, item_list))
    freshed_list = list(filter(('| ').__ne__, item_list))
    return freshed_list


# test = ['|||||', '1216', ' |||||||||| ', 'saom', '||||', 'asd', ' || || |||| ', 'defg', ' ||||', '| ', ' |', '4', ' | ']
# a = remove_from_list_item(test, '|')
# print(a)