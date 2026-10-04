
class Timer:
    def __init__(self,cycles,loc,IO,Timer_counter):
        self.cycles = cycles
        self.loc = loc
        self.IO = IO 
        self.Timer_counter = Timer_counter

    def set_count_timer(self):
        TMC = self.IO[0xFF07-0xff00]
    
        if TMC&0x3 == 0x0:
            self.Timer_counter[0] = 1024
        elif TMC&0x3 == 0x1:
            self.Timer_counter[0] = 16
        elif TMC&0x3 == 0x10:
            self.Timer_counter[0] = 64
        elif TMC&0x3 == 0x11:
            self.Timer_counter[0] = 256
        

        
        
