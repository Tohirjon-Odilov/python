def func(S, N, P, M, Q):
    natija = []
    summa = S

    for i in range(N):
        for j in range(M):
            if P[i] == Q[j]:
                natija.append(P[i])
                summa -= P[i]
                break

    if summa != 0:
        print("Impossible")
        return

    for i in range(N):
        if P[i] not in natija:
            natija.append(P[i])

    for i in range(M):
        if Q[i] not in natija:
            natija.append(Q[i])

    print(' '.join([f"+{nominal}" if nominal > 0 else f"{nominal}" for nominal in natija]))


# Test kodi
func(10, 3, [3, 9, 14], 2, [6, 2])
