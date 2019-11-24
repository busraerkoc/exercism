class Matrix(object):
	def __init__(self, matrix_string):
		self.matrix = []
		for rows in matrix_string.split('\n'):
			self.matrix.append([int(row) for row in rows.split()])
	def row(self, index):
		return self.matrix[index - 1]
	def column(self, index):
		return [col[index-1] for col in self.matrix] 
