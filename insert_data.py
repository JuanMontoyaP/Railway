from functions.functions import user_input

def input_thread() -> str:
    
    rail_thread = input("Insert the rail thread: ").upper()


    return rail_thread

def insert_data():
    data = {}
    data["Curve"] = user_input(int, "Insert the curve: ")
    data["thread"] = input_thread()
    print(data)

def main():
    insert_data()

if __name__ == '__main__':
    main()