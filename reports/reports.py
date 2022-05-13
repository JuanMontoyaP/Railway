import datahandling.filter as fil
from .makereport import make_report

def generate_reports(curve):
    curve_record = fil.filter_curves(curve, [1,2,4], ["curve", "thread", "date"])
    make_report(curve_record[0])

def main():
    pass

if __name__ == '__main__':
    main()