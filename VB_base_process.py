import VB_base_spark_session
import VB_base_objects

positions = "Middle blocker", "Opposite hitter", "Libero", "Setter", "Wing spiker"

while True:
    try:
        player = str(input("Enter the name of volleyball player: "))
    except ValueError:
        print("This is not name")
        continue
    break

print(player)

while True:
    try:
        print("Enter one of those positions: ", positions, " ")
        position = str(input())
        if position not in positions:
            print("This position doesn't exist! Try again: ")
            continue
    except ValueError:
        print("This is not name")
        continue
    break

print(position)

while True:
    try:
        points = int(input("Enter points from all elements: "))
        if points < 0:
            print("The value cannot be minus")
            continue
    except ValueError:
        print("This is not integer")
        continue
    break

print(points)

while True:
    try:
        block_points = int(input("Enter points from blocks: "))
        if block_points < 0:
            print("The value cannot be minus")
            continue
    except ValueError:
        print("This is not integer")
        continue
    break

print(block_points)

while True:
    try:
        aces = int(input("Enter points from serves: "))
        if aces < 0:
            print("The value cannot be minus")
            continue
    except ValueError:
        print("This is not integer")
        continue
    break

print(aces)

while True:
    try:
        spike_points = int(input("Enter points from spikes: "))
        if spike_points < 0:
            print("The value cannot be minus")
            continue
    except ValueError:
        print("This is not integer")
        continue
    break

print(spike_points)

while True:
    try:
        receive = int(input("Enter the percentage value of positive reception: "))
        if receive < 0:
            print("The value cannot be minus")
            continue
    except ValueError:
        print("This is not integer")
        continue
    break

print(receive)

Volleyball_Player = VB_base_objects.Player(player, position, points, block_points, aces, spike_points, receive)
df_update = VB_base_spark_session.df.union(VB_base_spark_session.spark.createDataFrame([Volleyball_Player.row], schema= VB_base_spark_session.vb_schema))
df_update.toPandas().to_csv(VB_base_spark_session.csv_path, index=False)
df_update.show(VB_base_spark_session.rows)