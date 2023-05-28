from xmlrpc.server import SimpleXMLRPCServer

class GameServer:
    state_player_one: None
    state_player_two: None
    replay_player_one: bool = False
    replay_player_two: bool = False
    players_in_game: int = 0
    jugadores= {i+1:{"opcion": None, "jugador_en_contra": i+2 if i == 0 else i} for i in range(2)}

    reglas = {
        "RT": {"ganador": 1, "frase" : "roca rompe tijeras"},
        "TR" : {"ganador" : 2, "frase": "roca rompe tijeras"},
        "PT" : {"ganador": 2, "frase" : "tijeras corta papel"},
        "TP": {"ganador": 1, "frase" : "tijeras corta papel"},
        "PR": { "ganador": 1, "frase":"papel cubre roca"},
        "RP" : { "ganador":2, "frase":"papel cubre roca"}
    }

    # #Comprobamos si los jugadores quieren seguir jugando
    # def check_players(self, num_player):
    #     if num_player == 1:
    #         self.replay_player_one = True
    #         self.state_player_one = True
    #     else:
    #         self.replay_player_two = True
    #         self.state_player_two = True

    #     #Checamos si ya seleccionaron si quieren jugar o no
    #     if not all([self.state_player_one, self.state_player_two]):
    #         return 0
        
    #     #Checamos si los 2 jugadores quieren jugar
    #     if self.replay_player_one and self.replay_player_two:
    #         self.state_player_one = self.replay_player_one = False
    #         self.state_player_two = self.replay_player_two = False
    #         return True
            
    #     self.state_player_one = self.replay_player_one = False
    #     self.state_player_two = self.replay_player_two = False

    #     return False
        


    def game_ends(self,num_player):
        self.players_in_game -= 1
        self.players[1]["choice"] = None
        self.players[2]["choice"] = None
        print(f"Jugador {num_player} se ha desconectado")

    # Hace la conexión con el cliente
    def get_connection(self):
        self.players_in_game += 1;
        print("Se ha unido un jugador")
        return self.players_in_game
    
    #Mandamos la elección del jugador al servidor
    def send_choice(self,num_player,choice):
        self.jugadores[num_player]["opcion"] = choice.capitalize()
        print("Se ha mandado su elección")
        return choice

    # Limpiamos la opción del jugador 
    def reset_choice(self, num_player):
        self.jugadores[num_player]["opcion"] = None
        return f"Se limpio la elección del Jugador {num_player}"
    
    # Escogemos al ganador
    def choose_winner(self, num_jugador):
        player_one = self.jugadores[num_jugador]
        player_two = self.jugadores[self.jugadores[num_jugador]['jugador_en_contra']]

        if not all([self.jugadores[1]["opcion"],self.jugadores[2]["opcion"]]):
            return False
        
        if player_one["opcion"] == player_two["opcion"]:
            return "Empate"
    
        return f"{player_one['opcion']}-{player_two['opcion']}: {self.reglas[player_one['opcion']+player_two['opcion']]['frase']} gana el jugador {self.reglas[player_one['opcion']+player_two['opcion']]['ganador']}"
        

        


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(GameServer())
print("Servidor en escucha: ")
server.serve_forever()

