import pygame
import random
import string

#import words from text file 
words_base = []
file = open(r#insert path to textfile here,"r+", encoding="utf-8")          
words_base = file.readlines()
for _ in range(len(words_base)):
    p = str(words_base[_].split())
    words_base[_] = p[2:7]
file.close()

#draw an answer
ans = random.choice(words_base)
letters = list(string.ascii_lowercase)
ans_letters = [[0 for i in range(2)] for j in range(len(letters))]

for i in range (len(letters)):
    ans_letters[i][0] = letters[i]
    if letters[i] in ans:
        ans_letters[i][1] = ans.count(letters[i])
    
print(ans)

pygame.init()

clock = pygame.time.Clock()

#rgb codes for colours
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255,165,0)
green = (0,255,0)
red = (139,0,0)

#dimensions of main screen
X_main = 600
Y_main = 600

#initializations of text fields
main_screen = pygame.display.set_mode((X_main, Y_main))
pygame.display.set_caption('Guess the word!')

font_1 = pygame.font.Font('freesansbold.ttf', 24)
font_2 = pygame.font.Font('freesansbold.ttf', 16)
font_3 = pygame.font.Font('freesansbold.ttf', 20)
 
title = font_1.render('Guess the word!', True, black, white)
title_Rect = title.get_rect()
title_Rect.center = (300, 30)

title_input = font_2.render('Write the word:', True, black, white)
title_input_Rect = title_input.get_rect()
title_input_Rect.center = (120, 535)

you_won = font_3.render('You won!', True, green, white)
you_won_Rect = you_won.get_rect()
you_won_Rect.center = (300, 70)

you_lost = font_3.render('You lost!', True, red, white)
you_lost_Rect = you_lost.get_rect()
you_lost_Rect.center = (300, 70)

next_game = font_3.render('Next game', True, red, white)
next_game_Rect = next_game.get_rect()
next_game_Rect.center = (520, 560)

not_found_word_text = font_2.render('Correct word:', True, red, white)
not_found_word_text_Rect = not_found_word_text.get_rect()
not_found_word_text_Rect.center = (80, 580)

not_found_word = font_2.render(ans, True, red, white)
not_found_word_Rect = not_found_word.get_rect()
not_found_word_Rect.midleft = (140, 580)

input_rect = pygame.Rect(200, 520, 200,35)
user_text = ''

game_lasts = True
draw_rectangles = False

columns = 5
rows = 6
y_start = 100
attempt = 0
word = ''
last_word = [0]*rows
word_letters = [[0 for i in range(7)] for j in range(len(letters))]

#function to draw fields for letters
def draw_fields():        
    x_start = 135
    y_start = 100
    for i in range (rows):
        x_start = 135
        for j in range (columns):
            pygame.draw.rect(main_screen, black, (x_start, y_start, 50, 50), width = 3)
            x_start += 70
        y_start += 70
  
# function do writing letters to fields          
def write_word():
    y_start = 100
    x_start = 135
    used_letters = [[0 for i in range(rows)] for j in range(len(letters))]
    
    #check number of each letter in answer
    
    for x in range (attempt): 
        for i in range (len(letters)):
            word_letters[i][0] = letters[i]
            if letters[i] in last_word[x]:
                word_letters[i][x+1] = last_word[x].count(letters[i])
            y_start += 70
                
    y_start = 100

    #in case of miscoroling text fields (e.g. in answer 'value' is one letter 'a'. If user will write word 'again',
    #we need to avoid situation, when app color two fields instead of one). So we should:
    #1. in first case find letters which are in good position (the same as in answer)
    #2. check numbers of specific letters. In word 'again', first 'a' will be colored, because it's the first 'a'
    #in this word and 'a' is also in word 'value'. Second 'a' won't be colored because in this moment numbers 
    #of 'a''s in user word is greater than number of 'a''s in answer.
        
    for x in range (attempt):
        x_start = 135
            
        for i in range (columns):
            if ((word[5*(x)+i] == ans[i])):
                pygame.draw.rect(main_screen, green, (x_start+3, y_start+3, 44, 44))
                used_letters[letters.index(ans[i])][x] += 1
            x_start += 70
        y_start += 70
        i = 0 
    y_start = 100   
         
    for x in range (attempt):
        x_start = 135
            
        for i in range (columns):    
            if (word[5*(x)+i] in ans and (word[5*(x)+i] != ans[i])):
                if (used_letters[letters.index((word[5*(x)+i]))][x] < ans_letters[letters.index(word[5*(x)+i])][1]):
                    used_letters[letters.index((word[5*(x)+i]))][x] += 1
                    pygame.draw.rect(main_screen, orange, (x_start+3, y_start+3, 44, 44)) ##kolorowanie!
                    
            letter = font_1.render((word[5*(x)+i]), True, black)
            letter_Rect = letter.get_rect() 
            letter_Rect.center = (x_start+25, y_start+25)
            main_screen.blit(letter, letter_Rect)
            x_start += 70
        y_start += 70
        i = 0
    if (word[len(word)-5:len(word)] == ans): #conditions to win a game
        main_screen.blit(you_won, you_won_Rect)
        pygame.draw.rect(main_screen, black, (460, 540, 120, 40), width = 3)
        main_screen.blit(next_game, next_game_Rect)
                    
    elif (word[len(word)-5:len(word)] != ans and attempt == 6): #conditions to lose a game
        main_screen.blit(you_lost,you_lost_Rect)
        pygame.draw.rect(main_screen, black, (460, 540, 120, 40), width = 3)
        main_screen.blit(next_game, next_game_Rect)
        main_screen.blit(not_found_word_text, not_found_word_text_Rect)
        not_found_word = font_2.render(ans, True, red, white)
        main_screen.blit(not_found_word, not_found_word_Rect)
        
while game_lasts == True: #app loop
    
    mouse = pygame.mouse.get_pos()
        
    main_screen.fill(white)    
    pygame.draw.rect(main_screen, green, input_rect, width = 3)
    text_surface = font_1.render(user_text, True, black)
    main_screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10) 
    main_screen.blit(title, title_Rect)
    main_screen.blit(title_input, title_input_Rect)
    
    draw_fields()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 460 <= mouse[0] <= 580 and 540 <= mouse[1] <= 580:
                if ((word[len(word)-5:len(word)] == ans) or (word[len(word)-5:len(word)] != ans and attempt == 6)):
                    #write start values for variables and draw new answer
                    y_start = 100
                    attempt = 0
                    word = ''
                    draw_rectangles = False
                    ans = random.choice(words_base)
                    print(ans)
                    
                    for i in range (len(letters)):
                        ans_letters[i][0] = letters[i]
                        if letters[i] in ans:
                            ans_letters[i][1] = ans.count(letters[i])
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif (len(user_text) < 5 and attempt < 6 and event.unicode.isalpha()): #permission to insert letters only
                user_text += event.unicode
            if (event.key == pygame.K_RETURN and len(user_text) == 5 and user_text in words_base and attempt < 6):
            
                word += user_text
                last_word[attempt] = word[(len(word)-5):(len(word))]
                
                write_word()
                
                attempt += 1
                print(attempt, y_start)
                user_text = ''
                draw_rectangles = True
            
        if (draw_rectangles == True):
            write_word()
        
        pygame.display.update()
        pygame.display.flip()
  
        clock.tick(60)