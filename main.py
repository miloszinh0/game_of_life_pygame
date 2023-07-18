import pygame
import random

FPS = 3
SIZE = 1000
WIN = pygame.display.set_mode((SIZE, SIZE))

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (204, 0, 0)
GREEN = (0, 204, 0)
BLUE = (0, 0, 204)
YELLOW = (255, 255, 0)

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

def draw_window(game):
    WIN.fill(WHITE)
    for x in range(game.board_size):
        for y in range(game.board_size):
            if game.board[x][y] == 0:
                color = BLUE
            else:
                color = YELLOW
            rect = pygame.Rect(x * SIZE/game.board_size, y * SIZE/game.board_size, SIZE/game.board_size, SIZE/game.board_size)
            pygame.draw.rect(WIN, color, rect)
    pygame.display.update()

def main():
    game = Game(20, 200)
    game.random_board()
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        game.update()
        draw_window(game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()
