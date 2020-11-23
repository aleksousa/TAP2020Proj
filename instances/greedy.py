#!/usr/bin/env python3

import math 

# Not in the solution nor covered by someone in the solution
OUT_SOL=0

# Not in solution, but covered by someone in the solution
COVERED=1

# In solution and covering its neighbours
IN_SOL =2

if __name__ == '__main__':
    
    # Read number of vertices and target (percentage)
    N, target = map( int, input().split() )
    
    # Read the number of people in each vertex
    P = tuple( map( int, input().split() ) )

    # Read the graph
    G = [ list( map( int, input().split() ) ) for x in range(N) ]

    # Initializations
    sol = [ OUT_SOL for x in range(N) ]
    acc = 0
    real_target = math.ceil( target * sum(P) / 100 )

    # Main loop (until target is reached)
    while( acc < real_target ):
        
        # The best vertex to put an facility
        best_i = -1
        best_cover = -1

        # Find The best for this iteration (cand=candidate)
        for cand in range(N):
            
            my_value = P[cand] if sol[cand]==OUT_SOL else 0
            
            for viz in range(N):
                if cand == viz: continue
                if G[cand][viz] == 0: continue
                if sol[viz] in (IN_SOL,COVERED): continue
                
                my_value = my_value + P[viz]
            
            if my_value > best_cover:
                best_cover = my_value
                best_i = cand
        
        # Update Best
        sol[ best_i ] = IN_SOL
        acc += best_cover

        # Update covers
        for viz in range(N):
            if best_i == viz: continue
            if G[best_i][viz] == 0: continue
            if sol[viz] in (IN_SOL,COVERED): continue
            
            sol[ viz ] = COVERED

    
    print( sol.count( IN_SOL ) )
    print( ' '.join( map( lambda x: '1' if x==2 else '0' , sol   )   ) )

