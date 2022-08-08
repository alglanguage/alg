import os
import sys
import lexer
import pars
import objgen
import platform

def main():
    
    content  = ""    
    path     = os.getcwd() 

    try: fileName = sys.argv[1]
    except:
        return

    try:
        print('Fatal Error: Expected 1 argument found 2 (' + sys.argv[1] + ", " + sys.argv[2] + ')')
        return
    except: pass

    try:
        with open(path + "/" + fileName, "r") as file:
            content = file.read()
    except: 
        print('Cannot find "' + fileName + '"')

    lex = lexer.Lexer()

    tokens = lex.tokenize(content)

    Parser = pars.Parser(tokens)

    source_ast = Parser.parse(tokens)

    object_generator = objgen.ObjectGenerator(source_ast)

    exec_string = object_generator.object_definer(False)

    exec(exec_string)

main()

