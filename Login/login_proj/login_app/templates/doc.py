def update_tuple(*args, tup, index):
    t1 = tup[0:index] + args + tup[index:]
    return t1


up = update_tuple(6, 8,10,tup=(1,2,3,4,5), index=4)
print(up)


def update_tuple(val, tup, index):
    lst = list(tup)
    lst[index] = val
    t1 = tuple(lst)
    return t1

up = update_tuple(val=6,tup=(1,2,3,4,5), index=0)
print(up)
