import pygame


class Board:
    # создание поля
    def __init__(self, width, height, amount, cell):
        self.width = width
        self.height = height
        self.cnt = amount
        self.board = [[0] * amount for _ in range(amount)]
        for i in range(amount):
            for j in range(amount):
                self.board[i][j] = cell(0)
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        w = self.width // self.cnt
        h = self.height // self.cnt
        x = 0
        y = 0
        # print(len(self.board), len(self.board[0]))
        dio = [[0] * self.cnt for _ in range(self.cnt)]
        # print(*dio, sep="\n")
        for i, field in enumerate(self.board):
            for j, cell in enumerate(field):
                pass
            # print(cell.stat, end=" ")

            # print()
        for i, field in enumerate(self.board):
            for j, cell in enumerate(field):
                cnt = 0
                # print(cell.stat, i, j)
                # print(x, y, w, h)
                if cell.stat == 0:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     ((x, y), (w, h)))
                    pygame.draw.rect(screen, (255, 255, 255),
                                     ((x, y), (w, h)),
                                     1)
                    x += self.width // self.cnt
                else:
                    pygame.draw.rect(screen, (155, 0, 0),
                                     ((x, y), (w, h)))
                    x += self.width // self.cnt
            x = 0
            y += self.height // self.cnt
            # print(x, y)
        # print(*dio, sep="\n")

    def life(self, ):
        w = self.width // self.cnt
        h = self.height // self.cnt
        x = 0
        y = 0
        dio = [[0] * self.cnt for _ in range(self.cnt)]
        for i, field in enumerate(self.board):
            for j, cell in enumerate(field):
                if cell.stat == 1:
                    dio[i][j] = 1

        for i, field in enumerate(self.board):
            for j, cell in enumerate(field):
                pass
                # print(cell.stat, end=" ")
            # print()
        # print(*dio, sep="\n")
        for i, field in enumerate(self.board):
            for j, cell in enumerate(field):
                cnt = 0
                if cell.stat == 1:
                    if j + 1 < self.cnt and self.board[i][j + 1].stat == 1:
                        cnt += 1
                    if i + 1 < self.cnt and self.board[i + 1][j].stat == 1:
                        cnt += 1
                    if j + 1 < self.cnt and i + 1 < self.cnt and self.board[i + 1][j + 1].stat == 1:
                        cnt += 1
                    if j - 1 >= 0 and self.board[i][j - 1].stat == 1:
                        cnt += 1
                    if i - 1 >= 0 and self.board[i - 1][j].stat == 1:
                        cnt += 1
                    if j - 1 >= 0 and i - 1 >= 0 and self.board[i - 1][j - 1].stat == 1:
                        cnt += 1
                    if i + 1 < self.cnt and j - 1 >= 0 and self.board[i + 1][j - 1].stat == 1:
                        cnt += 1
                    if cnt != 2 and cnt != 3:
                        dio[i][j] = 0
                    # print(cnt)
                else:
                    if j + 1 < self.cnt and self.board[i][j + 1].stat == 1:
                        cnt += 1
                    if i + 1 < self.cnt and self.board[i + 1][j].stat == 1:
                        cnt += 1
                    if j + 1 < self.cnt and i + 1 < self.cnt and self.board[i + 1][j + 1].stat == 1:
                        cnt += 1
                    if j - 1 >= 0 and self.board[i][j - 1].stat == 1:
                        cnt += 1
                    if i - 1 >= 0 and self.board[i - 1][j].stat == 1:
                        cnt += 1
                    if j - 1 >= 0 and i - 1 >= 0 and self.board[i - 1][j - 1].stat == 1:
                        cnt += 1
                    if i + 1 < self.cnt and j - 1 >= 0 and self.board[i + 1][j - 1].stat == 1:
                        cnt += 1
                    if j + 1 < self.cnt and i - 1 >= 0 and self.board[i - 1][j + 1].stat == 1:
                        cnt += 1
                    if cnt == 3:
                        dio[i][j] = 1
                    # print(cell.stat, i, j, cnt)
                # print(x, y, w, h)
            y = 0
            x += self.width // self.cnt
        for i, field in enumerate(self.board):
            for j, cell in enumerate(field):
                if dio[i][j] == 1:
                    cell.stat = 1
                else:
                    cell.stat = 0


class cell:
    def __init__(self, stat):
        self.stat = stat

    def check(self, num):
        pass


def search(pos, w, h, am, field):
    # print(pos, w, h)
    i = pos[0] // (w // am)
    j = pos[1] // (h // am)
    print(i, j)
    field.board[j][i].stat = 1


w = 800
h = 600
amount = int(input())
screen = pygame.display.set_mode((w, h))

board = Board(w, h, amount, cell)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                board.render(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            search(event.pos, w, h, amount, board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                board.life()
        board.render(screen)
        clock.tick(60)
        pygame.display.flip()
