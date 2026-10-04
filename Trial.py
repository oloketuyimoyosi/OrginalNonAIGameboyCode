from Timer import*
import typing
import cython
class Opcode:
    def __init__(self,BC,PC,AF,DE,HL,SP,Rombank,Rambank,IO,A,B,C,D,E,F,H,L,OAM,IER,cycles,s,Ramswitch,Romswitch,MCB,RamEnabled,VRAM,R,WRAM,HRAM,oplist,paused,ECHO,IMF,loc,Call,cuurent_cycles,Not_Usable,disable_Vram,disable_OAM,Timer_counter) -> None:
        self.BC:list = BC
        self.PC:list = PC
        self.AF:list =AF
        self.DE:list = DE
        self.HL:list= HL
        self.SP:list = SP
        self.Rombank:list =Rombank
        self.Rambank:list = Rambank
        self.IO:list = IO
        self.A:list =A
        self.B:list = B
        self.C:list = C 
        self.D:list =D
        self.E:list = E
        self.F:list = F 
        self.H:list = H
        self.L:list = L
        self.OAM:list = OAM
        self.IER:list = IER
        self.cycles:list = cycles
        self.s:list = s
        self.Ramswitch:list = Ramswitch
        self.Romswitch:list = Romswitch
        self.MCB=MCB
        self.RamEnabled:list = RamEnabled
        self.VRAM :list= VRAM
        self.R:list = R        
        self.WRAM:list = WRAM
        self.HRAM :list= HRAM
        self.oplist:list = oplist
        self.paused :list= paused
        self.ECHO:list =ECHO 
        self.IMF:list =IMF
        self.loc :list= loc
        self.Call:list = Call
        self.current_cycles:list = cuurent_cycles
        self.Not_Usable:list =Not_Usable
        self.disable_Vram:list= disable_Vram
        self.disable_OAM:list = disable_OAM
        self.Timer_Counter :list= Timer_counter
        
        
        
        

        
    def Write_to_Memory_u16(self,address,r8)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        # remove after test
        #print("PC: "+hex(address[0]))
        
        if address[0] > 0xFFFF:
            address[0] = address[0]-0xffff-1
        #if address[0]>= 0x0000 and address[0]<=0x3FFF:
            #print("YEEEEEEEEEEEEEEEEEEEEEE")
            #print("r8 : " + hex(r8[0]))
            #self.Rombank[self.s[0]][address[0]-0x0000] = r8[0]
            #print("SP: +" +hex(self.SP[0]))
            #print(self.Rombank[0][0x2900:0x2940])
        
        
        if address[0]>=0x0000 and address[0]<=0x1FFF: 
            #print(r8[0])
            if r8[0]& 0xF== 0xA:
                #print(self.RamEnabled[0],"kkkkkk")
                self.RamEnabled[0] = 1
            else:
                #print(self.RamEnabled[0],"yyyyyy")
                self.RamEnabled[0] =0
                
        if address[0]>=0x2000 and address[0]<=0x3FFF:
            #print("d",hex(address[0]),hex(r8[0]),hex(self.s[3]))
            #print(len(self.Rombank))
            self.s[0] = r8[0]&0x1F + self.s[3]
            


            
            
            

                
            
        #delete after test

        elif address[0]>= 0x4000 and address[0]<= 0x5FFF:
            
                #print(hex(self.PC[0]),"lol",self.s[1])
                self.s[1] =0
                self.s[1] = (r8[0]&0x3)
                self.s[3] = (r8[0]&0x3)<<5
                #print(hex(self.PC[0]),"lol",self.s[1])
                self.R[0] = r8[0]&0x3

        elif address[0] >= 0x6000 and address[0]<= 0x7FFF:
            #print("damn",r8[0],hex(self.PC[0]),hex(address[0]))
            if r8[0]&0x1 == 0x01:
                #print("sassa")
                self.Ramswitch[0] = 1
                self.Romswitch[0] = 1
            elif r8[0]&1 == 0x00:
                self.Romswitch[0] = 0
                self.Ramswitch[0] = 0

        
        elif address[0]>= 0x8000 and address[0]<= 0x9FFF:
            if self.disable_Vram[0] ==0:
                self.VRAM[address[0]-0x8000]=r8[0]
        elif address[0]>= 0xA000 and address[0]<= 0xBFFF:
            #print(self.RamEnabled[0],hex(address[0]),self.R[0])
            if self.RamEnabled[0]==1:
                if self.Ramswitch[0] == 1:
                    #print(len(self.Rambank),self.R[0])
                    if self.R[0]>0:
                        if len(self.Rambank)/8192 < 1: #wahala
                            self.Rambank[self.R[0]][address[0]-0xA000] = r8[0]
                        else:
                            self.Rambank[address[0]-0xA000] = r8[0]
                    else:
                        if len(self.Rambank)/8192 < 1: #wahala
                            self.Rambank[0][address[0]-0xA000] = r8[0]
                        else:
                            self.Rambank[address[0]-0xA000] = r8[0]

                    
                else:
                    if len(self.Rambank)/8192 < 1:
                        
                        self.Rambank[0][address[0]-0xA000] = r8[0]
                    else:
                        self.Rambank[address[0]-0xA000] = r8[0]
            
        elif address[0]>= 0xC000 and address[0]<= 0xDFFF:
           
            self.WRAM[address[0]-0xC000] = r8[0]
        elif address[0]>= 0xE000 and address[0]<=0xFDFF:
           
            self.ECHO[address[0]-0xE000] = r8[0]
            #print(self.ECHO[0:200])
            
        elif address[0]>= 0xFE00 and address[0]<=0xFE9F:
            self.OAM[address[0]-0xFE00] =r8[0]
        elif address[0]== 0xFF46:
                reg.DoDMATransfer(address)
        elif address[0] == 0xFF07: 
                current_freq = self.IO[0xFF07-0xFF00]&0x3
                self.IO[0xFF07-0xFF00] = r8[0]
                new = r8[0]&0x3
                if current_freq !=new:
                    tt= Timer(self.cycles,self.loc,self.IO,self.Timer_Counter)
                    tt.set_count_timer()
                    self.IO[0xff05-0xff00] +=1
        elif address[0] == 0xFF04:
                self.IO[address[0]-0xFF00] == 0
        elif address[0]>= 0xFEA0 and address[0]<= 0xFEFF:
            self.Not_Usable[address[0]-0xFEA0] = r8[0] 
        elif address[0]>= 0xFF00 and address[0]<= 0xFF7F:


            self.IO[address[0] &0x7F] = r8[0]
        elif address[0]>= 0xFF80 and address[0]<= 0xFFFE:
                self.HRAM[address[0]-0xFF80] = r8[0]
        elif address[0] == 0xFFFF:
             self.IER[0] = r8[0]
        #self.loc[0] = address
    def Read_memory(self,address,r8)-> None:
            if address[0] > 0xFFFF:
                address[0] = address[0]-0xffff
           
            if  address[0]<= 0x3FFF:
                if self.Romswitch[0] == 1:
                    if self.s[3] < len(self.Rombank) and self.s[3] > 0:
                        r8[0] = self.Rombank[self.s[3]][address[0]]
                    else:
                        r8[0] = self.Rombank[0][address[0]]
                else:
                    r8[0] = self.Rombank[0][address[0]]
            elif (address[0]>= 0x4000 and address[0]<=0x7FFF):
               
                if self.s[0]>0:
                    #print(len(self.Rombank), self.s[0])
                    if len(self.Rombank)>1:
                        r8[0] = self.Rombank[self.s[0]][address[0]-0x4000]
                else:
                    #self.s[0] = 1
                    r8[0] = self.Rombank[1][address[0]-0x4000]
                    
            elif address[0] >= 0x6000 and address[0]<= 0x7FFF:
                if r8[0] == 0x1:
                    self.Ramswitch[0] = 0
                    self.Romswitch[0] = 1
                elif r8[0] == 0x00:
                    self.Romswitch[0] = 1
                    self.Ramswitch[0] = 0
            elif address[0]>= 0X8000 and address[0]<= 0x9FFF:
                if self.disable_Vram[0] ==0:
                    r8[0] = self.VRAM[address[0]-0x8000]
                else:
                    r8[0] = 0xFF
            elif address[0]>= 0XA000 and address[0]<= 0xBFFF:
                if self.RamEnabled[0] == 1:
                    if self.Ramswitch[0] == 1:
                        #print(self.R[0], "Chai")
                        if self.R[0]>0:
                            if len(self.Rambank)/8192 < 1:
                                r8[0]=self.Rambank[self.R[0]][address[0]-0xA000] 
                            else:
                                r8[0] = self.Rambank[address[0]-0xA000] 
                        else:
                            if len(self.Rambank)/8192 < 1:
                                r8[0] = self.Rambank[0][address[0]-0xA000] 
                            else:
                                r8[0] = self.Rambank[address[0]-0xA000] 
                    else:
                         a = address[0]-0xA000
                         if len(self.Rambank)/8192 < 1:
                             r8[0]= self.Rambank[0][a]
                         else:
                             
                            r8[0] = self.Rambank[a]
                else:
                    r8[0] = 0xFF 
            elif address[0]>= 0XC000 and address[0]<= 0xDFFF:
                r8[0] = self.WRAM[address[0]-0xC000] 
            elif address[0]>= 0xE000 and address[0]<=0xFDFF:
                r8[0] = self.ECHO[address[0]-0xE000] 
            elif address[0]>= 0xFE00 and address[0]<=0xFE9F:
                 r8[0] = self.OAM[address[0]-0Xfe00]
            elif address[0]>= 0xFEA0 and address[0]<= 0xFEFF:
                r8[0] = self.Not_Usable[address[0]-0xFEA0] 
            elif address[0]>= 0xFF00 and address[0]<= 0xFF7F:
                r8[0] = self.IO[address[0]-0xFF00] 
            elif address[0]>= 0xFF80 and address[0]<= 0xFFFE:
                 r8[0] = self.HRAM[address[0]-0xFF80] 
            elif address[0] == 0xFFFF:
                r8[0]=self.IER[0]
        
    
    def pointer(self)-> int:
        
        if self.PC[0]>0xFFFF:
            self.PC[0] = self.PC[0]&0xFF
        address =self.PC


        if self.PC[0]>= 0x0000 and self.PC[0]<=0x3FFF:
            if self.Romswitch[0] == 1 and self.s[3] > 0:
                if (self.s[3]) < len(self.Rombank):
                    
                    opcode = self.Rombank[self.s[3]][address[0]]
                else:
                    opcode = self.Rombank[0][address[0]]
            else:
                opcode = self.Rombank[0][address[0]]
        elif (address[0]>= 0x4000 and address[0]<=0x7FFF):

            if self.s[0]>0:
                opcode = self.Rombank[self.s[0]][address[0]-0x4000]
            else:
                #self.s[0] = 1
                opcode= self.Rombank[1][address[0]-0x4000]
                
        elif address[0]>= 0X8000 and address[0]<= 0x9FFF:
            if self.disable_Vram[0] == 0:
                opcode = self.VRAM[address[0]-0x8000]
            else:
                opcode =0xFF
        elif address[0]>= 0XA000 and address[0]<= 0xBFFF:
            if self.RamEnabled[0] == 1:
                if self.Ramswitch[0] == 1:
                    if self.R[0]>0:
                        opcode = self.Rambank[self.R[0]][address[0]-0xA000] 
                    else:
                        opcode = self.Rambank[0][address[0]-0xA000] 
                    
                else:
                    opcode = self.Rambank[0][address[0]-0xA000]
            else:
                opcode = 0xFF 
        elif self.PC[0]>= 0XC000 and self.PC[0]<= 0xDFFF:
            opcode = self.WRAM[address[0]-0xC000] 
        elif self.PC[0]>= 0xE000 and self.PC[0]<=0xFDFF:

            opcode = self.ECHO[address[0]-0xE000] 

        elif address[0]>= 0xFE00 and address[0]<=0xFE9F:
            opcode = self.OAM[address[0]-0xFE00]
        elif address[0]>= 0xFEA0 and address[0]<= 0xFEFF:
            opcode =  self.Not_Usable[address[0]-0xFEA0] 
        elif address[0]>= 0xFF00 and address[0]<= 0xFF7F:
            opcode = self.IO[address[0]-0xFF00] 
        elif address[0]>= 0xFF80 and address[0]<= 0xFFFE:
            opcode= self.HRAM[address[0]-0xFF80] 
        elif address[0] == 0xFFFF:
             opcode = self.IER[0]
        return opcode
    
    def DoDMATransfer(self,data)-> None:
        address = data[0]<<8
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        loc =[0]
        for i in range(0,0xA0):
            reg.Read_memory([address+i],loc)
            reg.Write_to_Memory_u16([0xFE00+i],loc)
            
    
    
    
    def NOP(self)-> None:
        self.cycles[0] +=4
        self.current_cycles[0]=4
        self.PC[0] +=1



    def LD_r16_imm16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.PC[0]+=1
        opcode_2 = reg.pointer()
        self.PC[0]+=1
        opcode_3 = reg.pointer()
        address = opcode_3<<8|opcode_2
       
        
        if opcode & 0xF0 == 0x00:
            self.BC[0] = address
            self.B[0] = address>>8
            self.C[0] = address&0x00FF
        elif opcode & 0xF0 == 0x10:
            self.DE[0] = address
            self.D[0] = address>>8
            self.E[0] = address&0x00FF
            
        elif opcode & 0xF0 == 0x20:
            self.HL[0] = address
            self.H[0] = address>>8
            self.L[0] = address&0x00FF
            
        elif opcode & 0xF0 == 0x30:
            self.SP[0] = address
        self.cycles[0] += 12
        self.current_cycles[0] =12
        self.PC[0] +=1
    
    
    def LD_r16mem_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        
        opcode = reg.pointer()
        
        if opcode & 0xF0 == 0x00:
            reg.Write_to_Memory_u16(self.BC,self.A)
        elif opcode & 0xF0 == 0x10:
            reg.Write_to_Memory_u16(self.DE,self.A)
        elif opcode & 0xF0 == 0x20:
            reg.Write_to_Memory_u16(self.HL,self.A)
            self.HL[0] +=1
        elif opcode & 0xF0 == 0x30:
            reg.Write_to_Memory_u16(self.HL,self.A)
            self.HL[0] -=1 
        self.H[0] = self.HL[0]>>8
        self.L[0] = self.HL[0]&0xFF
        self.cycles[0]+=8 
        self.current_cycles[0]=8
        self.PC[0] += 1
        
    def LD_A_r16mem(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode&0xF0 == 0x00:
            
            reg.Read_memory(self.BC,self.A)
        elif opcode&0xF0 == 0x10:
            reg.Read_memory(self.DE,self.A)
        elif opcode&0xF0 == 0x20:
            reg.Read_memory(self.HL,self.A)
            self.HL[0] +=1
        elif opcode&0xF0 == 0x30:
            reg.Read_memory(self.HL,self.A)
            self.HL[0] -=1 
        self.H[0] = self.HL[0]>>8
        self.L[0] = self.HL[0]&0xFF
        self.cycles[0] +=8
        self.current_cycles[0]=8
        self.PC[0] +=1
        
    def LD_imm16_SP(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
 
        self.PC[0]+=1
        opcode_2 = reg.pointer()
        self.PC[0] +=1
        opcode_3 = reg.pointer()
        imm16 = [opcode_3<<8|opcode_2]
        address_1=[0]
        address_1[0]= self.SP[0]&0xFF
        reg.Write_to_Memory_u16(imm16,address_1)
        address_2=[0]
        address_2[0] = self.SP[0]>>8
        imm16[0]= imm16[0]+1
        reg.Write_to_Memory_u16(imm16,address_2)
        self.cycles[0]+=20
        self.current_cycles[0]=20
        self.PC[0] += 1
        

    def inc_r16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x00:
            self.BC[0] +=1
            self.B[0]= self.BC[0]>>8
            self.C[0]= self.BC[0]&0x00FF    
        elif opcode & 0xF0 == 0x10:
            self.DE[0] +=1
            self.D[0]= self.DE[0]>>8
            self.E[0]= self.DE[0]&0x00FF    
        elif opcode & 0xF0 == 0x20:
            self.HL[0] +=1
            self.H[0]= self.HL[0]>>8
            self.L[0]= self.HL[0]&0x00FF 
        elif opcode & 0xF0 == 0x30:
            self.SP[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
        self.PC[0]+=1


    def dec_r16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x00:
            self.BC[0] -=1
            self.B[0]= self.BC[0]>>8
            self.C[0]= self.BC[0]&0x00FF    
        elif opcode & 0xF0 == 0x10:
            self.DE[0] -=1
            self.D[0]= self.DE[0]>>8
            self.E[0]= self.DE[0]&0x00FF  
        elif opcode & 0xF0 == 0x20:
            self.HL[0] -=1
            self.H[0]= self.HL[0]>>8
            self.L[0]= self.HL[0]&0x00FF 
        elif opcode & 0xF0 == 0x30:
            self.SP[0] -=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
        self.PC[0]+=1
        
        
        
        

    def add_hl_r16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x80 # check the Z flag
        if opcode & 0xF0 == 0x00:
            if (self.HL[0]&0xFFF)+(self.BC[0]&0XFFF) > 0xFFF:#checks for overflow in the 11th bit
                
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if self.HL[0] + self.BC[0] >0xFFFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF
            self.HL[0] +=self.BC[0]

            
        elif opcode & 0xF0 == 0x10:
            if (self.HL[0]&0xFFF)+(self.DE[0]&0XFFF) > 0xFFF :
                
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if self.HL[0] + self.DE[0] >0xFFFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF
            self.HL[0] += self.DE[0]
        elif opcode & 0xF0 == 0x20:
            if (self.HL[0]&0xFFF)+(self.HL[0]&0XFFF) > 0xFFF:
                
                self.F[0] = self.F[0]|0x20#checks the H flag
            else:
                self.F[0] = self.F[0]&0xDF
            if self.HL[0] + self.HL[0] >0xFFFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF
    
            self.HL[0] += self.HL[0]
        elif opcode & 0xF0 == 0x30:
            if (self.HL[0]&0xFFF)+(self.SP[0]&0XFFF) > 0xFFF:
                
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if self.HL[0] + self.SP[0] >0xFFFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF
            self.HL[0] += self.SP[0]
            
            
        self.B[0]= self.BC[0]>>8
        self.C[0]= self.BC[0]&0x00FF     
        self.D[0]= self.DE[0]>>8
        self.E[0]= self.DE[0]&0x00FF
        self.H[0]= self.HL[0]>>8
        self.L[0]= self.HL[0]&0x00FF 
        if self.H[0]>0xFF:
            self.H[0] =self.H[0]&0xFF
            
        

            
            
        self.PC[0]+=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
    def inc_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x00:
            self.F[0] = self.F[0] &0x10
            self.B[0]+=1
            if ((self.B[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.B[0] = self.B[0]&0xFF
            if self.B[0] == 0x00 :
                
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] ="inc_B"
                    

            self.current_cycles[0]=4    
        elif opcode & 0xF0 == 0x10:
            self.F[0] = self.F[0] & 0x10
            self.D[0]+=1
            if ((self.D[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.D[0] = self.D[0]&0xFF
            if self.D[0] == 0 :  
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] = "inc_D"
            self.current_cycles[0]=4    
        elif opcode & 0xF0 == 0x20:
            self.F[0] = self.F[0] & 0x10
            self.H[0]+=1
            if ((self.H[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.H[0] = self.H[0]&0xFF
            if self.H[0] == 0 : 
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] = "inc_H"
            self.current_cycles[0]=4    
        elif opcode&0xF0 == 0x30:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            self.oplist[0]=(self.oplist[0]+1)&0xFF
            reg.Write_to_Memory_u16(self.HL,self.oplist)
            self.F[0] = self.F[0] & 0x10
            if ((self.oplist[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.oplist[0] = self.oplist[0]&0xFF
            if self.oplist[0] == 0 :
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] = "inc_HL"
            self.cycles[0] +=8
            self.current_cycles[0]=12
        self.cycles[0] +=4


        self.PC[0] +=1
        
    #CELA   
    def inc_CELA(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x00:
            self.F[0] = self.F[0] &0x10
            self.C[0]+=1
            if ((self.C[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            
            else:
                self.F[0] = self.F[0]&0xDF
            self.C[0] = self.C[0]&0xFF
            if self.C[0] == 0 :
                
                self.F[0] = self.F[0] | 0x80
            else:
                
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] ="inc_C"
                    

            
        elif opcode & 0xF0 == 0x10:
            self.F[0] = self.F[0] & 0x10
            self.E[0]+=1
            if ((self.E[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.E[0] = self.E[0]&0xFF
            if self.E[0] == 0x00 :  
                
                self.F[0] = self.F[0] | 0x80
            else:
               
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] = "inc_E"
        elif opcode & 0xF0 == 0x20:
            self.F[0] = self.F[0] & 0x10
            self.L[0]+=1
            if ((self.L[0]-1)&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.L[0] = self.L[0]&0xFF
            if self.L[0] == 0 : 
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] = "inc_L"
        elif opcode&0xF0 == 0x30:
            self.A[0]+=1
            self.F[0] = self.F[0] &0x10
            if (self.A[0]-1&0xF)+1 > 0xF:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            self.A[0]=self.A[0]&0xFF
            if self.A[0] == 0 :
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            self.oplist[0] = "inc_A"
        self.cycles[0] +=4
        self.current_cycles[0]=4
        self.PC[0] +=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
    def dec_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0]=self.F[0]|0x40
        self.F[0] = self.F[0]&0x50
        if opcode & 0xF0 == 0x00:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.B[0]-=1
            if ((self.B[0]+1)&0x1F)-1 < 0x10 and (((self.B[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.B[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            
            if self.B[0] == 0 :
                
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.B[0] <0:
                self.B[0] = (self.B[0]+0x80)|0x80
            self.oplist[0] = "dec_B"


        elif opcode & 0xF0 == 0x10:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.D[0]-=1

            if ((self.D[0]+1)&0x1F)-1 < 0x10 and (((self.D[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.D[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            
            if self.D[0] == 0 :  
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.D[0] <0:
                self.D[0] = (self.D[0]+0x80)|0x80
            self.oplist[0] = "dec_D"
            
        elif opcode & 0xF0 == 0x20:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.H[0]-=1
            if ((self.H[0]+1)&0x1F)-1 < 0x10 and (((self.H[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.H[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            
            if self.H[0] == 0 : 
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.H[0] <0:
                self.H[0] = (self.H[0]+0x80)|0x80
            self.oplist[0] = "dec_H"
            
            
        elif opcode&0xF0 == 0x30:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            self.oplist[0]-=1
            if ((self.oplist[0]+1)&0x1F)-1 < 0x10 and (((self.oplist[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.oplist[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            
            if self.oplist[0] == 0 :
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.oplist[0] <0:
                self.oplist[0] = (self.oplist[0]+0x80)|0x80
            reg.Write_to_Memory_u16(self.HL,self.oplist)
            self.cycles[0] +=8
            self.current_cycles[0]=12
            self.oplist[0] = "dec_HL"
        self.cycles[0] +=4
        if (opcode&0xF0) != 0x30:
            self.current_cycles[0]=4
        self.PC[0] +=1


    def dec_CELA(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x00:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.C[0]-=1
            if ((self.C[0]+1)&0x1F)-1 < 0x10 and (((self.C[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.C[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            if self.C[0] == 0 :
                
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.C[0] <0:
                self.C[0] = (self.C[0]+0x80)|0x80
            self.oplist[0] = "dec_C"


        elif opcode & 0xF0 == 0x10:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.E[0]-=1
            if ((self.E[0]+1)&0x1F)-1 < 0x10 and (((self.E[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.E[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            if self.E[0] == 0 :  
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.E[0] <0:
                self.E[0] = (self.E[0]+0x80)|0x80
            self.oplist[0] = "dec_E"
            
        elif opcode & 0xF0 == 0x20:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.L[0]-=1
            if ((self.L[0]+1)&0x1F)-1 < 0x10 and (((self.L[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.L[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            if self.L[0] == 0 : 
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.L[0] <0:
                self.L[0] = (self.L[0]+0x80)|0x80
            self.oplist[0] = "dec_L"
        elif opcode & 0xF0 == 0x30:
            self.F[0] = (self.F[0] & 0x10)|0x40
            self.A[0]-=1
            if ((self.A[0]+1)&0x1F)-1 < 0x10 and (((self.A[0]+1)&0x10)>>4)==1:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (self.A[0]+1)&0x1F == 0:
                    self.F[0] = self.F[0]|0x20
            if self.A[0] == 0 : 
                self.F[0] = self.F[0] | 0x80
            else:
                self.F[0] = self.F[0]&0x7F
            if self.A[0] <0:
                self.A[0] = (self.A[0]+0x80)|0x80
            self.oplist[0] = "dec_A"
        self.cycles [0]+=4
        self.current_cycles[0]=4
        self.PC[0] +=1


    def LD_r8_imm8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.PC[0]+=1
        pointer = reg.pointer()
        imm8 =[pointer]

        
        if opcode & 0xF0 == 0x00:
            self.B[0] = pointer
            self.current_cycles[0]=8
        elif opcode & 0xF0 == 0x10:
            self.D[0] = pointer
            self.current_cycles[0]=8
        elif opcode & 0xF0 == 0x20:
            self.H[0] = pointer
            self.current_cycles[0]=8
            
        elif opcode & 0xF0 == 0x30:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Write_to_Memory_u16(self.HL,imm8)
            self.cycles[0] += 4
            self.current_cycles[0]=12
        self.cycles[0]+=8

            
        self.PC[0] +=1





    def LD_CELA_imm8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.PC[0]+=1
        address = reg.pointer()
        #imm8=[address]
        
        if opcode & 0xF0 == 0x00:
            self.C[0] = address
        elif opcode & 0xF0 == 0x10:
            self.E[0] = address
        elif opcode & 0xF0 == 0x20:
            self.L[0] = address
            
        elif opcode & 0xF0 == 0x30:
           
            self.A[0] = address
        self.PC[0]+=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
        




    def daa(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        sums = [0]
        subs = [0]
        sums_1 = [0]
        subs_1 =[0]
        self.F[0] =self.F[0]

            
        a =[0]    
        #self.F[0] = self.F[0]&0x50    
        if (self.F[0]&0x40)>>6 ==0:
            
            if (self.F[0]&0x20)>>5 ==1:


                self.A[0] +=0x6
                
            if (self.F[0]&0x10)>>4 ==1 :
                a[0] = 1
                self.A[0] = self.A[0]+0x60


            g = self.A[0]
            if self.A[0]&0xF > 0x9 and (self.F[0]&0x20)>>5 ==0:
                    self.A[0] = self.A[0]+0x6

            if ((g&0xF0 > 0x90) or self.A[0]>0Xff or self.A[0]>0x9F) and  (self.F[0]&0x10)>>4 ==0 :

                    self.A[0] = self.A[0]+0x60

 



        elif (self.F[0]&0x40)>>6 ==1:
            if (self.F[0]&0x20)>>5 ==1:


                self.A[0] -=0x6
                
            if (self.F[0]&0x10)>>4 ==1 :
                a[0] =1
                self.A[0] = self.A[0]-0x60
                

                


        self.F[0] = self.F[0]&0x40   
        if a[0] == 1:
            self.F[0]=self.F[0]|0x10
        if self.A[0]>0xFF:
                self.F[0] = self.F[0]|0x10    
        if self.A[0]>0xFF:
            self.A[0] = self.A[0]&0xFF   
        if self.A[0]<0:
            self.A[0] = self.A[0]&0xFF 
            #self.F[0] = self.F[0]|0x10  
   
        if self.A[0] == 0:
            self.F[0] = self.F[0]|0x80
 
        self.F[0] =self.F[0]&0xD0
        
        
                
            
            
        
            
        

            
        self.PC[0] +=1
        self.cycles[0] +=4
        self.current_cycles[0]=4
    

    def rlca(self)-> None:
        sign_bit = self.A[0]>>7
        self.F[0] =0
        self.A[0] = ((self.A[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        elif sign_bit ==0:
            temp = self.F[0]&0x00
            self.F[0] = temp
        self.PC[0] +=1
        self.cycles[0]+=4
        self.current_cycles[0]=4
    def rrca(self)-> None:
        least_bit = self.A[0]&0x1 #get the least
        self.F[0] =0
        self.A[0] = (self.A[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        elif least_bit ==0:
            temp = self.F[0]&0x00
            self.F[0] = temp
        self.PC[0] +=1
        self.cycles[0]+=4
        self.current_cycles[0]=4
    def rla(self)-> None:
        sign_bit = self.A[0]>>7
        least_bit = (self.F[0]>>4)&0x1
        self.F[0]=0
        self.A[0] = ((self.A[0]<<1)|least_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        elif sign_bit ==0:
            temp = self.F[0]&0x00
            self.F[0] = temp
        self.PC[0] +=1
        self.cycles[0]+=4
        self.current_cycles[0]=4
    
    
    
    
    def rra(self)-> None:
        #sign_bit = self.A[0]>>7
        carry_bit = (self.F[0]>>4)&0x1
        least_sig_bit = self.A[0]&0x1
        self.F[0]=0
        self.A[0] = (self.A[0]>>1)|carry_bit<<7
        if least_sig_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        elif least_sig_bit ==0:
            temp = self.F[0]&0x00
            self.F[0] = temp
        self.PC[0] +=1
        self.cycles[0]+=4
        self.current_cycles[0]=4








    def cpl(self)-> None:
        self.A[0] =~self.A[0]
        self.F[0] = self.F[0]&0x90 #ZC
        self.F[0] = self.F[0]|0x60 #NH
        self.PC[0] +=1
        self.A[0] = self.A[0]&0xFF
        self.cycles[0]+=4
        self.current_cycles[0]=4
    
    
    
    
    def scf(self)-> None:
        self.F[0] =self.F[0]&0x80#Z
        self.F[0] =self.F[0]|0x10#C
        self.PC[0] +=1
        self.cycles[0]+=4
        self.current_cycles[0]=4
    
    
    
    
    
    def ccf(self)-> None:
        if self.F[0]&0x10 == 0x10:
            self.F[0] = self.F[0]&0x80 #inverts C 1 to 0
        else:
            self.F[0]= self.F[0]&0x90
            self.F[0] = self.F[0]|0x10
        self.PC[0] +=1
        self.cycles[0]+=4
        self.current_cycles[0]=4
    
    
    def jr_imm8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1
        imm8 = reg.pointer()
        self.PC[0]+=1

        if imm8 >= 0x80:
            imm = +(imm8&0x7F )-0x80
            self.PC[0] = self.PC[0]+imm
        else:
            self.PC[0] = self.PC[0]+imm8
       
        self.cycles[0]+=12
        self.current_cycles[0]=12
    
    
    
    def jr_Z_imm8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        if self.F[0]&0x80 == 0x80:
            self.PC[0]+=1
            imm8 = reg.pointer()
            self.PC[0]+=1
            if imm8 >= 0x80:
                imm = (imm8&0x7F) -0x80
                self.PC[0] = self.PC[0]+imm
            else:
                self.PC[0] = self.PC[0]+imm8

            self.cycles[0]+=12
            self.current_cycles[0]=12
        else:
            self.PC[0]+=2
            self.cycles[0] +=8
            self.current_cycles[0]=8
    
    
    
    def jr_C_imm8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        if self.F[0]&0x10 == 0x10:
            self.PC[0]+=1
            imm8 = reg.pointer()
            self.PC[0]+=1
            if imm8 >= 0x80:
                imm = (imm8&0x7F) -0x80
                self.PC[0] = self.PC[0]+imm
            else:
                self.PC[0] = self.PC[0]+imm8
            self.cycles[0]+=12
            self.current_cycles[0]=12
        else:
            self.PC[0]+=2
            self.cycles[0] +=8
            self.current_cycles[0]=8
            
    def jr_NZ_imm8(self)-> None:

        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        if self.F[0]&0x80 != 0x80:
            self.PC[0]+=1
            imm8 = reg.pointer()
            self.PC[0]+=1
            if imm8 >= 0x80:
                imm = (imm8&0x7F) -0x80
                self.PC[0] = self.PC[0]+imm
            else:
                self.PC[0] = self.PC[0]+imm8
            self.cycles[0]+=12
            self.current_cycles[0]=12
        else:
            self.PC[0]+=2
            self.cycles[0] +=8    
            self.current_cycles[0]=8
    def jr_NC_imm8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        if self.F[0]&0x10 != 0x10:
            self.PC[0] +=1 
            imm8 = reg.pointer()
            self.PC[0]+=1
            if imm8 >= 0x80:
                imm = (imm8&0x7F) -0x80
                self.PC[0] = self.PC[0]+imm
            else:
                self.PC[0] = self.PC[0]+imm8

            self.cycles[0]+=12
            self.current_cycles[0]=12
        else:
            self.PC[0]+=2
            self.cycles[0] +=8  
            self.current_cycles[0]=8  
    
    
    
    def stop(self):
        pass # will implement later
            
    def ld_r8_B(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.B[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.B[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.B[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4
            reg.Write_to_Memory_u16(self.HL,self.B)
        self.PC[0]+=1
        self.cycles[0] +=4

            
    
    
    def ld_r8_C(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.C[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.C[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.C[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4
            reg.Write_to_Memory_u16(self.HL,self.C)
        self.PC[0]+=1
        self.cycles[0] +=4    
  
    def ld_r8_D(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.D[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.D[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.D[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4
            reg.Write_to_Memory_u16(self.HL,self.D)
        self.PC[0]+=1
        self.cycles[0] +=4

    def ld_r8_E(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode =reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.E[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.E[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.E[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4
            reg.Write_to_Memory_u16(self.HL,self.E)
        self.PC[0]+=1
        self.cycles[0] +=4

        
        
        
    def ld_r8_H(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.H[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.H[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.H[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4
            reg.Write_to_Memory_u16(self.HL,self.H)
        self.PC[0]+=1
        self.cycles[0] +=4      



    def ld_r8_L(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.L[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.L[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.L[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4
            reg.Write_to_Memory_u16(self.HL,self.L)
        self.PC[0]+=1
        self.cycles[0] +=4   

        
    def ld_r8_HL(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        
        if opcode & 0xF0 == 0x40:
            reg.Read_memory(self.HL,self.B)
        elif opcode & 0xF0 == 0x50:
            reg.Read_memory(self.HL,self.D)
        elif opcode & 0xF0 == 0x60:
            reg.Read_memory(self.HL,self.H)
        self.PC[0]+=1
        self.cycles[0] +=8
        self.current_cycles[0]=8


    def ld_r8_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.B[0] = self.A[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x50:
            self.D[0] = self.A[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x60:
            self.H[0] =  self.A[0]
            self.current_cycles[0]=4
        elif opcode & 0xF0 == 0x70:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.current_cycles[0]=8
            self.cycles[0]+=4 
            reg.Write_to_Memory_u16(self.HL,self.A)
        self.PC[0]+=1
        self.cycles[0] +=4


        
        
        
        
    def ld_CELA_B(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.B[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.B[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.B[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.B[0]
        self.PC[0]+=1
        self.cycles[0] +=4 
        self.current_cycles[0]=4
 
        
        
    def ld_CELA_C(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.C[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.C[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.C[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.C[0]
        self.PC[0]+=1
        self.cycles [0]+=4  
        self.current_cycles[0]=4



    def ld_CELA_D(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.D[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.D[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.D[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.D[0]
        self.PC[0]+=1
        self.cycles [0]+=4  
        self.current_cycles[0]=4



    def ld_CELA_E(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.E[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.E[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.E[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.E[0]
        self.PC[0]+=1
        self.cycles[0]+=4 
        self.current_cycles[0]=4


    def ld_CELA_H(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.H[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.H[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.H[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.H[0]
        self.PC[0]+=1
        self.cycles [0]+=4   
        self.current_cycles[0]=4

        
    def ld_CELA_L(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.L[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.L[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.L[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.L[0]
        self.PC[0]+=1
        self.cycles[0] +=4 
        self.current_cycles[0]=4

        

    def ld_CELA_HL(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        
        if opcode & 0xF0 == 0x40:
            reg.Read_memory(self.HL,self.C)
        elif opcode & 0xF0 == 0x50:
            reg.Read_memory(self.HL,self.E)
        elif opcode & 0xF0 == 0x60:
            reg.Read_memory(self.HL,self.L)
        elif opcode & 0xF0 == 0x70:
            reg.Read_memory(self.HL,self.A)
        self.PC[0]+=1
        self.cycles[0] +=8  
        self.current_cycles[0]=8

        
    def ld_CELA_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode & 0xF0 == 0x40:
            self.C[0] = self.A[0]
        elif opcode & 0xF0 == 0x50:
            self.E[0] = self.A[0]
        elif opcode & 0xF0 == 0x60:
            self.L[0] =  self.A[0]
        elif opcode & 0xF0 == 0x70:
            self.A[0] = self.A[0]
        self.PC[0]+=1
        self.cycles[0] +=4 
        self.current_cycles[0]=4

        
        
        
    def ADD_A_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0x00

        if opcode & 0x0F == 0x00:
            if ((self.A[0])&0x0F)+((self.B[0])&0xF)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.B[0])&0xFF)>0xFF:
                
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            
            self.A[0] = self.A[0]+self.B[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x01:
            if ((self.A[0])&0x0f)+((self.C[0])&0x0f)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.C[0])&0xFF)>0xFF:
                self.F[0] = self.F[0]|0x10
                
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.C[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x02:
            if ((self.A[0])&0x0f)+((self.D[0])&0x0f)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.D[0])&0xFF)>0xFF:
                self.F[0] = self.F[0]|0x10
                
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.D[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x03:
            if ((self.A[0])&0x0f)+((self.E[0])&0x0f)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.E[0])&0xFF)>0xFF:
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.E[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x04:
            if ((self.A[0])&0x0f)+((self.H[0])&0x0f)>0x7:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.H[0])&0xFF)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.H[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x05:
            if ((self.A[0])&0x0f)+((self.L[0])&0x0f)>0xf:
                self.F[0] = self.F[0]|0x20
                
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.L[0])&0xFF)>0xFF:

                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.L[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x06:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            if ((self.A[0])&0x0f)+((self.oplist[0])&0x0f)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.oplist[0])&0xFF)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.oplist[0]
            self.A[0] = self.A[0]&0xFF

            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode & 0x0F == 0x07:
            if ((self.A[0])&0x0f)+((self.A[0])&0x0f)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+((self.A[0])&0xFF)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.A[0]
            self.A[0] = self.A[0]&0xFF
            self.current_cycles[0]=4
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0]=self.F[0]&0x7F
        self.oplist[0]="add_A"
        self.cycles[0] += 4


        self.PC[0] +=1
        
    def ADC_A_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        d = self.F[0]&0x10
        carry= d>>4
        self.F[0] = 0x00
        if opcode & 0x0F == 0x08:
            if (((self.A[0])&0x0f)+(((self.B[0])&0x0f)+carry))>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
    
            if ((self.A[0])&0xFF)+(((self.B[0])&0xFF)+carry)>0xFF:

                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
                
            self.A[0] = self.A[0]+self.B[0]+carry
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x09:
            if ((self.A[0])&0x0f)+(((self.C[0])&0x0f)+carry)>0xf:
                
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.C[0])&0xFF)+carry)>0xFF:

                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.C[0]+carry
        elif opcode & 0x0F == 0x0A:
            if ((self.A[0])&0x0f)+(((self.D[0])&0x0f)+carry)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.D[0])&0xFF)+carry)>0xFF:

                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]+self.D[0]+carry
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0B:
            if ((self.A[0])&0x0f)+(((self.E[0])&0x0f)+carry)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.E[0])&0xFF)+carry)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
                
            self.A[0] = self.A[0]+self.E[0]+carry
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0C:
            if ((self.A[0])&0x0f)+(((self.H[0])&0x0f)+carry)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.H[0])&0xFF)+carry)>0xFF:
                self.F[0] = self.F[0]|0x10
                
                
            else:
                self.F[0] = self.F[0]&0xEF 
                
            self.A[0] = self.A[0]+self.H[0]+carry
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0D:
            if ((self.A[0])&0x0f)+(((self.L[0])&0x0f)+carry)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.L[0])&0xFF)+carry)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 

            self.A[0] = self.A[0]+self.L[0]+carry
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0E:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            if ((self.A[0])&0x0f)+(((self.oplist[0])&0x0f)+carry)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.oplist[0])&0xFF)+carry)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 

            self.A[0] = self.A[0]+self.oplist[0]+carry
            self.cycles[0]+=4
            self.current_cycles[0]=8
            
        elif opcode & 0x0F == 0x0F:
            if ((self.A[0])&0x0f)+(((self.A[0])&0x0F)+carry)>0xf:
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
            if ((self.A[0])&0xFF)+(((self.A[0])&0xFF)+carry)>0xFF:
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 

            self.A[0] = self.A[0]+self.A[0]+carry
            self.current_cycles[0]=4
        self.A[0] = self.A[0]&0xFF
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0] = self.F[0]&0x7F
        self.oplist[0]="adc_A"
        self.current_cycles[0]=4

        if opcode&0xF != 0x0E:
            self.current_cycles[0]=4
        self.PC[0] +=1



    def SUB_A_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0x40
        if opcode & 0x0F == 0x00:
            if (((self.A[0])&0x0F)-((self.B[0])&0x0F)<0x00)  and (((self.A[0])&0x0F)>0x8 or ((self.B[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.B[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.B[0]):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            
            self.A[0] = self.A[0]-self.B[0]
            
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x01:
            if ((self.A[0])&0x0F)-((self.C[0])&0x0F)<0x00  and (((self.A[0])&0x0F)>0x8 or ((self.C[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.C[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.C[0]):
                self.F[0] = self.F[0]|0x10


            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-self.C[0]
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x02:
            if ((self.A[0])&0x0F)-((self.D[0])&0x0F)<0x00  and (((self.A[0])&0x0F)>0x8 or ((self.D[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.D[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.D[0]):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-self.D[0]
            self.current_cycles[0]=4
            
            
        elif opcode & 0x0F == 0x03:
            if ((self.A[0])&0x0F)-((self.E[0])&0x0F)<0x00  and (((self.A[0])&0x0F)>0x8 or ((self.E[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.E[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.E[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-self.E[0]
            self.current_cycles[0]=4
            
            
        elif opcode & 0x0F == 0x04:
            if ((((self.A[0])&0x0F)-((self.H[0])&0x0F)<0x0))  and (((self.A[0])&0x0F)>0x8 or ((self.H[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.H[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.H[0]):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-self.H[0]
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x05:
            if ((((self.A[0])&0x0F)-((self.L[0])&0x0F)<0x0))  and (((self.A[0])&0x0F)>0x8 or ((self.L[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.L[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.L[0]):
                self.F[0] = self.F[0]|0x10

            self.A[0] = self.A[0]-self.L[0]
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x06:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            if ((((self.A[0])&0x0F)-((self.oplist[0])&0x0F))<0x0) and (((self.A[0])&0x0F)>0x8 or ((self.oplist[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.oplist[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.oplist[0]):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-self.oplist[0]
            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode & 0x0F == 0x07:
            self.F[0] = self.F[0]&0xCF
            self.A[0] = self.A[0]-self.A[0]
            self.current_cycles[0]=4
            
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0]=self.F[0]&0x7F
        if self.A[0]<0:

            self.A[0] = (self.A[0]+0x80)+0x80
        self.oplist[0]="SUB_A"


        self.cycles[0] += 4
        self.PC[0] +=1
        
        
        
        
        
    def SUBC_A_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        d = self.F[0]&0x10
        carry= d>>4
        if opcode & 0x0F == 0x08:
            self.F[0] = 0x40
            if (((self.A[0])&0x0F)-(((self.B[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.B[0])&0x0F)+carry)))<0x0):
 
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.B[0]+carry):
                self.F[0] = self.F[0]|0x10
 
            else:
                self.F[0] = self.F[0]&0xEF #set C to Zero
            
            self.A[0] = self.A[0]-(self.B[0]+carry)
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x09:
            self.F[0] = 0x40
            if (((self.A[0])&0x0F)-(((self.C[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.C[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.C[0]+carry):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-(self.C[0]+carry)
            self.current_cycles[0]=4
            
            
        elif opcode & 0x0F == 0x0A:
            self.F[0] = 0x40
            if (((self.A[0])&0x0F)-(((self.D[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.D[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.D[0]+carry):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-(self.D[0]+carry)
            self.current_cycles[0]=4
            
            
        elif opcode & 0x0F == 0x0B:
            self.F[0] = 0x40
            if (((self.A[0])&0x0F)-(((self.E[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.E[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.E[0]+carry):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-(self.E[0]+carry)
            self.current_cycles[0]=4
            
            
        elif opcode & 0x0F == 0x0C:
            self.F[0] = 0x40
            if (((self.A[0])&0x0F)-(((self.H[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.H[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.H[0]+carry):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-(self.H[0]+carry)
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x0D:
            self.F[0] = 0x40
            if (((self.A[0])&0x0F)-(((self.L[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.L[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.L[0]+carry):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-(self.L[0]+carry)
            self.current_cycles[0]=4
            
            
            
        elif opcode & 0x0F == 0x0E:
            self.F[0] = 0x40
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            if (((self.A[0])&0x0F)-(((self.oplist[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.oplist[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.oplist[0]+carry):
                self.F[0] = self.F[0]|0x10

            else:
                self.F[0] = self.F[0]&0xEF 
            self.A[0] = self.A[0]-(self.oplist[0]+carry)
            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode & 0x0F == 0x0F:
            self.F[0] = self.F[0]|0x40
            if (((self.A[0])&0x0F)-(((self.A[0])&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if (((((self.A[0])&0x0F)-(((self.A[0])&0x0F)+carry)))<0x0):
                    self.F[0] = self.F[0]|0x20


            self.A[0] = self.A[0]-(self.A[0]+carry)
            self.current_cycles[0]=4
        if self.A[0]<0:

            self.A[0] = (self.A[0]+0x80)+0x80
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0]=self.F[0]&0x7F

        self.oplist[0]="SUBC_A"
        self.cycles [0]+= 4


        self.PC[0] +=1
    
    
    
    def AND_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] =0x0
        if opcode&0x0F == 0x00:
            self.A[0] = self.A[0]&self.B[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x01:
            self.A[0] = self.A[0]&self.C[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x02:
            self.A[0] = self.A[0]&self.D[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x03:
            self.A[0] = self.A[0]&self.E[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x04:
            self.A[0] = self.A[0]&self.H[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x05:
            self.A[0] = self.A[0]&self.L[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x06:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            self.A[0] = self.A[0]&self.oplist[0]
            
            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode&0xF == 0x07:
            self.A[0] = self.A[0]&self.A[0]
            self.current_cycles[0]=4
        if self.A[0] ==0:
            self.F[0] = self.F[0]|0xA0 #set flag Z to 1 and flag H to 1
        else:
            self.F[0] = self.F[0]|0x20 #set flag Z TO 0
        self.cycles[0]+=4


        self.PC[0]+=1

    
    
    def XOR_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] =0x0
        if opcode&0x0F == 0x08:
            self.A[0] = self.A[0]^self.B[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x09:
            self.A[0] = self.A[0]^self.C[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x0A:
            self.A[0] = self.A[0]^self.D[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x0B:
            self.A[0] = self.A[0]^self.E[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x0C:
            self.A[0] = self.A[0]^self.H[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x0D:
            self.A[0] = self.A[0]^self.L[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x0E:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)

            self.A[0] = self.A[0]^self.oplist[0]
            
            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode&0xF == 0x0F:
            self.A[0] = self.A[0]^self.A[0]
            self.current_cycles[0]=4
            
        if self.A[0] ==0:
            self.F[0] = self.F[0]|0x80 #set flag Z to 1 and flag H to 1
        else:
            self.F[0] = self.F[0]&0x0F #set flag Z TO 0
        self.cycles[0]+=4

        self.PC[0]+=1




    def OR_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] =0
        if opcode&0x0F == 0x00:
            self.A[0] = self.A[0]|self.B[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x01:
            self.A[0] = self.A[0]|self.C[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x02:
            self.A[0] = self.A[0]|self.D[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x03:
            self.A[0] = self.A[0]|self.E[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x04:
            self.A[0] = self.A[0]|self.H[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x05:
            self.A[0] = self.A[0]|self.L[0]
            self.current_cycles[0]=4
        elif opcode&0xF == 0x06:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            self.A[0] = self.A[0]|self.oplist[0]
            
            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode&0xF == 0x07:
            self.A[0] = self.A[0]|self.A[0]
            self.current_cycles[0]=4
        if self.A[0] ==0:
            self.F[0] = self.F[0]|0x80 #set flag Z to 1 
            
        else:
            self.F[0] = self.F[0]&0x00 #set flag Z TO 0
        self.cycles[0]+=4


        self.PC[0]+=1



            
    def CP_A_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0x40
        if opcode & 0x0F == 0x08:
            if(((self.A[0])&0x0F)-((self.B[0])&0x0F)<0x00)  and (((self.A[0])&0x0F)>0x8 or ((self.B[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.B[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.B[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            
            if self.A[0]-self.B[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
            
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x09:
            if ((self.A[0])&0x0F)-((self.C[0])&0x0F)<0x00  and (((self.A[0])&0x0F)>0x8 or ((self.C[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.C[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.C[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            if self.A[0]-self.C[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
                
                
                
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0A:
            if ((self.A[0])&0x0F)-((self.D[0])&0x0F)<0x00  and (((self.A[0])&0x0F)>0x8 or ((self.D[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.D[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.D[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            if self.A[0]-self.D[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
                
                
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0B:
            if ((self.A[0])&0x0F)-((self.E[0])&0x0F)<0x00  and (((self.A[0])&0x0F)>0x8 or ((self.E[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.E[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.E[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            if self.A[0]-self.E[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
                
                
            self.current_cycles[0]=4
        elif opcode & 0x0F == 0x0C:
            if ((((self.A[0])&0x0F)-((self.H[0])&0x0F)<0x0))  and (((self.A[0])&0x0F)>0x8 or ((self.H[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.H[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.H[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            if self.A[0]-self.H[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
            self.current_cycles[0]=4
            
        elif opcode & 0x0F == 0x0D:
            if ((((self.A[0])&0x0F)-((self.L[0])&0x0F)<0x0))  and (((self.A[0])&0x0F)>0x8 or ((self.L[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.L[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.L[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            if self.A[0]-self.L[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
            self.current_cycles[0]=4    
                
            
        elif opcode & 0x0F == 0x0E:
            
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.HL,self.oplist)
            
            if ((((self.A[0])&0x0F)-((self.oplist[0])&0x0F))<0x0) and (((self.A[0])&0x0F)>0x8 or ((self.oplist[0])&0x0F)>0x8):
                self.F[0] = self.F[0]|0x20
            else:
                self.F[0] = self.F[0]&0xDF
                if ((((self.A[0])&0x0F)-((self.oplist[0])&0x0F))<0x0):
                    self.F[0] = self.F[0]|0x20
            if (self.A[0])<(self.oplist[0]):
                self.F[0] = self.F[0]|0x10
            else:
                self.F[0] = self.F[0]&0xEF 
            if self.A[0]-self.oplist[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
            self.cycles[0]+=4
            self.current_cycles[0]=8
        elif opcode & 0x0F == 0x0F:
            self.F[0] = self.F[0]&0xCF
            if self.A[0]-self.A[0]==0:
                self.F[0]=self.F[0]|0x80#
            else:
                self.F[0] = self.F[0]&0x7F
            self.current_cycles[0]=4


        self.oplist[0]="CP_A"
        self.cycles[0] += 4

        self.PC[0] +=1
        
        
    def PUSH_r16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode&0xF0 == 0xC0:
            high_value = [((self.BC[0]&0xFF00)>>8)]
            least_value = [(self.BC[0]&0x00FF)]
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,high_value)
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,least_value)
            
        elif opcode&0xF0 == 0xD0:
            high_value = [((self.DE[0]&0xFF00)>>8)]
            least_value = [(self.DE[0]&0x00FF)]
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,high_value)
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,least_value)
            
        elif opcode&0xF0 == 0xE0:
            high_value = [((self.HL[0]&0xFF00)>>8)]
            least_value = [(self.HL[0]&0x00FF)]
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,high_value)
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,least_value)
            #self.SP[0] = self.SP[0]-1
        elif opcode&0xF0 == 0xF0:
            high_value = [((self.AF[0]&0xFF00)>>8)]
            least_value = [(self.AF[0]&0x00FF)]
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,high_value)
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,least_value)
            #self.SP[0] = self.SP[0]-1
        self.cycles[0] +=16
        self.current_cycles[0]=16
        self.PC[0] +=1
    def POP_r16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        if opcode&0xF0 == 0xC0:
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            
            value_1 = self.Call[0]
            
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            value_2 = self.Call[0]<<8
            self.BC[0]= value_1|value_2
            self.B[0] =value_2>>8
            self.C[0] = value_1
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
        elif opcode&0xF0 == 0xD0:
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            
            value_1 = self.Call[0]
            
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            value_2 = self.Call[0]<<8
            self.DE[0]= value_1|value_2
            self.D[0] = value_2>>8
            self.E[0] = value_1
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
        elif opcode&0xF0 == 0xE0:
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            
            value_1 = self.Call[0]
            
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            value_2 = self.Call[0]<<8
            self.HL[0]= value_1|value_2
            self.H[0] = value_2>>8
            self.L[0] = value_1
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
        elif opcode&0xF0 == 0xF0:
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            
            value_1 = self.Call[0]
            
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            reg.Read_memory(self.SP,self.Call)
            self.SP[0] =self.SP[0]+1
            
            value_2 = self.Call[0]<<8
            self.AF[0]= value_1|value_2
            self.A[0] = value_2>>8
            self.F[0] = value_1
            self.F[0]= self.F[0]&0xF0
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
        self.cycles[0] +=12
        self.current_cycles[0]=12
        self.PC[0] +=1
    
    def CALL_n16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        opcode = reg.pointer()

        self.PC[0]+=1

        
        opcode_2 = reg.pointer()
        value_2 = opcode_2

        value_1 =opcode
        self.PC[0]+=1
       
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        
        
        
        self.cycles[0] +=24
        self.current_cycles[0]=24
        self.PC[0] = value_2<<8|value_1
        
        
    def CALL_Z_n16(self)-> None:
        if self.F[0]&0x80 == 0x80:#checks whether NZ is 1
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1

            opcode = reg.pointer()
            self.PC[0]+=1


            opcode_2 = reg.pointer()
            value_2 = opcode_2
            value_1 =opcode
            self.PC[0]+=1
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
            
                
                
            
            self.PC[0] = value_2<<8|value_1
            self.cycles[0] +=24
            self.current_cycles[0]=24
        else:
            self.cycles[0]+=12
            self.current_cycles[0]=12
            self.PC[0]+=3
    def CALL_C_n16(self)-> None:
        if self.F[0]&0x10 == 0x10:#checks whether NZ is 1
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1

            opcode = reg.pointer()
            self.PC[0]+=1


            opcode_2 = reg.pointer()
            value_2 = opcode_2
            value_1 =opcode
            self.PC[0]+=1
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
            
            
            
            
            self.PC[0] = value_2<<8|value_1
            self.cycles[0] +=24
            self.current_cycles[0]=24
        else:
            self.cycles[0]+=12
            self.current_cycles[0]=12
            self.PC[0]+=3
    
    
    
    
    def CALL_NZ_n16(self)-> None:
        if self.F[0]&0x80  != 0x80:#checks whether NZ is 1
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1

            opcode = reg.pointer()
            self.PC[0]+=1

            opcode_2 = reg.pointer()
            value_2 = opcode_2
            value_1 =opcode
            self.PC[0]+=1
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
            
            
            
            
            self.PC[0] = value_2<<8|value_1
            self.cycles[0] +=24
            self.current_cycles[0]=24
        else:
            self.current_cycles[0]=12
            self.cycles[0]+=12
            self.PC[0]+=3

    def CALL_NC_n16(self)-> None:
        if self.F[0]&0x10!=0x10:#checks whether NZ is 1
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1

            opcode = reg.pointer()
            self.PC[0]+=1


            opcode_2 = reg.pointer()
            value_2 = opcode_2
            value_1 =opcode
            self.PC[0]+=1
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
            self.SP[0] = self.SP[0]-1
            reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
            
            
            self.PC[0] = value_2<<8|value_1
            self.cycles[0] +=24
            self.current_cycles[0]=24
        else:
            self.current_cycles[0]=12
            self.cycles[0]+=12
            self.PC[0]+=3
    
            
    def JUMP(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1
        opcode = reg.pointer()
        self.PC[0]+=1
        opcode_2 = reg.pointer()
        imm16 =opcode_2<<8|opcode
        self.PC[0]+=1
        self.PC[0] = imm16

        self.cycles[0]+=16
        self.current_cycles[0]=16





    def JUMP_Z_imm16(self)-> None:
        if self.F[0]&0x80 == 0x80:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1
            opcode = reg.pointer()
            self.PC[0]+=1
            opcode_2 = reg.pointer()
            imm16 =opcode_2<<8|opcode
            self.PC[0]+=1
            self.PC[0] = imm16
            
            self.cycles[0]+=16
            self.current_cycles[0]=16
        else:
            self.PC[0] +=3
            self.current_cycles[0]=12
            self.cycles[0] +=12
    
    
    
    def JUMP_C_imm16(self)-> None:
        if self.F[0]&0x10 == 0x10:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1
            opcode = reg.pointer()
            self.PC[0]+=1
            opcode_2 = reg.pointer()
            self.PC[0]+=1
            imm16 =opcode_2<<8|opcode
            
            self.PC[0] = imm16
            self.cycles[0]+=16
            self.current_cycles[0]=16

        else:
            self.PC[0] +=3
            self.cycles[0] +=12
            self.current_cycles[0]=12
            
    def JUMP_NZ_imm16(self)-> None:
        if self.F[0]&0x80 != 0x80:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1
            opcode = reg.pointer()
            self.PC[0]+=1
            opcode_2 = reg.pointer()
            self.PC[0]+=1
            imm16 =opcode_2<<8|opcode
            
            self.PC[0] = imm16
            #self.PC[0]+=1
            self.cycles[0]+=16
            self.current_cycles[0]=16
        else:
            self.PC[0] +=3
            self.cycles[0] +=12  
            self.current_cycles[0]=12
    def JUMP_NC_imm16(self)-> None:
        if self.F[0]&0x10 != 0x10:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            self.PC[0]+=1
            opcode = reg.pointer()
            self.PC[0]+=1
            opcode_2 = reg.pointer()
            imm16 =opcode_2<<8|opcode
            #self.PC[0]+=1
            self.PC[0] = imm16
            self.cycles[0]+=16
            self.current_cycles[0]=16
        else:
            self.PC[0] +=3
            self.cycles[0] +=12   
            self.current_cycles[0]=12
        
    def RET (self)-> None:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            t = [0]
            
            reg.Read_memory(self.SP,t)
            value_1 = t[0]

            self.SP[0] =self.SP[0]+1
            reg.Read_memory(self.SP,self.Call)
            value_2 = self.Call[0]<<8
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            self.SP[0] =self.SP[0]+1



            self.PC[0]= value_2|value_1

            #self.PC[0]+=1
            self.cycles[0]+=16
            self.current_cycles[0]=16
    def RET_Z(self)-> None:
        if self.F[0]&0x80 == 0x80:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.SP,self.Call)
            value_1 = self.Call[0]
            self.SP[0] =self.SP[0]+1
            reg.Read_memory(self.SP,self.Call)
            value_2 = self.Call[0]<<8
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            self.SP[0] =self.SP[0]+1


            self.PC[0]= value_2|value_1

            #self.PC[0]+=1
            self.cycles[0]+=16
            self.current_cycles[0]=16
        else:
            self.PC[0]+=1
            self.cycles[0] +=8
            self.current_cycles[0]=8
    
    
    
    def RET_C(self)-> None:
        if self.F[0]&0x10 == 0x10:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.SP,self.Call)
            value_1 = self.Call[0]
            self.SP[0] =self.SP[0]+1
            reg.Read_memory(self.SP,self.Call)
            value_2 = self.Call[0]<<8
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            self.SP[0] =self.SP[0]+1


            self.PC[0]= value_2|value_1
 
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
            self.cycles[0]+=16
            self.current_cycles[0]=16
        else:
            self.PC[0]+=1
            self.cycles[0] +=8
            self.current_cycles[0]=8
    # intresting fixing tommorrow or anytime from tommorrow        
    def RET_NZ(self)-> None:
        if self.F[0]&0x80 != 0x80:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.SP,self.Call)
            value_1 = self.Call[0]
            self.SP[0] =self.SP[0]+1
            reg.Read_memory(self.SP,self.Call)
            value_2 = self.Call[0]<<8
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            self.SP[0] =self.SP[0]+1


            self.PC[0]= value_2|value_1

            #self.PC[0]+=1
            self.cycles[0]+=20
            self.current_cycles[0]=20
        else:
            self.PC[0]+=1
            self.cycles[0] +=8
            self.current_cycles[0]=8
    def RET_NC(self)-> None:
        if self.F[0]&0x10 != 0x10:
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.SP,self.Call)
            value_1 = self.Call[0]
            self.SP[0] =self.SP[0]+1
            reg.Read_memory(self.SP,self.Call)
            value_2 = self.Call[0]<<8
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            self.SP[0] =self.SP[0]+1


            self.PC[0]= value_2|value_1

            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
            self.cycles[0]+=20
            self.current_cycles[0]=20
        else:
            self.PC[0]+=1
            self.cycles[0] +=8   
            self.current_cycles[0]=8
    def LDH_a8_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1 
        imm8 = reg.pointer()
        address = [0xFF00+imm8]
        
        reg.Write_to_Memory_u16(address,self.A)
        self.PC[0]+=1
        self.cycles[0]+=12
        self.current_cycles[0]=12
    
    def LDH_A_a8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1 
        imm8 = reg.pointer()
       
        address = [0xFF00+imm8]
        
        reg.Read_memory(address,self.A)
        self.PC[0]+=1
        self.cycles[0]+=12
        self.current_cycles[0]=12
        
    def request_interrupt(self,id)-> None:

        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)        

        if id == 0:
             self.IO[0xFF0F-0Xff00]= self.IO[0xFF0F-0Xff00]|0x01
        elif id == 1:
             self.IO[0xFF0F-0Xff00]= self.IO[0xFF0F-0Xff00]|0x02
        elif id == 2:
             self.IO[0xFF0F-0Xff00]=  self.IO[0xFF0F-0Xff00]|0x04
        elif id == 3:
             self.IO[0xFF0F-0Xff00]= self.IO[0xFF0F-0Xff00]|0x08
        elif id == 4:
             self.IO[0xFF0F-0Xff00]= self.IO[0xFF0F-0Xff00]|0x10

        
    
    def servicing(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)        
        self.paused[0] = 0
        address=[0xFF0F]
        reg.Read_memory(address,self.IMF)
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        if  (self.IMF[0]&self.IER[0])&0x1 == 1:
            self.IMF[0] = self.IMF[0]&0xFE
            self.PC[0] = 0x40
        elif ((self.IMF[0]&self.IER[0])&0x2)>>1 == 1:
            self.IMF[0] = self.IMF[0]&0xFD
            self.PC[0] = 0x48
        elif ((self.IMF[0]&self.IER[0])&0x4)>>2 == 1:
            self.IMF[0] = self.IMF[0]&0xFB
            self.PC[0] =0x50
        elif ((self.IMF[0]&self.IER[0])&0x8)>>3 == 1:
            self.IMF[0] = self.IMF[0]&0xF7
            self.PC[0] =0x58 #serial port
        elif ((self.IMF[0]&self.IER[0])&0x10)>>4 == 1:
            self.IMF[0] = self.IMF[0]&0xEF
            self.PC[0] = 0x60
        reg.Write_to_Memory_u16(address,self.IMF)
        self.cycles[0]+=20
        self.current_cycles[0]=20
        
        

    
    
    
    
    

    def checking_interrupt(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)        
        address=[0xFF0F]
        if self.paused[0] == 1:
            reg.Read_memory(address,self.IMF)
            if self.oplist[0] =="halted" :
                self.PC[0]+=1
            if (self.IMF[0]&self.IER[0])&0x1 == 0x1:
                
                    reg.servicing()
            elif ((self.IMF[0]&self.IER[0])&0x2)>>1 == 1:

                    reg.servicing()

            elif ((self.IMF[0]&self.IER[0])&0x4)>>2 == 1:

                    reg.servicing()
            elif ((self.IMF[0]&self.IER[0])&0x8)>>3 == 1:

                    reg.servicing()
            elif ((self.IMF[0]&self.IER[0])&0x10)>>4 == 1:

                    reg.servicing()


            

                
            
        
    def DI(self)-> None:
        self.paused[0] = 0
        self.cycles[0]+=4
        self.PC[0]+=1
        self.current_cycles[0]=4
    def EI(self)-> None:
        self.paused[0] = 1
        self.cycles[0]+=4
        self.current_cycles[0]=4
        self.PC[0]+=1
        
    

    def LDI_C_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)        
        C = [self.C[0]+0xFF00]
        reg.Write_to_Memory_u16(C,self.A)
        self.cycles[0]+=8
        self.current_cycles[0]=8
        self.PC[0]+=1
    def LDI_A_C(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)        
        C = [self.C[0]+0xFF00]
        reg.Read_memory(C,self.A)
        self.cycles[0]+=8
        self.current_cycles[0]=8
        self.PC[0]+=1
        
    def LD_n16_A(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.PC[0]+=1
        opcode_2 = reg.pointer()
        self.PC[0]+=1
        opcode_3 = reg.pointer()
        address = [opcode_3<<8|opcode_2]
        reg.Write_to_Memory_u16(address,self.A)
        self.PC[0]+=1
        self.cycles[0] +=16
        self.current_cycles[0]=16
        
        
    def LD_A_n16(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.PC[0]+=1
        opcode_2 = reg.pointer()
        self.PC[0]+=1
        opcode_3 = reg.pointer()
        address = [opcode_3<<8|opcode_2]

        reg.Read_memory(address,self.A)
        self.PC[0]+=1
        self.cycles[0] +=16
        self.current_cycles[0]=16
        
    def ADC_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        
        opcode = reg.pointer()
        self.PC[0] +=1
        imm8 = reg.pointer()
        d = self.F[0]&0x10
        carry= d>>4
        self.F[0] = 0x00

        if ((self.A[0])&0x0F)+(((imm8)&0x0F)+carry)>0xF:
                self.F[0] = self.F[0]|0x20
        else:
            self.F[0] = self.F[0]&0xDF
    
        if ((self.A[0])&0xFF)+(((imm8)&0xFF)+carry)>0xFF:

            self.F[0] = self.F[0]|0x10
        else:
            self.F[0] = self.F[0]&0xEF 
                
        self.A[0] = self.A[0]+imm8+carry
        self.A[0] =self.A[0]&0xFF
        
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0] = self.F[0]&0x7F
        self.A[0] = self.A[0]&0xFF
        self.oplist[0]="adc_A"
        self.PC[0]+=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
    def SUB_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        
        self.F[0] = 0x40
        
        opcode = reg.pointer()
        self.PC[0] +=1
        imm8 = reg.pointer()

        if (((((self.A[0])&0x0F)-((imm8)&0x0F))<0x0) and (((self.A[0])&0x0F)>0x8 or ((imm8)&0x0F)>0x8)):
                self.F[0] = self.F[0]|0x20
            
        else:

            self.F[0] = self.F[0]&0xDF
            if ((((self.A[0])&0x0F)-((imm8)&0x0F))<0x0) :
                self.F[0] = self.F[0]|0x20
        
        if (self.A[0])<imm8:
            self.F[0] = self.F[0]|0x10

        else:
            self.F[0] = self.F[0]&0xEF 

                
            
            
        self.A[0] = self.A[0]-imm8
        if self.A[0]<0:
            self.A[0] = (self.A[0]+0x80)+0x80
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0]=self.F[0]&0x7F


        self.oplist[0]="SUB_A"
        self.cycles[0] += 8
        self.current_cycles[0]=8
        self.PC[0] +=1
    
    
    def SUBC_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        d = self.F[0]&0x10
        carry= d>>4
        self.PC[0] +=1
        imm8 = reg.pointer()
        

        self.F[0] = 0x40
        if (((self.A[0])&0x0F)-(((imm8)&0x0F)+carry)<0x00)  :
                self.F[0] = self.F[0]|0x20
        else:
            self.F[0] = self.F[0]&0xDF
            if (((((self.A[0])&0x0F)-(((imm8)&0x0F)+carry)))<0x0):
                self.F[0] = self.F[0]|0x20
        if (self.A[0])<(imm8+carry):
            self.F[0] = self.F[0]|0x10

        else:
            self.F[0] = self.F[0]&0xEF #set C to Zero

            
        self.A[0] = self.A[0]-(imm8+carry)
        if self.A[0]==0:
            
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0]=self.F[0]&0x7F
        if self.A[0]<0:
            self.A[0] = (self.A[0]+0x80)+0X80
        self.oplist[0]="SUBC_A"
        self.cycles [0]+= 8
        self.current_cycles[0]=8
        self.PC[0] +=1
    def CP_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0x40
        self.PC[0] +=1
        imm8 = reg.pointer()
        if (((((self.A[0])&0x0F)-((imm8)&0x0F))<0x0) and (((self.A[0])&0x0F)>0x8 or ((imm8)&0x0F)>0x8)):
                self.F[0] = self.F[0]|0x20
            
        else:

            self.F[0] = self.F[0]&0xDF
            if ((((self.A[0])&0x0F)-((imm8)&0x0F))<0x0) :
                self.F[0] = self.F[0]|0x20
        if (self.A[0])<imm8:
            self.F[0] = self.F[0]|0x10

        else:
            self.F[0] = self.F[0]&0xEF 
            
        if self.A[0]-imm8==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0] = self.F[0]&0x7F

        self.oplist[0]="CP_A"
        self.cycles[0] += 8
        self.current_cycles[0]=8
        self.PC[0] +=1
    def AND_d8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.F[0] = 0x0
        self.PC[0] +=1
        imm8 = reg.pointer()
        self.A[0] = self.A[0]&imm8
        
        if self.A[0] ==0:
            self.F[0] = self.F[0]|0xA0 #set flag Z to 1 and flag H to 1
        else:
            self.F[0] = self.F[0]|0x20 #set flag Z TO 0
        self.cycles[0]+=8
        self.current_cycles[0]=8
        self.PC[0]+=1
            
    def RETI(self)-> None:
            self.paused[0] = 1
            reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
            reg.Read_memory(self.SP,self.Call)
            value_1 = self.Call[0]
            self.SP[0] =self.SP[0]+1
            reg.Read_memory(self.SP,self.Call)
            value_2 = self.Call[0]<<8
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            self.SP[0] =self.SP[0]+1


            self.PC[0]= value_2|value_1
 
            #reg.Write_to_Memory_u16(self.SP,[0x0])
            #self.SP[0] =self.SP[0]+1
            
            self.cycles[0]+=16
            self.current_cycles[0]=16
        
        
    def RST_10(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])

        self.PC[0] = 0x0010
        self.cycles[0]+=16
        self.current_cycles[0]=16
    def RST_18(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        self.PC[0] = 0x18
        self.cycles[0]+=16
        self.current_cycles[0]=16
        
    def RST_00(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        self.PC[0] = 0x0000
        #print("yessssssssssssss")
        self.cycles[0]+=16
        self.current_cycles[0]=16
    def RST_08(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        self.PC[0] = 0x08
        self.cycles[0]+=16
        self.current_cycles[0]=16
        
        
        
    def RST_20(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        #self.SP[0] = self.SP[0]-1
        self.PC[0] = 0x20
        self.cycles[0]+=16
        self.current_cycles[0]=16
        
    def RST_28(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        self.PC[0] = 0x28
        self.cycles[0]+=16
        self.current_cycles[0]=16
        
    def RST_30(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        self.PC[0] = 0x30
        self.cycles[0]+=16
        self.current_cycles[0]=16
        
    def RST_38(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1

        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[(self.PC[0]&0xFF00)>>8])
        self.SP[0] = self.SP[0]-1
        reg.Write_to_Memory_u16(self.SP,[self.PC[0]&0xFF])
        self.PC[0] = 0x38
        self.cycles[0]+=16
        self.current_cycles[0]=16
    def ADD_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0x00
        self.PC[0] +=1
        imm8 = reg.pointer()

        if ((self.A[0])&0x0f)+((imm8)&0x0f)>0xf:
            self.F[0] = self.F[0]|0x20
        else:
            self.F[0] = self.F[0]&0xDF
        if ((self.A[0])&0xFF)+((imm8)&0xFF)>0xFF:
                
            self.F[0] = self.F[0]|0x10
        else:
            self.F[0] = self.F[0]&0xEF 
            
        self.A[0] = self.A[0]+imm8
        self.A[0] = self.A[0]&0xFF
        
        if self.A[0]==0:
            self.F[0]=self.F[0]|0x80#
        else:
            self.F[0]=self.F[0]&0x7F
        
        self.oplist[0]="add_A"
        self.current_cycles[0]=8
        self.PC[0]+=1
        self.cycles[0]+=8
    def OR_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        
        self.PC[0] +=1
        imm8 = reg.pointer()
        self.F[0] = 0
        self.A[0] = self.A[0]|imm8
        if self.A[0] ==0:
            self.F[0] = self.F[0]&0x80 #set flag Z to 1 and flag H to 1

        else:
            self.F[0] = self.F[0]&0x00
        self.current_cycles[0]=8
        self.PC[0]+=1
        self.cycles[0]+=8
    
    
    def XOR_A_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)

        self.F[0] =0x0
        self.PC[0] +=1
        imm8 = reg.pointer()
        self.A[0] = self.A[0]^imm8
        self.current_cycles[0]=8
        if self.A[0] ==0:
            self.F[0] = self.F[0]|0x80 #set flag Z to 1 and flag H to 1
        else:
            self.F[0] = self.F[0]&0x00 #set flag Z TO 0
            
        self.cycles[0]+=8

        self.PC[0]+=1
        
    def JUMP_HL(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)

        self.PC[0] = self.HL[0]
        
      
        
        self.cycles[0]+=4
        self.current_cycles[0]=4
            
        
    
        
        
    
    
    
    
    
    
    
    def halt(self)-> None: #do later
        n=0
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)


        if (self.IO[0xFF0F-0xff00]&self.IER[0])>0:

                    self.PC[0]+=1
                    self.oplist[0] = 1
                    self.cycles[0] +=4
                    self.current_cycles[0]=4
                    self.oplist[0] = 0

        else:
                    self.cycles[0] +=4
                    self.current_cycles[0]=4
                    self.oplist[0] = "halted"

            






            
            
            
            
            
            
            
            
            
            
            
    #CB OPCODE
    
    def rlc_B(self)-> None:
        sign_bit = self.B[0]>>7
        self.F[0]= 0
        self.B[0] = ((self.B[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.B[0]==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rlc_C(self)-> None:
        sign_bit = self.C[0]>>7
        self.F[0] =0
        self.C[0] = ((self.C[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.C[0] == 0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        
        self.PC[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8

    def rlc_D(self)-> None:
        sign_bit = self.D[0]>>7
        self.F[0] =0
        self.D[0] = ((self.D[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.D[0]==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        
        self.PC[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8


    def rlc_E(self)-> None:
        sign_bit = self.E[0]>>7
        self.F[0] =0
        self.E[0] = ((self.E[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.E[0]==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        
        self.PC[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
        

    def rlc_H(self)-> None:
        sign_bit = self.H[0]>>7
        self.F[0] =0
        self.H[0] = ((self.H[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.H[0]==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        
        self.PC[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rlc_L(self)-> None:
        sign_bit = self.L[0]>>7
        self.F[0]=0
        self.L[0] = ((self.L[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.L[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        
        self.PC[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rlc_HL(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        value = [0]
        reg.Read_memory(self.HL,value)
        sign_bit = value[0]>>7
        self.F[0]= 0
        value[0] = ((value[0]<<1)|sign_bit)&0xFF
        reg.Write_to_Memory_u16(self.HL,value)
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if value[0]==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp

        self.PC[0] +=1
        self.cycles[0]+=16
        self.current_cycles[0]=16
    def rlc_A(self)-> None:
        sign_bit = self.A[0]>>7
        self.F[0] =0 
        self.A[0] = ((self.A[0]<<1)|sign_bit)&0xFF
        if sign_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.A[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp

        self.PC[0] +=1
        self.cycles[0]+=8
        self.current_cycles[0]=8 
        
        
    def rrc_B(self)-> None:
        least_bit = self.B[0]&0x1 #get the least
        self.F[0] =0 
        self.B[0] = (self.B[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.B[0] == 0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
    def rrc_C(self)-> None:
        least_bit = self.C[0]&0x1 #get the least
        self.F[0] =0 
        self.C[0] = (self.C[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.C[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rrc_D(self)-> None:
        least_bit = self.D[0]&0x1 #get the least
        self.F[0] =0 
        self.D[0] = (self.D[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.D[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
        
    def rrc_E(self)-> None:
        least_bit = self.E[0]&0x1 #get the least
        self.F[0] =0 
        self.E[0] = (self.E[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.E[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rrc_H(self)-> None:
        self.F[0] =0 
        least_bit = self.H[0]&0x1 #get the least
        
        self.H[0] = (self.H[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.H[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rrc_L(self)-> None:
        self.F[0] =0 
        least_bit = self.L[0]&0x1 #get the least
        
        self.L[0] = (self.L[0]>>1)|least_bit<<7
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if self.L[0]==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1
        
        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rrc_HL(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.F[0] =0 
        value =[0]
        reg.Read_memory(self.HL,value)
        least_bit = value[0]&0x1 #get the least
        value[0] = (value[0]>>1)|least_bit<<7
        reg.Write_to_Memory_u16(self.HL,value)
        
        
        if least_bit == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if value[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp

        self.PC[0] +=1
        self.cycles[0]+=16
        self.current_cycles[0]=16
        
    def rrc_A(self)-> None:
        least_bit = self.A[0]&0x1 #get the least
        self.A[0] = (self.A[0]>>1)|least_bit<<7
        self.F[0] = 0
        if least_bit == 1:
            
            temp= self.F[0]|0x10
            self.F[0] = temp
        elif self.A[0] ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0] +=1

        self.cycles[0]+=8
        self.current_cycles[0]=8
        
    def rl_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        
        bit=(self.F[0]&0x10)>>4
        self.F[0] = 0 
        if opcode&0x0F== 0x00:
            test = (self.B[0]&0x80)>>7
            
            self.B[0] = ((self.B[0]<<1)|bit)&0xFF
            prev = self.B[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x01:
            test = (self.C[0]&0x80)>>7
            
            self.C[0] = ((self.C[0]<<1)|bit)&0xFF
            prev = self.C[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x02:
            test = (self.D[0]&0x80)>>7
            
            self.D[0] = ((self.D[0]<<1)|bit)&0xFF
            prev = self.D[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x03:
            test = (self.E[0]&0x80)>>7
            
            self.E[0] = ((self.E[0]<<1)|bit)&0xFF
            prev = self.E[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x04:
            test = (self.H[0]&0x80)>>7
            
            self.H[0] = ((self.H[0]<<1)|bit)&0xFF
            prev = self.H[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x05:
            test = (self.L[0]&0x80)>>7
            
            self.L[0] = ((self.L[0]<<1)|bit)&0xFF
            prev = self.L[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)
            test = (value[0]&0x80)>>7
            
            value[0] = ((value[0]<<1)|bit)&0xFF
            reg.Write_to_Memory_u16(self.HL,value)
            prev = value[0]
            self.current_cycles[0]=16
            self.cycles[0]+=8
        elif opcode&0x0F== 0x07:
            test = (self.A[0]&0x80)>>7
            
            self.A[0] = ((self.A[0]<<1)|bit)&0xFF
            prev = self.A[0]
            self.current_cycles[0]=8
        if test == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if prev ==0:
            #temp = self.F[0]&0x00
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0]+=1
        self.cycles[0]+=8
        
        
    def rr_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        bit=(self.F[0]&0x10)>>4
        self.F[0]=0
        if opcode&0x0F== 0x08:
            test = (self.B[0]&0x01)

            self.B[0] = ((self.B[0]>>1)|bit<<7)
            prev = self.B[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x09:
            test = (self.C[0]&0x01)
            
            self.C[0] = ((self.C[0]>>1)|bit<<7)&0xFF
            prev = self.C[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0A:
            test = (self.D[0]&0x01)

            
            self.D[0] = ((self.D[0]>>1)|bit<<7)&0xFF
            prev = self.D[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0B:
            test = (self.E[0]&0x01)
            
            self.E[0] = ((self.E[0]>>1)|bit<<7)&0xFF
            prev = self.E[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0C:
            test = (self.H[0]&0x01)
            
            self.H[0] = ((self.H[0]>>1)|bit<<7)&0xFF
            prev = self.H[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0D:
            test = (self.L[0]&0x01)
            
            self.L[0] = ((self.L[0]>>1)|bit<<7)&0xFF
            prev = self.L[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            test = (value[0]&0x01)
            
            value[0] = ((value[0]>>1)|bit<<7)&0xFF
            reg.Write_to_Memory_u16(self.HL,value)
            prev = value[0]
            self.current_cycles[0]=16
            self.cycles[0]+=8
        elif opcode&0x0F== 0x0F:
            test = (self.A[0]&0x01)
            
            self.A[0] = ((self.A[0]>>1)|bit<<7)&0xFF
            prev = self.A[0]
            self.current_cycles[0]=8
        if test == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if prev ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0]+=1
        self.cycles[0]+=8
        
        
    def SLA_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0
        if opcode&0x0F== 0x00:
            test = (self.B[0]&0x80)>>7
            self.B[0] = (self.B[0]<<1)&0xFF
            prev = self.B[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x01:
            test = (self.C[0]&0x80)>>7
            self.C[0] = (self.C[0]<<1)&0xFF
            prev = self.C[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x02:
            test = (self.D[0]&0x80)>>7
            self.D[0] = (self.D[0]<<1)&0xFF
            prev = self.D[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x03:
            test = (self.E[0]&0x80)>>7
            self.E[0] = (self.E[0]<<1)&0xFF
            prev = self.E[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x04:
            test = (self.H[0]&0x80)>>7
            self.H[0] = (self.H[0]<<1)&0xFF
            prev = self.H[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x05:
            test = (self.L[0]&0x80)>>7
            self.L[0] = (self.L[0]<<1)&0xFF
            prev = self.L[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)
            test = (value[0]&0x80)>>7
            value[0] = (value[0]<<1)&0xFF
            prev = value[0]
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
        elif opcode&0x0F== 0x07:
            test = (self.A[0]&0x80)>>7
            self.A[0] = (self.A[0]<<1)&0xFF
            prev = self.A[0]
            self.current_cycles[0]=8
        if test == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if prev ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0]+=1
        self.cycles[0]+=8

    def SRL_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] =0
        if opcode&0x0F== 0x08:
            test = (self.B[0]&0x01)
            self.B[0] = (self.B[0]>>1)&0xFF
            prev = self.B[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x09:
            test = (self.C[0]&0x01)
            self.C[0] = (self.C[0]>>1)&0xFF
            prev = self.C[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0A:
            test = (self.D[0]&0x01)
            self.D[0] = (self.D[0]>>1)&0xFF
            prev = self.D[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0B:
            test = (self.E[0]&0x01)
            self.E[0] = (self.E[0]>>1)&0xFF
            prev = self.E[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0C:
            test = (self.H[0]&0x01)
            self.H[0] = (self.H[0]>>1)&0xFF
            prev = self.H[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0D:
            test = (self.L[0]&0x01)
            self.L[0] = (self.L[0]>>1)&0xFF
            prev = self.L[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            test = (value[0]&0x01)
            value[0] = (value[0]>>1)&0xFF
            prev = value[0]
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
        elif opcode&0x0F== 0x0F:
            test = (self.A[0]&0x01)
            self.A[0] = (self.A[0]>>1)&0xFF
            prev = self.A[0]
            self.current_cycles[0]=8
        if test == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if prev ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0]+=1
        self.cycles[0]+=8
        
        
    def SWAP_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = 0
        if opcode&0x0F== 0x00:
            self.B[0] = (self.B[0]>>4|self.B[0]<<4)&0xFF
            if self.B[0] == 0:
                self.F[0] = 0x80

            self.current_cycles[0]=8
        elif opcode&0x0F== 0x01:
            self.C[0] = (self.C[0]>>4|self.C[0]<<4)&0xFF
            if self.C[0] == 0:
                self.F[0] = 0x80
                
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x02:
            self.D[0] = (self.D[0]>>4|self.D[0]<<4)&0xFF
            if self.D[0] == 0:
                self.F[0] = 0x80
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x03:
            self.E[0] = (self.E[0]>>4|self.E[0]<<4)&0xFF
            if self.E[0] == 0:
                self.F[0] = 0x80
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x04:
            self.H[0] = (self.H[0]>>4|self.H[0]<<4)&0xFF
            if self.H[0] == 0:
                self.F[0] = 0x80
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x05:
            self.L[0] = (self.L[0]>>4|self.L[0]<<4)&0xFF
            if self.L[0] == 0:
                self.F[0] = 0x80
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)

            value[0] = (value[0]>>4| value[0]<<4)&0xFF
            reg.Write_to_Memory_u16(self.HL,value)
            if value[0] == 0:
                self.F[0] = 0x80
            self.current_cycles[0]=16
            self.cycles[0]+=8
        elif opcode&0x0F== 0x07:
            self.A[0] = (self.A[0]>>4|self.A[0]<<4)&0xFF
            if self.A[0] == 0:
                self.F[0] = 0x80
            self.current_cycles[0]=8
        self.PC[0]+=1
        self.cycles[0]+=8

        
        
    def SRA_r8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] =0
        if opcode&0x0F== 0x08:
            test = (self.B[0]&0x01)
            sig_bit = (self.B[0]&0x80)
            self.B[0] = ((self.B[0]>>1)|sig_bit)&0xFF
            prev = self.B[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x09:
            test = (self.C[0]&0x01)
            sig_bit = (self.C[0]&0x80)
            self.C[0] = ((self.C[0]>>1)|sig_bit)&0xFF
            prev = self.C[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0A:
            test = (self.D[0]&0x01)
            sig_bit = (self.D[0]&0x80)
            self.D[0] = ((self.D[0]>>1)|sig_bit)&0xFF
            prev = self.D[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0B:
            test = (self.E[0]&0x01)
            sig_bit = (self.E[0]&0x80)
            self.E[0] = ((self.E[0]>>1)|sig_bit)&0xFF
            prev = self.E[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0C:
            test = (self.H[0]&0x01)
            sig_bit = (self.H[0]&0x80)
            self.H[0] = ((self.H[0]>>1)|sig_bit)&0xFF
            prev = self.H[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0D:
            test = (self.L[0]&0x01)
            sig_bit = (self.L[0]&0x80)
            self.L[0] = ((self.L[0]>>1)|sig_bit)&0xFF
            prev = self.L[0]
            self.current_cycles[0]=8
        elif opcode&0x0F== 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            test = (value[0]&0x01)
            sig_bit = (value[0]&0x80)
            value[0] = ((value[0]>>1)|sig_bit)&0xFF
            prev = value[0]
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
        elif opcode&0x0F== 0x0F:
            test = (self.A[0]&0x01)
            sig_bit = (self.A[0]&0x80)
            self.A[0] = ((self.A[0]>>1)|sig_bit)&0xFF
            prev = self.A[0]
            self.current_cycles[0]=8
        if test == 1:
            temp= self.F[0]|0x10
            self.F[0] = temp
        if prev ==0:
            temp = self.F[0]
            temp = temp|0x80
            self.F[0] = temp
        self.PC[0]+=1
        self.cycles[0]+=8
        
        
        
        
    def BIT_0_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        if opcode&0x0F == 0x00:
            d = self.B[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x01:
            d = self.C[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x02:
            d = self.D[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x03:
            d = self.E[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x04:
            d = self.H[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x05:
            d = self.L[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = value[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x07:
            d = self.A[0]&0x1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
        
    def BIT_1_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        if opcode&0x0F == 0x08:
            d = (self.B[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x09:
            d = (self.C[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0A:
            d = (self.D[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0B:
            d = (self.E[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0C:
            d = (self.H[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0D:
            d = (self.L[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x0F:
            d = (self.A[0]&0x2)>>1
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
        
        
    def BIT_2_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        mask = 0x4
        shift = 2
        if opcode&0x0F == 0x00:
            d = (self.B[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x01:
            d = (self.C[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x02:
            d = (self.D[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x03:
            d = (self.E[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x04:
            d = (self.H[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x05:
            d = (self.L[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x07:
            d = (self.A[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
    def BIT_3_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        mask = 0x8
        shift = 3
        if opcode&0x0F == 0x08:
            d = (self.B[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x09:
            d = (self.C[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0A:
            d = (self.D[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0B:
            d = (self.E[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0C:
            d = (self.H[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0D:
            d = (self.L[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x0F:
            d = (self.A[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
        
        
    def BIT_4_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        mask = 0x10
        shift = 4
        if opcode&0x0F == 0x00:
            d = (self.B[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x01:
            d = (self.C[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x02:
            d = (self.D[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x03:
            d = (self.E[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x04:
            d = (self.H[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x05:
            d = (self.L[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x07:
            d = (self.A[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
        
    def BIT_5_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        mask = 0x20
        shift = 5
        if opcode&0x0F == 0x08:
            d = (self.B[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x09:
            d = (self.C[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0A:
            d = (self.D[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0B:
            d = (self.E[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0C:
            d = (self.H[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0D:
            d = (self.L[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x0F:
            d = (self.A[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
    def BIT_6_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        mask = 0x40
        shift = 6
        if opcode&0x0F == 0x00:
            d = (self.B[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x01:
            d = (self.C[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x02:
            d = (self.D[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x03:
            d = (self.E[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x04:
            d = (self.H[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x05:
            d = (self.L[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x06:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x07:
            d = (self.A[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
        
    def BIT_7_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        self.F[0] = self.F[0]&0x10
        self.F[0] = self.F[0]|0x20
        mask = 0x80
        shift = 7
        if opcode&0x0F == 0x08:
            d = (self.B[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        
        elif opcode&0x0F == 0x09:
            d = (self.C[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0A:
            d = (self.D[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0B:
            d = (self.E[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0C:
            d = (self.H[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0D:
            d = (self.L[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        elif opcode&0x0F == 0x0E:
            value = [0]
            reg.Read_memory(self.HL,value)
            d = (value[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=12
            self.cycles[0]+=4
        elif opcode&0x0F == 0x0F:
            d = (self.A[0]&mask)>>shift
            if d == 0 :
                self.F[0] = self.F[0]|0x80
            self.current_cycles[0]=8
        self.PC[0] +=1
        self.cycles[0]+=8
        
        
    def RES_0_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xFE
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        
    def RES_1_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xFD
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8

    def RES_2_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xFB
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
    def RES_3_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xF7
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
    
    def RES_4_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xEF
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        
        
    def RES_5_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xDF
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        

    def RES_6_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0xBF
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        
    def RES_7_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x7F
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]&mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]&mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]&mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8

    def SET_0_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x1
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        
        
    def SET_1_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x2
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        
        
    def SET_2_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x4
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
            

    def SET_3_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x8
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8

    def SET_4_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x10
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
            

    def SET_5_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x20
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
        
    def SET_6_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x40
        if opcode & 0x0F == 0x0:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x1:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x2:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x3:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x4:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x5:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x6:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0x7:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8
            

    def SET_7_R8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        opcode = reg.pointer()
        mask = 0x80
        if opcode & 0x0F == 0x8:
            self.B[0] = self.B[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0x9:
            self.C[0] = self.C[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xA:
            self.D[0] = self.D[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xB:
            self.E[0] = self.E[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xC:
            self.H[0] = self.H[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xD:
            self.L[0] = self.L[0]|mask
            self.current_cycles[0] = 8
        elif opcode & 0x0F == 0xE:
            value = [0]
            reg.Read_memory(self.HL,value)


            value[0] = value[0]|mask
            reg.Write_to_Memory_u16(self.HL,value)
            self.current_cycles[0]=16
            self.cycles[0]+=8
            
        elif opcode & 0x0F == 0xF:
            self.A[0] = self.A[0]|mask
            self.current_cycles[0] = 8
            
        self.PC[0] +=1
        self.cycles[0] +=8

            

    def CB(self)-> None:
        self.PC[0] +=1
        
    def ADD_SP_n8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1
        imm8= reg.pointer() 
        self.F[0] =0 
        if imm8 >= 0x80:
            imm8 = +(imm8&0x7F )-0x80 
        if ((self.SP[0])&0x0F)+((imm8)&0xF)>0xf:
            self.F[0] = self.F[0]|0x20
        else:
            self.F[0] = self.F[0]&0xDF
        if ((self.SP[0])&0xFF)+((imm8)&0xFF)>0xFF:
                
            self.F[0] = self.F[0]|0x10
        else:
            self.F[0] = self.F[0]&0xEF   
        self.SP[0] = self.SP[0]+imm8
        if self.SP[0]>0xFFFF:
            self.SP[0] = self.SP[0]&0xFFFF
        
        self.PC[0]+=1
        self.cycles[0] +=16
        self.current_cycles[0] = 16   
        
        
    def LD_HL_SP(self)-> None:
        self.SP[0] = self.HL[0]
        self.PC[0]+=1
        self.cycles[0] +=8
        self.current_cycles[0] = 8
        
    def LD_HL_SP_e8(self)-> None:
        reg = Opcode(self.BC,self.PC,self.AF,self.DE,self.HL,self.SP,self.Rombank,self.Rambank,self.IO,self.A,self.B,self.C,self.D,self.E,self.F,self.H,self.L,self.OAM,self.IER,self.cycles,self.s,self.Ramswitch,self.Romswitch,self.MCB,self.RamEnabled,self.VRAM,self.R,self.WRAM,self.HRAM,self.oplist,self.paused,self.ECHO,self.IMF,self.loc,self.Call,self.current_cycles,self.Not_Usable,self.disable_Vram,self.disable_OAM,self.Timer_Counter)
        self.PC[0]+=1
        imm8= reg.pointer() 
        self.F[0] =0 
        if imm8 >= 0x80:
            imm8 = +(imm8&0x7F )-0x80 
        if ((self.SP[0])&0x0F)+((imm8)&0xF)>0xf:
            self.F[0] = self.F[0]|0x20
        else:
            self.F[0] = self.F[0]&0xDF
        if ((self.SP[0])&0xFF)+((imm8)&0xFF)>0xFF:
                
            self.F[0] = self.F[0]|0x10
        else:
            self.F[0] = self.F[0]&0xEF   
        self.HL[0] = self.SP[0]+imm8
        if self.HL[0]>0xFFFF:
            self.HL[0] = self.HL[0]&0xFFFF
        
        self.L[0] = self.HL[0]&0xFF
        self.H[0] = (self.HL[0]>>8)&0xFF
        self.PC[0]+=1
        self.cycles[0] +=12
        self.current_cycles[0] = 12  
    def stop(self)-> None:
        self.PC[0]+=2
        self.cycles[0]+=4
        self.current_cycles[0]=4
           

 


        
        
    
            
            
        
        

        


        
        
        
    

        
        
        

    
            
        
        
            
    