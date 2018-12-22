import tamagochi as tmg
import tamagochidb
import logger

# inicia o projeto
if __name__ == '__main__':
    tamagochi = tmg.Tamagochi()
    tamagochi.nome = input("Nome: ").strip()
    tamagochi.verificar_nome(tamagochi.nome)
    tamagochidb.adicionar(tamagochi.nome, tamagochi.nivel)
    logger.log_info(f"Tamagochi criado - Nome: {tamagochi.nome}")
    tamagochi.mostrar_profile()
