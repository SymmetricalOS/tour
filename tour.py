import pygame as pg
import os

pg.init()

width = 1280
height = 720

win = pg.display.set_mode((width, height), pg.RESIZABLE)
pg.display.set_caption("Symmetrical OS Tour")

path1 = os.path.dirname(os.path.realpath(__file__))
print(path1)

h = 1
cl = pg.time.Clock()
offset1 = -300
offset2 = -300
offset3 = -300
offset4 = -300
o2s = False
o3s = False
o4s = False

ready1 = False
ready2 = False
ready3 = False
ready4 = False

oc1 = 6
oc2 = 5
oc3 = 35
oc4 = 34
animstate = 0
bts = 0
animationplaying = True
btschange = 0

def retract1(offset1):
    o1tmp = - offset1 - 300
    o1tmp /= oc3
    o1tmp *= oc4
    return -(o1tmp + 300)

def retract2(offset2):
    o2tmp = - offset2 - 300
    o2tmp /= oc3
    o2tmp *= oc4
    return -(o2tmp + 300)

def retract3(offset3):
    o3tmp = - offset3 - 300
    o3tmp /= oc3
    o3tmp *= oc4
    return -(o3tmp + 300)

def retract4(offset4):
    o4tmp = - offset4 - 300
    o4tmp /= oc3
    o4tmp *= oc4
    return -(o4tmp + 300)
    

while h:
    if animstate == 0:
        if offset1 < 0:
            offset1 /= oc1
            offset1 *= oc2
            if round(offset1) == 0:
                offset1 = 0
        if offset1 > -100 or o2s:
            o2s = True
            offset2 /= oc1
            offset2 *= oc2
            if round(offset2) == 0:
                offset2 = 0
        if offset2 > -100 or o3s:
            o3s = True
            offset3 /= oc1
            offset3 *= oc2
            if round(offset3) == 0:
                offset3 = 0
        if offset3 > -100 or o4s:
            o4s = True
            offset4 /= oc1
            offset4 *= oc2
            if round(offset4) == 0:
                offset4 = 0
                animationplaying = False
    elif animstate == 1:
        offset1 = retract1(offset1)
        if round(offset1) <= -100:
            offset1 = -300
            ready1 = True
        offset2 = retract2(offset2)
        if round(offset2) <= -100:
            offset2 = -300
            ready2 = True
        offset3 = retract3(offset3)
        if round(offset3) <= -100:
            offset3 = -300
            ready3 = True
        offset4 = retract4(offset4)
        if round(offset4) <= -100:
            offset4 = -300
            ready4 = True
        if ready1 and ready2 and ready3 and ready4:
            animstate = 2
            btschange = 1
            animationplaying = False
    elif animstate == 2:
        if btschange:
            if bts == 0:
                bts = 1
            else:
                bts = 0
            btschange = 0
        offset1 /= oc1
        offset1 *= oc2
        if round(offset1) == 0:
            offset1 = 0
        offset2 /= oc1
        offset2 *= oc2
        if round(offset2) == 0:
            offset2 = 0
        offset3 /= oc1
        offset3 *= oc2
        if round(offset3) == 0:
            offset3 = 0
        offset4 /= oc1
        offset4 *= oc2
        if round(offset4) == 0:
            offset4 = 0
            animationplaying = False
    elif animstate == 11:
        offset1 /= oc1
        offset1 *= oc2
        if round(offset1) == 0:
            offset1 = 0
        offset2 = retract2(offset2)
        if round(offset2) <= -100:
            offset2 = -300
        offset3 = retract3(offset3)
        if round(offset3) <= -100:
            offset3 = -300
        offset4 = retract4(offset4)
        if round(offset4) <= -100:
            offset4 = -300
            animationplaying = False
    elif animstate == 12:
        offset1 = retract1(offset1)
        if round(offset1) <= -100:
            offset1 = -300
        offset2 /= oc1
        offset2 *= oc2
        if round(offset2) == 0:
            offset2 = 0
        offset3 = retract3(offset3)
        if round(offset3) <= -100:
            offset3 = -300
        offset4 = retract4(offset4)
        if round(offset4) <= -100:
            offset4 = -300
            animationplaying = False
    elif animstate == 13:
        offset1 = retract1(offset1)
        if round(offset1) <= -100:
            offset1 = -300
        offset2 = retract2(offset2)
        if round(offset2) <= -100:
            offset2 = -300
        offset3 /= oc1
        offset3 *= oc2
        if round(offset3) == 0:
            offset3 = 0
        offset4 = retract4(offset4)
        if round(offset4) <= -100:
            offset4 = -300
            animationplaying = False
    elif animstate == 14:
        offset1 = retract1(offset1)
        if round(offset1) <= -100:
            offset1 = -300
        offset2 = retract2(offset2)
        if round(offset2) <= -100:
            offset2 = -300
        offset3 = retract3(offset3)
        if round(offset3) <= -100:
            offset3 = -300
        offset4 /= oc1
        offset4 *= oc2
        if round(offset4) == 0:
            offset4 = 0
            animationplaying = False
    for event in pg.event.get():
        if event.type in [pg.QUIT]:
            h = 0
        elif event.type == pg.VIDEORESIZE:
            win = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            width = event.w
            height = event.h
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            (10, height-40)
            ready1 = False
            ready2 = False
            ready3 = False
            ready4 = False
            if not bts:
                if x <= 380 and y >= height-40:
                    if not animationplaying:
                        animationplaying = True
                        animstate = 1
            else:
                if x <= 300 and y >= height-40:
                    if not animationplaying:
                        animationplaying = True
                        animstate = 1
            if x >= 380 or y <= height-40:
                if not animationplaying:
                    animstate = 11
    if not h:
        break
    win.fill((255, 255, 255))
    logo = pg.image.load(os.path.join(path1, "symmosicons/symmosicon.svg"))
    sw = pg.font.SysFont("Arial", 30)
    fontButton = pg.font.SysFont("Arial", 40)
    fontButtonSm = pg.font.SysFont("Arial", 20)
    fontLarge = pg.font.SysFont("Arial", 50)
    if not bts:
        img = pg.image.load(os.path.join(path1, "symmosicons/symmosred.svg"))
        btn1 = fontButtonSm.render("Learn the", 1, (255, 255, 255))
        btn1x = fontButtonSm.render("basics", 1, (255, 255, 255))
        img2 = pg.image.load(os.path.join(path1, "symmosicons/symmosyellow.svg"))
        btn2 = fontButtonSm.render("Get connected", 1, (0, 0, 0))
        img3 = pg.image.load(os.path.join(path1, "symmosicons/symmosgreen.svg"))
        btn3 = fontButtonSm.render("Computer", 1, (0, 0, 0))
        btn3x = fontButtonSm.render("Safety", 1, (0, 0, 0))
        img4 = pg.image.load(os.path.join(path1, "symmosicons/symmosblue.svg"))
        btn4 = fontButtonSm.render("What's next?", 1, (255, 255, 255))
    else:
        img = pg.image.load(os.path.join(path1, "symmosicons/symmosorange.svg"))
        btn1 = fontButtonSm.render("What comes", 1, (0, 0, 0))
        btn1x = fontButtonSm.render("preinstalled?", 1, (0, 0, 0))
        img2 = pg.image.load(os.path.join(path1, "symmosicons/symmoslime.svg"))
        btn2 = fontButtonSm.render("Advanced", 1, (0, 0, 0))
        btn2x = fontButtonSm.render("Features", 1, (0, 0, 0))
        img3 = pg.image.load(os.path.join(path1, "symmosicons/symmospurple.svg"))
        btn3 = fontButtonSm.render("Additional", 1, (255, 255, 255))
        btn3x = fontButtonSm.render("Software", 1, (255, 255, 255))
        img4 = pg.image.load(os.path.join(path1, "symmosicons/symmoscyan.svg"))
        btn4 = fontButtonSm.render("Extra", 1, (0, 0, 0))
        btn4x = fontButtonSm.render("Customization", 1, (0, 0, 0))
    win.blit((sw.render("Advanced user? Click here!", 1, (55, 195, 255)) if not bts else sw.render("New user? Click here!", 1, (55, 195, 255))), (10, height-40))
    win.blit((fontLarge.render("Exit", 1, (0, 0, 0))), (width-100, 20))
    win.blit(pg.transform.scale_by(logo, 0.175), (20, 18))
    win.blit(pg.transform.scale_by(img, 0.25), (120, 20+offset1))
    win.blit(btn1, (135, 30+offset1))
    win.blit(btn1x, (135, 50+offset1))
    win.blit(pg.transform.scale_by(img2, 0.25), (320 if width >= 1000 else 280, 40+offset2))
    win.blit(pg.transform.scale_by(img3, 0.25), (520 if width >= 1000 else (480-40), 20+offset3))
    win.blit(btn3, (535 if width >= 1000 else (495-40), 30+offset3))
    win.blit(btn3x, (535 if width >= 1000 else (495-40), 50+offset3))
    win.blit(pg.transform.scale_by(img4, 0.25), (720 if width >= 1000 else (680-80), 40+offset4))
    if not bts:
        win.blit(btn2, (334 if width >= 1000 else 296, 60+offset2))
        win.blit(btn4, (740 if width >= 1000 else (710-80), 60+offset4))
    else:
        win.blit(btn2, (335 if width >= 1000 else 295, 50+offset2))
        win.blit(btn2x, (335 if width >= 1000 else 295, 70+offset2))
        win.blit(btn4, (735 if width >= 1000 else (695-80), 50+offset4))
        win.blit(btn4x, (735 if width >= 1000 else (695-80), 70+offset4))
    cl.tick(30)
    pg.display.flip()
pg.quit()