import sys

class TicTacToeGame(object):
	board = [[None, None, None], [None, None, None], [None, None, None]]
	turn = True # Use boolean switching to alternate between turns instead of -1 and 1

	def reset_game(self):
		print('\n Game reset')
		# Reset turn
		self.turn = True
		# Reset self.board
		for i in range(3):
			for j in range(3):
				self.board[i][j] = None

	def play(self):
		# Game loop
		while 1:
			move_position = self.get_player_move()
			# Place move on self.board
			self.board[move_position[0]][move_position[1]] = 'X' if self.turn else 'O'
			self.print_board()
			# Check for win condition
			# Check horizontal win condition
			for i in range(3):
				checkh = set(self.board[i])
				if len(checkh) == 1 and self.board[i][0]:
					print('Player {} wins horizontally!'.format(self.board[i][0]))
					return
			# Check vertical win condition
			for i in range(3):
				checkv = set([self.board[0][i], self.board[1][i], self.board[2][i]])
				if len(checkv) == 1 and self.board[0][i]:
					print('Player {} wins vertically!'.format(self.board[0][i]))
					return
			# Check diagonal win condition
			if self.board[1][1] and ((self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) or (self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2])):
				print('Player {} wins diagonally!'.format(self.board[1][1]))
				return
			# Toggle turn
			self.turn =  not self.turn

	def print_board(self):
		for row in self.board:
			print([v if v else '-' for v in row])

	def get_player_move(self):
		"""
		Get coordinates form player input
		"""
		while 1:
			user_input = input('~~~ Player {}, please choose your square by specifying row,column coordinates: '.format(1 if self.turn else 2))
			if user_input == 'exit':
				print('Exiting game')
				sys.exit()
			if user_input == 'board':
				self.print_board()
			elif user_input == 'reset':
				self.reset_game()
				self.print_board()
			else:
				if len(user_input) != 3:
					print('\nYour coordinates were not valid. Try again. \n')
					continue
				else:
					try:
						coordinates = [int(i)-1 for i in user_input.split(',')]
						# Validate coordinates are valid
						if self.board[coordinates[0]][coordinates[1]]:
							print('\nSorry that square has already been played...\n')
							continue
						if any(coordinate < 0 or coordinate > 2 for coordinate in coordinates):
							print('\n Coordinates are out of bounds')
							continue
						return coordinates

					except ValueError:
						 print('\nInput values must be numbers between 1 and 3 inclusive.\n')

game = TicTacToeGame()
game.play()