from typing import List

from fpdf import FPDF

class PDF(FPDF):
    
    def __init__(self, orientation='P',unit='mm',format='A4'):
        super().__init__(orientation, unit, format)

    def identifier(self, curve: int, thread: str, date: str, reprofiling: str):
        self.set_font('Arial','B',12)
        self.cell(0,10,'Informe CAT Curva {}'.format(curve),0,2,'C')
        self.cell(0,10, "1. Identificación", 0,2,'L')
        self.set_font('Arial','',12)
        self.cell(0,10, "Curva: {}".format(curve), 0,2,'L')
        self.cell(0,10, "Hilo: {}".format(thread), 0,2,'L')
        self.cell(0,10, "Fecha: {}".format(date), 0,2,'L')
        self.cell(0,10, "Reperfilado: {}".format(reprofiling), 0,2,'L')

    def graphs(self):
        self.set_font('Arial','B',12)
        self.cell(0,10, "2. Gráficos", 0,2,'L')
        self.cell(0,10, "2.1 Raw data", 0,2,'L')
        