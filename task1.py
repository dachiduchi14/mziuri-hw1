def didiasoebi(sityva):
    xmovnebi = "a , e , i , o , u"
    result = ""
    
    for char in sityva:
        if char.lower() in xmovnebi:
            result += char.upper()
        else:
            result += char
            
    return result

print(didiasoebi("dachi"))
print(didiasoebi("shota"))