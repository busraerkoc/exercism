class Queen:
	def __init__(self, row, column):
            self.row = row
            self.column = column
            if self.row < 0 or self.column < 0 or self.row > 7 or self.column >7: 
                raise ValueError("Error")
	def can_attack(self, another_queen):
            if self.row == another_queen.row and self.column == another_queen.column:
                raise ValueError("Error")
            if self.row == another_queen.row or self.column == another_queen.column or abs(self.column-another_queen.column) == abs(self.row-another_queen.row):
                return True
            else:
                return False
