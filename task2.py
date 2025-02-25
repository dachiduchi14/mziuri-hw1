def ricxvebi(num):
    number_str = str(abs(num))
    total = 0
    
    for digit in number_str:
        total += int(digit)
        
    return total


print(ricxvebi(3792487327487329))
print(ricxvebi(6737247324766))