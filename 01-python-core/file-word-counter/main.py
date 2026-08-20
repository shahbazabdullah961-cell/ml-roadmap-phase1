with open("WWW.txt", "r") as file:
    ReadFile = file.readlines()

NoofLines = 0
NoofWords = 0
NoofChars = 0

for tray in ReadFile:
    NoofLines += 1
    NoofChars += len(tray)
    
    Words = tray.split()
    NoofWords += len(Words)
    print(Words)

print(f"Total Lines: {NoofLines}")
print(f"Total Words: {NoofWords}")
print(f"Total Characters: {NoofChars}")



