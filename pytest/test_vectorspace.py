import numpy as np
import os, sys
sys.path.append('/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1]) + '/groebner')
from vector_space import VectorSpace
from multi_power import MultiPower
from multi_cheb import MultiCheb
import pytest
import pdb

def test_makeBasis():
    f1 = MultiPower(np.array([[0,-1.5,.5],[-1.5,1.5,0],[1,0,0]]))
    f2 = MultiPower(np.array([[0,0,0],[-1,0,1],[0,0,0]]))
    f3 = MultiPower(np.array([[0,-1,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    G = [f1, f2, f3]
    vs = VectorSpace()
    basis = vs.makeBasis(G)
    trueBasis = [(0,0), (1,0), (0,1), (1,1), (0,2)]

    assert (len(basis) == len(trueBasis)) and (m in basis for m in trueBasis), \
            "Failed on MultiPower in 2 vars."

    f1_coeff = np.array([[[0,0,1],[0,3/20,0],[0,0,0]],[[0,0,0],[-3/40,1,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
    f2_coeff = np.array([[[3/16,-5/2,0],[0,3/16,0],[0,0,0]],[[0,0,1],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
    f3_coeff = np.array([[[0,1,1/2],[0,3/40,1],[0,0,0]],[[-1/2,20/3,0],[-3/80,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
    f4_coeff = np.array([[[3/32,-7/5,0,1],[-3/16,83/32,0,0],[0,0,0,0],[0,0,0,0]],[[3/40,-1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], \
                        [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]])
    f5_coeff = np.array([[[5,0,0],[0,0,0],[0,0,0]],[[0,-2,0],[0,0,0],[0,0,0]],[[1,0,0],[0,0,0],[0,0,0]]])
    f6_coeff = np.array([[[0,0,0],[0,0,0],[1,0,0]],[[0,-8/3,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])

    f1 = MultiPower(f1_coeff)
    f2 = MultiPower(f2_coeff)
    f3 = MultiPower(f3_coeff)
    f4 = MultiPower(f4_coeff)
    f5 = MultiPower(f5_coeff)
    f6 = MultiPower(f6_coeff)

    G = [f1, f2, f3, f4, f5, f6]
    basis = vs.makeBasis(G)
    trueBasis = [(0,0,0),(1,0,0),(0,1,0),(1,1,0),(0,0,1),(0,0,2),(1,0,1),(0,1,1)]

    assert (len(basis) == len(trueBasis)) and (m in basis for m in trueBasis), \
            "Failed on MultiPower in 3 vars."
