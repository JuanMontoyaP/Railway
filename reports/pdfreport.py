from graphs.rawgraph import raw_data_graph
from graphs.filtergraph import filter_data_graph
from graphs.exceedencegraph import exceedence_data_graph

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

    def get_graph(self, curve_record, graph_type, graph_func):
        graph_dir = "data/figures/{}_curve{}_{}_{}.png".format(graph_type, curve_record['curve'], curve_record["thread"], curve_record["date"][:10])
        if not os.path.exists(graph_dir):
            graph_func(curve_record)
        return graph_dir
    
    def print_graph(self, graph_type, curve_record, w=190, h=80):
        type_of_graphs = {
            "raw": raw_data_graph,
            "filter": filter_data_graph,
            "exc": exceedence_data_graph
            }
        image = self.get_graph(curve_record, graph_type, type_of_graphs[graph_type])
        self.image(image, w=w, h=h, type='PNG')

    def graphs(self, curve_record):
        self.set_font('Arial','B',12)
        self.cell(0,10, "2. Gráficos", 0,2,'L')
        self.cell(0,10, "2.1 Raw data", 0,2,'L')
        self.print_graph("raw", curve_record)
        self.cell(0,10, "2.3 Filtro 30 - 100", 0,2,'L')
        self.print_graph("filter", curve_record)
        self.add_page()
        self.cell(0,10, "2.3. Excedencia.", 0,2,'L')
        self.print_graph("exc", curve_record, w=100, h=100)



