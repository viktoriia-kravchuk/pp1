class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.channels=[]
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print("Telewizor jest załaczony, kanał {}".format(self.channel_no))
        else:
            print("Telewizor jest wyłączony")
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self,channels_list):
        self.channels+=channels_list
    def show_channels(self):
        print("Lista kanałów TV: ")
        for i in range(len(self.channels)):
            print(f"{i+1}. {self.channels[i]}")  
        
telewizor=TV()
telewizor.show_status()
telewizor.on()
telewizor.show_status()
telewizor.show_channels()
tab=["TVP1", "TVP2", "Polsat", "TVN", "Filmbox"]
telewizor.set_channels(tab)
telewizor.show_channels()
telewizor.show_status()
telewizor.off()


            
            
        