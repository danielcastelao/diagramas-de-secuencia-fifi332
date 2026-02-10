from second import second
class main(second):
    print("main: interaccion")
    second = second()
    respuesta = second.mensaje()
    print("Main: valor retornado ->", respuesta)

if __name__ == "__main__":
    main()
