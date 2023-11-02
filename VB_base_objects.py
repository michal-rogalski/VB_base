from pyspark.sql import Row

class Player:
    def __init__(self, player, position, points, block_points, aces, spike_points, receive_percentage):
        self.row = Row(Player=player, Position=position, Points=points, Block_points=block_points, Aces=aces,
                       Spike_points=spike_points, Receive_percentage=receive_percentage)