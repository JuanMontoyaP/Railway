import datahandling.filter as fil

def generate_reports(curve):
    curve_record = fil.filter_curves(curve, [1,2,4], ["curve", "thread", "date"])
    print(curve_record)

def main():
    pass

if __name__ == '__main__':
    main()