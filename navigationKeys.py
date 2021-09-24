from createButton import createButton

def createNavigationPad(panel):

    createButton(panel,0,0,3,"Insert\n","ist")
    createButton(panel,0,1,3,"Home\n","home")
    createButton(panel,0,2,3,"Page\nUp","pup")
    createButton(panel,1,0,3,"Delete\n","del")
    createButton(panel,1,1,3,"End\n","end")
    createButton(panel,1,2,3,"Page\nDown","pdown")
    createButton(panel,2,0,0,"","")
    createButton(panel,3,1,1,"↑","up")
    createButton(panel,4,1,1,"↓","down")
    createButton(panel,4,0,1,"←","left")
    createButton(panel,4,2,1,"→","right")


