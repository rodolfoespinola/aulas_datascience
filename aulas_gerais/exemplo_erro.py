def dividir(a,b):
    r = 0
    try:
        r = a / b
        return print(r)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    except:
        print("Erro inesperado. Desculpe.")
    finally:
        print("Execução finalizada.")

dividir(4,0)