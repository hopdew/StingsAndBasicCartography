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