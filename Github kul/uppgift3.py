password = 'python'
succeded = False

while succeded == False:
    attempt = input('Vad är lösenordet?')
    if attempt == password:
        print('Korrekt!')
        succeded = True
    else:
        print('Försök igen')



