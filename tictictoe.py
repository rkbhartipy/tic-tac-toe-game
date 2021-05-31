from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from random import *




class ttt_cls:
    def __init__(self,window):
        self.window=window
        self.count=""                              ## used in opration funcion
        self.player=1                              ## this will be used for player updation
        self.j="a"                                 ## usd un opration method
        self.pressed_no_list=[]                    ## for opration method
        self.getting_re_new={0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
        self.point_x=0                             ## used in result_fun method
        self.point_o=0

        
##-------------------------------creating and placing buttons on root---------------------------------------
        style=Font(size=40)
        ## creating buttons
        self.btn=[]
        for x in range(0,10):
            self.btn.append(Button(window,text="",bd=5,font=style,width=4,command=lambda v=x:self.opration(v)))
        ## placing buttons on root or window
        a=0
        for i in range(0,3):
            for j in range(0,3):
                self.btn[a].place(x=j*137+10,y=i*110+10)
                a+=1
                
##-------------------label and score updation---------------------------------------------
                
        ## label player1
        self.player_x=Label(self.window,text="Player X:",font=(20))
        self.player_x.place(x=10,y=350)

        ## player 1 score updation label
        self.score_label_x=Label(self.window,text="",bg=None,font=(20))
        self.score_label_x.place(x=90,y=350)

        ## label player2
        self.player_o=Label(self.window,text="Player 0 :",font=(20))
        self.player_o.place(x=10,y=390)

        ## player 2 score updation label
        self.score_label_o=Label(self.window,text="",bg=None,font=(20))
        self.score_label_o.place(x=90,y=390)

        
        ## working of the application  
        ## focusing on "no same buttons shouls be pressed again"
        
##------------------------------inserting "0" at random buttons-----------------------------------
        if (self.point_x==0) or (self.point_x%2==0):
            pass
        else:
            a=randint(2,8)
            self.btn[a].config(text="0")
            self.getting_re_new[a]="0"

##----------------------------logic for programe---------------------------------------------
        
    def opration(self,x):
        n=x

        if self.count==n or (n in self.pressed_no_list):
            pass

        elif  self.count!=n and (self.j=='a') and (n not in self.pressed_no_list) :
            self.btn[x].config(text="X")
            self.pressed_no_list.append(n)
            self.j='b'

            self.getting_re_new[n]=("X")
            

        elif self.count!=n and (self.j=='b' ) and (n not in self.pressed_no_list):
            self.btn[x].config(text="0")
            self.pressed_no_list.append(n)
            self.j='a'

            self.getting_re_new[n]=("0")
            

        else:
            pass

        self.count=n

    


##---------------------------------------calculatin and showing result---------------------------------------------------------
      
    

##---------------------------------------conditions to win "X"----------------------------------
    
        
        if True:
            if True:
                if (self.getting_re_new[0]=="X" and self.getting_re_new[1]=="X" and self.getting_re_new[2]=="X"):
                    self.btn[0].config(bg="red")
                    self.btn[1].config(bg="red")
                    self.btn[2].config(bg="red")
                    self.point_x+=1
                    self.score_fun()
                    
                elif (self.getting_re_new[3]=="X" and self.getting_re_new[4]=="X" and self.getting_re_new[5]=="X"):
                    self.btn[3].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[5].config(bg="red")
                    self.point_x+=1
                    self.score_fun()

                elif (self.getting_re_new[6]=="X" and self.getting_re_new[7]=="X" and self.getting_re_new[8]=="X"):
                    self.btn[6].config(bg="red")
                    self.btn[7].config(bg="red")
                    self.btn[8].config(bg="red")
                    self.point_x+=1
                    self.score_fun()

                elif (self.getting_re_new[0]=="X" and self.getting_re_new[3]=="X" and self.getting_re_new[6]=="X"):
                    self.btn[0].config(bg="red")
                    self.btn[3].config(bg="red")
                    self.btn[6].config(bg="red")
                    self.point_x+=1
                    self.score_fun()

                elif (self.getting_re_new[1]=="X" and self.getting_re_new[4]=="X" and self.getting_re_new[7]=="X"):
                    self.btn[1].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[7].config(bg="red")
                    self.point_x+=1
                    self.score_fun()

                elif (self.getting_re_new[2]=="X" and self.getting_re_new[5]=="X" and self.getting_re_new[8]=="X"):
                    self.btn[2].config(bg="red")
                    self.btn[5].config(bg="red")
                    self.btn[8].config(bg="red")
                    self.point_x+=1
                    self.score_fun()

                elif (self.getting_re_new[0]=="X" and self.getting_re_new[4]=="X" and self.getting_re_new[8]=="X"):
                    self.btn[0].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[8].config(bg="red")
                    self.point_x+=1
                    self.score_fun()

                elif (self.getting_re_new[2]=="X" and self.getting_re_new[4]=="X" and self.getting_re_new[6]=="X"):
                    self.btn[2].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[6].config(bg="red")
                    self.point_x+=1
                    self.score_fun()



##----------------------------conditions to win "0"----------------------------------------------------------

        
                elif (self.getting_re_new[0]=="0" and self.getting_re_new[1]=="0" and self.getting_re_new[2]=="0"):
                    self.btn[0].config(bg="red")
                    self.btn[1].config(bg="red")
                    self.btn[2].config(bg="red")
                    self.point_o+=1
                    self.score_fun()
                    
                elif (self.getting_re_new[3]=="0" and self.getting_re_new[4]=="0" and self.getting_re_new[5]=="0"):
                    self.btn[3].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[5].config(bg="red")
                    self.point_o+=1
                    self.score_fun()

                elif (self.getting_re_new[6]=="0" and self.getting_re_new[7]=="0" and self.getting_re_new[8]=="0"):
                    self.btn[6].config(bg="red")
                    self.btn[7].config(bg="red")
                    self.btn[8].config(bg="red")
                    self.point_o+=1 
                    self.score_fun()

                elif (self.getting_re_new[0]=="0" and self.getting_re_new[3]=="0" and self.getting_re_new[6]=="0"):
                    self.btn[0].config(bg="red")
                    self.btn[3].config(bg="red")
                    self.btn[6].config(bg="red")
                    self.point_o+=1 
                    self.score_fun()

                elif (self.getting_re_new[1]=="0" and self.getting_re_new[4]=="0" and self.getting_re_new[7]=="0"):
                    self.btn[1].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[7].config(bg="red")
                    self.point_o+=1 
                    self.score_fun()

                elif (self.getting_re_new[2]=="0" and self.getting_re_new[5]=="0" and self.getting_re_new[8]=="0"):
                    self.btn[2].config(bg="red")
                    self.btn[5].config(bg="red")
                    self.btn[8].config(bg="red")
                    self.point_o+=1
                    self.score_fun()

                elif (self.getting_re_new[0]=="0" and self.getting_re_new[4]=="0" and self.getting_re_new[8]=="0"):
                    self.btn[0].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[8].config(bg="red")
                    self.point_o+=1 
                    self.score_fun()

                elif (self.getting_re_new[2]=="0" and self.getting_re_new[4]=="0" and self.getting_re_new[6]=="0"):
                    self.btn[2].config(bg="red")
                    self.btn[4].config(bg="red")
                    self.btn[6].config(bg="red")
                    self.point_o+=1 
                    self.score_fun()
            
        else:
            print("hi")


##----------------------------score of player----------------------------------------------------------
    def score_fun(self):
        if self.point_x!=0:
            self.score_label_x.config(text=self.point_x)
            messagebox.showinfo("result","X won")

        elif self.point_o!=0:
            self.score_label_o.config(text=self.point_o)
            messagebox.showinfo("result","0 won")

    
            



##----------------------main funcion of the program-------------------------------------------------------

def main():
    root=Tk()
    root.title("tic tac too")
    root.geometry("439x440")
    root.resizable(False,False)
    tictacto_obj=ttt_cls(root)
    
    root.mainloop()

if __name__=="__main__":
    main()
