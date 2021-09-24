from createButton import createButton

def createNumericPad(panel):

    # * Create Numpad
    createButton(panel,0,0,3,"Num\nLock","nl")
    createButton(panel,0,1,1,"/","/")
    createButton(panel,0,2,1,"*","*")
    createButton(panel,0,3,1,"-","-")
    createButton(panel,1,0,1,"7","7")
    createButton(panel,1,1,1,"8","8")
    createButton(panel,1,2,1,"9","9")
    createButton(panel,1,3,1.3,"+","+")
    createButton(panel,2,0,1,"4","4")
    createButton(panel,2,1,1,"5","5")
    createButton(panel,2,2,1,"6","6")
    createButton(panel,3,0,1,"1","1")
    createButton(panel,3,1,1,"2","2")
    createButton(panel,3,2,1,"3","3")
    createButton(panel,3,3,1.3,"Enter","en")
    createButton(panel,4,0,1.2,"0","0")
    createButton(panel,4,2,1,".",".")
