# Count vowels in a string
# Problem_01

vowels="aeiou"
word="pavanbiradar"
count=0
for char in word:
    if char in vowels:
        count+=1
print(count)
