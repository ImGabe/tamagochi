from random import randint

class Tamagochi:
  def __init__(self):
    self.nome = 'sem_nome'
    self.nivel = 0
    self.fome = 0
    self.vida = 100
    self.energia = 100
    self.felicidade = 100
    self.vivo = True

  # nome
  def mostrar_nome(self):
    print(f"O nome do seu tamagochi é {self.nome}.")

  # nivel
  def mostrar_nivel(self):
    print(f"Nivel: {self.nivel}")

  def subir_nivel(self):
    self.nivel += 1
    print(f"{self.nome} upou para o nível {self.nivel}")

  # fome
  def mostrar_fome(self):
    print(f"Fome: {self.fome}")

  def subir_fome(self):
    n = randint(1, 10)
    self.fome += n

  def descer_fome(self):
    n = randint(1, 10)
    self.fome -= n

  # vida 
  def mostrar_vida(self):
    print(f"Vida: {self.vida}")

  def subir_vida(self):
    n = randint(1, 10)
    self.vida += n

  def descer_vida(self):
    n = randint(1, 10)
    self.vida -= n

  # energia
  def mostrar_energia(self):
    print(f"Energia: {self.energia}")

  def subir_energia(self):
    n = randint(1, 10)
    self.energia += n

  def descer_energia(self):
    n = randint(1, 10)
    self.energia -= n

  # felicidade
  def mostrar_felicidade(self):
    print(f"Felicidade: {self.felicidade}")

  def subir_felicidade(self):
    n = randint(1, 10)
    self.felicidade += n

  def descer_felicidade(self):
    n = randint(1, 10)
    self.felicidade -= n

  # Profile e Status
  def mostrar_profile(self):
    self.mostrar_nome()
    self.mostrar_nivel()
    self.mostrar_fome()
    self.mostrar_vida()
    self.mostrar_energia()
    self.mostrar_felicidade()

  def mostrar_status(self):
    self.mostrar_nivel()
    self.mostrar_fome()
    self.mostrar_vida()
    self.mostrar_energia()
    self.mostrar_felicidade()

# inicia o projeto
if __name__ == '__main__':
  tamagochi = Tamagochi()
  tamagochi.nome = "Jabe"
  tamagochi.mostrar_profile()