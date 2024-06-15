import pandas as pd
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Monthly Sales Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

class ReportGenerator:
    def __init__(self, data_path):
        self.data_path = data_path

    def generate_summary(self, df):
        total_sales = df['Sales'].sum()
        return f'Total Sales: ${total_sales}\n\n'

    def generate_report(self, output_path='sales_report.pdf'):
        df = pd.read_csv(self.data_path)
        summary = self.generate_summary(df)
        
        pdf = PDF()
        pdf.add_page()
        pdf.chapter_title('Sales Summary')
        pdf.chapter_body(summary)
        
        pdf.output(output_path)
        print(f"Report generated and saved to {output_path}")
