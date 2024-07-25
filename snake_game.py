import pygame
import sys
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()

# Constants
SPEED = 10  # Movement speed of the snake
SNAKE_SIZE = 9  # Size of each segment of the snake
EGG_SIZE = SNAKE_SIZE  # Size of the egg (same as snake segment)
SEPARATION = 10  # Separation between snake segments when growing
SCREEN_HEIGHT = 600  # Height of the game screen
SCREEN_WIDTH = 800  # Width of the game screen
FPS = 25  # Frames per second
KEY = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}  # Key mappings for directions

# Colors
BACKGROUND_COLOR = pygame.Color(0, 0, 0)  # Black background
SNAKE_COLOR = pygame.Color(0, 255, 0)  # Green snake
EGG_COLOR = pygame.Color(255, 165, 0)  # Orange egg
TEXT_COLOR = pygame.Color(255, 255, 255)  # White text

# Fonts
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 38)
game_over_font = pygame.font.Font(None, 46)
play_again_font = pygame.font.Font(None, 28)
score_msg = score_font.render("Score:", 1, TEXT_COLOR)
time_msg = score_font.render("Time:", 1, TEXT_COLOR)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE)
gameClock = pygame.time.Clock()

def checkCollision(posA, As, posB, Bs):
    """Check if two rectangles (A and B) collide."""
    if (posA.x < posB.x + Bs and posA.x + As > posB.x and posA.y < posB.y + Bs and posA.y + As > posB.y):
        return True
    return False

def checkLimits(snake):
    """Check if the snake's head is outside the screen boundaries."""
    if snake.x >= SCREEN_WIDTH or snake.x < 0 or snake.y >= SCREEN_HEIGHT or snake.y < 0:
        return True
    return False

class Egg:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state  # 1 = visible, 0 = eaten
        self.color = EGG_COLOR

    def draw(self, screen):
        """Draw the egg on the screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, EGG_SIZE, EGG_SIZE), 0)

class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]
        self.stack = [Segment(x, y)]  # Initialize the snake with one segment
        self.grow()  # Grow the snake by adding additional segments
        self.grow()

    def move(self):
        """Move the snake in the current direction."""
        last_element = len(self.stack) - 1
        # Shift the segments to follow the segment in front of them
        while last_element != 0:
            self.stack[last_element].direction = self.stack[last_element - 1].direction
            self.stack[last_element].x = self.stack[last_element - 1].x
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -= 1
        # Move the head of the snake
        last_segment = self.stack[0]
        if self.direction == KEY["UP"]:
            self.stack[0].y -= SPEED
        elif self.direction == KEY["DOWN"]:
            self.stack[0].y += SPEED
        elif self.direction == KEY["LEFT"]:
            self.stack[0].x -= SPEED
        elif self.direction == KEY["RIGHT"]:
            self.stack[0].x += SPEED

    def grow(self):
        """Add a new segment to the snake."""
        last_segment = self.stack[-1]
        new_segment = Segment(last_segment.x, last_segment.y)
        # Position the new segment relative to the last segment
        if last_segment.direction == KEY["UP"]:
            new_segment.y += SNAKE_SIZE + SEPARATION
        elif last_segment.direction == KEY["DOWN"]:
            new_segment.y -= SNAKE_SIZE + SEPARATION
        elif last_segment.direction == KEY["LEFT"]:
            new_segment.x += SNAKE_SIZE + SEPARATION
        elif last_segment.direction == KEY["RIGHT"]:
            new_segment.x -= SNAKE_SIZE + SEPARATION
        self.stack.append(new_segment)

    def setDirection(self, direction):
        """Change the snake's direction if it's not a reverse direction."""
        if (self.direction == KEY["RIGHT"] and direction == KEY["LEFT"]) or (self.direction == KEY["LEFT"] and direction == KEY["RIGHT"]):
            return
        if (self.direction == KEY["UP"] and direction == KEY["DOWN"]) or (self.direction == KEY["DOWN"] and direction == KEY["UP"]):
            return
        self.direction = direction

    def checkCrashing(self):
        """Check if the snake collides with itself."""
        head = self.stack[0]
        for segment in self.stack[1:]:
            if checkCollision(head, SNAKE_SIZE, segment, SNAKE_SIZE):
                return True
        return False

    def draw(self, screen):
        """Draw the snake on the screen."""
        for segment in self.stack:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment.x, segment.y, SNAKE_SIZE, SNAKE_SIZE), 0)

    def getHead(self):
        """Get the head of the snake."""
        return self.stack[0]

def getKey():
    """Handle keyboard input and return the corresponding direction."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            elif event.key == pygame.K_y:
                return "yes"
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame(score):
    """Display the game over message and ask if the player wants to play again."""
    message = game_over_font.render("Game Over", 1, TEXT_COLOR)
    message_play_again = play_again_font.render("Play Again? (Y/N)", 1, TEXT_COLOR)
    screen.blit(message, (320, 240))
    screen.blit(message_play_again, (320 + 12, 240 + 40))

    pygame.display.flip()
    pygame.display.update()

    while True:
        key = getKey()
        if key == "yes":
            main()  # Restart the game
        elif key == "no" or key == "exit":
            pygame.quit()
            sys.exit(0)

def drawScore(score):
    """Draw the score on the screen."""
    score_numb = score_numb_font.render(str(score), 1, TEXT_COLOR)
    screen.blit(score_msg, (10, 10))
    screen.blit(score_numb, (120, 10))

def drawGameTime(gameTime):
    """Draw the elapsed game time on the screen."""
    game_time_numb = score_numb_font.render(str(gameTime // 1000), 1, TEXT_COLOR)
    screen.blit(time_msg, (10, 50))
    screen.blit(game_time_numb, (120, 50))

def respawnEgg(eggs, index, sx, sy):
    """Respawn a single egg at a random location, avoiding the snake's current position."""
    radius = math.sqrt((SCREEN_WIDTH / 2 * SCREEN_WIDTH / 2 + SCREEN_HEIGHT / 2 * SCREEN_HEIGHT / 2)) / 2
    angle = 999
    while angle > radius:
        angle = random.uniform(0, 800) * math.pi * 2
        x = SCREEN_WIDTH / 2 + radius * math.cos(angle)
        y = SCREEN_HEIGHT / 2 + radius * math.sin(angle)
        if x == sx and y == sy:
            continue
    new_egg = Egg(x, y, 1)
    eggs[index] = new_egg

def respawnEggs(eggs, quantity, sx, sy):
    """Respawn multiple eggs at random locations, avoiding the snake's current position."""
    counter = 0
    del eggs[:]  # Clear the existing eggs
    radius = math.sqrt((SCREEN_WIDTH / 2 * SCREEN_WIDTH / 2 + SCREEN_HEIGHT / 2 * SCREEN_HEIGHT / 2)) / 2
    angle = 999
    while counter < quantity:
        while angle > radius:
            angle = random.uniform(0, 800) * math.pi * 2
            x = SCREEN_WIDTH / 2 + radius * math.cos(angle)
            y = SCREEN_HEIGHT / 2 + radius * math.sin(angle)
            # Ensure the new egg is not too close to the snake's current position
            if (x - EGG_SIZE == sx or x + EGG_SIZE == sx) and (y - EGG_SIZE == sy or y + EGG_SIZE == sy) or radius - angle <= 10:
                continue
        eggs.append(Egg(x, y, 1))
        angle = 999
        counter += 1

def main():
    """Main function to run the game loop."""
    score = 0
    mySnake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    mySnake.setDirection(KEY["UP"])
    mySnake.move()
    start_segments = 3
    while start_segments > 0:
        mySnake.grow()
        mySnake.move()
        start_segments -= 1

    max_eggs = 1
    eggs = [Egg(random.randint(60, SCREEN_WIDTH - 60), random.randint(60, SCREEN_HEIGHT - 60), 1)]
    respawnEggs(eggs, max_eggs, mySnake.x, mySnake.y)

    startTime = pygame.time.get_ticks()
    endgame = False

    while not endgame:
        gameClock.tick(FPS)
        keyPress = getKey()
        if keyPress == "exit":
            endgame = True

        if keyPress:
            mySnake.setDirection(keyPress)

        mySnake.move()

        if checkLimits(mySnake.getHead()):
            endgame = True

        if mySnake.checkCrashing():
            endgame = True

        for myEgg in eggs:
            if myEgg.state == 1:
                if checkCollision(mySnake.getHead(), SNAKE_SIZE, myEgg, EGG_SIZE):
                    mySnake.grow()
                    myEgg.state = 0
                    score += 1
                    respawnEgg(eggs, eggs.index(myEgg), mySnake.x, mySnake.y)
                    break

        screen.fill(BACKGROUND_COLOR)
        for myEgg in eggs:
            if myEgg.state == 1:
                myEgg.draw(screen)

        mySnake.draw(screen)
        drawScore(score)
        drawGameTime(pygame.time.get_ticks() - startTime)
        pygame.display.flip()
        pygame.display.update()

    endGame(score)

main()
