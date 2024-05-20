import binaryTree
import inputInteractive

print("Running main file !!")

binaryTree.main()

arvore = binaryTree.ArvoreBinaria()
prompt = inputInteractive.InputInteractive()
print("Uma arvore binária foi iniciada !!")
prompt.LoopNumberInput("Digite um novo valor: ", arvore.inserir )

print(arvore)
