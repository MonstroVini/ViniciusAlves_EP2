# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:35:44 2015

@author: viniciusra
"""


import turtle
import random



f = open("entrada.txt", encoding="UTF-8").readlines()
palavra = random.choice(f)
print (palavra)


window = turtle.Screen()
window.bgcolor('black')
window.title('A Forca')

tartaruga = turtle.Turtle()
tartaruga.color('white')
tartaruga.speed(5)
tartaruga.penup()
tartaruga.setpos(-120, 150)
tartaruga.pendown()
tartaruga.left(90)
tartaruga.forward(50)
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.forward(400)
tartaruga.right(90)
tartaruga.forward(30)
tartaruga.right(180)
tartaruga.forward(60)
tartaruga.penup()
tartaruga.forward(55)
tartaruga.pendown()
tartaruga.forward(25)
tartaruga.penup()

i = 0

while i != len(palavra)-1:
    tartaruga.forward(25)
    tartaruga.pendown()
    tartaruga.forward(25)
    tartaruga.penup()
    i += 1


letra = window.textinput("A Forca", "Faça seu chute")
    
         

def head ():
    head = turtle.Turtle()
    head.pendown()
    head.setpos(-120,100)
    head.color('white')
    head.pendown()
    head.circle(25)
    head.forward(-10)
    

def body():
    body = turtle.Turtle()
    body.penup()
    body.color('white')
    body.setpos(-120,100)
    body.pendown()    
    body.right(90)
    body.forward(120)
    

def arm1 ():
    arm1 = turtle.Turtle()
    arm1.penup()
    arm1.color('white')
    arm1.setpos(-120,70)
    arm1.pendown()
    arm1.right(45)
    arm1.forward(50)
    

def arm2 ():
    arm2 = turtle.Turtle()
    arm2.penup()
    arm2.color('white')
    arm2.setpos(-120,70)
    arm2.pendown()
    arm2.right(135)
    arm2.forward(50)


def leg1 ():
    leg1 = turtle.Turtle()
    leg1.penup()
    leg1.color('white')
    leg1.setpos(-120,-15)
    leg1.pendown()
    leg1.right(45)
    leg1.forward(50)
    

def leg2 ():
    leg2 = turtle.Turtle()
    leg2.penup()
    leg2.color('white')
    leg2.setpos(-120,-15)
    leg2.pendown()
    leg2.right(135)
    leg2.forward(50)



x = 'acerto'
y = 'erro'
acerto = 0
erro = 0


while erro != 7:
    if letra in palavra:
        
        acerto =+1
    else:
        erro += 1
        
    if erro ==1:
        head()
        letra = window.textinput("A Forca", "Faça seu chute")
                    
    if erro == 2:
        body()
        letra = window.textinput("A Forca", "Faça seu chute")
        
    if erro == 3:
        arm1()
        letra = window.textinput("A Forca", "Faça seu chute")
    
    if erro == 4:
        arm2()
        letra = window.textinput("A Forca", "Faça seu chute")
        
    if erro == 5:
        leg1()
        letra = window.textinput("A Forca", "Faça seu chute")
        
    if erro == 6:
        leg2()
        
        
        
        
        
   
        
    

    
    
    

    
        
    
    
    

    
    
    
    
    
     


     










#for i in range(3):
#    tartaruga.left(angulo)
#    tartaruga.forward(dist)
#    
window.exitonclick()














    
    









    
    
    












