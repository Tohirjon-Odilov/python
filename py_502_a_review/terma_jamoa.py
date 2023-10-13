def team(score):
    scr, ai, bi = 0, 0, 0
    for i in score:
        a, b = i.split(":")
        a, b = int(a), int(b)
        ai, bi = ai+a, bi+b
        if a > b:
            scr += 3
        elif a == b:
            scr += 1
    print(f"{scr} scores {ai}-{bi}")

team(["3:1","2:2","1:5","4:0"])