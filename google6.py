def odd(a,b):
    return ((a+b)%2 == 1)

def cont_alt(a,b):
    if b > a:
        b -= a
        a *= 2
    elif a > b:
        a -= b
        b *= 2
    return a,b
        
    
def test_pairs_bf(a,b):
    for i in range(10):
        a,b = cont_alt(a,b)
        print ">" + str(a) + " " + str(b)
        if a==b:
            break

    

def test_pairs(a, b):
    # tests for whether pair (a,b) results
    # in an infinite game or not

    # If it sums to an odd number
    # it loop. If it starts out equal it ends.
    # if sums to a power of 2 then it loops
    # otherwise it ends
    
    if ((a+b)%2 == 1):  # if odd
        return True
    elif (a == b):
        return False
    else:
        sum_ab = a+b
        return (sum_ab & (sum_ab - 1) != 0)
        

def solution(banana_list):
    # we don't have to worry about overflows on ints on 32 bit
    # since total bananas for any user is 2^30-1

    n = len(banana_list)

    game_type_all_pairs = [[0 for i in range(n)] for i in range(n)]

    # for all up to O(100^2) pairs, compute whether
    # they result in an infinite game or not
    # (skipping the identity but not dup perms)
    for i in range(n):
        for j in range(n):
            game_type_all_pairs[i][j] += int(test_pairs(banana_list[i],
                                            banana_list[j]))

    for i in range(n):
        print game_type_all_pairs[i]

    # greedymodular to find best pairings
    used_players = set()

    num_ifgm_per_player = [sum(game_type_all_pairs[i]) for i in range(n)]
    order = list(enumerate(num_ifgm_per_player))
    order.sort(key=lambda p:p[1])

    # print order
    # print

    order = [e[0] for e in order]
    count = 0


    while(count < n):
        index = order[count]
        # print used_players
        # print count
        if num_ifgm_per_player[index] == 0:
            count += 1
        else:
            potential_matches = [i for i in range(n) if game_type_all_pairs[index][i] > 0]
            potential_scores = [num_ifgm_per_player[e] for e in potential_matches]

            # print "---------------"
            # print potential_matches
            # print potential_scores
            # print "---------------"

            tmp = zip(potential_matches, potential_scores)
            tmp.sort(key = lambda p:p[1])
            smallest_match_index, smallest_score = tmp[[e[1] for e in tmp].rindex(0) + 1]

            # first_nonzero = 0
            # while potential_scores[first_nonzero] == 0:
            #     first_nonzero += 1
            # smallest_match_index = potential_matches[first_nonzero]
            # smallest_score = potential_scores[first_nonzero]
            # for i in range(first_nonzero+1, len(potential_matches)):
            #     if (potential_scores[i] != 0) and (smallest_score > potential_scores[i]):
            #         smallest_match_index = potential_matches[i]
            #         smallest_Score = potential_scores[i]

            # print ">matched " + str(index) + " " + str(smallest_match_index)
            # pair these two and update everything
            used_players.add(index)
            used_players.add(smallest_match_index)
            # print game_type_all_pairs
            for j in range(n):
                if (game_type_all_pairs[index][j] > 0):
                    game_type_all_pairs[index][j] -= 1
                    num_ifgm_per_player[index] -= 1
                if (game_type_all_pairs[j][index] > 0):
                    num_ifgm_per_player[j] -= 1
                    game_type_all_pairs[j][index] -= 1
                if (game_type_all_pairs[smallest_match_index][j] > 0):
                    game_type_all_pairs[smallest_match_index][j] -= 1
                    num_ifgm_per_player[smallest_match_index] -= 1
                if (game_type_all_pairs[j][smallest_match_index] > 0):
                    num_ifgm_per_player[j] -= 1
                    game_type_all_pairs[j][smallest_match_index] -= 1
                print game_type_all_pairs
    # print used_players
    # print count
    return n-len(used_players)

# print(test_pairs(1,4))
# print(test_pairs(3,5))
# print(test_pairs(3,7))
# print(test_pairs(1,13))
# print(test_pairs(1,15))

print(solution([1,7,3,21,13,19]))
# print(solution([1,1, 2, 2]))
