class InputInteractive:
    
    def InitInput(self, message):
        value = input("\n" + message)

    def LoopInput(self, message):
        value = 10
        while value != "0":
            value = input("\n Para sair do loop digite 0\n" + message)
    
    def InitNumberInput(self, message):
        value = int(input("\n" + message))

    def LoopNumberInput(self, message):
        value = 10
        while value != 0:
            value = int(input("\n Para sair do loop digite 0\n" + message))
        
