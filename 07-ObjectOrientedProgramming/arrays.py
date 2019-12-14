from random import randrange
class arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_col2(array):
        l=len(array)
        for i in range(l):
            print(array[i],end="")
            if i!=l-1:
                print(", ",end="")        
    @staticmethod
    def create_array(number,value):
        array=[]
        for i in range(number):
            array.append(value)
        return array       
    @staticmethod
    def create_random(number,begin,end):
        array=[]
        for i in range(number):
            array.append(randrange(begin,end+1)) 
        return array     
    @staticmethod
    def number_of_item(array,begin,end):
        if end>begin:
            return end-begin
        elif begin==end:
            return 0    
        else:
            return begin-end    
                 
#my_array = [4,1,8,7,2]
#arrays.print_in_col(my_array)
#arrays.print_in_col2(my_array)
