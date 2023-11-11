import pygame,sys,Buttons

class main():
    pygame.init()
    #what we want the res to be
    window_size = (800,800)     
    #setting the windows res
    window = pygame.display.set_mode(window_size)
    # giving the window a caption
    pygame.display.set_caption("pygame window")

    # load images
    OrbIMG = pygame.image.load('Images/OrbitingPB.png').convert_alpha()
    gravIMG = pygame.image.load('Images/SandGravIMG.png').convert_alpha()
    GOLIMG = pygame.image.load('Images/GOLimg.png').convert_alpha()


    # create new button instances
    OrbB = Buttons.button(100,400,OrbIMG,0.8)
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

        if OrbB.draw(window):
            import SolarSIm
            SolarSIm()
        # updatest the entire contents of the display
        pygame.display.flip()
        

pygame.quit

