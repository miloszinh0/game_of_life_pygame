import random

class Game:
    def __init__(self, board_size, tiles):
        self.board_size = board_size
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.tiles = tiles

    def random_board(self):
        tiles_alive = 0
        while tiles_alive < self.tiles:
            a = random.randint(0, self.board_size-1)
            b = random.randint(0, self.board_size-1)
            if self.board[a][b] == 0:
                self.board[a][b] = 1
                tiles_alive += 1

    def find_neighbours(self, x, y):
        self.possible_neighbours = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
        self.neighbours = []
        for n in self.possible_neighbours:
            if 0 <= n[0] < self.board_size and 0 <= n[1] < self.board_size:
                self.neighbours.append(n)

    def check_number(self):
        self.count = 0
        for n in self.neighbours:
            if self.board[n[0]][n[1]] == 1:
                self.count += 1

    def update(self):
        self.next_board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]

        for x in range(self.board_size):
            for y in range(self.board_size):
                self.find_neighbours(x, y)
                self.check_number()
                if self.count == 3:
                    self.next_board[x][y] = 1
                elif self.count == 2:
                    self.next_board[x][y] = self.board[x][y]
                else:
                    self.next_board[x][y] = 0

        self.board = self.next_board
        print(self.board)