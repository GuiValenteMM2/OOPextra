import pandas
from fpdf import FPDF

df = pandas.read_csv("extra/articles.csv", dtype={"id":str})


class Artigo:
    
    def __init__(self, id_artigo):
        self.id_artigo= id_artigo
        self.nome = df.loc[df["id"] == self.id_artigo, "nome"].squeeze()
        self.preco = df.loc[df["id"] == self.id_artigo, "preço"].squeeze()
    
    def estoque(self):
        """Avalia a quantidade de itens disponíveis"""
        disponivel = df.loc[df["id"] == self.id_artigo, "disponivel"].squeeze()
        return disponivel

        
class RegistroVenda:
    def __init__(self, artigo):
        self.artigo = artigo

    def nota(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Este é o recibo nr.{self.artigo.id_artigo}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"O nome do item é {self.artigo.nome}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"O preço do item foi {self.artigo.preco}", ln=1)

        pdf.output("recibo.pdf")
            

print(df)
artigo_escolhido = input("Escolha o ID do seu item: ")
artigo = Artigo(id_artigo=artigo_escolhido)
recibo = RegistroVenda(artigo)
if artigo.estoque():
    recibo = RegistroVenda(artigo)
    recibo.nota() 
else:
    print("Escolha um item válido.")

    
    
        
    
