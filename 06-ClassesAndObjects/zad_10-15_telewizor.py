class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.channels=[]
        self.volume=0
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self,channels_list):
        self.channels+=channels_list
    def show_channels(self):
        print("Lista kanałów TV: ")
        for i in range(len(self.channels)):
            print(f"{i+1}. {self.channels[i]}")  
    def increase(self):
        if self.volume<10:
            self.volume+=1
    def decrease(self):
        if self.volume>0:
            self.volume-=1                    
    def show_status(self):
        if self.is_on:
            if self.channel_no-1>=len(self.channels):
                print('Telewizor jest załączony, ','kanał ',self.channel_no,'\nPoziom głosności to: ',self.volume)
            else:
                print('Telewizor jest załączony, ','kanał ',self.channel_no, '(',self.channels[self.channel_no -1],')','\nPoziom głosności to: ',self.volume)
        else:
            print("Telewizor jest wyłączony")

telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.show_channels()
tab=["TVP1", "TVP2", "Polsat", "TVN", "Filmbox","ABC","News"]
telewizor.set_channels(tab)
telewizor.show_channels()
telewizor.show_status()
telewizor.set_channel(2)
telewizor.show_status()
telewizor.set_channel(3)
telewizor.show_status()
telewizor.set_channel(4)
telewizor.show_status()
telewizor.set_channel(5)
telewizor.show_status()
telewizor.set_channel(6)
telewizor.show_status()
telewizor.set_channel(7)
telewizor.show_status()
telewizor.set_channel(8)
telewizor.show_status()
telewizor.increase()
telewizor.show_status()
telewizor.increase()
telewizor.show_status()
telewizor.decrease()
telewizor.show_status()
telewizor.off()



            
            
        