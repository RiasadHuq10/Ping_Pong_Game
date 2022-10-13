def setup():
    global bg, leftScore, rightScore, leftY, rightY, ballX,ballY, balldx, balldy, speed, gameStart,gameRestart,loadingScreen, gameOver, winner
    
    loadingScreen = True
    gameStart = False
    gameOver = False
    winner = -1
    leftScore = 0
    rightScore = 0
    leftY = 350
    rightY = 350
    ballX = 665
    ballY = 375
    balldx = 5
    balldy = 5
    speed = 40
    if(random(0,10) > 5):
        balldx = -balldx
    if(random(0,10) > 5):
        balldy = -balldy
    size(1350,800)
    bg = loadImage("pingPongBg.png")
def draw():
    global bg, leftScore, rightScore, leftY, rightY, ballX,ballY, balldx, balldy, speed, gameStart,gameRestart,loadingScreen, gameOver, winner
    image(bg,0,0,width,height)
    if(loadingScreen):
        fill(255)
        rect(425,275,500,200)
        textSize(50)
        fill(0)
        text("PRESS X TO START!", 445,400)
    elif(gameStart):
        fill(255,255,255)
        textSize(75)
        text(str(leftScore),550,100)
        text(str(rightScore),750,100)
        rect(50,leftY,15,100)
        rect(1285,rightY,15,100)
        fill(200)
        rect(ballX,ballY,25,25)
        ballX += balldx
        ballY += balldy
        if((ballY > height - 25) or (ballY < 0)):
            balldy = -balldy
        if( ( ((ballX <= 65 ) and (ballX>=40) )and ( (ballY+25 >= leftY) and (ballY <= leftY + 100 ) )) or ( ((ballX >= 1260 ) and ( ballX<=1285 )and ( (ballY+25 >= rightY) and (ballY <= rightY + 100) ) ) ) ):
            balldx = -balldx
        if(ballX<=0):
            rightScore+=1
            ballX = 662
            ballY = 375
        if(ballX>= width-25):
            leftScore+=1
            ballX = 662
            ballY = 375
        if(leftScore>=10):
            gameOver = True
            gameStart = False
            winner = -1
            bg = loadImage("pingPongBg.png")
            fill(255)
            rect(425,275,500,200)
            textSize(50)
            fill(0)
            text("LEFT WINS", 545,400)
            
        if(rightScore>=10):
            gameOver = True
            gameStart = False
            winner = 1
            bg = loadImage("pingPongBg.png")
            fill(255)
            rect(425,275,500,200)
            textSize(50)
            fill(0)
            text("RIGHT WINS", 545,400)
            
    elif(gameOver):
        if(winner<0):
            bg = loadImage("pingPongBg.png")
            fill(255)
            rect(425,275,500,200)
            textSize(50)
            fill(0)
            text("LEFT WINS", 545,400)
        else:
            bg = loadImage("pingPongBg.png")
            fill(255)
            rect(425,275,500,200)
            textSize(50)
            fill(0)
            text("RIGHT WINS", 545,400)
            
            
    
        
        
        
def keyPressed():
    global leftY, rightY, gameStart,gameRestart,loadingScreen
    if(key == 'x' or key == 'X'):
        gameStart = True
        loadingScreen = False
    
    if(key == 'w' and leftY - speed >= 0):
        leftY -= speed
    if(key == 's' and leftY + speed <= height - 100):
        leftY += speed
    if(keyCode == UP and rightY - speed >= 0):
        rightY -= speed
    if(keyCode == DOWN and rightY + speed <= height - 100):
        rightY += speed
