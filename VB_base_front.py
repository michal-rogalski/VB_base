import VB_base_spark_session
from tkinter import Tk, Label, Button, Toplevel

#
root = Tk()
root.title('VB_base')
root.geometry('600x400')

VB_base_spark_session.df_vb.createOrReplaceTempView('FullView')
elements = "Points", 'BlockPoints', 'Aces', 'SpikePoints', 'Receive'

all_rows = VB_base_spark_session.df_vb.count()

welcome ="""Welcome to Plusliga Database.
This is Database of volleyball players played in season 2022/2023
"""

VB_base_label = Label(root, text=welcome, font=30, fg="blue")
VB_base_label.pack()

#1. Show all statistics
def Show_all_stats():
    VB_base_spark_session.df_vb.show(all_rows)

Button_Show_all_statistics = Button(root, text="Show all statistics", width=20, command=Show_all_stats)

Button_Show_all_statistics.pack()

#2. Add new player
def Add_new_player():
    import VB_base_process

Button_Add_new_player = Button(root, text="Add new player", width=20, command=Add_new_player)

Button_Add_new_player.pack()

#3. Show all players from one position


def Show_all_players_from_one_position_window():

    #Showing new window
    New_window = Toplevel(root)
    New_window.title('Show all players from one position window')
    New_window.geometry('600x400')

    #Buttons with commands
    Middle_blocker = Button(New_window, text="Middle blocker", width=20, command=lambda: VB_base_spark_session.Choose_position("Middle blocker"))
    Libero = Button(New_window, text="Libero", width=20, command=lambda: VB_base_spark_session.Choose_position("Libero"))
    Opposite_hitter = Button(New_window, text="Opposite hitter", width=20, command=lambda: VB_base_spark_session.Choose_position("Opposite hitter"))
    Wing_spiker = Button(New_window, text="Wing spiker", width=20, command=lambda: VB_base_spark_session.Choose_position("Wing spiker"))
    Setter = Button(New_window, text="Setter", width=20,
                         command=lambda: VB_base_spark_session.Choose_position("Setter"))

    #Placing buttons
    Middle_blocker.pack()
    Libero.pack()
    Opposite_hitter.pack()
    Wing_spiker.pack()
    Setter.pack()


Show_all_players_from_one_position_button = Button(root, text="Show all players from one position", command=Show_all_players_from_one_position_window)
Show_all_players_from_one_position_button.pack()

#4. Showing best players from specific elements

def Show_best_players_from_specific_elements_window():
    # Showing new window
    New_window = Toplevel(root)
    New_window.title('Show best players from specific elements window')
    New_window.geometry('600x400')

    # Buttons with commands
    Points = Button(New_window, text="Points", width=20,
                            command=lambda: VB_base_spark_session.Choose_element("Points"))
    Block_Points = Button(New_window, text="Block Points", width=20,
                    command=lambda: VB_base_spark_session.Choose_element("BlockPoints"))
    Aces = Button(New_window, text="Aces", width=20,
                         command=lambda: VB_base_spark_session.Choose_element("Aces"))
    Spike_Points = Button(New_window, text="Spike Points", width=20,
                         command=lambda: VB_base_spark_session.Choose_element("SpikePoints"))
    Receive = Button(New_window, text="Receive", width=20,
                    command=lambda: VB_base_spark_session.Choose_element("Receive"))

    # Placing buttons
    Points.pack()
    Block_Points.pack()
    Aces.pack()
    Spike_Points.pack()
    Receive.pack()


Show_best_players_from_specific_elements_button = Button(root, text="Show best players from specific elements window",
                                                   command=Show_best_players_from_specific_elements_window)
Show_best_players_from_specific_elements_button.pack()

#5. Show one player
def Show_one_player():

    player1 = input("Choose player: ")
    sql_sequence = f"SELECT * FROM FullView WHERE Player = '{player1}'"
    One_Player = VB_base_spark_session.spark.sql(sql_sequence)
    One_Player.show()

Show_one_player_button = Button(root, text="Show one player", command=Show_one_player)
Show_one_player_button.pack()

#6. Own filters
def Own_filters():
    Filters_Possibility = []
    while len(Filters_Possibility)<6:

        print("Choose one of those filters: ", elements, "or write END if you want to go back to our menu.")
        Choosing_Filters = input("Choose your filters: ")
        if Choosing_Filters == "END":
            break

        elif Choosing_Filters not in elements or Choosing_Filters in Filters_Possibility:
            print("Wrong header's name or you actually chose it. Try again!")
            continue
        else:
            Filters_Possibility.append(Choosing_Filters)
            Own_Filters = VB_base_spark_session.df_vb.select(Filters_Possibility)
            Own_Filters.show(all_rows)

Own_filters_button = Button(root, text="Choose your filters", command=Own_filters)
Own_filters_button.pack()

#7 Ending button
def close_vb_base_app():
    root.destroy()

Close_button = Button(root, text="Close", command=close_vb_base_app)
Close_button.pack()

root.mainloop()