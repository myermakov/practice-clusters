# this is likely out of date
# TODO: recover the rest

def mean(vec):
    return sum(vec) / len(vec)

def sum_of_squares(vec):
    return sum([x**2 for x in vec])

def variance(vec, mean):
    return sum([(x-mean)**2 for x in vec])

def residuals(vec, mean):
    rated = [(x, (x-mean)**2) for x in vec]
    return sorted(rated, reverse=True, key=lambda x: x[1])


#def partition_my_data(data, k=3):
    # step 1: sort!
    #variance1 = variance(data1, mean1)
    #@variance2 = variance(data2, mean2)

    # quantity to minimize
    #sum_of_variances = variance1 + variance2

     

k=3
data = sorted([
    1,2,3,4,5,\
    1,2,3,4,5,\
    1,2,3,4,5,\
    1,2,3,4,5,\
    1,2,3,4,5,\
    1,2,3,4 \
        ])
l = len(data)

point_progress = [(i, i/(l-1)) for i in range(l)]
split_progress = [(j, (1/k)*i,  (1/k) * j) for i, j in zip(range(0,k),range(1,k+1))]


# TODO map point progress to its bin
mymap = {}
for i, ext in point_progress:
    x = list(filter(lambda tup: tup[1] <= ext <= tup[2], split_progress))
    #print(f"pt {i} goes to {x}")
    mymap.update({i:x[0][0]}) 

print(mymap)

#if __name__ == '__main__':
#    sl = partition_my_data(data)





#TODO: closures maybe? 

lcmp = lambda l,x,h: l <= x < h
lrcmp = lambda l,x,h: l <= x <= h

def compare(strip, k):
    
    if k_x < (k-1)
        use lcmp
    else:
        use lrcmp




    

#    for every partition
#        compute mean
#        compute variance
#        compute rated residuals
#        pluck out greatest value and recalculate mean, variance
#        record delta variance 
#    sum original variances
#    select the value whose absence decreases variance of its partition the most
#    move it over to the closest cluster
#    recalculate that clusters  variance
#    sum all variances after swap
#
#    compare before and after sum of variances
#    sum decreased - great. commit the change, rinse and repeat
#    if it increased - sucks.
#        you just moved over a point thats better off in the old cluster
#        what does it mean?
#            old cluster will surely decrease it SOV (one less point to care about!)
#            new cluster increased its SOV way more than old clstr decreased it
#            what does it mean?
#                its mean is farther away from the old clusters mean
#                rightly so? yes -> it was a wrong move indeed
#                            no -> mean of the receiving cluster is swamped with some other dirty values, 
#                                it appears that adding it makes things worse
#                                
#                                guess we need to go to another high rated point(different cluster) and repeat with that one
#
#            if nothing was moved after all the highest rated pts in its cluster were traversed, we are at a local minimum
#                which sucks.
#            if something was moved, repeat the process,
#






