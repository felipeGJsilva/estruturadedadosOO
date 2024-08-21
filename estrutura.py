class Pilha:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.pilha = []
        
    def is_empty(self):
        return len(self.pilha) == 0
    
  
    def push(self, item):
        if len(self.pilha) < self.tamanho_maximo:
            self.pilha.append(item)
        else:
            print("a pilha esta cheia")

    def pop(self):
        if not self.is_empty():
            return self.pilha.pop()
        else:
            print("a pilha esta vazia.")
    
    def peek(self):
        if not self.is_empty():
            return self.pilha[-1]
        else:
            print("a pilha está vazia.")

    def mostrar_pilha(self):
        print("pilha:", self.pilha)

def main():
    tamanho_maximo =  int(input("digite o tamanho maximo da pilha: "))
    pilha = Pilha(tamanho_maximo)

    while True:
        print("--------------------------------------")
        print("\n1. adicionar (push)")
        print("2. remover (pop)")
        print("3. ver o topo (peek)")
        print("4. sair")
        opcao = input("escolha uma opção: ")

        if opcao == "1":
            item = input("Elemento: ")
            pilha.push(item)
        elif opcao == "2":
            pilha.pop()
        elif opcao == "3":
            pilha.peek()
        elif opcao == "4":
            break
        else:
            print("opção invalida.")

        pilha.mostrar_pilha()

if __name__ == "__main__":
    main()