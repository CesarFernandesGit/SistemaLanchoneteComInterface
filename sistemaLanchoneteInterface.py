# SISTEMA DE LANCHONETE QUE ANOTA O PEDIDO E CALCULA O PREÇO DOS ALIMENTOS

import locale
import customtkinter as ctk

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252') 

cardapioAlimentos = ["Cachorro Quente", "Hambúrguer", "Batata Frita", "Pastel"]
cardapioBebidas = ["Suco", "Refrigerante"]
escolhaAdicionar = ["Não", "Sim"]
precoAlimentos = [9.50, 15.00, 8.00, 10.00]
precoBebidas = [5.00, 6.00]
formaPagamento = ["Dinheiro", "Crédito", "Débito", "PIX"]

# CRIANDO A INTERFACE

ctk.set_appearance_mode('System')
app = ctk.CTk()
app.title('Sistema de Lanchonete')
app.geometry('300x300')

ctk.CTkLabel(app, text="Olá! Seja bem-vindo à PyLunch!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
alimento_dropdown = ctk.CTkOptionMenu(app, values=cardapioAlimentos)
alimento_dropdown.pack(pady=5)
quantidade_alimento_entry = ctk.CTkEntry(app, placeholder_text="Quantidade de Alimentos")
quantidade_alimento_entry.pack(pady=5)

bebida_dropdown = ctk.CTkOptionMenu(app, values=cardapioBebidas)
bebida_dropdown.pack(pady=5)
quantidade_bebida_entry = ctk.CTkEntry(app, placeholder_text="Quantidade de Bebidas")
quantidade_bebida_entry.pack(pady=5)

pagamento_dropdown = ctk.CTkOptionMenu(app, values=formaPagamento)
pagamento_dropdown.pack(pady=5)

valor_pago_entry = ctk.CTkEntry(app, placeholder_text="Valor pago(se for dinheiro)")
valor_pago_entry.pack(pady=10)