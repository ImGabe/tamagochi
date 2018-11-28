class Tamagochi:
  def __init__(self):
    self.nome = 'sem_nome'
    self.nivel = 0
    self.energia = 100

  # nome
  def mostrar_nome(self):
    print(f"O nome do seu tamagochi é {self.nome}.")

  # nivel
  def mostrar_nivel(self):
    print(f"Nivel: {self.nivel}")

  def subir_nivel(self):
    self.nivel += 1
    print(f"{self.nome} upou para o nível {self.nivel}")

  # energia
  def mostrar_energia(self):
    print(f"Energia: {self.energia}")

  def mostrar_profile(self):
    self.mostrar_nome()
    self.mostrar_nivel()
    self.mostrar_energia()

  def mostrar_status(self):
    self.mostrar_nivel()
    self.mostrar_energia()

# inicia 
if __name__ == '__main__':
  tamagochi = Tamagochi()
  tamagochi.nome = input("Nome: ")
  tamagochi.mostrar_profile()