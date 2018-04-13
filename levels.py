# Levels in this file are property of Sen Games Studio, https://www.sengamesstudio.com/

# Tiles
blank = "."
wall = "W"
water = "~"
ice = "I"
dirt = "G"    # The which the fox can step on only once.
portal = "@"  # The ending point of the animals. Not to be confused with teleporters.
telep = "%"

# Animals
yak = "y"
fox = "f"
duck = "d"

# The following levels are taken from Woodways game.
# Levels are written in ascii, see legend above.
# Animals and teleporters are in separate lists.
board_27 = ["~~G~~~",
            "W.II~@",
            "~.II.@",
            "W.IIG@",
            "...~~~"]

animals_27 = [[fox, (1,1)], [duck, (2, 1)], [yak, (3, 1)]]

board_30 = [".I.I.",
            "GIIIG",
            "@IIIG",
            "~@.@~"]

animals_30 = [[fox, (3,1)], [yak, (3,2)], [duck, (3,3)]]

board_32 = ["..@~@",
            "~W.~~",
            "...@~",
            ".W.~~",
            ".~.~~"]

animals_32 = [[yak, (0,0)], [fox, (2,0)], [duck, (4,0)]]

board_37 = ["~G.~~",
            "~@.@~",
            ".III.",
            ".IWI.",
            "~.@.~",
            "~...~",
            "~~~~~"]

animals_37 = [[ fox ,  (0,2)], [duck, (1,2)], [yak, (2,2)]]

board_39 = ["~~W..",
            "@G@..",
            "GIIII",
            "@W@~I",
            "GG..."]

animals_39 = [[ fox ,  (1,1)], [yak, (1,3)], [duck, (1,2)], [duck, (4,2)]]

board_43 = ["~~@~~",
            "~~W~~",
            "..@..",
            "~~W~~",
            "~~@~~"]

animals_43 = [[duck, (2,1)], [fox, (2,2)], [duck, (2,3)]]
teleports_43 = {(2,0):(2,4), (2,4):(2,0)}

board_45 = ["~@~@~",
            "@.@..",
            ".~.~.",
            ".~W~.",
            "~~~~~~"]
animals_45 = [[fox, (1,1)], [duck,(1,2)], [yak,(1,3)], [duck, (0,3)]]
teleports_45 = {(2,0):(2,4),(2,4):(2,0)}
