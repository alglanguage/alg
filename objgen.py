from Objects.varObject       import VariableObject
from Objects.conditionObject import ConditionObject
from Objects.builtinObject   import BuiltInFunctionObject
from Objects.commentObject   import CommentObject
from Objects.loopObject      import LoopObject

class ObjectGenerator():


    def __init__(self, source_ast):
        self.source_ast  = source_ast['main_scope']
        self.exec_string = ""


    def object_definer(self, isGettingBody):
        for ast in self.source_ast:
            if self.check_ast('VariableDecleration', ast):
                gen_var = VariableObject(ast)
                self.exec_string += gen_var.transpile() + '\n'

            if self.check_ast('ConditionalStatement', ast):
                gen_condition = ConditionObject(ast, 1)
                self.exec_string += gen_condition.transpile() + '\n'

            if self.check_ast('PrebuiltFunction', ast):
                gen_builtin = BuiltInFunctionObject(ast)
                self.exec_string += gen_builtin.transpile() + "\n"

            if self.check_ast('Comment', ast):
                gen_comment = CommentObject(ast)
                self.exec_string += gen_comment.transpile() + "\n"

            if self.check_ast('ForLoop', ast):
                gen_loop = LoopObject(ast, 1)
                self.exec_string += gen_loop.transpile() + "\n"

        return self.exec_string


    def check_ast(self, astName, ast):
        try:
            if ast[astName]: return True
        except: return False
