import tkinter as tk
from tkinter import ttk, messagebox
from geminiAPI import GeminiAPI

class GiftAdvisorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poradnik prezentowy")
        self.gemini_api = GeminiAPI()

        self.label = ttk.Label(root, text="Wprowadź dane osoby, dla której szukasz prezentu:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.age_label = ttk.Label(root, text="Wiek:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.age_entry = ttk.Entry(root, width=10)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.sex_label = ttk.Label(root, text="Płeć:")
        self.sex_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.sex_var = tk.StringVar()
        self.sex_combobox = ttk.Combobox(root, textvariable=self.sex_var, values=["Mężczyzna", "Kobieta", ""])
        self.sex_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.sex_combobox.current(2)  

        self.relationship_label = ttk.Label(root, text="Kim jest dla ciebie?:")
        self.relationship_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.relationship_entry = ttk.Entry(root,width=30)
        self.relationship_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.budget_label = ttk.Label(root, text="Budżet (Podaj walutę):")
        self.budget_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.budget_entry = ttk.Entry(root)
        self.budget_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.hobbies_label = ttk.Label(root, text="Zainteresowania (wymień po przecinku):")
        self.hobbies_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.hobbies_entry = ttk.Entry(root, width=50)
        self.hobbies_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.celebration_label = ttk.Label(root, text="Okazja:")
        self.celebration_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.celebration_entry = ttk.Entry(root)
        self.celebration_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        self.submit_button = ttk.Button(root, text="Pokaż propozycje", command=self.submit)
        self.submit_button.grid(row=7, column=0, columnspan=2, pady=20)

        self.result_label = ttk.Label(root, text="Pomysły:")
        self.result_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        self.result_text = tk.Text(root, height=20, width=70)
        self.result_text.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    def validate_inputs(self):
        if not self.age_entry.get():
            messagebox.showerror("Error", "Podaj wszystkie informacje.")
            return False
        if not self.relationship_entry.get():
            messagebox.showerror("Error", "Podaj wszystkie informacje.")
            return False
        if not self.budget_entry.get():
            messagebox.showerror("Error", "Podaj wszystkie informacje.")
            return False
        if not self.hobbies_entry.get():
            messagebox.showerror("Error", "Podaj wszystkie informacje.")
            return False
        if not self.celebration_entry.get():
            messagebox.showerror("Error", "Podaj wszystkie informacje.")
            return False
        return True

    def submit(self):
    
        if not self.validate_inputs():
            return  

        age = self.age_entry.get()
        sex = self.sex_var.get()
        relationship = self.relationship_entry.get()
        max_budget = self.budget_entry.get()
        hobbies = self.hobbies_entry.get().split(",") 
        celebration = self.celebration_entry.get()

  
        self.stored_data = {
            "age": age,
            "sex": sex,
            "relationship": relationship,
            "max_budget": max_budget,
            "hobbies": hobbies,
            "celebration": celebration
        }

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Wiek: {age}\n")
        self.result_text.insert(tk.END, f"Płeć: {sex}\n")
        self.result_text.insert(tk.END, f"Relacja: {relationship}\n")
        self.result_text.insert(tk.END, f"Max Budżet: {max_budget}\n")
        self.result_text.insert(tk.END, f"Zainteresowania: {', '.join(hobbies)}\n")
        self.result_text.insert(tk.END, f"Okazja: {celebration}\n")

        print(self.stored_data)

        self.generate_gift_ideas()

    def generate_gift_ideas(self):
        self.gemini_api.gen_gift_ideas(self.stored_data)
        self.result_text.insert(tk.END, "\nPomysły:\n")
        for idea in self.gemini_api.get_gift_ideas():
            self.result_text.insert(tk.END, f"{idea}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = GiftAdvisorApp(root)
    root.mainloop()