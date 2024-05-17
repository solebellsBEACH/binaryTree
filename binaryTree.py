from node import No

def main():
    print("Running binaryTree file !!")

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    def __str__(self):
        return self._str_recursivo(self.raiz, '', True)

    def _str_recursivo(self, no_atual, prefixo, eh_ult):
        if no_atual is None:
            return ''

        linha = ''
        linha += prefixo
        linha += '|-- ' if eh_ult else '|-- '
        linha += str(no_atual.valor) + '\n'

        prefixo += '    ' if eh_ult else '|   '
        linha += self._str_recursivo(no_atual.esquerda, prefixo, False)
        linha += self._str_recursivo(no_atual.direita, prefixo, True)

        return linha
