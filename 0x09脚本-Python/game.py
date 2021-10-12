# game.py
# -*- coding: utf-8 -*-

#调用游戏模块
import pygame
from pygame.locals import *
#调用数学计算模块
import math
#调用随机数模块
import random


#初始化游戏
pygame.init()
#设置游戏界面大小
width,height=640,480
screen=pygame.display.set_mode((width,height))
#按键顺序为WASD
keys=[False,False,False,False]
#角色位置变量
playerpos=[100,100]
#跟踪玩家和跟踪箭头变量
acc=[0,0]
#箭头变量
arrows=[]
#定义定时器，一段时间出现一个敌人
badtimer = 100
badtimer1 = 0
badguys = [[640,100]]
healthvalue = 194
#添加音乐
pygame.mixer.init()


#加载游戏角色图片
player = pygame.image.load("resources/images/dude.png")#兔子
#添加背景
grass = pygame.image.load("resources/images/grass.png")#草地
castle = pygame.image.load("resources/images/castle.png")#城堡
#添加箭头
arrow = pygame.image.load("resources/images/bullet.png")#箭头
#添加敌人角色图片
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
#添加血量图片
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
#添加游戏结束界面
gameover = pygame.image.load("resources/images/gameover.png")
#添加玩家获胜界面
youwin = pygame.image.load("resources/images/youwin.png")
#添加音效
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
#设置音量
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
#添加背景音乐
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


#循环运行
running  = 1
exitcode = 0
while running:
#while True:
    #定时器自减
    badtimer-=1
    #使用黑色填充游戏界面
    screen.fill(0)
    #在游戏界面放置草地和城堡
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):#  长X 宽，一共放下这么多块草地
            screen.blit(grass,(x*100,y*100))
    #4个城堡
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))
    #在游戏界面坐标为（100，100）的位置图片
    #screen.blit(player,playerpos)
    #添加角色转向功能
    position = pygame.mouse.get_pos() #获取鼠标位置
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player,360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
    #游戏角色位置变化
    screen.blit(playerrot,playerpos1)

    #添加放箭功能
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
	#超出屏幕范围，删除箭
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1=pygame.transform.rotate(arrow,360-projectile[0]*57.29)
            screen.blit(arrow1,(projectile[1],projectile[2]))
    #添加敌人
    if badtimer==0:#定时器时间到
        badguys.append([640,random.randint(50,430)])#从右边开始，随机出现一个敌人
        badtimer = 100-(badtimer1*2)#重新定义定时器时间
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index = 0
    for badguy in badguys:
        if badguy[0]<-64:#超出屏幕范围时
            badguys.pop(index)#删除敌人
        badguy[0]-=7 #水平移动敌人(移动速度)
        #攻击城堡
        badrect = pygame.Rect(badguyimg.get_rect())#获取敌人的矩形
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left<64: #碰撞到城堡时
	    #插入击打音乐
            hit.play()
            healthvalue-=random.randint(5,20) #减少城堡的健康值
            badguys.pop(index) #删除敌人
        #使用箭攻击敌人
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):#当箭与敌人相碰时
                #插入消灭敌人的声音
                enemy.play()
                acc[0]+=1
                badguys.pop(index)#删除敌人
                arrows.pop(index1)#删除箭
            index1+=1
            
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg,badguy)  #放置敌人个数

    font = pygame.font.Font(None,24)#默认24号字体
    #时间计算，90000代表1分30秒，按照分和秒的形式来显示，pygame.time.get_ticks()得出的结果是毫秒
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]#时间显示的位置
    screen.blit(survivedtext,textRect) #屏幕显示时间

    #在屏幕上显示血量
    screen.blit(healthbar,(5,5))
    for health1 in range(healthvalue):
        screen.blit(health,(health1+8,8))
    #更新游戏界面
    pygame.display.flip()
    #检查游戏是否需要退出
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        #检查游戏是否有按键按下  
        if event.type==pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        #检查游戏是否有按键放开        
        if event.type==pygame.KEYUP:
            if event.key==K_w:
                 keys[0]=False
            elif event.key==K_a:
                keys[1]=False
            elif event.key==K_s:
                keys[2]=False
            elif event.key==K_d:
                keys[3]=False
        #检测游戏中是否有按下鼠标的操作
        if event.type==pygame.MOUSEBUTTONDOWN:
	    #插入发射箭的声音
            shoot.play()
            position=pygame.mouse.get_pos()
            acc[1]+=1
            #arrows.append([math.anat2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)))
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])              
    #根据按键方向移动,在规定范围内
    if keys[0]:
        playerpos[1]-=5
        if playerpos[1] < 0:
           playerpos[1] = 0 
    elif keys[2]:
        playerpos[1]+=5
        if playerpos[1] > 480: 
           playerpos[1] = 480
    if keys[1]:
        playerpos[0]-=5
        if playerpos[0] < 0:
           playerpos[0] = 0
    elif keys[3]:
        playerpos[0]+=5
        if playerpos[0] > 640:
           playerpos[0] = 640
           
    #游戏输赢处理
    if pygame.time.get_ticks()>90000:#时间到了
        running = 0
        exitcode = 1
    if healthvalue<=0:#城堡被炸毁
        running = 0
        exitcode= 0
    if acc[1]!=0:
        accuracy = acc[0]*1.0/acc[1]*100
    else:
        accuracy = 0
    #屏幕界面显示
if exitcode == 0: 
    pygame.font.init()
    font = pygame.font.Font(None,24)
    text = font.render("Accuracy:"+str(accuracy)+"%",True,(255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text,textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None,24)
    text = font.render("Accuracy:"+str(accuracy)+"%",True,(0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin,(0,0)) 
    screen.blit(text,textRect)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
        
        
            
                
            

