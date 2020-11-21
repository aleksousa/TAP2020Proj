#!/usr/bin/env python3

from random import randint as ri
from random import choice as cc
from random import shuffle as ss

import sys

def validate( val, lb, ub ):
    
    try:
        val = int(val)
    except:
        print('%s conversion fail.' % val )
        exit(0)
    
    if val < lb or val > ub:
        print('%d out of bounds.' % val )
        exit(0)

    return val
    

if __name__ == '__main__':
    
    # Help !
    if len( sys.argv ) != 6:
        print( '   *** Usage: %s <num_vertices> <target> <densidy> <min_p> <max_p>' % sys.argv[0] )
        exit(0)

    # Validade each input
    N      = validate( sys.argv[1], 1, 1000 )
    target = validate( sys.argv[2], 1, 100  )
    dens   = validate( sys.argv[3], 1, 100  )
    min_p  = validate( sys.argv[4], 1, 1000 )
    max_p  = validate( sys.argv[5], 1, 1000 )

    # Header
    print( N, target )

    # Number of people in each city
    P = [ str(ri( min_p, max_p)) for i in range(N) ]
    print( ' '.join(P) )

    # The graph
    G = {}
    target_edges = dens * (N*(N-1)//2) // 100

    while len(G) < 2*target_edges:
        x, y = ri( 0, N-1), ri( 0, N-1)
        if not G.get((x,y)): G[ (x,y) ] = G[ (y,x) ] = 1
        
    # Printing the graph
    for i in range(N):
        for j in range(N):
            if j==N-1: print( G.get((i,j),'0'), end = '\n' )
            else     : print( G.get((i,j),'0'), end = ' ' )





