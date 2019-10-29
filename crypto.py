# this_is_a_secret_that_i_want_to_transmit

# tis _ asce _ esg _ htiwn _ otasi
# hsi_ertmsaeta_att_rnmt

# so now we want to write a python method to made the computer do this
#   Transcription Cipher

# original: this_is_a_secret_that_i_want_to_transmit
# encrypted:

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

# Decrypting

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]


    #if the text is not even
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]
        # the -1 gets up to the end the fastest

    return plainText

def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)