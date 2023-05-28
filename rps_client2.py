from xmlrpc.client import ServerProxy
import threading

def play_game(server):
    player2_choice = input("Jugador 2, elige Roca (R), Papel (P) o Tijeras (T): ")
    result = server.play("", player2_choice)
    print(result)

server = ServerProxy("http://localhost:8000/")
thread = threading.Thread(target=play_game, args=(server,))
thread.start()
thread.join()
