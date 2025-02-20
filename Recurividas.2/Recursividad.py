

#Secuencia de Fibonacci

def Fibonacci(n):
    if n ==0 or n == 1: 
        return n
    else:   
        return Fibonacci(n-1) + Fibonacci(n-2)  

print(Fibonacci(10))

# Forma iterada de contar libros
libros = [50, 100, 75, 67, 300, 200]

total = 0

for libro in libros:
    total += libro

print(total)

# Forma recursiva

def totalPaginas (libross):
    if len(libross) == 1:
        return libross[0]       
    return libross[0] + totalPaginas(libross[1:])

    totalPaginas([50, 100, 75, 67, 300, 200])

print(totalPaginas([50, 100, 75, 67, 300, 200]))
