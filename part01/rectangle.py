def area(rec1, rec2, rec3):
    x_overlap = overlap(rec1[0], rec1[2], rec2[0], rec2[2], rec3[0], rec3[2])
    y_overlap = overlap(rec1[1], rec1[3], rec2[1], rec2[3], rec3[1], rec3[3])

    if x_overlap > 0 and y_overlap > 0:
        return x_overlap * y_overlap
    else:
        return 0

def overlap(a1, a2, b1, b2, c1, c2):
    return max(0, min(a2, b2, c2) - max(a1, b1, c1))

if __name__ == "__main__":
    rec1 = (-1, 1, 1, -1)
    rec2 = (0, 3, 2, 0)
    rec3 = (0, 2, 3, -2)
    print(area(rec1, rec2, rec3))  # odotettu vastaus on 16
