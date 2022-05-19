class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        players_list = [p for p in self.players if player_name == p.name]
        if players_list:
            player = players_list[0]
            player.guild = "Unaffiliated"
            self.players.remove(player)
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        data = ''
        data += f'Guild: {self.name}\n'
        data += '\n'.join([p.player_info() for p in self.players])
        return data
