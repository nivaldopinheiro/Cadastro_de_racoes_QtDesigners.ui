#!/usr/bin/env python
# coding: utf-8

# Texto explicativo do que vou fazer no meu código

# In[6]:


# Para criação do código de barras
from barcode import EAN13
from barcode.writer import ImageWriter
codigo_barra = EAN13 ("123456789123", writer=ImageWriter())
codigo_barra.save("codigo_barra")


# In[1]:


# para inserir um controle das rações recebidas
codigos_produtos = {
    "Racao A":"123456789123",# código com doze caracteres da ração doada onde o "A" é a marca ou tipo
    "Racao B":"234567891234",
    "Racao C":"345678912345",
    "Racao D":"456789123456"}

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    codigo_barra = EAN13 (codigo, writer=ImageWriter())
    codigo_barra.save(f"codigo_barra_{produto}")


# In[23]:


# Para criação do QRcode
import qrcode
imagem_qrcode = qrcode.make("https://share.streamlit.io/maos-por-patas/movimento/main")
imagem_qrcode.save("qrcode_python.png")


# In[ ]:




