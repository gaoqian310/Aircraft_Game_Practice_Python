# Aircraft Game Practice with Python

A classic Aircraft war game

### Instruction
This game is a classic aircraft war game, user controls a Hero aircraft to survive through enemy aircrafts. Enemy aircrafts are appearing from the top of the screen and moving downwards at random speed. Hero Aircraft will automatically firing bullet stright up and will destroy enemy aircraft once touch it. If hero aircraft collide with enemy aircraft, the game is over.

### How to Achieve

#### 1. Background
Background is one picture, by moving this picture at a constant speed from top to bottom, to achieve a flying effect.

#### 2. Hero Aircraft
Hero Aircraft will appear at the bottom of the screen, at a given coordinates. Monitoring the keyboard input, and given a speed (eg. 2px) to change Hero Aircraft coordinates accordingly if key <- or -> is pressed. Also, Hero Aircraft will be limited to screen pixel size to avoid Hero Aircraft move out of screen.

#### 3. Enemy Aircrafts
Enemy Aircrafts are created through sprite group, they will appearing at random corrrdinates from the top of the screen and moving at a constant (randomly from 2px to 5px). Same as Hero Aircraft, Enemy Aircrafts are limited in screen and not allow appearing from outside.

#### 4. Firing
Hero Aircraft will automatically firing bullet stright up and bullet moving at speed of 3px.

#### 5. Collision
When Bullet collied with Enemy Aircraft, Enemy Aircraft will be destoried. If hero aircraft collide with Enemy Aircraft, the game is over.


###### Credit
This project was completed by following the tutorial on Bilibili @黑马程序员

For more information, see "[More Info](https://www.bilibili.com/video/BV1ex411x7Em?p=461)"
