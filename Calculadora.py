import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x330")
        self.resizable(False, False)
        self.iconbitmap("calculator.ico")
        self.expresion = ""
        self.Entry = None
        self.entrada_StringVar = tk.StringVar()
        self._creacion_componentes()
    
    def _creacion_componentes(self):
        #Frame de expresión
        Entry_frame = tk.Frame(self,width=400,height=50,bg="grey")
        Entry_frame.pack(side=tk.TOP)
        Entry = tk.Entry(Entry_frame,textvariable=self.entrada_StringVar,width=30,font=("Arial",20,"bold"),justify=tk.RIGHT)
        Entry.pack(side=tk.LEFT,ipady=10)

        #Frame de botones
        Botones_frame = tk.Frame(self,width=400,height=450,bg="grey")
        Botones_frame.pack(side=tk.TOP)
        
        #Botones de operaciones
        boton_limpiar= tk.Button(Botones_frame,text="C",width=44,height=3,bd=0,bg="#eee",cursor="hand2", command=self._limpiar)
        boton_limpiar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

        boton_dividir = tk.Button(Botones_frame, text="/",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda: self._click("/"))
        boton_dividir.grid(row=0,column=3,padx=1,pady=1)

        boton_siete = tk.Button(Botones_frame, text="7",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("7"))
        boton_siete.grid(row=1,column=0,padx=1,pady=1)

        boton_ocho = tk.Button(Botones_frame, text="8",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("8"))
        boton_ocho.grid(row=1,column=1,padx=1,pady=1)

        boton_nueve = tk.Button(Botones_frame, text="9",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("9"))
        boton_nueve.grid(row=1,column=2,padx=1,pady=1)

        boton_multiplicar = tk.Button(Botones_frame, text="*",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda: self._click("*"))
        boton_multiplicar.grid(row=1,column=3,padx=1,pady=1)
        
        boton_cuatro = tk.Button(Botones_frame, text="4",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("4"))
        boton_cuatro.grid(row=2,column=0,padx=1,pady=1)

        boton_cinco = tk.Button(Botones_frame, text="5",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("5"))
        boton_cinco.grid(row=2,column=1,padx=1,pady=1)

        boton_seis = tk.Button(Botones_frame, text="6",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("6"))
        boton_seis.grid(row=2,column=2,padx=1,pady=1)

        boton_restar = tk.Button(Botones_frame, text="-",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda: self._click("-"))
        boton_restar.grid(row=2,column=3,padx=1,pady=1)

        boton_uno = tk.Button(Botones_frame, text="1",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("1"))
        boton_uno.grid(row=3,column=0,padx=1,pady=1)

        boton_dos = tk.Button(Botones_frame, text="2",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("2"))
        boton_dos.grid(row=3,column=1,padx=1,pady=1)

        boton_tres = tk.Button(Botones_frame, text="3",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("3"))
        boton_tres.grid(row=3,column=2,padx=1,pady=1)

        boton_sumar = tk.Button(Botones_frame, text="+",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda: self._click("+"))
        boton_sumar.grid(row=3,column=3,padx=1,pady=1)
        
        boton_cero = tk.Button(Botones_frame, text="0",width=29,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("0"))
        boton_cero.grid(row=4,column=0,padx=1,pady=1, columnspan=2)

        boton_punto = tk.Button(Botones_frame, text=".",width=14,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda: self._click("."))
        boton_punto.grid(row=4,column=2,padx=1,pady=1)
        
        boton_igual = tk.Button(Botones_frame, text="=",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=self._resultado)
        boton_igual.grid(row=4,column=3,padx=1,pady=1)


    def _limpiar(self):
        self.expresion = ""
        self.entrada_StringVar.set(self.expresion)
    
    def _click(self,operacion):
        self.expresion = self.expresion + operacion
        self.entrada_StringVar.set(self.expresion)

    def _resultado(self):
        try:
            self.expresion = str(eval(self.expresion))
            self.entrada_StringVar.set(self.expresion)
            self.expresion = ""
        except:
            messagebox.showerror("Error","No se puede dividir entre 0")
            self.expresion = ""
            self.entrada_StringVar.set(self.expresion)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()