from numpy import *
import FacilityData
import MILPSolver
MILPSolver.DFSSolver(FacilityData.c,FacilityData.d,FacilityData.A,FacilityData.G,FacilityData.b)
MILPSolver.BFSSolver(FacilityData.c,FacilityData.d,FacilityData.A,FacilityData.G,FacilityData.b)
MILPSolver.BestFirstSolver(FacilityData.c,FacilityData.d,FacilityData.A,FacilityData.G,FacilityData.b)
