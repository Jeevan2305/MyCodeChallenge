# Merge two dictionaries.
def merge_dicts(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1:
            dict1.update({k:list(dict1.get(k))})
            dict1[k].append(v)
        else:
            dict1[k] = v
           
    return dict1

d1 = {1:'a', 2:'b', 3:'c', 4:'d'}
d2 = {5:'e', 6:'f', 7:'g', 8:'h', 1:'i'}

print("Merged Dictionary : ",merge_dicts(d1, d2))
