

def bucketize(ranges, k):

    intervals = list(
        map(lambda x: (x[1] - x[0]) / k ,
        ranges)
        )

    bla = list(
            map(lambda x: [(x[0][0] + kk*x[1]) for kk in range(k-1)] + [x[0][1]],
        zip(ranges,intervals)))

    return bla 

