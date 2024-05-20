class InputInteractive:
    
    def InitInput(self, message, callBack):
        value = input("\n" + message)
        callback(value)

    def LoopInput(self, message, callBack):
        value = 10
        while value != "0":
            value = input("\nPara sair do loop digite 0\n" + message)
            if(value != "0" ):
                callback(value)
    
    def InitNumberInput(self, message, callBack):
        value = int(input("\n" + message))
        callBack(value)

    def LoopNumberInput(self, message, callBack):
        value = 10
        while value != 0:
            value = int(input("\nPara sair do loop digite 0\n" + message))
            if(value != 0 ):
                callBack(value)
        
