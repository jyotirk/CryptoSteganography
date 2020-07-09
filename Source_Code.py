"""This is implementation of image cryptosteganography
usig AES256 algorithm for cryptography and LSB for image steganography
"""


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from cryptosteganography import CryptoSteganography
class App:
       
    def decode(self):
        
        dec = Tk()
        dec.title("Decoding")
        dec.geometry("650x400")  
        dec['background']='blanched almond' 
        
        label1 = Label(dec, text="verification key", bg = 'blanched almond',font = ("Calibiri,4") ).place(relx = 0.1, rely = 0.2, height = 20, width = 120)
        
        entrykeyd = Entry(dec, textvariable = "entrykeyd", show = "*",font = ("Calibiri,2"), highlightcolor = "medium orchid", highlightthickness = 2)
        entrykeyd.place(relx = 0.33, rely = 0.2,height = 30, width = 200 )
    
    
        label3 = label2 = Label(dec, text = "Secret message", bg = 'blanched almond',font = ("Calibiri,4"))
        label3.place(relx = 0.1, rely = 0.5)
        
    
        def openfile():
            global fileopen
            fileopen = StringVar()
            fileopen = askopenfilename(parent = dec, initialdir = "/Desktop/Information security internship",title = "select files", filetypes=(("png files", "*png"), ("all files","*.*")))
        
            label4 = Label(dec, text=fileopen, bg = "white",font = ("Calibiri,1"))
            label4.place(relx = 0.33, rely = 0.3)
    
        def decrypt():
            
            if entrykeyd.get()=="123456":
                crypt = CryptoSteganography("my secret message")
                dec_message = crypt.retrieve(fileopen)
                new = StringVar()
                label5 = Text(dec,bg = "white",font = ("Calibiri,2"), highlightcolor = "medium orchid", highlightthickness = 2)
                new.set(dec_message)
                label5.place(relx = 0.33, rely = 0.5, width = 200, height = 50)
                label5.delete(0.0,END)
                label5.insert(0.0,dec_message)
            else:
                wierdo = "$$$%%%%%%%4444$$$"
                wrong = StringVar()
                label6 = Text(dec, bg = "white",font = ("Calibiri,2"), highlightcolor = "medium orchid", highlightthickness = 2)
                wrong.set(wierdo)
                label6.place(relx = 0.33, rely = 0.5, width = 200, height = 50)
                label6.delete(0.0,END)
                label6.insert(0.0,wierdo)
                m3 = messagebox.showerror("ERROR", "wrong verification key", parent = dec) 
        fileb1 = Button(dec, text="Select file", command = openfile, overrelief = 'groove',font = ("Calibiri,4")).place(relx = 0.1, rely = 0.3, height = 40, width= 80)
        decbutton = Button(dec, text="Decrypt", command = decrypt, overrelief = 'groove',font = ("Calibiri,4")).place(relx = 0.1, rely = 0.65, height = 40, width= 80)
        
    
    def encode(self):
        
        enc = Tk()
        enc.title("Encoding")
        enc.geometry("650x400")
        enc['background']='blanched almond' 
        
        label1 = Label(enc, text="Enter the key", bg = 'blanched almond' ,font = ("Calibiri,4")).place(relx = 0.1, rely = 0.2, height = 20, width = 130)
        
        entrykey = Entry(enc, textvariable = "entrykey", show = "*",font = ("Calibiri,4"), highlightcolor = "medium orchid", highlightthickness = 2)
        entrykey.place(relx = 0.35, rely = 0.2,height = 20, width = 200)
    
        label2 = Label(enc, text = "Secret message", bg = 'blanched almond',font = ("Calibiri,4"))
        label2.place(relx = 0.1, rely = 0.3, height =  25, width = 130)
        
        message = Text(enc,font = ("Calibiri,4"), highlightcolor = "medium orchid", highlightthickness = 2)
        message.place(relx = 0.35, rely = 0.3, height = 40, width = 200)
        message.insert(END,"\n")
        
        label3 = Label(enc, text = "File name", bg = 'blanched almond',font = ("Calibiri,2"))
        label3.place(relx = 0.1, rely = 0.5)
        
        fname = Entry(enc,  textvariable = "fname",font = ("Calibiri,4"), highlightcolor = "medium orchid", highlightthickness = 2)
        fname.place(relx = 0.35, rely = 0.5, width = 200)
    
        def openfile():
            global fileopen
            fileopen = StringVar()
            fileopen = askopenfilename(parent = enc, initialdir = "/Desktop",title = "select files", filetypes=(("jpeg files", "*jpg"), ("all files","*.*")))
        
            label4 = Label(enc, text=fileopen,font = ("Calibiri,1"))
            label4.place(relx = 0.3, rely = 0.6)
        def encrypt():
            
            crypt = CryptoSteganography(entrykey.get())
            if fname.get():
                crypt.hide(fileopen, fname.get()+".png", message.get(0.0,END))
                m1 = messagebox.showinfo("pop-up", "succesfully encrypted",parent = enc)
            else:
                crypt.hide(fileopen, "output.png", message.get(0.0,END))
                m2 = messagebox.showinfo("pop-up", "succesfully encrypted",parent = enc) 
            
    
        
        fileb = Button(enc, text="Select file", command = openfile,font = ("Calibiri,3"), overrelief = 'groove').place(relx = 0.1, rely = 0.6, height = 40, width= 80)
    
        encbutton = Button(enc, text="Encrypt", command = encrypt,font = ("Calibiri,3"), overrelief = 'groove').place(relx = 0.4, rely = 0.7, height = 40, width= 80)
    
        
    
    def choice(self):
        root.destroy()
        ch = Tk()
        ch.title("Encode/decode")
        ch.geometry("300x200")
        ch['background']='powder blue'    
        labell = Label(ch, text="Please select one option", bg = 'powder blue',font = ("Calibiri,9") ).pack()
    
        encb = Button(ch, text="Encode", width=15, height=2,command = self.encode, font = ("Calibiri,3"), overrelief = 'sunken').place(relx = 0.1, rely = 0.3, height = 40, width= 80)
        decb = Button(ch, text="Decode", width=15, height=2,command = self.decode,font = ("Calibiri,3"), overrelief = 'groove').place(relx = 0.6, rely = 0.3, height = 40, width= 80)
    
   
    def validate(self):
      
        u1 = self.username1.get()
        p1 = self.password1.get()
        
        dict = {"101": "1122","102": "1256","103":"7894"}
        if u1 in dict:
            if dict[u1] == p1:
                    
                self.choice()
            else:
                messagebox.showinfo("invalid","Invalid Password")
        else:
            messagebox.showinfo("invalid","Invalid Username")
    
    def __init__(self,main):    
        main.title("Login")
        main.geometry("500x400")
        main['background']='powder blue'    
        self.username1 = StringVar()
        self.password1= StringVar()
        self.entrykey = StringVar()
       
        l1 = Label(main, text="Please enter login details", bg = 'powder blue', font = ("Calibiri,15") ).pack()
        l2 = Label(main, text="", bg = 'powder blue').pack()
        l3 = Label(main, text="Username",bg = 'powder blue', height = 2,font = ("Calibiri,9")).pack()
        self.username = Entry(main, textvariable=self.username1,font = ("Calibiri,5"), highlightcolor = "medium orchid", highlightthickness = 2).pack( ipady = 5)
        l4 = Label(main, text="",bg = 'powder blue',height = 2).pack()
        l5 = Label(main, text="Password",bg = 'powder blue',font = ("Calibiri,9")).pack()
        self.password = Entry(main, textvariable=self.password1, show= '*',font = ("Calibiri,5"),highlightcolor = "medium orchid", highlightthickness = 2)
        self.password.pack(ipady = 5)
        
        
        Label(main, text="",bg = 'powder blue').pack()
        
        
        loginb = Button(main, text="LOGIN", width=10, height=1,command = self.validate, overrelief = 'groove',font = ("Calibiri,4")).pack()
        
       

root=Tk()
App(root)
root.mainloop()
