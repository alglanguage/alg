class CommentObject():

	def __init__(self, ast):
		self.ast = ast['Comment']
		self.exec_string = ""


	def transpile(self):
		self.exec_string += "# " + self.ast
		return self.exec_string
