import pygame


def draw_square(surface, color, x, y, width, height):
    pygame.draw.rect(surface, color, ((x, y), (width, height)), 0)

class Covid:
    def __init__(self):
        pygame.init()
        self.grid = []

        self.clock = pygame.time.Clock()
        self.alive = True
        self.running = True

        self.load_data()

    def load_data(self):
        with open('wrld.txt', 'r') as file:
            c = 0
            for i in file:
                self.grid.append([])
                for j in i:
                    if j.isdigit():
                        self.grid[c].append(int(j))
                c += 1

        #self.grid[60][300] = 1




    def new(self):
        self.square = 5
        self.width = len(self.grid[0])*self.square
        self.height = len(self.grid)*self.square

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.run()

    def run(self):
        while self.running:
            self.clock.tick()
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.alive = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        colors = [(255, 255, 255), (255, 0, 0), 0, (0, 0, 100)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                draw_square(self.screen, colors[self.grid[i][j]], self.square * j, self.square * i, self.square, self.square)

        pygame.display.flip()




c = Covid()
while c.alive:
    c.new()

pygame.quit()
