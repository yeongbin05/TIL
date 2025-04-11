x, y, w, s = map(int, input().split())
temp = 0
if w * 2 < s:
    print((x + y) * w)

else:
    min_xy = min(x, y)
    temp += min_xy * s

    x -= min_xy
    y -= min_xy

    if (x + y) % 2 == 0:
        temp += (x + y) * min(w, s)
    else:
        temp += (x + y - 1) * min(w, s) + w

    print(temp)
