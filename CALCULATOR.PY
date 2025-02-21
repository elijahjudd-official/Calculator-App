import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        
        # Display
        self.display = tk.Entry(self.window, width=25, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  # Clear button
        ]
        
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=5, height=2,
                     font=('Arial', 14), command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.window.mainloop()
    
    def click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    calc = Calculator()
