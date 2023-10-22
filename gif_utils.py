def create_gif(gif_folder_path, music_file="music_file.wav", width=400, height=400, speed=0.1):
    import pygame, os, sys
    pygame.init()
    # sets caption
    pygame.display.set_caption(gif_folder_path)
    # screen
    SCREEN = pygame.display.set_mode((width,height))
    # sprites
    current_image = 0
    images = []
    # loop through sprites and add them to the images list
    for file in os.listdir(gif_folder_path):
        img = pygame.image.load(gif_folder_path+'/'+file); img = pygame.transform.scale(img, (width,height))
        images.append(img)
    # sound track
    pygame.mixer.music.load(music_file)
    # play then pause music
    pygame.mixer.music.play(-1)
    pygame.mixer.music.pause()
    # main loop
    while True:
        # blit the image
        SCREEN.blit(images[int(current_image)], (0,0))
        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # move gif/play sound if space bar click
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            # move gif
            current_image += speed
            if current_image > len(images):
                current_image = 0 
            # play sound
            pygame.mixer.music.unpause()
        else:
            # stop it
            pygame.mixer.music.pause()
        # update screen
        pygame.display.flip()

    
