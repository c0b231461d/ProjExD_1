import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img1, True, False)
    ch_img = pg.image.load("fig/3.png")
    ch_img = pg.transform.flip(ch_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        x = tmr%3200
        screen.blit(bg_img1, [-x, 0])#背景画像
        screen.blit(bg_img2, [-x+1600, 0])#背景画像
        screen.blit(bg_img1, [-x+3200, 0])#背景画像
        screen.blit(bg_img2, [-x+4800, 0])#背景画像
        ch_rct = ch_img.get_rect()#工科トンのRectを抽出
        ch_rct.center = 300, 200
        screen.blit(ch_img, ch_rct)#工科トンの配置
        pg.display.update()
        tmr += 1
        clock.tick(200)#fps


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()