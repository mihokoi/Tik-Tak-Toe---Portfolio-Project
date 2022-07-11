
# Game of Tic Tac Toe. You should put in the coordinates remembering that
# grid starts with 0 instead of 1 and ends in 2 instead of 3.
# Have fun!!!

class Game:

    players = ['X', 'O']
    player = 'X'
    grid = [[]]
    victory = False
    turns = 9

    # Creates first grid
    def createGrid(self, rows, cols):
        self.grid = [[' ' for i in range(cols)] for j in range(rows)]
        for row in self.grid:
            print('>>', row, '<<')

    # Prints grid
    def printGrid(self):
        for row in self.grid:
            print('>>', row, '<<')

    # Fill the grid with player figure
    def takeAction(self):
        inp = input('Select column and row split by ",": ')
        coordinates = tuple(int(x) for x in inp.split(","))
        print(f"Your entered choice: {coordinates}")
        try:
            if self.grid[coordinates[0]][coordinates[1]] == ' ':
                self.grid[coordinates[0]][coordinates[1]] = self.player
                self.printGrid()
            else:
                game.takeAction()
        except IndexError:
            print(f"You've entered coordinates which were out of range!")
            game.takeAction()
        self.turns -= 1

    # Change Players figure
    def changePlayer(self):
        if self.player == 'X':
            self.player = 'O'
        elif self.player == 'O':
            self.player = 'X'
        else:
            print("Something unexpected happened :(")
            exit(1)

    # Check win conditions
    def checkConditions(self):
        if self.grid[0][0] == self.player and self.grid[1][1] == self.player and self.grid[2][2] == self.player:
            print(f"Game won by player: {self.player}!!!")
            self.victory = True
        elif self.grid[0][2] == self.player and self.grid[1][1] == self.player and self.grid[2][0] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.grid[0][0] == self.player and self.grid[0][1] == self.player and self.grid[0][2] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.grid[0][0] == self.player and self.grid[1][0] == self.player and self.grid[2][0] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.grid[0][2] == self.player and self.grid[1][2] == self.player and self.grid[2][2] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.grid[2][2] == self.player and self.grid[0][2] == self.player and self.grid[0][2] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.grid[1][0] == self.player and self.grid[1][1] == self.player and self.grid[1][2] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.grid[0][1] == self.player and self.grid[1][1] == self.player and self.grid[2][1] == self.player:
            self.victory = True
            print(f"Game won by player: {self.player}!!!")
        elif self.turns == 0:
            print(f"Game resulted in a draw!!!")
            exit(1)

    def __init__(self):
        self.createGrid(3, 3)


game = Game()
while not game.victory:
    game.takeAction()
    game.checkConditions()
    game.changePlayer()

