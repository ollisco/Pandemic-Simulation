import pygame
import random
"""
1. place start


"""
def draw_square(surface, color, x, y, width, height):
    pygame.draw.rect(surface, color, ((x, y), (width, height)), 0)

class Covid:
    def __init__(self):
        pygame.init()
        self.grid = []

        self.clock = pygame.time.Clock()
        self.alive = True
        self.running = True
        self.updating = False



        self.alpha = 0.5
        self.beta = 0.35
        self.gamma = 0.1

        self.load_data()

    def load_data(self):
        with open('fullworld.txt', 'r') as file:
            c = 0
            for i in file:
                self.grid.append([])
                for j in i:
                    if j.isdigit():
                        self.grid[c].append(int(j))
                c += 1

        self.grid[60][300] = 1




    def new(self):
        self.square = 3
        self.width = len(self.grid[0])*self.square
        self.height = len(self.grid)*self.square

        print(print(pygame.font.get_fonts()))

        self.sucseptible = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    self.sucseptible.append((i, j))


        self.infected = [(60, 300)]
        self.recovered = []
        self.deaths = 0
        self.day = 0

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.run()

    def startscreen(self):
        pass


    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()

            if self.updating and self.infected:
                self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.alive = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.alive = False

                if event.key == pygame.K_SPACE:
                    self.updating = True if not self.updating else False

            try:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    col, row = (int(pos[0] / self.square), int(pos[1] / self.square))  # Grid coordinates
                    if self.grid[row][col] == 0:
                        self.grid[row][col] = 1
                        self.infected.append((row, col))
                        self.sucseptible.remove((row, col))



                # Removing nodes
                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    col, row = (int(pos[0] / self.square), int(pos[1] / self.square))  # Grid coordinates
                    if self.grid[row][col] == 1:
                        self.grid[row][col] = 0
                        self.infected.remove((row, col))
                        self.sucseptible.append((row, col))
            except Exception as e:
                print(e)

    def find_neighbours(self, i , j):
        neighbours = []

        cords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for row, col in cords:
            if 0 <= row <= len(self.grid)-1:
                if 0 <= col <= len(self.grid[0])-1:
                    neighbours.append((row, col))
        return neighbours


    def infect(self, alpha):
        return True if random.random() < alpha else False

    def recover(self, beta):
        return True if random.random() < beta else False

    def spread(self, gamma):
        return True if random.random() < gamma else False


    def update(self):
        self.day += 1
        # Infect
        preliminary_infections = []
        preliminary_recovered = []
        for row, col in self.infected:
            n = self.find_neighbours(row, col)
            # Infect Neigbours
            for i, j in n:
                if self.grid[i][j] == 0:
                    if self.infect(self.alpha):
                        self.grid[i][j] = 1
                        preliminary_infections.append((i, j))
            # Recover?
            if self.recover(self.beta):
                self.grid[row][col] = 2
                self.recovered.append((row, col))
                preliminary_recovered.append((row, col))

        for cordinate in preliminary_infections:
            self.sucseptible.remove(cordinate)

        if self.infected:
            if self.spread(self.gamma):
                if self.sucseptible:
                    i, j = random.choice(self.sucseptible)
                    self.grid[i][j] = 1
                    self.infected.append((i, j))
                    self.sucseptible.remove((i, j))






        for cordinate in preliminary_recovered:
            self.infected.remove(cordinate)



        self.infected += preliminary_infections



    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(pygame.font.match_font('arial'), size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill((255, 255, 255))
        colors = [(255, 255, 255), (255, 0, 0), (0, 100, 0), (0, 0, 100)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                draw_square(self.screen, colors[self.grid[i][j]], self.square * j, self.square * i, self.square, self.square)

        #1920x1080
        """self.draw_text('day: ' + str(self.day), 60, (255, 255, 0), 300, 600)
        self.draw_text('suceptible: ' + str(len(self.sucseptible)), 60, (255, 255, 255), 300, 700)
        self.draw_text('infected: ' + str(len(self.infected)), 60, (100 ,0, 0), 300, 800)
        self.draw_text('recovered: ' + str(len(self.recovered)), 60, (0, 100, 12), 300, 900)"""

        # 1440x980
        self.draw_text('day: ' + str(self.day), 60, (255, 255, 0), 200, 250)
        self.draw_text('suceptible: ' + str(len(self.sucseptible)), 60, (255, 255, 255), 200, 350)
        self.draw_text('infected: ' + str(len(self.infected)), 60, (100, 0, 0), 200, 450)
        self.draw_text('recovered: ' + str(len(self.recovered)), 60, (0, 100, 12), 200, 550)

        pygame.display.flip()




c = Covid()
while c.alive:
    c.new()

pygame.quit()
