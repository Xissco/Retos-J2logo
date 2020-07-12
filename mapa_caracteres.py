def es_letra(caracter): return 1 if 96<ord(caracter)<123 else 0

def mapa_caracteres(palabra):
  palabra=palabra.lower()
  contador = 0
  for i in range(len(palabra)):
    if (es_letra(palabra[i])):
      palabra = palabra.replace(palabra[i],str(contador),-1)
      contador += 1
  return [int(letra) for letra in palabra]

print(mapa_caracteres("abcd"))
print(mapa_caracteres('aabbb'))
print(mapa_caracteres('zagzdaa'))
print(mapa_caracteres('baaacbb'))