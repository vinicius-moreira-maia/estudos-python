from fpdf import FPDF, Align

def main():
    nome = input("Name: ").strip()

    pdf = FPDF()
    pdf.add_page()

    pdf.image(name = "shirtificate.png", x = Align.C, y = 80.0, w = 180.0)

    pdf.set_font("Helvetica", size = 36)

    # se a margem horizontal é 10, então a vertical será 10 * 3
    pdf.set_xy(10, 30)
    
    # w = 0 significa que a célula ocupa toda a linha
    pdf.cell(w = 0, txt = "CS50 Shirtificate", align = Align.C)

    pdf.set_font("Helvetica", size = 24)
    pdf.set_text_color(255, 255, 255)

    # para não criar nova página automaticamente
    pdf.set_auto_page_break(auto = False)

    # posição em relação à célula anterior (?)
    pdf.set_xy(10, 160)
    pdf.cell(w = 0, txt = f"{nome} took CS50", align = Align.C)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()