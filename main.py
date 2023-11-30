import tkinter as tk
from collections import defaultdict

class TonnerManager:
    def __init__(self):
        self.tonners = defaultdict(int)
        self.ordered_tonners = defaultdict(int)

    def add_tonner(self, model, quantity):
        self.tonners[model] += quantity

    def remove_tonner(self, model, quantity):
        if self.tonners[model] >= quantity:
            self.tonners[model] -= quantity
        else:
            print(f"Not enough {model} tonner(s) in inventory!")

    def order_tonner(self, model, quantity):
        self.ordered_tonners[model] += quantity

        # Salva o pedido no arquivo .txt
        with open('pedidos.txt', 'a') as file:
            file.write(f"Pedido: {quantity} unidades do modelo {model}\n")

    def generate_report(self):
        print("\nInventory Report:")
        for model, quantity in self.tonners.items():
            print(f"{model}: {quantity}")
        print("\nOrdered Tonner Report:")
        for model, quantity in self.ordered_tonners.items():
            print(f"{model}: {quantity}")

def update_inventory():
    tonner_listbox.delete(0, tk.END)
    for model, quantity in manager.tonners.items():
        tonner_listbox.insert(tk.END, f"{model}: {quantity}")

def add_tonner():
    model = add_model_entry.get()
    quantity = int(add_quantity_entry.get())
    manager.add_tonner(model, quantity)
    update_inventory()

def remove_tonner():
    model = remove_model_entry.get()
    quantity = int(remove_quantity_entry.get())
    manager.remove_tonner(model, quantity)
    update_inventory()

def order_tonner():
    model = order_model_entry.get()
    quantity = int(order_quantity_entry.get())
    manager.order_tonner(model, quantity)
    update_inventory()

def generate_report(manager_instance):  # Passa a instância do gerenciador de tonners como argumento
    manager_instance.generate_report()  # Chama o método do gerenciador de tonners

manager = TonnerManager()
manager.add_tonner("T06", 2)
manager.add_tonner("285A", 2)
manager.add_tonner("283A", 2)
manager.add_tonner("TN580", 2)
manager.add_tonner("TN750", 2)

app = tk.Tk()
app.title("Tonner Manager")

tonner_listbox = tk.Listbox(app, width=60, height=20)
tonner_listbox.grid(row=0, column=0, columnspan=3, pady=10)

add_frame = tk.Frame(app)
add_frame.grid(row=1, column=0, pady=10)
add_model_label = tk.Label(add_frame, text="Modelo:")
add_model_label.grid(row=0, column=0)
add_model_entry = tk.Entry(add_frame)
add_model_entry.grid(row=0, column=1)
add_quantity_label = tk.Label(add_frame, text="Quantidade:")
add_quantity_label.grid(row=1, column=0)
add_quantity_entry = tk.Entry(add_frame)
add_quantity_entry.grid(row=1, column=1)
add_button = tk.Button(add_frame, text="Add Tonner", command=add_tonner)
add_button.grid(row=2, column=0, columnspan=2)

remove_frame = tk.Frame(app)
remove_frame.grid(row=1, column=1, pady=10)
remove_model_label = tk.Label(remove_frame, text="Modelo:")
remove_model_label.grid(row=0, column=0)
remove_model_entry = tk.Entry(remove_frame)
remove_model_entry.grid(row=0, column=1)
remove_quantity_label = tk.Label(remove_frame, text="Quantidade:")
remove_quantity_label.grid(row=1, column=0)
remove_quantity_entry = tk.Entry(remove_frame)
remove_quantity_entry.grid(row=1, column=1)
remove_button = tk.Button(remove_frame, text="Remove Tonner", command=remove_tonner)
remove_button.grid(row=2, column=0, columnspan=2)

order_frame = tk.Frame(app)
order_frame.grid(row=1, column=2, pady=10)
order_model_label = tk.Label(order_frame, text="Modelo:")
order_model_label.grid(row=0, column=0)
order_model_entry = tk.Entry(order_frame)
order_model_entry.grid(row=0, column=1)
order_quantity_label = tk.Label(order_frame, text="Quantidade:")
order_quantity_label.grid(row=1, column=0)
order_quantity_entry = tk.Entry(order_frame)
order_quantity_entry.grid(row=1, column=1)
order_button = tk.Button(order_frame, text="Order Tonner", command=order_tonner)
order_button.grid(row=2, column=0, columnspan=2)

def generate_report():
    manager.generate_report()

report_button = tk.Button(app, text="Generate Report", command=generate_report)
report_button.grid(row=2, column=0, columnspan=3, pady=10)

update_inventory()
app.mainloop()