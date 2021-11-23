import pygame as pg

# Initialitation
pg.init()
pg.font.init()

screen_width = 1024
screen_height = 600

window = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("TIC TAC TOE")

player1 = []
player2 = []
draw = True


#Load Image

circle_ = pg.image.load("circle.png")
cross_ = pg.image.load("cross 1.png")
vertical = pg.image.load("line_ver.png")
horizontal = pg.image.load("line_hori.png")
diag_1 = pg.image.load("diagonal 1.png")
diag_2 = pg.image.load("diagonal 2.png")
draw_img = pg.image.load("DRAW.png")

play_sheet = pg.image.load("11.png")
playsheet= pg.transform.scale(play_sheet,(int(screen_width/3),int(screen_height/2)))

#Load FOnt

font_label = pg.font.SysFont("comicsans",70)
font_label_2 = pg.font.SysFont("comicsans",25)
start = font_label.render("RESTART",1,(0,0,0))

    
#REsizing window
circle= pg.transform.scale(circle_,(int(screen_width/9-25),int(screen_height/6-25)))
cross= pg.transform.scale(cross_,(int(screen_width/9-25),int(screen_height/6-25)))
pg.draw.rect(window,(255,255,255),(0,0,screen_width,screen_height))


x = int(screen_width/9)
y = int(screen_height/6)

#redraw window
def redraw_window(restart):
    if restart !=True:
        window.blit(playsheet,(180,190))
        pg.draw.rect(window,(0,0,0),(120,130,int(screen_width/3 + 120),int(screen_height/2 + 120)),20,15)
        window.blit(start,(screen_width-start.get_width()-10,10))
    pg.display.update()

def positioning_func(pos,run,list_,lis_):
                global draw
                def player_position_list(position):
                    if pict == circle:
                        player1.append(position)
                    else:
                        player2.append(position)

                        
                if len(list_) in lis_ :
                    pict = circle
                
                else :
                    pict = cross

       #1         
                if pos[0] < 285 and pos[1]< 285 and pos[0] > 170 and pos[1]> 170:
                    player_position_list(1)
                    window.blit(pict,(180,190))
                    pg.display.update()
                    result(run,draw = False)
       #2             
                elif pos[0] < 415 and pos[1] < 285 and pos[0] > (190+x) and pos[1] > 190:
                    player_position_list(2)
                    window.blit(pict,(190+x,190))
                    pg.display.update()
                    result(run,draw = False)
        #3            
                elif pos[0] < 525 and pos[1]< 285 and pos[0] > (200+(2*x)) and pos[1] > 190:
                    player_position_list(3)
                    window.blit(pict,(200+(2*x),190))
                    pg.display.update()
                    result(run,draw = False)
        #4            
                elif pos[0] < 280 and pos[1] < 385 and pos[0] > 180 and  pos [1] > (200+y):
                    player_position_list(4)
                    window.blit(pict,(180,200+y))
                    pg.display.update()
                    result(run,draw = False)
         #5           
                elif pos[0] < 410 and pos[1]< 385 and pos[0] > 190+x and pos[1] > (200+y):
                    player_position_list(5)
                    window.blit(pict,(190+x,200+y))
                    pg.display.update()
                    result(run,draw = False)
         #6           
                elif pos[0] < 525 and pos[1] < 390 and pos[0] > (200+(2*x)) and pos[1] > (200+y):
                    player_position_list(6)
                    window.blit(pict,(200+(2*x),200+y))
                    pg.display.update()
                    result(run,draw = False)
          #7          
                elif pos < (280,495) and pos > (180,210+(2*y)):
                    player_position_list(7)
                    window.blit(pict,(180,210+(2*y)))
                    pg.display.update()
                    result(run,draw = False)
          #8          
                elif pos < (410,495) and pos > (190+x,210+(2*y)):
                    player_position_list(8)
                    window.blit(pict,(190+x,210+(2*y)))
                    pg.display.update()
                    result(run,draw = False)
          #9          
                elif pos[0] < 522 and pos[1] < 492 and pos[0] > (200+(2*x)) and pos[1] > (210+(2*y)):
                    player_position_list(9)
                    window.blit(pict,(200+(2*x),210+(2*y)))
                    pg.display.update()
                    result(run,draw = False)


def position(q,w):
    position = w.index(q)
    
    if position == 0:
        window.blit(horizontal,(180,180))
        pg.display.update()
        
    elif position == 1:
        window.blit(horizontal,(180,190+y))
        pg.display.update()
        
    elif position == 2:
        window.blit(horizontal,(180,200+(2*y)))
        pg.display.update()
        
    elif position == 3:
        window.blit(diag_1,(170,180))
        pg.display.update()
        
    elif position == 4:
        window.blit(diag_2,(170,180))
        pg.display.update()
        
    elif position == 5:
        window.blit(vertical,(180,190))
        pg.display.update()
       
    elif position == 6:
        window.blit(vertical,(190+x,190))
        pg.display.update()
        
    elif position == 7:
        window.blit(vertical,(200+(2*x),190))
        pg.display.update()
        
def result(run,draw):
    restart = False
    hori_1 = {1,2,3}
    hori_2 = {4,5,6}
    hori_3 = {7,8,9}
    diag_1 = {1,5,9}
    diag_2 = {3,5,7}
    ver_1 = {1,4,7}
    ver_2 = {2,5,8}
    ver_3 = {3,6,9}
    winning_list = [hori_1,hori_2,hori_3,diag_1,diag_2,ver_1,ver_2,ver_3]
    if len(player1) >= 3 or len(player2) >=3 and len(player1)<= 5:
        p1,p2 = set(player1),set(player2)
        if (len(p1) == len(p2)):
            a,b = p1,p2
        else:
            a,b = p2,p1
        c = 0
        for i in winning_list:
            if i.issubset(a):
                position(i,winning_list)
                c = 1
                run = False
                redraw_window(restart)
                break
        if c != 1:
            for i in winning_list:
                if i.issubset(b):
                    position(i,winning_list)
                    run = False
                    redraw_window(restart)
                    break
                
    elif draw:    
        window.blit(draw_img,(130,250))
        pg.display.update()
    return run
#main Program

def main(restart):

    FPS = 60
    clock = pg.time.Clock()
    run = True
    restart = False
    restart_button = False
    count = 0
    list_ = []
    lis_ = [1,3,5,7,9]

    while run:
        clock.tick(FPS)
        if restart:
            count += 1
            restart_button = True
        if restart_button:
            if count > FPS*2:
                run = False
                main()
            else :
                continue
        for event in pg.event.get():
            
                
            if len(list_) >= 9:
                run = False
                result(run,draw)
                  
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()

                list_.append(0)
                
                positioning_func(pos,run,list_,lis_)
                
                run = result(run,draw=False)

            if event.type == pg.QUIT:
                run = False
                pg.quit()

def main_menu():
    run = True
    restart = False
    while run:
        pg.draw.rect(window,(255,255,255),(screen_width,screen_height,0,0))
        title = font_label.render("TIC TAC TOE",1,(0,0,0))
        under_title = font_label_2.render("Press Mouse Button To Start...",1,(0,0,0))
        window.blit(title,(int(screen_width/2 - title.get_width()/2),int(screen_height/2 - title.get_height()/2)))
        window.blit(under_title,(int(screen_width/2 - title.get_width()/2)+40,int(screen_height/2 + title.get_height()/2)))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                post = pg.mouse.get_pos()
                window.fill((255,255,255))
                redraw_window(restart)
                if post[0] > 775 and post[1] > 5 and post[0] < 1024 and post [1] < 58:
                    restart = True
                    redraw_window(restart)
                    main_menu()
                    
                else :
                    restart = False
                    main(restart)
                    
                
                

            

"""
print (pos)
                print (list_)
                
print("Circle :",player1)
                print("Cross :",player2)
                print()"""


main_menu()

