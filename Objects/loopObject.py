import Objects.conditionObject
from Objects.varObject       import VariableObject
from Objects.builtinObject   import BuiltInFunctionObject
from Objects.commentObject   import CommentObject

class LoopObject(object):

	def __init__(self, ast, nesting_count):
		self.ast = ast['ForLoop']
		self.exec_string = ""
		self.nesting_count = nesting_count


	def transpile(self):
		initValName = ""
		initVal     = ""
		comparison  = ""
		incrementer = ""
		endVal      = ""
		body        = []

		for val in self.ast:
			try: initValName = val['initialValueName']
			except: pass

			try: initVal = val['initialValue']
			except: pass

			try: comparison = val['comparison']
			except: pass

			try: endVal = val['endValue']
			except: pass

			try: incrementer = val['incrementer']
			except: pass

			try: body = val['body']
			except: pass

		if incrementer[0] == "+": incrementer = incrementer[1:len(incrementer)]

		self.exec_string += "for " + initValName + " in range(" + str(initVal) + ", " + str(endVal) + ", " + incrementer + "):\n"

		self.exec_string += self.transpile_body(body, self.nesting_count)

		return self.exec_string


	def transpile_body(self, body_ast, nesting_count):
		body_exec_string = ""

		for ast in body_ast:

			if self.check_ast('VariableDecleration', ast):
				var_obj = VariableObject(ast)
				transpile = var_obj.transpile()
				if self.should_dedent_trailing(ast, self.ast):
					body_exec_string += ("   " * (nesting_count - 1)) + transpile + "\n"
				else:
					body_exec_string += ("   " * nesting_count) + transpile + "\n"

			if self.check_ast('PrebuiltFunction', ast):
				gen_builtin = BuiltInFunctionObject(ast)
				transpile = gen_builtin.transpile()
				if self.should_dedent_trailing(ast, self.ast):
					body_exec_string += ("   " * (nesting_count - 1)) + transpile + "\n"
				else:
					body_exec_string += ("   " * nesting_count) + transpile + "\n"

			if self.check_ast('Comment', ast):
				gen_comment = CommentObject(ast)
				transpile = gen_comment.transpile()
				if self.should_dedent_trailing(ast, self.ast):
					body_exec_string += ("   " * (nesting_count - 1)) + transpile + "\n"
				else:
					body_exec_string += ("   " * nesting_count) + transpile + "\n"

			if self.check_ast('ConditionalStatement', ast):
				if self.should_increment_nest_count(ast, self.ast):
					nesting_count += 1
				condition_obj = Objects.conditionObject.ConditionObject(ast, nesting_count)
				body_exec_string += ("   " * (nesting_count - 1)) + condition_obj.transpile()
			if self.check_ast('ForLoop', ast):
				if self.should_increment_nest_count(ast, self.ast):
					nesting_count += 1
				loop_obj = LoopObject(ast, nesting_count)
				if nesting_count == 2: 
					body_exec_string += "   " + loop_obj.transpile()
				else: 
					body_exec_string += ("   " * (nesting_count - 1)) + loop_obj.transpile()
		
		return body_exec_string

	
	def check_ast(self, astName, ast):
		try:
			if ast[astName] == []: return True
			if ast[astName]: return True
		except: return False



	def should_dedent_trailing(self, ast, full_ast):
		new_ast = full_ast[len(full_ast) - 1]['body']
		dedent_flag = False
		for x in new_ast:
			if self.check_ast('ForLoop', x):
				dedent_flag = True

			if ast == x and dedent_flag == True:
				return True

		return False


	def should_increment_nest_count(self, ast, full_ast):
		statement_counts = 0
		for x in full_ast[len(full_ast) - 1]['body']:
			if self.check_ast('ForLoop', x): statement_counts += 1
			if ast == x: break
		if statement_counts > 1: return False
		else: return True









