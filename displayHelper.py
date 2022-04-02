#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
from copyreg import constructor
from imp import init_builtin
from mimetypes import init
from multiprocessing.pool import INIT
import os
import string
import sys 
import time
import logging
from tracemalloc import start
import spidev as SPI
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont
import textwrap; 


class displayHelper():
    # Raspberry Pi pin configuration:
    # RST = 27
    # DC = 25
    # BL = 18
    # bus = 0 
    # device = 0 
    logging.basicConfig(level=logging.DEBUG)
    
    def __init__(self) -> None:
          # display with hardware SPI:
        ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
        #disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
        self.disp = LCD_2inch.LCD_2inch()
        # Initialize library.
        self.disp.Init()
        # Clear display.
        self.disp.clear()
        self.image, self.draw = self.__newImage()
        

    def __newImage(self):
        # Create blank image for drawing.
        image = Image.new("RGB", (self.disp.height, self.disp.width ), "BLACK")
        draw = ImageDraw.Draw(image)
        return image, draw

    # def displayImage(disp):
    #     image = Image.open('./pic/LCD_2inch.jpg')	
    #     image = image.rotate(180)
    #     disp.ShowImage(image)


    def completeDisplay(self, listOfDisplayProperties):
        for displayProperty in listOfDisplayProperties:
            self.displayText(displayProperty)
        self.__outputDisplay()

    def displayBigText(self,inputStr, color, breakLongWords = True):
        self.__displayText(inputStr, color,90, 7, 3, breakLongWords = breakLongWords)

    def displayText(self,DisplayProperties):
        self.__displayText(DisplayProperties.text, DisplayProperties.color, DisplayProperties.size, 0, 1, startPosition=DisplayProperties.startPosition)

    def __displayText(self, inputStr, color, size, eachLineLen, numOfLines,startPosition = (0,0), breakLongWords = True):
        startPosition = self.__positionPercentToPixel(startPosition)
        font3 = ImageFont.truetype("./Font/Capsmall.ttf",size)
        wrappedText = textwrap.wrap(inputStr, eachLineLen, break_long_words=breakLongWords ) if numOfLines > 1 else [inputStr]
        eachLineHeight = (240 - startPosition[1])/numOfLines
        for text in wrappedText:
            self.draw.text(startPosition, text , fill = color,font=font3)
            listPosition = list(startPosition)
            listPosition[1] += eachLineHeight
            startPosition = tuple(listPosition)

    def __outputDisplay(self):
        try:
            self.image=self.image.rotate(180)
            self.disp.ShowImage(self.image)
            self.disp.module_exit()
            logging.info("quit:")
        except IOError as e:
            logging.info(e)    
        except KeyboardInterrupt:
            self.disp.module_exit()
            logging.info("quit:")
            exit()

    def __positionPercentToPixel(self,position):
        return (position[0]*self.disp.height/100, position[1]*self.disp.width/100)

      
class DisplayObject():
    def __init__(self, text, color, size, startPosition = (0,0)) -> None:
        self.text = text
        self.color = color
        self.size = size
        self.startPosition = startPosition
    
    