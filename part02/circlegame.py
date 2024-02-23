def create(n):
    if n == 1:
        return [1]

    circle = list(range(1, n + 1))
    result = []

    index = 0
    while len(circle) > 0:
        index = (index + 1) % len(circle)
        result.append(circle.pop(index))

    return result

def create2(n):
    players = list(range(1, n+1))
    order = []

    i = 0
    while i < len(players):
        if i % 2 == 0:
            players.append(players[i])
        else:
            order.append(players[i])
        i += 1
    return order
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7] [1, 2, 3, 4]
                        # [2, 4, 1, 3]
                        #  