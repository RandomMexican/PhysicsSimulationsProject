import pygame,sys,Buttons

class main():
    pygame.init()
    #what we want the res to be
    window_size = (800,800)     
    #setting the windows res
    window = pygame.display.set_mode(window_size)
    # giving the windo a caption
    pygame.display.set_caption("pygame window")

    # load images
    gravIMG = pygame.image.load('Images/SandGravIMG.png').convert_alpha()
    GOLIMG = pygame.image.load('Images/GOLimg.png').convert_alpha()


    # create new button instances
    GravSim = Buttons.button(100,200,gravIMG,0.8)
    GOLSim = Buttons.button(450,200, GOLIMG,0.8)

    # starts loop
    running = True
    while running:
    # handles events

        for event in pygame.event.get():
            # ends the loop
            if event.type == pygame.QUIT:
                running = False
        
        # fills in the window so its not blank
        window.fill((128,128,128))
        
        # "draws" the button on the window lets 
        # them do something
        if GravSim.draw(window):
            from Sims.SandGrav import SandGrav
            SandGrav()
        if GOLSim.draw(window):
            from Sims.GOLmain import main
            main()
        # updatest the entire contents of the display
        pygame.display.flip()
        

pygame.quit

