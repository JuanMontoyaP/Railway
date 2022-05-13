from .pdfreport import PDF

from typing import Dict
from datetime import datetime

def make_report(curve_record : Dict):
    pdf = PDF()
    pdf.set_font(family='Arial', size=12)
    pdf.add_page()
    pdf.identifier(curve_record['curve'], curve_record['thread'], curve_record['date'][:10] ,curve_record['reprofiling'])
    pdf.graphs()
    pdf.output(
        "data/reports/report{}_{}_{}.pdf"
        .format(curve_record['curve'], curve_record["thread"], curve_record["date"][:10])
        )

def main():
    pass

if __name__ == '__main__':
    main()