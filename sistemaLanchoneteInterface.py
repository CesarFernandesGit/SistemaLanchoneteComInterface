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

ctk.set_appearance_mode("System")
app = ctk.CTk()
app.title("Sistema de Lanchonete")
app.geometry("300x200")

fonte = ctk.CTkFont(size=20, weight="bold")
label_titulo = ctk.CTkLabel(app, text="Olá! Seja bem-vindo à PyLunch!", font=fonte)
label_titulo.pack(pady=int(10))

alimento_dropdown = ctk.CTkOptionMenu(app, values=cardapioAlimentos)
alimento_dropdown.pack(pady=int(5))
quantidade_alimento_entry = ctk.CTkEntry(app, placeholder_text="Quantidade de Alimentos")
quantidade_alimento_entry.pack(pady=Int(5))

bebida_dropdown = ctk.CTkOptionMenu(app, values=cardapioBebidas)
bebida_dropdown.pack(pady=5)
quantidade_bebida_entry = ctk.CTkEntry(app, placeholder_text="Quantidade de Bebidas")
quantidade_bebida_entry.pack(pady=int(5))

pagamento_dropdown = ctk.CTkOptionMenu(app, values=formaPagamento)
pagamento_dropdown.pack(pady=int(5))

valor_pago_entry = ctk.CTkEntry(app, placeholder_text="Valor pago(se for dinheiro)")
valor_pago_entry.pack(pady=int(10))

resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=int(10))

def calcular():
    try:
        alimento = alimento_dropdown.get()
        bebida = bebida_dropdown.get()
        forma_pagamento = pagamento_dropdown.get()

        qtd_alimento = int(quantidade_alimento_entry.get())
        qtd_bebida = int(quantidade_bebida_entry.get())

        idx_alimento = cardapioAlimentos.index(alimento)
        idx_bebida = cardapioBebidas.index(bebida)

        total_alimento = precoAlimentos[idx_alimento] * qtd_alimento
        total_bebida = precoBebidas[idx_bebida] * qtd_bebida
        total = total_alimento + total_bebida

        resumo = f"{qtd_alimento}x {alimento} = {locale.currency(total_alimento, grouping=True)}\n"
        resumo += f"{qtd_bebida}x {bebida} = {locale.currency(total_bebida, grouping=True)}\n"
        resumo += f"Total: {locale.currency(total, grouping=True)}\n"

        if forma_pagamento == "Dinheiro":
            valor_pago = float(valor_pago_entry.get())
            if valor_pago < total:
                resumo += "Valor Insuficiente!"
            else:
                troco = valor_pago - total
                resumo += f"Troco: {locale.currency(troco, grouping=(True))}"
        else:
            resumo += f"Pagamento via {forma_pagamento} confirmado."

        resultado_label.configure(text=resumo)
    except:
        resultado_label.configure(text="Erro no preenchimento. Por favor, verifique os dados e tente novamente.")

botao_calcular = ctk.CTkButton(app, text="Calcular Pedido", command=calcular)
botao_calcular.pack(pady=10)

app.mainloop()