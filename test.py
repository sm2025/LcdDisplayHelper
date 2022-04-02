import displayHelper as dh;

displayH = dh.displayHelper()
dis1 = dh.DisplayObject("saroj", "red", 100)
dis2 = dh.DisplayObject("test1", "blue", 50, (10, 50))
allDisplay = [dis1, dis2]
displayH.completeDisplay(allDisplay)