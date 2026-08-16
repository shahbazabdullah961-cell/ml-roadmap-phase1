string =input("Enter your text:")
data=string.lower()
data2=data.replace(".","").replace(",","").replace("?","").replace("''","").replace("!","").replace(":","")
data3=data2.split()

frequency={
    
}
for words in data3:
    if words in frequency:
        frequency[words] += 1
    else:
        frequency[words] = 1
    

print(frequency)

