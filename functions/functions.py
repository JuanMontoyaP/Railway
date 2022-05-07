
def print_line(length: int = 70):
    print(length*"=")

def print_message(msg: str, end: str ='\n'):
    print(msg, end=end)

def user_input(function, msg: str):
    while True:
        value = input(msg)
        try :
            value = function(value)
            break
        except ValueError:
            print("Insert a valid value")
            pass
    return value

def main():
    pass

if __name__ == '__main__':
    main()