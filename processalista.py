# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
  impares = [num for num in lista if num % 2 != 0]
  if impares:
    return max(impares)
  else:
    return None

# Encontra e retorna o menor número impar presente na lista
def menor_impar(lista):
  impares = [num for num in lista if num % 2 != 0]
  if impares:
    return min(impares)
  else:
    return None
# Encontra e retorna o maior e o menor número ímpar presentes na lista
def maior_menor_impar(lista):
  maior = maior_impar(lista)
  menor = menor_impar(lista)
  return maior, menor