from xmlrpc.server import SimpleXMLRPCServer

class GameServer:
    state_player_one: bool= False
    state_player_two: bool = False
    players_in_game: int = 0
    jugadores= {i+1:{"opcion": None, "jugador_en_contra": i+2 if i == 0 else i} for i in range(2)}

    opciones = {
        "R": "Roca",
        "P": "Papel",
        "T": "Tijeras"
    }

    reglas = {
        "RT": "roca rompe tijeras",
        "TP": "papel cubre roca",
        "PR": "papel es cortado por tijeras"
    }

    def reset_play(self,num_player):
        if num_player == 1:
            self.state_player_one = True
        else:
            self.state_player_two = True

        if self.state_player_one and self.state_player_two:
            self.jugadores[1]["opcion"]  = None
            self.jugadores[2]["opcion"]  = None

            #Si se resetearon ambos jugadores
            return True

        # Sí solo un jugador reseteó
        return False

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
    
    #Escogemos al ganador
    def choose_winner(self, num_jugador):
        player_one = self.jugadores[num_jugador]
        player_two = self.jugadores[self.jugadores[num_jugador]['jugador_en_contra']]
        
        if not all([self.jugadores[1]["opcion"],self.jugadores[2]["opcion"]]):
            return False
        
        if player_one["opcion"] == player_two["opcion"]:
            return "Empate"

        if player_one["opcion"] + player_two["opcion"]:
            return f"{self.opciones[player_one['opcion']]}-{self.opciones[player_two['opcion']]} {self.reglas[player_one['opcion'] + player_two['opcion']]} gana el jugador2"

        return f"{self.opciones[player_two['opcion']]}-{self.opciones[player_one['opcion']]} {self.reglas[player_two['opcion']+player_one['opcion']]} gana el jugador1"
        

        


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(GameServer())
print("Servidor en escucha: ")
server.serve_forever()

