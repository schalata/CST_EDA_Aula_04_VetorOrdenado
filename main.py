from VetorOrdenado import VetorOrdenado

if __name__ == '__main__':
  vetor = VetorOrdenado(10)
  vetor.imprime()
  vetor.insere(6)
  vetor.insere(4)
  vetor.insere(5)
  vetor.insere(4)
  vetor.insere(8)
  vetor.imprime()
  print(vetor.pesquisa_linear(0))
  print(vetor.pesquisa_linear(7))
  print(vetor.pesquisa_linear(9))
  print(vetor.pesquisa_linear(4))