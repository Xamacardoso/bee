def main():
    while True:
        try:
            string = input();
            maiuscula = True;
            copy = "";
            for carac in string:
                if (carac.isalpha()):
                    copy += carac.upper() if maiuscula else carac.lower();
                    maiuscula = not maiuscula;
                else:
                    copy += carac;


            print(copy);
        except EOFError:
            break;

main();