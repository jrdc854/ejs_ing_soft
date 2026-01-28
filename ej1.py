def frio(lst: list) -> list:
    frios = []
    for i in lst:
        if i < 15:
            frios.append(i)
    return frios

def templado(lst: list) -> list:
    templados = []
    for i in lst:
        if i >= 15 and i <= 25:
            templados.append(i)
    return templados

def caluroso(lst:list) -> list:
    calurosos = []
    for i in lst:
        if i > 25:
            calurosos.append(i)
    return calurosos

def extremos(lst :list)-> list:
    maxima = 0
    minima = 0
    for i in lst:
        if maxima >= i:
            maxima = i
    for i in lst:
        if minima <= i:
            minima = i
    return maxima, minima

def clasificar_temperaturas(lst:list) -> None:
    frios = frio(lst)
    templados = templado(lst)
    calurosos = caluroso(lst)
    max, min = extremos(lst)
    return frios, templados, calurosos, max, min

def main():
    lst = [12, 14, 25, 30, 20, 28]
    frios, templados, calurosos, max, min =clasificar_temperaturas(lst)
    print(f'Fríos: {frios}')
    print(f'templados: {templados}')
    print(f'calurosos: {calurosos}')
    print(f'máxima: {max}')
    print(f'mínima: {min}')

main()
