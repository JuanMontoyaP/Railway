from graphs.rawgraph import raw_data_graph
from graphs.filtergraph import filter_data_graph

import os

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

    def get_raw_data_graph(self, curve_record):
        graph_dir = "data/figures/raw_curve{}_{}_{}.png".format(curve_record['curve'], curve_record["thread"], curve_record["date"][:10])
        if not os.path.exists(graph_dir):
            raw_data_graph(curve_record)
        return graph_dir

    def print_raw_graph(self, curve_record):
        image = self.get_raw_data_graph(curve_record)
        self.image(image, w=190, h=80, type='PNG')

    def get_filter_data_graph(self, curve_record):
        graph_dir = "data/figures/filter_curve{}_{}_{}.png".format(curve_record['curve'], curve_record["thread"], curve_record["date"][:10])
        if not os.path.exists(graph_dir):
            filter_data_graph(curve_record)
        return graph_dir

    def print_filter_graph(self, curve_record):
        image = self.get_filter_data_graph(curve_record)
        self.image(image, w=190, h=80, type='PNG')

    def graphs(self, curve_record):
        self.set_font('Arial','B',12)
        self.cell(0,10, "2. Gráficos", 0,2,'L')
        self.cell(0,10, "2.1 Raw data", 0,2,'L')
        self.print_raw_graph(curve_record)
        self.cell(0,10, "2.3 Filtro 30 - 100", 0,2,'L')
        self.print_filter_graph(curve_record)