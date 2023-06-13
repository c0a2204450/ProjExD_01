import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True,False)
    kk_imgs=[]
    for i in range(1, 11):
        kk_imgs.append(pg.transform.rotozoom(kk_img, i, 1.0))
     
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img,[-tmr,0])
        screen.blit(pg.transform.flip(bg_img, True,False),[1600-tmr,0])
        screen.blit(bg_img,[3200-tmr,0])
        screen.blit(kk_imgs[tmr%10],[300,200])
        pg.display.update()
        tmr += 1  
        if tmr%3200==0:
           tmr = 0      

        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()