# Pide al usuario que ingrese los ahorros
savings = input()
print(savings, type(savings))
# Convierte la entrada del usuario en un valor decimal y actualiza la variable
savings = float(savings)
print(savings, type(savings))
# Los ahorros crecen después de 1 año con una tasa de interés anual del 5%
balance = savings * 1.05 
print(balance, type(balance))

# Convierte el saldo en una cadena y actualiza la variable
balance = str(balance)
print(balance, type(balance))
# Concatena las 2 cadenas para producir un mensaje
message = "Amount in 1 year: " + balance

# Muestra el mensaje
print(message, type(message))


#---------------------

