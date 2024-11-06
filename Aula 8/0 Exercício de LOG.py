from datetime import datetime

def registrar_evento():
    descricao = input("Insira a descrição do evento: ")
    with open("sistema_log.txt", "a") as arquivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"{timestamp} - {descricao}\n")
    print("Evento registrado com sucesso.")

def visualizar_log():
    try:
        with open("sistema_log.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print("\nLog de eventos:")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo de log não encontrado.")

def main():
    while True:
        opcao = input("Digite '1' para registrar um evento, '2' para visualizar o log ou '0' para sair: ")
        if opcao == "1":
            registrar_evento()
        elif opcao == "2":
            visualizar_log()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()