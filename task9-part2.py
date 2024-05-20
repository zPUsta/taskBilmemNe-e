points = [5, 3, 4, 2, 1, 6]
places = [0] * len(points)
print(places)

for order, point in enumerate(sorted(points, reverse=True), 1):
    print("bal:", point, "index:",points.index(point), "sira;", order)
    places[points.index(point)] = f"{order}-ci"

print(places)




