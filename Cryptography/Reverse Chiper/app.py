from fnmatch import translate


message = input("Enter Message : ")
translate = ""
i = len(message) -1 
while i>=0:
    translate = translate + message[i]
    i = i - 1
print(translate)