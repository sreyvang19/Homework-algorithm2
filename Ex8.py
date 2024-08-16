# #Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
text = "9394884039"
# sum = 0
# for i in range(len(text)):
#     if text[i] == "8":
#         sum += 1
# print(sum)

# Q2 - What is first index of letter 8
isFound = False
for i in range(len(text)):
     if (text[i] == "8") and not isFound:
           print("First index letter 8:", i)
           isFound = True