price = {
    ("x",): 1,
    ("y",): 2
}

quantity = {
    ("x",): 10,
    ("y",): 20
}
# l1 = []
# for i in price.values():
#     l1.append(i)
# l2 = []
# for i in quantity.values():
#     l2.append(i)
# # print(l2)
# # print(l1)
# l3 = []
# for i in range(len(l1)):
#     l3.append((l1[i]*l2[i]))
# #print(l3)
# print(f"Total Bill = {sum(l3)} rupees")
for k,v1 in price.items():
    catageory = k[0]
    if k in quantity:
        price[k] = v1 * quantity[k]
print(price)

