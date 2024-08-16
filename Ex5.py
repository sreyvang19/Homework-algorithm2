# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
text = "454639"
count_odd = 0
count_even = 0
for i in range(len(text)):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Even number",count_even)
print("Odd number",count_odd)

# Q2 - Sum all number
text = "454639"
sum = 0
for i in range(len(text)):
    sum += int(text[i])
print(sum)

# Q3 - Sum only even number 
text = "454639"
sum = 0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        sum += int(text[i])
print(sum)

# Q4 - Reverse
text = "454639"
result = ""
last_index = len(text) - 1
for i in range(len(text)):
    result += text[last_index - i]
print(result)