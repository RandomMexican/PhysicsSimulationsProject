import pygame,sys

class main():
    pygame.init()

    window_size = (800,800) #what we want the res to be
    window = pygame.display.set_mode(window_size) #setting the windows res
    pygame.display.set_caption("pygame window") # giving the windo a caption

    #define button props

    grav_button_color = (255,255,255)
    grav_button_hover_color = (200,200,200)
    grav_button_rect = pygame.Rect(300,250,200,100)
    grav_button_font = pygame.font.SysFont(None,36)
    grav_button_text = grav_button_font.render("Grav sim",True,(0,0,0))
    grav_button_text_rect = grav_button_text.get_rect(center = grav_button_rect.center)

    # starts loop
    running = True
    while running:
    # handles events
        for event in pygame.event.get():
            # ends the loop
            if event.type == pygame.QUIT:
                running = False
                
            # runs when user clicks on button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if grav_button_rect.collidepoint(mouse_pos):
                    # loads SandGrav script 
                    from Sims.SandGrav import SandGrav
                    SandGrav()
                    
                    

            # changes color when mouse hovers over button and sets it back when its not
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if grav_button_rect.collidepoint(mouse_pos):
                    grav_button_color = grav_button_hover_color
                else:
                    grav_button_color = (255,255,255)

        window.fill((128,128,128))
        pygame.draw.rect(window,grav_button_color,grav_button_rect)
        window.blit(grav_button_text, grav_button_text_rect)
        pygame.display.flip()
pygame.quit

