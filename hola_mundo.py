import os
def main():
    nombre= os.getenv("USERNAME")
    print('!Hola, {nombre} mundo desde github!')

if __name__ == "__main__":
    main()
