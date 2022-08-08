class VariableObject():

    def __init__(self, ast):
        self.ast = ast['VariableDecleration']
        self.exec_string = ""

    
    def transpile(self):
        for val in self.ast:
            try: self.exec_string += val['name'] + " = "
            except: pass
            try: self.exec_string += str(val['value'])
            except: pass

        return self.exec_string
