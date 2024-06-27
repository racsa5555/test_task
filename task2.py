data = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]

def group_data(data):
    unique_data = set(tuple(item)+(0,) for item in data)
    tuple_data = [tuple(item) for item in data]
    unique_data_dict = {(id,version): count for id, version,count in unique_data}
    for item in tuple_data:
        if item in unique_data_dict.keys():
            unique_data_dict[item] += 1

    res = []

    for k,v in unique_data_dict.items():
        res.append(list(k+(v,)))
    
    return res

print(group_data(data))
