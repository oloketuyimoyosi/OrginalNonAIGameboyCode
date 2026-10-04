
import pygame
from math import*
import typing
class LCD:
    def __init__(self,VRAM,OAM,IO,using_window,yPos,xPos,screen,Width,Height,canvas,counter,buffer)-> None:
        self.VRAM:list = VRAM
        self.OAM:list =OAM
        self.IO:list =IO
        self.window:list = using_window
        self.yPos:list = yPos
        self.xPos:list= xPos
        self.Width:int = Width
        self.Height:int  = Height
        self.screen:object = screen
        self.canvas:object = canvas
        self.counter:list = counter
        self.buffer:list = buffer
    
    def GetColour(self,colornum,address):
        palette = self.IO[address-0xff00]

        colour = [0]

        res = ["#CADC9F"]
        if colornum[0] == 0:
            colour[0] = ((palette&0x2)>>1)<<1
            colour_2 = [(palette&0x1)]
           
            colour[0]= colour[0]|colour_2[0]
        elif colornum[0] ==1:
            colour[0] = ((palette&0x8)>>3)<<1
            colour_2 = [(palette&0x4)>>2]

            colour[0]= colour[0]|colour_2[0]
            
        elif colornum[0] ==2:
            colour[0] = ((palette&0x20)>>5)<<1
            colour_2 = [(palette&0x10)>>4]
            colour[0]= colour[0]|colour_2[0]
            
        elif colornum[0] ==3:
            colour[0] = ((palette&0x80)>>7)<<1
            colour_2 = [(palette&0x40)>>6]
            colour[0]= colour[0]|colour_2[0]
        else:

            colour[0] = (palette&0x1)<<1
            colour_2 = [(palette&0x1)]
            colour[0]= colour[0]|colour_2[0]
            
            
        if colour[0] == 0:
            res[0] = "#CADC9F"
        elif colour[0]==1:
            res[0] ="#8bac0f"
        elif colour[0]==2:
            res[0] ="#306230"
        elif colour[0]==3:
            
            res[0] ="#0f380f"
        
        return [res[0],colour]
            
            
    
    
    
    
    
    
    def Render_Tiles(self) -> None:
        #self.canvas.delete("all")
        
        test = LCD(self.VRAM,self.OAM,self.IO,self.window,self.yPos,self.xPos,self.screen,self.Width,self.Height,self.canvas,self.counter,self.buffer)
        lcd_control = self.IO[0xFF40-0xff00]
        tile_Data =[0]
        background_Memory = [0]
        unsig = [1]
        scrollY = [self.IO[0xFF42-0xFF00]]

        scrollX = [self.IO[0xFF43-0xff00]]
        windowY=[self.IO[0xFF4A-0xff00]]
        windowX = [self.IO[0xFF4B-0xff00] -7]#might change to plus later
        self.window[0] = 0
        window_line_Counter =[0] 
        x =[0]
        y =[0]


        
            
            
            
            
            
        
        x_counter = [0]
        for i in range(0,160):
            


                
                
            if self.IO[0xff44-0xff00]>143:
                self.counter[0] = 0
            if (self.IO[0xFF40-0xff00]&0x20)>>5 == 1:
                
            
                if windowY[0]<self.IO[0xff44-0xff00] and i+1 > windowX[0]:    
                    self.window[0] = 1
                else:
                    self.window[0] = 0


            if (self.IO[0xFF40-0xff00]&0x10)>>4 == 1: 
                tile_Data[0]=0x8000
                unsig[0]=1
                #self.window[0]=0
            
                
                
                
            else:
                tile_Data[0]=0x8800
                unsig[0]= 0           
            if self.window[0] == 0:
                if (self.IO[0xFF40-0xff00]&0x8)>>3 == 1:
                    background_Memory[0]=0x9C00
                else:
                    background_Memory[0]=0x9800
            
            else:
                if (self.IO[0xFF40-0xff00]&0x40)>>6 == 1:
                    background_Memory[0]=0x9C00
                else:
                    background_Memory[0]=0x9800
                    
                    
            
            self.yPos[0]=0
            a = self.window[0]^1
            if a ==1:
                self.yPos[0]=(scrollY[0]+self.IO[0xFF44-0xff00]-1)&0xFF
                tile_Row = [(((self.yPos[0]))>>3)<<5]

                
            else:
                #window_line_Counter[0]+=1
                self.yPos[0]= self.counter[0]

                tile_Row = [(((self.yPos[0]))>>3)<<5]


                
                
                
            if self.window[0] == 0:    
                self.xPos[0] = i+(scrollX[0])
                tile_Col = [(self.xPos[0]>>3)&0x1f]
            else:
                self.xPos[0] = i - windowX[0]
                tile_Col = [(self.xPos[0]>>3)]
                



            tileNum=[0]        
            
            
            tile_Address = [(background_Memory[0]+tile_Row[0]+tile_Col[0])]
            tile_num_1 = [0]
            
            
            
            if unsig[0]==1:
                tileNum[0]= self.VRAM[tile_Address[0]-0x8000]
            else:
                tileNum[0]= self.VRAM[tile_Address[0]-0x8000]
                if tileNum[0] >= 0x80:
                    tileNum[0] =(tileNum[0]&0x7F )-0x80
                    
            tileLocation = [tile_Data[0]]
            
            if unsig[0] ==1:
                tileLocation[0]= tileLocation[0]+(tileNum[0]<<4)
            else:
                tileLocation[0]= tileLocation[0]+((tileNum[0]+128)<<4)
                
            

            Line= [self.yPos[0]%8]
            
            Line[0] = Line[0]<<1
            data_1= [self.VRAM[((tileLocation[0]+Line[0])-0x8000)]]
            data_2= [self.VRAM[((tileLocation[0]+Line[0]+1)-0x8000)]]
            
            
            colourBit = [self.xPos[0]%8]
            colourBit[0] = colourBit[0]-7
            
            colourBit[0] = colourBit[0]*-1

            
            if colourBit[0]==0:
                pos = 0x1
            elif colourBit[0]==1:
                pos = 0x2
            elif colourBit[0]==2:
                pos = 0x4
            elif colourBit[0]==3:
                pos = 0x8
            elif colourBit[0]==4:
                pos = 0x10
            elif colourBit[0]==5:
                pos = 0x20
            elif colourBit[0]==6:
                pos = 0x40
            elif colourBit[0]==7:
                pos = 0x80
            
            
            
            colour_num=[0]
            colour_num[0] = (data_2[0]&pos)>>colourBit[0]

            colour_num[0] = colour_num[0]<<1
            colour_num2 = [(data_1[0]&pos)>>colourBit[0]]
            colour_num[0]= colour_num[0]|colour_num2[0]

            if (self.IO[0xFF40-0xff00]&0x01) == 0:
                self.window[0] = 0
                color = "green"
            else:
                
                color = test.GetColour(colour_num,0xFF47)[0]
            
            final = self.IO[0xFF44-0xff00]
            new_y =[0]
            if scrollY[0]>112:
                new_y[0] = scrollY[0]-112
                final_y = 144+final  - new_y[0]
            else:
                final_y = final
            
            
            if (final<0 or final>143) or ((i<0)or(i>159)):
                continue
            
            

            screen_X = i +((scrollX[0]+159)%256)%159
            screen_Y = final+((scrollY[0]+143)%256)%143



            #self.canvas.create_rectangle(i*2,final*2,i*2,final*2,fill=color,outline=color)
            test_surface = pygame.Surface((i,final))
            square = pygame.Rect(i*2,final*2,2,2)
            pygame.draw.rect(self.screen,color,square)
            self.buffer[final*160+i] = test.GetColour(colour_num,0xFF47)[1]
            #self.canvas.pack()
        if self.window[0] == 1:
                self.counter[0]+=1


    def RenderSprite(self) -> None:
        use8x16 = False
        test = LCD(self.VRAM,self.OAM,self.IO,self.window,self.yPos,self.xPos,self.screen,self.Width,self.Height,self.canvas,self.counter,self.buffer)

        sprite = 0
        for i in range(0,10):
            if (self.IO[0xFF40-0xff00]&0x4)>>2 == 1:
                use8x16 = True
            scanline = self.IO[0xFF44-0xFF00]
            a = self.OAM
            b = [a[i:i+4] for i in range(0,len(a),4)]
            c = list(filter(lambda x: x[0]==scanline+16, b))
            if len(c) > 10:
                c= c[0:10]
            
            index = sprite*4
            c.sort(key = lambda item: item[1])
            ypos = c[9-i][0] -16
            xpos = c[9-i][1] - 8




            
                
            attribute = c[9-i][3]
            
            yFlip = (attribute&0x40)>>6
            xFlip = (attribute&0x20)>>5

            tileLocation = c[9-i][2]
            #print(b)

            


            
            
            ysize = 8
            if use8x16 == True:
                ysize = 16
                
            if ((scanline> ypos)and(scanline<=(ypos+ysize))):
                line = scanline - ypos -1
                
                if yFlip == 1 :
                    #print("ok")
                    line -= ysize-1
                    line *=-1
                    
                line *=2
                if use8x16 ==1:
                    tileLocation &= 0xFE

                dataAddress = (tileLocation<<4)+line

                data1 = [self.VRAM [dataAddress]]
                data2 = [self.VRAM [dataAddress+1]]


                tilePixel = 7 
                for c in range(0,8):
                    
                    
                    colourbit = [tilePixel]
                    
                    if xFlip == 1 :
                        colourbit[0] -=7
                        colourbit[0] *=-1
                    if colourbit[0]==0:
                        pos = 0x1
                    elif colourbit[0]==1:
                        pos = 0x2
                    elif colourbit[0]==2:
                        pos = 0x4
                    elif colourbit[0]==3:
                        pos = 0x8
                    elif colourbit[0]==4:
                        pos = 0x10
                    elif colourbit[0]==5:
                        pos = 0x20
                    elif colourbit[0]==6:
                        pos = 0x40
                    elif colourbit[0]==7:
                        pos = 0x80
                    colour_num=[0]
                    colour_num[0] = (data2[0]&pos)>>colourbit[0]
                    colour_num[0] = colour_num[0]<<1
                    colour_num2 = [(data1[0]&pos)>>colourbit[0]]
                    colour_num[0]= colour_num[0]|colour_num2[0]
                    colorAddress = (attribute & 0x10)>>4
                    if colorAddress ==1:
                        col = test.GetColour(colour_num,0xFF49)[0]
                    else:
                        col = test.GetColour(colour_num,0xFF48)[0]
                    priority = (attribute&0x80)>>7

                    
                    xpix = 0 - tilePixel
                    xpix+=7 
                    pixel = xpos+xpix
                    #print(priority)
                    if self.buffer[scanline*160+pixel][0] == 0 and priority == 1:
                        
                        
                        if (scanline<0 or scanline>143) or ((pixel<0)or(pixel>159)):
                                    continue
                                
                                


                        
                        #self.canvas.create_rectangle(pixel*2,scanline*2,pixel*2,scanline*2,fill=col,outline=col)
                        square = pygame.Rect(pixel*2,scanline*2,2,2)
                        pygame.draw.rect(self.screen,col,square)
                        #self.canvas.pack()
                    #print(priority)
                    if priority == 0 and col !="#CADC9F" :
                        

                            
                            
                            if (scanline<0 or scanline>143) or ((pixel<0)or(pixel>159)):
                                        continue
                                    
                                    


                            
                            #self.canvas.create_rectangle(pixel*2,scanline*2,pixel*2,scanline*2,fill=col,outline=col)
                            square = pygame.Rect(pixel*2,scanline*2,2,2)
                            pygame.draw.rect(self.screen,col,square)
                            
                            #self.canvas.pack()
                        
                        

                    tilePixel -=1 
            sprite = i 

        
        
            
            
    def DrawScanLine(self) -> None:
        test = LCD(self.VRAM,self.OAM,self.IO,self.window,self.yPos,self.xPos,self.screen,self.Width,self.Height,self.canvas,self.counter,self.buffer)
        control = self.IO[0xFF40-0xFF00]
        if (control&0x1) == 1:
            test.Render_Tiles()

        if ((control&0x2))>>1 == 1:
            test.RenderSprite()


            
            
            
        
            
                
            
             

                
        