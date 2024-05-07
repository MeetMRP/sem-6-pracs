from math import atan2

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def sort_by_polar_angle(pivot, points):
    points.sort(key=lambda p: (atan2(p[1] - pivot[1], p[0] - pivot[0]), (p[0] - pivot[0])**2 + (p[1] - pivot[1])**2))

def graham_scan(points):
    if len(points) < 3:
        return points

    points = sorted(points, key=lambda p: (p[1], p[0]))
    pivot = points.pop(0)

    sort_by_polar_angle(pivot, points)

    hull = [pivot, points[0]]

    for point in points[1:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], point) >= 0:
            hull.pop()
        hull.append(point)

    if len(hull) > 1 and hull[0] != hull[-1]:
        hull.append(hull[0])

    return hull

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(points)
print("Convex Hull:", convex_hull)
