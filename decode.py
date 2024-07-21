# this code used to decode any text message
# for leaning purpose
# powerd by mosa technologies 
# its end to end encrypted 
message = str(input('input your message for decoding : '))
decoded = ''
for words in message:
    words = words.lower()
    if words == 'a':
        words = '{'
    decoding = ord(words) - 1
    decoded += chr(decoding)

print(decoded)

