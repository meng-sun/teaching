def dp_populate(i, j, dp_store):
    # case(i,j) =
    #       stay at the same horz length, case(i-j,j)
    #       increase the horz length by 1, case(i-j+1, j-1)

    # we want to swap the direction of the second parameter
    # because right now the base case is a point (1,1) but
    # to find the total number of configurations we have to
    # sum (200,i) for all i in range(2,200)
    # therefore we will let the case recursion be

    # case(i,j) =
    #       stay at the same horz length, case(i-j,j)
    #       increase the horz length by 1, case(i-j-1, j+1)
    # so that the end point is a single evaluation (200,1)
    # and the base cases span (0,i) which is easy to determine

    # base cases
    if (i-j) < 0:
        return 0

    if (i-j,j) in dp_store:
        same_horz = dp_store[(i-j,j)]
    else:
        same_horz = dp_populate(i-j,j, dp_store)
        dp_store[(i-j,j)] = same_horz

    if (i-j-1, j+1) in dp_store:
        diff_horz = dp_store[(i-j-1,j+1)]
    else:
        diff_horz = dp_populate(i-j-1,j+1, dp_store)
        dp_store[(i-j-1,j+1)] = diff_horz

    return same_horz + diff_horz

def solution(n):
    dp_store = {}

    # sanity check
    if (n < 3): return 0

    # base cases
    for i in range(n):
        dp_store[(0,i)] = 1

    no_configurations = 0
    no_configurations = dp_populate(n-1, 1, dp_store)
    

    # remove pole edge case
    no_configurations -= 1

    return no_configurations

print(solution(5))
