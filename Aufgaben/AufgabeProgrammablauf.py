kartenstapel = ["gr7", "gl2" , "+4"]
while len(kartenstapel) !=0 :
    print(kartenstapel)
    aktuelleKarte = kartenstapel.pop(0)
    if aktuelleKarte == +4 :
        print("+4 kann gespielt werden")
        break 
if len(kartenstapel) ==0:
    print("Stapel ist leer")
else:
    print("Stapel ist nicht leer")
    
#while ist ein loop und if eine Verzweigung