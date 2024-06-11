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
    ch_rct = ch_img.get_rect()#工科トンのRectを抽出
    tmr = 0
    speed = 1
    ch_rct.center = 300, 200
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        x = tmr%3200
        screen.blit(bg_img1, [-x, 0])#背景画像
        screen.blit(bg_img2, [-x+1600, 0])#背景画像
        screen.blit(bg_img1, [-x+3200, 0])#背景画像
        screen.blit(bg_img2, [-x+4800, 0])#背景画像
        ksy_lst = pg.key.get_pressed()#keyの状態を取得
        if ksy_lst[pg.K_UP]:#↑
            ch_rct.move_ip((0, -speed))
        elif ksy_lst[pg.K_DOWN]:#↓
            ch_rct.move_ip((0, speed))
        elif ksy_lst[pg.K_LEFT]:#←
            ch_rct.move_ip((-speed*2, 0))#後ろに下がるための調節
        elif ksy_lst[pg.K_RIGHT]:#→
            ch_rct.move_ip((speed*2, 0))#前に二倍速で進む
        else:#流されるなら
            ch_rct.move_ip((-speed, 0))
        screen.blit(ch_img, ch_rct)#工科トンの配置
        pg.display.update()
        tmr += speed
        clock.tick(200)#fps


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()