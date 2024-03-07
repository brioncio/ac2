def eq_seg_grau(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    primeira_raiz = (-b + (delta ** 0.5)) / (2 * a)
    segunda_raiz = (-b - (delta ** 0.5)) / (2 * a)
    
    print("O valor da primeira raiz é: ", primeira_raiz)
    print("O valor da segunda raiz é: ", segunda_raiz)



def bissexto(ano):
    if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
        return True
    else:
        return False
    
def main():
    print(eq_seg_grau(1,-6,8))
    print(bissexto(2024))

main()