import os
from time import sleep
try:
    from colorama import init,Fore

except ModuleNotFoundError:

    print('Instalando colorama...')
    os.system('pip install colorama')
    init(autoreset=True)

def main():
    """
    funciones lambda add, subtract, multiply y divide. Las funciones reciben
    como argumento otra funcion que retorna una lista de 2 numeros ingresados
    por el usuario. Las lambdas descomponen la funcion y ejecutan la operacion
    correspondiente. Exepcion add, esta lambda usa una funcion propia de python
    para sumar lista "sum()"
    """
    add = lambda num: sum(num)
    subtract = lambda num: num[0] - num[1]
    multiply = lambda num: num[0] * num[1]
    text = lambda text: print(f'{Fore.CYAN}{text} numeros ->{Fore.RESET}\n')
    
    def divide(num):

        try:
            return num[0] / num[1]
        
        except ZeroDivisionError:
            return f"{Fore.RED}Error: No se puede dividir entre cero !!!{Fore.RESET}"
    
    def user_numbers() -> list:
        try:
            style = Fore.BLUE
            reset = Fore.RESET
            num_x = float(input(f'{style}Ingrese el primer numero:{reset} '))
            num_y = float(input(f'{style}Ingrese el segundo numero:{reset} '))

            user_numbers = [num_x, num_y]
            return user_numbers

        except ValueError:
            print(f"{Fore.RED}Error: Caracteres invalidos !!!{Fore.RESET}")
            exit()

    def handle_output(result):
        print(f'{Fore.CYAN}Resultado: {result}{Fore.RESET}\n')
    
    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        
        else:
            os.system('clear')
    
    def exit_app(arg=None):
        clear_screen() 
        print('Gracias por Usar Easy Calculator')
        sleep(0.9)
        exit()


    ### Diccionario de opciones ###
    option = {
        '1':add,
        'sumar':add,

        '2':subtract,
        'restar':subtract,

        '3':multiply,
        'multiplicar':multiply,

        '4':divide,
        'dividir':divide
    }

    def user_input_manage():

        ### Get de user input ###
        try:
            user_input = input("Ingrese una opcion: ").lower()

            if user_input == '5' or user_input == 'salir':
                exit_app()
            else:
                function = option[user_input]
                handle_output(function(user_numbers()))

        except KeyError:
            print(f"{Fore.RED}Error: Opcion no disponible !!{Fore.RESET}")
    
    
    ### Executing App ###
    def master():
        
        presentation = Fore.GREEN + '\t.:|Easy Calculator|:.'+Fore.RESET
        menu_options = f'''{Fore.CYAN}
1: sumar                                                                    
2: restar
3: multiplicar
4: dividir
5: salir{Fore.RESET}
        '''
        clear_screen()
        while True:
            print(presentation)
            print(menu_options)
            user_input_manage()
    master()

try:
    main()

except KeyboardInterrupt:
    print(Fore.RED + "\nOperacion cancelada por el usuario"+Fore.RESET)

