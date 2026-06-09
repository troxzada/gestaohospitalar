import os


class Paciente:
    def __init__(self, nome, cpf, prioridade="Normal"):
        self.nome = nome
        self.cpf = cpf
        self.prioridade = prioridade
        self.proximo = None

    def __str__(self):
        return f"{self.nome} | CPF: {self.cpf} | Prioridade: {self.prioridade}"


class FilaHospitalar:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def adicionar_paciente(self, nome, cpf, prioridade="Normal"):
        novo_paciente = Paciente(nome, cpf, prioridade)

        if self.esta_vazia():
            self.inicio = novo_paciente
            self.fim = novo_paciente
        else:
            self.fim.proximo = novo_paciente
            self.fim = novo_paciente

        self.tamanho += 1
        print("\nPaciente adicionado à fila com sucesso.")

    def chamar_proximo(self):
        if self.esta_vazia():
            print("\nNão há pacientes na fila.")
            return None

        paciente_chamado = self.inicio
        self.inicio = self.inicio.proximo
        self.tamanho -= 1

        if self.esta_vazia():
            self.fim = None

        print("\nPaciente chamado para atendimento:")
        print(paciente_chamado)

        return paciente_chamado

    def primeiro_da_fila(self):
        if self.esta_vazia():
            print("\nA fila está vazia.")
        else:
            print("\nPrimeiro paciente da fila:")
            print(self.inicio)

    def mostrar_fila(self):
        if self.esta_vazia():
            print("\nA fila está vazia.")
            return

        atual = self.inicio
        posicao = 1

        print("\n=== FILA ATUAL DE PACIENTES ===")

        while atual is not None:
            print(f"{posicao}º - {atual}")
            atual = atual.proximo
            posicao += 1

        print(f"\nTotal de pacientes na fila: {self.tamanho}")

    def limpar_fila(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        print("\nFila limpa com sucesso.")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Entrada inválida. Digite novamente.")


def menu():
    fila = FilaHospitalar()

    while True:
        limpar_tela()

        print("=" * 40)
        print("      SISTEMA DE FILA HOSPITALAR")
        print("=" * 40)
        print("1 - Adicionar paciente")
        print("2 - Chamar próximo paciente")
        print("3 - Ver primeiro da fila")
        print("4 - Mostrar fila completa")
        print("5 - Mostrar quantidade de pacientes")
        print("6 - Limpar fila")
        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if not opcao:
            continue

        if opcao == "1":
            nome = ler_texto("Nome do paciente: ")
            cpf = ler_texto("CPF do paciente: ")

            print("\nPrioridade:")
            print("1 - Normal")
            print("2 - Preferencial")
            print("3 - Urgente")

            escolha_prioridade = input("Escolha a prioridade: ").strip()

            if escolha_prioridade == "2":
                prioridade = "Preferencial"
            elif escolha_prioridade == "3":
                prioridade = "Urgente"
            else:
                prioridade = "Normal"

            fila.adicionar_paciente(nome, cpf, prioridade)
            pausar()

        elif opcao == "2":
            fila.chamar_proximo()
            pausar()

        elif opcao == "3":
            fila.primeiro_da_fila()
            pausar()

        elif opcao == "4":
            fila.mostrar_fila()
            pausar()

        elif opcao == "5":
            print(f"\nQuantidade de pacientes na fila: {fila.tamanho}")
            pausar()

        elif opcao == "6":
            confirmar = input("Tem certeza que deseja limpar a fila? (s/n): ").strip().lower()

            if confirmar == "s":
                fila.limpar_fila()
            else:
                print("\nOperação cancelada.")

            pausar()

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
            pausar()


if __name__ == "__main__":
    menu()