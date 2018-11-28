class Tamagochi:
  def __init__(self):
    self.nome = 'sem_nome'
    self.nivel = 0

  def mostrar_nome(self):
    print(f"O nome do seu tamagochi é {self.nome}.")

  def mostrar_nivel(self):
    print(f"Nivel: {self.nivel}")

  def subir_nivel(self):
  	self.nivel += 1
  	print("")

  def mostrar_status(self):
  	self.mostrar_nome()
  	self.mostrar_nivel()

if __name__ == '__main__':
	tamagochi = Tamagochi()
	tamagochi.nome = "Null"
	tamagochi.mostrar_status()