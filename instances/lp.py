#!/usr/bin/env python3

import math 

if __name__ == '__main__':
    
    N, target = map( int, input().split() )
    P = tuple( map( int, input().split() ) )

    G = [ list( map( int, input().split() ) ) for x in range(N) ]

    print('MIN')
    for i in range(N):
        print('+x_%d' % i , end=' ' )

    print('\nST')

    for i in range(N):
        print('+ %d y_%d' % (P[i], i) , end=' ' )
    print('>= %d' % math.ceil(target * sum(P) / 100) )

    for i in range(N):
        print('y_%d - x_%d' % (i,i) , end = ' ' )
        for j in range(N):
            if( G[i][j] == 1 ):
                print('-x_%d' % j , end=' ' )
        print( '<= 0' )

    print('BIN')
    for i in range(N):
        print('x_%d' % i )
        print('y_%d' % i )

    print('END')
