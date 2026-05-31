inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}
orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for product, qty in orders:
    match (product, inventory.get(product)):
        
        case (p, None):
            print(f"{p}: not in inventory")
            
        case (p, stock) if stock >= qty:
            inventory[p] -= qty
            print(f"{p}: shipped {qty}, {inventory[p]} left")
            
        case (p, stock):
            print(f"{p}: only {stock} in stock, cannot ship {qty}")