resultados = {"Player 1": 0, "Player 2": 0, "Tie": 0}


def juguemos(lista: list):
    for ele in lista:
        if ele[0] == ele[1]:
            resultados["Tie"] += 1
        elif ((ele[0] == "R" and ele[1] == "S") or
              (ele[0] == "S" and ele[1] == "P") or
              (ele[0] == "P" and ele[1] == "R")):
            resultados["Player 1"] += 1
        else:
            resultados["Player 2"] += 1

    if resultados["Player 1"] > resultados["Player 2"]:
        return "Player 1"
    elif resultados["Player 1"] < resultados["Player 2"]:
        return "Player 2"
    else:
        return "Tie"


jugadas = [("R", "S"), ("S", "R"), ("P", "S")]
resultado = juguemos(jugadas)
print("El ganador es:", resultado)
