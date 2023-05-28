from xmlrpc.client import ServerProxy
from threading import Thread

# Conectar al servidor RPC
server = ServerProxy("http://localhost:8000/")

# Obtener el número de player
player = server.get_connection()


def play():
    while True:
        global server, player
        server.reset_choice(player)
        choice = input("Escoge una opción R(Roca), P(Papel) o T(Tijera): ")
        server.send_choice(player, choice)

        result = server.choose_winner(player)
        while result == False:
            result = server.choose_winner(player)

        print(result)
        continua_opcion = input("Quieres seguir jugando? (S/N): ")
        # if continua_opcion.capitalize() == "S":
        #     resultado_continua = server.check_players(player)
            
        #     #Esperamos resultado
        #     while resultado_continua == 0:
        #         resultado_continua = server.check_players(player)

        #     if resultado_continua == False:
        #         break
        if continua_opcion.capitalize() == "N":
            break

            
            


# Hilo
thread = Thread(target=play)
thread.start()
thread.join()