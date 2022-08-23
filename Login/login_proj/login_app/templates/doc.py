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



import random
card_type=["diamond", "heart", "spade", "club"]
card_point=["A","K","Q","J","2","3","4","5","6","7","8","9","10"]
deck = []
for i in range(len(card_point)):
    for j in range(len(card_type)):
        deck.append(f"{card_point[i]} of {card_type[j]}")
# print(deck)

print(random.choice(deck))
# rand = random.randrange(card["diamond"])