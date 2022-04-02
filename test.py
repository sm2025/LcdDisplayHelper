import displayHelper as dh;
import time; 

displayH = dh.DisplayHelper()
dis1 = dh.DisplayObject("saroj", "red", 100)
dis2 = dh.DisplayObject("test1", "yellow", 50, (10, 50))
allDisplay = [dis1, dis2]
displayH.completeDisplay(allDisplay)
