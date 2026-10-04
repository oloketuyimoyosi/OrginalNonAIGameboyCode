from tkinter import *
from tkinter import filedialog
import multiprocessing



import numpy as np 
window =Tk()
p = []

mcb = {
    0x0:1,
    0x01:4,
    0x02:8,
    0x03:16,
    0x04:32,
    0x05:64
}
ram ={
    0x0:0,
    0x01: 2048,
    0x02: 8192,
    0x03:32768,
    0x04: 131072,
    0x05: 65536
}
mcb_type = {
    0x0:"None",
    0x01: ("MBC1","NONE"),
    0x02: ("MBC1","RAM"),
    0x03: ("MBC1","Battery-Buffered RAM"),
    0x05: ("MBC2","None"),
    0x06: ("MBC2","RAM"),
    0x08:("None","RAM"),
    0x09: ("None","RAM"),
    0X0B: ("MM01","None"),
    0x0C: ("MM01","RAM"),
    0x0D: ("MM01","Battery-Buffered RAM"),
    0x0F: ("MBC3","Real Time Clock"),
    0x10:("MBC3","Battery-Buffered RAM"),
    0x11:("MBC3","None"),
    0x12:("MBC3", "Battery-Buffered RAM"),
    0x13:("MBC3","Battery-Buffered RAM"),
    0x19:("MBC5","None"),
    0x1A: ("MBC5","RAM"),
    0x1B: ("MBC51","Battery-Buffered RAM"),
    0x1C: ("MBC5","Rumble"),
    0x1D: ("MBC5","Rumble+Ram"),
    0x1E: ("MBC5","Batttery-Buffered RAM"),
    0x20: ("MCB6","None")
}

def opens():
    file = filedialog.askopenfilename()
    with open(file,"rb") as d:
        program = d.read()
        return program
rom = opens()        

A= np.array([0x01],dtype= np.int64)
#A= [0x01]

B= np.array([0x00],dtype= np.int64)
#B= [0x00]
#C= [0x13]
C = np.array([0x13],dtype= np.int64)
#D=[0x00]
D= np.array([0x13],dtype= np.int64)
#E = [0xDE]
E= np.array([0xDE],dtype= np.int64)
#H = [0x01]
H= np.array([0x01],dtype= np.int64)
#L = [0x4D]
L= np.array([0x4D],dtype= np.int32)
F=[0xB0]
F= np.array([0xB0],dtype= np.int32)

PC = [0x100]
AF =[0x0001]
BC =[0x0013]
DE =[0x00DE]
HL=[0x014D]
buffer = [0]*160*144

#AF[0] = A[0]<<8 | F[0]
#AF[0]= 0x0001
#F[0]=0xB0
#BC[0] = B[0]<<8 | C[0]
#BC[0] = 0x0013
#DE[0] =D[0]<<8| E[0]
#DE[0] = 0x00DE
#HL[0] = H[0]<<8| L[0]
HL[0]=0x014D
SP = [0xFFFE]
#IO = [0]*0x80
IO = np.zeros(0x80,dtype= np.int32)

OAM= [0]*0xA0


#HRAM =[0]*0x7F
HRAM = np.zeros(0x7F, dtype= np.int32)

IER = [0x0]



IO[0xFF00-0xff00] = 0xCF
IO[0xFF01-0xff00] = 0x00
IO[0xFF02-0xff00] = 0x7E
IO[0xFF04-0xff00] = 0x18
IO[0xFF05-0xff00] = 0x00
IO[0xFF06-0xff00] = 0x00
IO[0xFF07-0xff00] = 0xFD
IO[0xFF0F-0xff00] = 0xE1
IO[0xFF10-0xff00] =0x80
IO[0xFF11-0xff00] = 0xBF
IO[0xFF12-0xff00] = 0xF3
IO[0xFF14-0xff00] = 0xBF
IO[0xFF16-0xff00] = 0X3F
IO[0xFF17-0xff00] = 0x00
IO[0xFF19-0xff00] = 0xBF
IO[0xFF1A-0xff00] = 0x7F
IO[0xFF1C-0xff00] =0x9F
IO[0xFF1E-0xff00] = 0xBF
IO[0xFF20-0xff00] = 0xFF
IO[0xFF21-0xff00] = 0x00
IO[0xFF22-0xff00] = 0x00
IO[0xFF23-0xff00] = 0xBF
IO[0xFF24-0xff00] = 0x77
IO[0xFF25-0xff00] = 0xF3
IO[0xFF26-0xff00] = 0xF1
IO[0xFF40-0xff00] = 0x91
IO[0xFF41-0xff00] = 0x81
IO[0xFF42-0xff00] = 0x00
IO[0xFF43-0xff00] = 0x00
IO[0xFF44-0xff00] = 0x91
IO[0xFF45-0xff00] = 0x00
IO[0xFF47-0xff00] = 0xFC
IO[0xFF46-0xff00] = 0xFF

IO[0xFF4A-0xff00] = 0x00
IO[0xFF4B-0xff00] = 0x00

#print(IO)

#VRAM = [0]*0x2000
VRAM = np.zeros(0x2000, dtype= np.int32)

#WRAM = [0]*(8*1024)
WRAM = np.zeros(8192, dtype= np.int32)

MCB = mcb_type[rom[0x0147]][0]
import pygame
pygame.init()

cycles = [0]

Ramswitch = [0]
Romswitch = [0]
R=[0]
s =[0,0,0,0]
disable_Vram=[0]
disable_OAM=[0]
current_cycles=[0]
RamEnabled = [0]
banks = mcb[rom[0x0148]]
no_ram = ram[rom[0x0149]]
#Rambank = [0]*no_ram
Rambank = np.zeros(no_ram, dtype= np.int32)
oplist =[0] 
if no_ram > 8192:
    Rambank=[Rambank[i:i+8192]for i in range(0,len(Rambank),8192)]
else:
    Rambank=np.zeros(8192,dtype= np.int32)
Rombank = [rom[i:i+16384]for i in range(0,len(rom),16384)]
loc = [0]
Call =[0]
#print(Rombank[1][0x100],2222222222222222222222)
#print(len(Rombank))
n = 0
#print(Rombank[0][0x0149],99999999999999999999999999999999999)   
paused = [False]
IMF =[0]
ECHO = [0]*0x1E00
#ECHO = [WRAM[0:0+0x1E00]]
Not_Usable = [0]*0x60
counter = [0]
Timer_counter = [0]


import sys
import os
sys.path.append("C:\\Users\\oloke\\Downloads\\New folder (3) - Copy")

from CPU import *
dd = Opcode(BC,PC,AF,DE,HL,SP,Rombank,Rambank,IO,A,B,C,D,E,F,H,L,OAM,IER,cycles,s,Ramswitch,Romswitch,MCB,RamEnabled,VRAM,R,WRAM,HRAM,oplist,paused,ECHO,IMF,loc,Call,current_cycles,Not_Usable,disable_Vram,disable_OAM,Timer_counter)
g =[]
using_window=[0]
yPos =[0]
xPos = [0]
Width = 160*2
Heigth = 144*2
display = pygame.display.set_mode((Width,Heigth))
canvas =0
from LCD import*
screen = LCD(VRAM,OAM,IO,using_window,yPos,xPos,display,Width,Heigth,canvas,counter,buffer)
from Timer import *
Enabled = [0]
timer = Timer(cycles,loc,IO,Timer_counter)
divide_reg = [0]

def divide():
    divide_reg[0]+=current_cycles[0]
    if divide_reg[0] >= 255:
        divide_reg[0] =0
        IO[0xFF04-0xff00] +=1


timer.set_count_timer()
def Update_Timer():
    divide()

    if (IO[0xFF07-0xff00]&0x4)>>2 ==1:
        
        Timer_counter[0] -= current_cycles[0]

        if Timer_counter[0]<=0:
            timer.set_count_timer()
            
            if IO[0xFF05-0xff00] >= 255:
                dd.Write_to_Memory_u16([0xFF05],[IO[0xFF06-0xff00]])
                dd.request_interrupt(2)
            else:
                dd.Write_to_Memory_u16([0xFF05],[IO[0xFF05-0xff00]+1])
   
   
LCD_ENABLED = [(IO[0xFF40-0xff00]&0x80)>>7]
   
Scanline = [456]   
mode =[0]
reqInt=[0]
currentlines = [0]
count = [0]
def SET_LCD_STATUS():
    status= [IO[0xFF41-0xff00]]





    if (IO[0xFF40-0xff00]&0x80)>>7 == 0:
        Scanline[0]=456
        IO[0xFF44-0xff00] = 0
        status[0]= status[0]&252
        status[0] = status[0]|0x1
        dd.Write_to_Memory_u16([0xFF41],status)
    currentline = IO[0xFF44-0xff00]
    currentmode = status[0]&0x3
    mode[0]=0
    reqInt[0]=0
    if currentline >= 144:
        mode[0] =1
        status[0]= status[0]|0x1
        disable_OAM[0] =0
        disable_Vram[0] =0
        status[0] = status[0]&0xFD
        #print("yes")
        reqInt[0] = (status[0]&0x10)>>4
        #dd.request_interrupt(0)

    else:
        mode2bounds =456-80
        mode3bounds = mode2bounds-172
        
        if Scanline[0]>=mode2bounds:
            mode[0] =2
            disable_Vram[0] = 0
            status[0]= status[0]|0x2
            status[0] = status[0]&0xFE


            reqInt[0] = (status[0]&0x20)>>5
        elif Scanline[0]>=mode3bounds:
            mode[0] =3
            disable_Vram[0] =0


            status[0]= status[0]|0x2
            status[0] = status[0]|0x1
        else:
            mode[0]=0
            disable_Vram[0] =0
            status[0] = status[0]&0xFD
            status[0] = status[0]&0xFE
            
            reqInt[0] = (status[0]&0x08)>>3
            
    if reqInt[0] == 1 and  mode[0] != currentmode:
        dd.request_interrupt(1)


    if IO[0xFF44-0xff00]== IO[0xFF45-0xff00]:
        status[0]= status[0]|0x4
        if ((status[0]&0x40)>>6) == 1:
            if (IO[0xFF0F-0xff00]&0x2)>>1 ==0 and count[0] == 0:
                dd.request_interrupt(1)
                
                count[0] +=1
    else:
        status[0]=status[0]&0xFB
        count[0] = 0

            

    dd.Write_to_Memory_u16([0xFF41],status)
v= [0]
def UpdateGraphic():
    

    #print("LCD:"+hex(LCD_ENABLED[0]))

        
    if (IO[0xFF40-0xff00]&0x80)>>7==1:
        Scanline[0] = Scanline[0] - current_cycles[0]
        #print("scanline"+hex(Scanline[0]))

    if Scanline[0]<=0:
        IO[0xFF44-0xff00] = IO[0xFF44-0xff00]+1
        currentlines[0] = IO[0xFF44-0xff00]
        Scanline[0] =456
        
        if currentlines[0] == 144:
            dd.request_interrupt(0)


            
            
        elif currentlines[0]>153:
            IO[0xFF44-0xff00]=0
        if currentlines[0]<144:
            screen.DrawScanLine()
        else:
            counter[0] =0
    SET_LCD_STATUS()

            
    

            

        
    
    
            

    
    

    

s[3]=0
R[0] = 0
def execute(PC):
    if (IO[0xFF0F-0xff00]&IER[0])==0 and oplist[0] =="halted" :

        PC[0]-=1


    address = PC
    
    if PC[0]>= 0x0000 and PC[0]<=0x3FFF:
        if Romswitch[0] == 1:
            if s[3] <=len(Rombank) and s[3]>0:

                opcode = Rombank[s[3]][PC[0]-0x0000]
            else:
                opcode = Rombank[0][PC[0]-0x0000]
        else:

            opcode = Rombank[0][PC[0]-0x0000]
    elif (address[0]>= 0x4000 and address[0]<=0x7FFF):
            
            if s[0]>0:

                opcode = Rombank[s[0]][address[0]-0x4000]
            else:
                    #self.s[0] = 1
                opcode= Rombank[1][address[0]-0x4000]
    
    elif address[0]>= 0X8000 and address[0]<= 0x9FFF:
        if disable_Vram[0] ==0:
            opcode =  VRAM[address[0]-0x8000]
        else:
            opcode = 0xFF
    elif address[0]>= 0XA000 and address[0]<= 0xBFFF:
        if RamEnabled[0] == 1:
            if Ramswitch[0] == 1:
                if  R[0]>0:
                    opcode =  Rambank[ R[0]][address[0]-0xA000] 
                else:
                     opcode =Rambank[0][address[0]-0xA000] 
        
            else:
                opcode =  Rambank[ 0][address[0]-0xA000] 

    elif  PC[0]>= 0XC000 and  PC[0]<= 0xDFFF:
            
            opcode =  WRAM[address[0]-0xC000] 
    elif  PC[0]>= 0xE000 and  PC[0]<=0xFDFF:
            opcode =  ECHO[address[0]-0xE000] 
    elif address[0]>= 0xFE00 and address[0]<=0xFE9F:
            
            opcode =  OAM[address[0]-0xFE00]
    elif address[0]>= 0xFEA0 and address[0]<= 0xFEFF:
            opcode =  Not_Usable[address[0]-0xFEA0] 
    elif address[0]>= 0xFF00 and address[0]<= 0xFF7F:
            opcode =  IO[address[0]-0xff00] 

    elif address[0]>= 0xFF80 and address[0]<= 0xFFFE:
            
            opcode=  HRAM[address[0]-0xFF80] 
    elif address[0] == 0xFFFF:
        opcode =IER[0]


    #print(hex(PC[0]),s[1])


    
    AF[0] = A[0]<<8 | F[0]
    BC[0] = B[0]<<8 | C[0]
    #BC[0] = 0x0013
    DE[0] =D[0]<<8| E[0]
    #DE[0] = 0x00DE
    HL[0] = H[0]<<8| L[0]
    command = [[0x00],#0
               [0x10],#1
               [[0x20],[0x30]],# 2 JR NZ ,r8
               [0x01,0x11,0x21,0x31], # 3 LD r16 d16
               [0x02,0x12,0x22,0x32], # 4 LD r16 A
               [0x03,0x13,0x23,0x33], # 5 INC r16
               [0x04,0x14,0x24,0x34], # 6 INC r8
               [0x05,0x15,0x25,0x35], # 7 DEC r8
               [0x06,0x16,0x26,0x36], # 8 LD r8 d8
               [0x07,0x17],# 9 RLCA,RLA
               [0x27,0x37],# 10 DAA,SCF
               [0x08],# 11 LD a16 SP
               [0x18,0x28,0x38],# 12 JR imm8
               [0x09,0x19,0x29,0x39],# 13 ADD HL r16
               [0x0A,0x1A,0x2A,0x3A],# 14 LD A r16
               [0x0B,0x1B,0x2B,0x3B],#15 DEC r16 
               [0x0C,0x1C,0x2C,0x3C],#161NC_CELA
               [0x0D,0x1D,0x2D,0x3D],#17DEC_CELA
               [0x0E,0x1E,0x2E,0x3E],#18LD_CELA
               [[0x0F],[0x1F]],#19RRCA,RRA
               [[0x2F],[0x3F]],#20 CPL,CCF
               [0x40,0x50,0x60,0x70],#21 LD B
               [0x41,0x51,0x61,0x71],#22 LD C
               [0x42,0x52,0x62,0x72],#23LD D
               [0X43,0x53,0x63,0x73],#24 LD E
               [0x44,0x54,0x64,0x74],#25 LD H
               [0x45,0x55,0x65,0x75],#26 LD L
               [0x46,0x56,0x66],#27 LD [HL]
               [0x47,0x57,0x67,0x77],#28 LD A
               [0x48,0x58,0x68,0x78],#29 LD CELA B
               [0x49,0x59,0x69,0x79],#30 LD CELA C
               [0x4A,0x5A,0x6A,0x7A],#31 LD CELA D
               [0x4B,0x5B,0x6B,0x7B],#32 LD CELA E
               [0x4C,0x5C,0x6C,0x7C],#33LD CELA H
               [0X4D,0x5D,0x6D,0x7D],#34 LD CELA L
               [0x4E,0x5E,0x6E,0x7E],#35 LD CELA [HL]
               [0x4F,0x5F,0x6F,0x7F],#36 LD CELA A

               [0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87],#37
               [0x88,0x89,0x8A,0x8B,0x8C,0x8D,0x8E,0x8F],#38
               [0x90,0x91,0x92,0x93,0x94,0x95,0x96,0x97],#39
               [0x98,0x99,0x9A,0x9B,0x9C,0x9D,0x9E,0x9F],#40
               [0xA0,0xA1,0xA2,0xA3,0xA4,0xA5,0xA6,0xA7],#41
               [0xA8,0xA9,0xAA,0xAB,0xAC,0xAD,0xAE,0xAF],#42
               [0xB0,0xB1,0xB2,0xB3,0xB4,0xB5,0xB6,0xB7],#43
               [0xB8,0xB9,0xBA,0xBB,0xBC,0xBD,0xBE,0xBF],#44
               [0xC1,0xD1,0xE1,0xF1],#45 POP
               [0xC5,0xD5,0xE5,0xF5],#46 PUSH
               [0xC2,0xD2],#47 JUMP NZ NC
               [0xC3],#48 JUMP n16
               [0xCA,0xDA],#49 JUMP Z,JUMP C  
               [0XC0,0xD0],#50 RET NZ NC
               [0xC4,0xD4],#51 CALL NZ NC
               [0xC8,0xD8],#52 RET Z C
               [0xC9],#53 RET
               [0xCC,0xDC],#54 CALL Z C
               [0xCD], #55 CALL 
               [0xE0],#56 LD [a8] A
               [0XF0],#57 LD A [a8]
               [0xF3],#58DI
               [0xFB],# 59EI
               [0xEA],#60
               [0xFE],#61
               [0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17],#62
               [0x18,0x19,0x1A,0x1B,0x1C,0x1D,0x1E,0x1F],#63
               [0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27],#64
               [0x28,0x29,0x2A,0x2B,0x2C,0x2D,0x2E,0x2F],#65
               [0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37],#66
               [0x38,0x39,0x3A,0x3B,0x3C,0x3D,0x3E,0x3F],#67
               [0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47],#68
               [0x48,0x49,0x4A,0x4B,0x4C,0x4D,0x4E,0x4F],#69
               [0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57],#70
               [0x58,0x59,0x5A,0x5B,0x5C,0x5D,0x5E,0x5F],#71
               [0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67],#72
               [0x68,0x69,0x6A,0x6B,0x6C,0x6D,0x6E,0x6F],#73
               [0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77],#74
               [0x78,0x79,0x7A,0x7B,0x7C,0x7D,0x7E,0x7F],#75
               [0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87],#76
               [0x88,0x89,0x8A,0x8B,0x8C,0x8D,0x8E,0x8F],#77
               [0x90,0x91,0x92,0x93,0x94,0x95,0x96,0x97],#78
               [0x98,0x99,0x9A,0x9B,0x9C,0x9D,0x9E,0x9F],#79
               [0xA0,0xA1,0xA2,0xA3,0xA4,0xA5,0xA6,0xA7],#80
               [0xA8,0xA9,0xAA,0xAB,0xAC,0xAD,0xAE,0xAF],#81
               [0xB0,0xB1,0xB2,0xB3,0xB4,0xB5,0xB6,0xB7],#82
               [0xB8,0xB9,0xBA,0xBB,0xBC,0xBD,0xBE,0xBF],#83
               [0xC0,0xC1,0xC2,0xC3,0xC4,0xC5,0xC6,0xC7],#85
               [0xC8,0xC9,0xCA,0xCB,0xCC,0xCD,0xCE,0xCF],#86
               [0xD0,0xD1,0xD2,0xD3,0xD4,0xD5,0xD6,0xD7],#87
               [0xD8,0xD9,0xDA,0xDB,0xDC,0xDD,0xDE,0xDF],#88
               [0xE0,0xE1,0xE2,0xE3,0xE4,0xE5,0xE6,0xE7],#89
               [0xE8,0xE9,0xEA,0xEB,0xEC,0xED,0xEE,0xEF],#90
               [0xF0,0xF1,0xF2,0xF3,0xF4,0xF5,0xF6,0xF7],#72
               [0xF8,0xF9,0xFA,0xFB,0xFC,0xFD,0xFE,0xFF],#73
               ]# 


    






    
    if opcode in command[0]:
        #print("andddddddddd")
        #print(PC)
        dd.NOP()
        current_cycles[0]=4
    elif opcode in command[2][0]:
        dd.jr_NZ_imm8()
    elif opcode in command[2][1]:
        dd.jr_NC_imm8()
        
    elif opcode in command[3]:
        dd.LD_r16_imm16()
        
        
    elif opcode in command[4]:
        #print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        dd.LD_r16mem_A()
        
    elif opcode in command[5]:
        dd.inc_r16()
    elif opcode in command[6]:
        dd.inc_r8()
    elif opcode in command[7]:
        dd.dec_r8()
    elif opcode in command[8]:
        dd.LD_r8_imm8()
    elif opcode == command[9][0]:
        
        dd.rlca()
    elif opcode == command[9][1]:
        
        dd.rla()

    elif opcode in command[11]:
        #print("okkkkkkkkkkkkkkkkkkkkkk")

        dd.LD_imm16_SP()
        current_cycles[0] =20
    elif opcode == 0x18:
        dd.jr_imm8()
        #print("wjgkhjgmhghjfhjfjgfjhg")
    elif opcode == command[12][1]:
        dd.jr_Z_imm8()
    elif opcode == command[12][2]:
        dd.jr_C_imm8()
    
    elif opcode in command[13]:
        dd.add_hl_r16()
    elif opcode in command[14]:
        #print("okkkkkkkkkkkkkkkkkkkkkk")

        dd.LD_A_r16mem() 

    elif opcode in command[15]:
        dd.dec_r16()
    elif opcode in command[16]:
        dd.inc_CELA()
    elif opcode in command[17]:
        dd.dec_CELA()
    elif opcode in command[18]:
        dd.LD_CELA_imm8()
    elif opcode in command[19][0]:
        dd.rrca()
    elif opcode in command[19][1]:
        dd.rra()
    elif opcode in command[20][0]:
        dd.cpl()
    elif opcode in command[20][1]:
        dd.ccf()
    elif opcode in command[21]:
        dd.ld_r8_B()
    elif opcode in command[22]:
        dd.ld_r8_C()
    elif opcode in command[23]:
        dd.ld_r8_D()
    elif opcode in command[24]:
        dd.ld_r8_E()
    elif opcode in command[25]:
        dd.ld_r8_H()
        
    elif opcode in command[26]:
        dd.ld_r8_L()
    elif opcode in command[27]:
        dd.ld_r8_HL()
    elif opcode in command[28]:
        dd.ld_r8_A()        
    elif opcode in command[29]:
        dd.ld_CELA_B()
    elif opcode in command[30]:
        dd.ld_CELA_C()
    elif opcode in command[31]:
        dd.ld_CELA_D()
    elif opcode in command[32]:
        dd.ld_CELA_E()
    elif opcode in command[33]:
        dd.ld_CELA_H()
    elif opcode in command[34]:
        dd.ld_CELA_L()
    elif opcode in command[35]:
        dd.ld_CELA_HL()
    elif opcode in command[36]:
        dd.ld_CELA_A()
    elif opcode in command[37]:
        dd.ADD_A_r8()
    elif opcode in command[38]:
        dd.ADC_A_r8()
    elif opcode in command[39]:
        dd.SUB_A_r8()
    elif opcode in command[40]:
        dd.SUBC_A_r8()
    elif opcode in command[41]:
        dd.AND_A()
    elif opcode in command[42]:
        dd.XOR_A()
    elif opcode in command[43]:
        dd.OR_A()
        
    elif opcode in command[44]:
        dd.CP_A_r8()
    elif opcode in command[45]:
        dd.POP_r16()
    elif opcode in command[46]:
        dd.PUSH_r16()
    elif opcode == command[47][0]:
        dd.JUMP_NZ_imm16()
    elif opcode == command[47][1]:
        dd.JUMP_NC_imm16()
    elif opcode in command[48]:
        dd.JUMP()
    elif opcode == command[49][0]:
        dd.JUMP_Z_imm16()
    elif opcode == command[49][1]:
        dd.JUMP_C_imm16()
    elif opcode == command[50][0]:
        dd.RET_NZ()
    elif opcode == command[50][1]:
        dd.RET_NC()
    elif opcode == command[51][0]:
        dd.CALL_NZ_n16()
    elif opcode == command[51][1]:
        dd.CALL_NC_n16()
    elif opcode == command[52][0]:
        dd.RET_Z()

    elif opcode == command[52][1]:
        dd.RET_C()
    elif opcode in command[53]:
        dd.RET()
    elif opcode == command[54][0]:
        dd.CALL_Z_n16()
    elif opcode == command[54][1]:
        dd.CALL_C_n16()
    elif opcode in  command[55]:
        dd.CALL_n16()
    elif opcode in command[56]:
        dd.LDH_a8_A()
    elif opcode in command[57]:
        dd.LDH_A_a8()
    elif opcode in command[58]:
       
        dd.DI()
    elif opcode in command[59]:
        dd.EI()
    elif opcode in command[60]:
        dd.LD_n16_A()
    elif opcode in command[61]:
        dd.CP_A_n8()
    elif opcode == 0xFA:
        dd.LD_A_n16()
    elif opcode == 0xE6:
        dd.AND_d8()
    elif opcode == 0x27:
        dd.daa()
    elif opcode == 0xC6:
        dd.ADD_A_n8()
    elif opcode == 0xD6:
        dd.SUB_A_n8()
    elif opcode == 0x37:
        dd.scf()
    elif opcode == 0xF6:
        dd.OR_A_n8()
    elif opcode == 0xEE:
        dd.XOR_A_n8()
    elif opcode == 0xCE:
        dd.ADC_A_n8()
    elif opcode == 0xE9:
        dd.JUMP_HL()
    elif opcode == 0xC7:
        dd.RST_00()

  
        print("PC"+hex(PC[0]))
    elif opcode == 0xCF:
        dd.RST_08()


    elif opcode == 0xD7:
        dd.RST_10()


    elif opcode == 0xDF:
        dd.RST_18()


    elif opcode == 0xD9:
        dd.RETI()
        
    elif opcode == 0xDE:
        dd.SUBC_A_n8()
    elif opcode == 0xE2:
        dd.LDI_C_A()
    elif opcode == 0xF2:
        dd.LDI_A_C()
    elif opcode==0x76:
        h=[0]
        
        dd.halt()

          
    elif opcode == 0xE7:
        dd.RST_20()


    elif opcode == 0xE8:
        dd.ADD_SP_n8()
    elif opcode == 0xEF:
        dd.RST_28()


    elif opcode== 0xF7:
        dd.RST_30()


    elif opcode == 0xFF:
        dd.RST_38()


    elif opcode == 0xF8:
        dd.LD_HL_SP_e8()
    elif opcode == 0xF9:
        dd.LD_HL_SP()
    elif opcode == 0x10:
        #dd.stop()
        pass
        
    elif opcode == 0xCB:
        dd.CB()
        opcode = dd.pointer()
        if opcode in command[62]:
            dd.rl_r8()
        elif opcode in command[63]:
            dd.rr_r8()
        elif opcode in command[64]:
            dd.SLA_r8()
        elif opcode in command[65]:
            dd.SRA_r8()
        elif opcode in command[66]:
            dd.SWAP_r8()
        elif opcode in command[67]:
            dd.SRL_r8()
        elif opcode in command[68]:
            dd.BIT_0_R8()
        elif opcode in command[69]:
            dd.BIT_1_R8()
        elif opcode in command[70]:
            dd.BIT_2_R8()
        elif opcode in command[71]:
            dd.BIT_3_R8()
        elif opcode in command[72]:
            dd.BIT_4_R8()
        elif opcode in command[73]:
            dd.BIT_5_R8()
        elif opcode in command[74]:
            dd.BIT_6_R8()
            
            
        elif opcode in command[75]:
            dd.BIT_7_R8()
        elif opcode in command[76]:
            dd.RES_0_R8()
        elif opcode in command[77]:
            dd.RES_1_R8()
        elif opcode in command[78]:
            dd.RES_2_R8()
        elif opcode in command[79]:
            dd.RES_3_R8()
        elif opcode in command[80]:
            dd.RES_4_R8()
        elif opcode in command[81]:
            dd.RES_5_R8()
        elif opcode in command[82]:
            dd.RES_6_R8()
        elif opcode in command[83]:
            dd.RES_7_R8()
        elif opcode in command[84]:
            dd.SET_0_R8()
        elif opcode in command[85]:
            dd.SET_1_R8()
           
        elif opcode in command[86]:
            dd.SET_2_R8()
        elif opcode in command[87]:
            dd.SET_3_R8()
        elif opcode in command[88]:
            dd.SET_4_R8()
        elif opcode in command[89]:
            dd.SET_5_R8()
        elif opcode in command[90]:
            dd.SET_6_R8()
        elif opcode in command[91]:
            dd.SET_7_R8()
        
        
        elif opcode == 0x0:
            dd.rlc_B()
        elif opcode == 0x1:
            dd.rlc_C()
        elif opcode == 0x2:
            dd.rlc_D()
        elif opcode == 0x3:
            dd.rlc_E()
        elif opcode == 0x4:
            dd.rlc_H()
        elif opcode == 0x5:
            dd.rlc_L()
        elif opcode == 0x6:
            dd.rlc_HL()
        elif opcode == 0x7:
            dd.rlc_A()
        elif opcode == 0x08:
            dd.rrc_B()
        elif opcode == 0x09:
            dd.rrc_C()
        elif opcode == 0x0A:
            dd.rrc_D()
        elif opcode == 0x0B:
            dd.rrc_E()
        elif opcode == 0x0C:
            dd.rrc_H()
        elif opcode == 0x0D:
            dd.rrc_L()
        elif opcode == 0x0E:
            dd.rrc_HL()
        elif opcode == 0x0F:
            dd.rrc_A()
        else:
            PC[0]-=1
            
    if PC[0] > 0xFFFF:
        PC[0] = PC[0]&0xFF
    if PC[0]<0:
        PC[0] = PC[0]+0x10000
    if SP[0] > 0xFFFF:
        SP[0] = SP[0]&0xFF
    if SP[0]<0:
        SP[0] = SP[0]+0x10000
    if B[0]<0:
        B[0] = B[0]+0x80+0x80
    if H[0]<0:
        H[0] = H[0]+0x80+0x80
    if D[0]<0:
        D[0] = D[0]+0x80+0x80
    if B[0]>0xFF:
        B[0] = B[0]&0xFF
    if H[0]>0Xff:
        H[0] = H[0]&0xFF
    if D[0]>0xff:
        D[0] = D[0]&0xFF
    if paused[0] == 0 and (IER[0]&IO[0xFF0F-0xff00])!=0 and opcode== 0x76:
        execute(PC)
        PC[0]-=1
        oplist[0]=0
    if paused[0] == 1 :

        dd.checking_interrupt()
        oplist[0]=0
        v[0] =0
    
    v[0] = 1

        



        
        
        

    
        


    
        
        
        
        
        
        
        
        
with open("C:\\Users\\oloke\\Downloads\\d.txt","w")as f:
    f.write(str(Rombank))
   
def Timer(cycles):
    timer_counter = 0

        
def is_clock_enabled():
    Enabled = IO[0xFF07&0xFF]&0x2
    if loc[0]== 0xFF07:
        current_time_counter= IO[0xFF07&0xFF]&0x3
    
    #PC +=1 
    #print(hex(opcode))
    #print(hex(opcode))
#print(hex(BC[0]))
#print(Rombank[0])
#print(cycles,9999999999999999999999)   
Button(window,text="Open",command=opens).pack()
#print(len(Rambank))
n=0
display.fill("#CADC9F")
clock = pygame.time.Clock()
tick = 0
while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                current_cycles[0] =0
                #p1 =multiprocessing.Process(target= execute, args= PC)
                execute(PC)
                
                Update_Timer()

                UpdateGraphic()
                
                



                
       


                
                #window.update()
                if tick % 25000 == 0:
                    pygame.display.flip()
                #clock.tick(20)
                tick +=1
                

  












            
    



    

    



    

#print(g)   
#print(Rombank)


#print(Rombank)
#print(mcb_type[rom[0x0147]])
#print(Rombank[0][0x0149])   
#print(sum(Rombank[0]),sum(Rombank[1]))
#print(len(Rombank))
#print(Rambank)


window.mainloop()
#window_2.mainloop()



