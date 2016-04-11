from numpy import *
import data2
import data
import MILPSolver
MILPSolver.DFSSolver(data2.c,data2.d,data2.A,data2.G,data2.b)
MILPSolver.BFSSolver(data2.c,data2.d,data2.A,data2.G,data2.b)
MILPSolver.BestFirstSolver(data2.c,data2.d,data2.A,data2.G,data2.b)
