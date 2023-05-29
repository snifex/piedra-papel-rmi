from xmlrpc.client import ServerProxy
from threading import Thread

# Conectar al servidor RPC
server = ServerProxy("http://localhost:8000/")

# Obtener el número de player
num_player = server.get_connection()


def play():
    while True:
        global server, num_player
        server.reset_choice(num_player)
        choice = input("Escoge una opción R(Roca), P(Papel) o T(Tijera): ").capitalize()

        while choice not in ["R", "P", "T"]:
            choice = input("Escoge una opción valida R(Roca), P(Papel) o T(Tijera): ").capitalize()

        server.send_choice(num_player, choice)

        result = server.choose_winner(num_player)
        while result == False:
            result = server.choose_winner(num_player)

        print(result)
        continua_opcion = input("Quieres seguir jugando? (S/N): ").capitalize()
        if continua_opcion == "N":
            server.game_ends(num_player)
            break
        
    

# Hilo
thread = Thread(target=play)
thread.start()
thread.join()