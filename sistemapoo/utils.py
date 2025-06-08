from banco import conexao
from reportlab.pdfgen import canvas

def gerar_pdf():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos;")
    dados = cursor.fetchall()
    cursor.close()

    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "NOME")
    pdf.drawString(210, 750, "VALOR")
    pdf.drawString(310, 750, "QUANTIDADE")

    for produto in dados:
        y += 50
        pdf.drawString(10, 750 - y, str(produto[0]))
        pdf.drawString(110, 750 - y, str(produto[1]))
        pdf.drawString(210, 750 - y, str(produto[2]))
        pdf.drawString(310, 750 - y, str(produto[3]))

    pdf.save()
    print("PDF gerado com sucesso!")
