from fpdf import FPDF, Align
import webbrowser

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", x=Align.C, y=80, w=200, h=200)
        self.set_font(family="Times", style="B", size=45)
        self.ln(30)
        self.cell(w=40, text="CS50 SHIRTIFICATE", center=True, align="C")

def main():
    user_input = input("Name: ").strip()
    pdf = PDF()
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=25)
    pdf.ln(100)
    pdf.set_text_color(255,255,255)
    pdf.cell(w=50, text=user_input, center=True, align="C")
    pdf.output("test.pdf")
    # webbrowser.open("test.pdf")


if __name__ == "__main__":
    main()