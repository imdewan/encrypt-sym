
string_name = input("text: ")
dec=""
psswrd=input("password: ")
# Iterate over the string
for element in string_name:
    dec=dec+str(ord(element))+" "

res = ''.join(format(ord(i), '08b') for i in psswrd) #password binary
result=""


def cvrt(txtdec, bininput):
    if txtdec==" ":
        outputr=" "
    if txtdec=="0":
        if bininput=="1":
            outputr="8"
        else:
            outputr="5"
    if txtdec=="1":
        if bininput=="1":
            outputr="4"
        else:
            outputr="7"
    if txtdec=="2":
        if bininput=="1":
            outputr="7"
        else:
            outputr="4"
    if txtdec=="3":
        if bininput=="1":
            outputr="2"
        else:
            outputr="9"
    if txtdec=="4":
        if bininput=="1":
            outputr="1"
        else:
            outputr="2"
    if txtdec=="5":
        if bininput=="1":
            outputr="6"
        else:
            outputr="0"
    if txtdec=="6":
        if bininput=="1":
            outputr="9"
        else:
            outputr="6"

    if txtdec=="7":
        if bininput=="1":
            outputr="5"
        else:
            outputr="3"
    if txtdec=="8":
        if bininput=="1":
            outputr="3"
        else:
            outputr="1"
    if txtdec=="9":
        if bininput=="1":
            outputr="0"
        else:
            outputr="8"
    return(outputr)
output=""
elemr=""
for elementrr in dec:
    elemr=elementrr
    for elementoo in res:
        elemr=cvrt(elemr, elementoo)
    output=output+elemr


print("output: "+output)
