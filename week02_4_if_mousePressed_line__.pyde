def setup ():  #設定
    size(500,500)
def draw():
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
