class BuiltInFunctionObject():

    def __init__(self, ast):
        # This will hold the dictionary version of the AST
        self.ast = ast['PrebuiltFunction']
        # This will hold the exec string being formed
        self.exec_string = ""


    def transpile(self):
        """ Transpile 
        
        This method will use the AST in order to create a python version of the Y#
        generated dictionary AST.

        return:
            exec_string (str) : The python transpiled code
        """
        
        for ast in self.ast:
            
            # Get the name of the builtin function being called
            try:
                if ast['type'] == "print":
                    self.exec_string += "print("
            except: pass

            # Get arguments for the function being called
            #TODO Add support for more than one argument
            try: self.exec_string += str(ast['arguments'][0]) + ")"
            except: pass

        return self.exec_string
