
# you sick bastard 
count = lambda x: sum(map(lambda x: 1, x))

# definitions
# n - number of dimensions of a point
# k - number of partitions of whatever



def n_ranges(data):
    return list(
            map(lambda x: ( min(x), max(x) ),
            zip(*data) )
            )

def centroid(data):
    return tuple(
        map(lambda x: x / len(data),
        map(sum,
        zip(*data)
                )
            )
        )

# TODO: note squaring and taking root of the thing 
def distance(p1, p2):
    return sum(
        map(lambda x: (x[1]-x[0])**2, 
        zip(p1, p2)
            )
        )**(1/2)


def map_to_k_space(pt, hypercube, k):
    pt_k = []
    for dim, (min_x, max_x) in enumerate(hypercube):
        interval = ( max_x - min_x  ) / k
        val = int( divmod(pt[dim] - min_x, interval)[0] )
        val = val if val < k else (k-1)
        pt_k.append(val) 
    return tuple(pt_k)








data = [
(1,0,10),
(1,0,0),
(1,0,0),
(1,1,2),
(1,2,2),
(1,2,1),
(2,1,4),
(2,4,3),
(1.5,1.5,2.0),
(1.7,1.11,3.4),
]


average = centroid(data)

# TODO: note squaring and taking root of the thing 
squared_distances = [(i, (distance(average, x))**2) for i, x in enumerate(data)]
# TODO:  proper sequence id?



#ordered_squared_distances = sorted(squared_distances, key=lambda x:x[1], reverse=True)



N = count(data[0])
K = 4 # arbitrary

hypercube = n_ranges(data)

inverse_map = {pt: map_to_k_space(pt, hypercube, K) for pt in data}

bla = list(inverse_map.values()) 

# TODO: make a forward map from k to points

forward_map = {}
for point, point_in_k_space in inverse_map.items():
    x = forward_map.get(point_in_k_space, [])
    x.append(point)
    forward_map[point_in_k_space] = x

density = {kpt: count(pts) for kpt, pts in forward_map.items()}

#sorts = {n : sorted(data, key=lambda x: x[n]) for n in range(N)}






#lookup = dict.fromkeys(data)

