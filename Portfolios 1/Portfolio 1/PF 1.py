choice = input("Would you like to use Encryption or Decryption?\nPlease type the one you would like to use:\n")
if choice == "Encryption" or "encryption":
    print("You have selected Encryption, the message you type can only include letters from the alphabet!")
    message = input("Enter message: ")
    encryptedKey = int(input("Enter key (key must be between 0 and 25): "))

    encryptedText = ""

    for i in range(len(message)):
        if ord(message[i]) == 32:
            encryptedText += chr(ord(message[i]))

        elif (ord(message[i]) + encryptedKey > 90) and (ord(message[i]) <= 96):
            temp = (ord(message[i]) + encryptedKey) - 90
            encryptedText += chr(64+temp)
            
        elif ord(message[i]) + encryptedKey > 122:
            temp = (ord(message[i]) + encryptedKey) - 122  
            encryptedText += chr(96+temp)

        else:
            encryptedText += chr(ord(message[i]) + encryptedKey)

    print("Your encrypted message is: " + encryptedText)
    
elif choice == "Decryption" or "decryption":
    print("Message can only be Lower or Uppercase alphabet")
    encryptedMessage = input("Enter encrypted Text: ")
    decryptedKey = int(input("Enter key (key must be between 0 and 25): "))

    decryptedText = ""

    for i in range(len(encryptedMessage)):
        if ord(encryptedMessage[i]) == 32:
            decryptedText += chr(ord(encryptedMessage[i]))
            
        elif (ord(encryptedMessage[i]) - decryptedKey) < 65:
            temp = (ord(encryptedMessage[i]) - decryptedKey) + 26
            decryptedText += chr(temp)    

        elif ((ord(encryptedMessage[i]) - decryptedKey) < 97) and ((ord(encryptedMessage[i]) - decryptedKey) > 90):
            temp = (ord(encryptedMessage[i]) - decryptedKey) + 26
            decryptedText += chr(temp)
            
        else:
            decryptedText += chr(ord(encrpMessage[i]) - decryptedKey)

    print("Your decrypted text is:: " + decryptedText)
else:
    print("Please enter which you would like to use?\n")
