# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# text = "3 4 5 6"
# number = " "
# for i in range(len(text)):
#     if text[i] != " ":
#         number += text[i]
# print(number)

# Q2 - Multiple each letter by 2 result = "6 8 10 12"
text = "3 4 5 6"
result = 0
total = " "
for i in range(len(text)):
    if text[i] != " ":
        result = int(text[i])*2
        total += str(result) + str(" ")
print(total)