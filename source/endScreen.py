players = {"Alice": 23, "Bob": 25, "Charlie": 30, "David": 18, "Eva": 27}



def endScreen(players):
    import tkinter as tk
    #Create window and greeting 
    window = tk.Tk()
    window.geometry("500x500")
    greeting = tk.Label(text="Good Game! Here's the results:")
    greeting.configure(font=("Calibri", 30), fg="green")
    greeting.pack(pady=50)
    #Create list of players and scores
    player_list = tk.Listbox(window, width=50, font=("Calibri", 24), fg="gold")
    player_list.pack(pady=20)

    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)

    for player, score in sorted_players:
        player_list.insert(tk.END, f"{player}: {score}")

    window.mainloop()

endScreen(players)