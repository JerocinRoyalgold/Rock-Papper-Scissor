import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 32)

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)
    #jerokfcmkcd

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def draw_text(surface, text, position, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def main():
    running = True
    user_choice = None
    computer_choice = None
    result = None
    user_score = 0
    computer_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    user_choice = 'rock'
                elif event.key == pygame.K_p:
                    user_choice = 'paper'
                elif event.key == pygame.K_s:
                    user_choice = 'scissors'
                
                if user_choice:
                    computer_choice = get_computer_choice()
                    result = determine_winner(user_choice, computer_choice)
                    
                    if result == 'user':
                        user_score += 1
                    elif result == 'computer':
                        computer_score += 1

                    print(f"User: {user_choice}, Computer: {computer_choice}, Result: {result}")
        
        screen.fill(WHITE)

        draw_text(screen, "Press R for Rock, P for Paper, S for Scissors", (20, 20), font, BLACK)
        draw_text(screen, f"User Score: {user_score}  Computer Score: {computer_score}", (20, 60), font, BLACK)
        
        if user_choice and computer_choice:
            draw_text(screen, f"User choice: {user_choice}", (20, 100), font, BLACK)
            draw_text(screen, f"Computer choice: {computer_choice}", (20, 140), font, BLACK)
            draw_text(screen, f"Result: {result}", (20, 180), font, BLACK)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
