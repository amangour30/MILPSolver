from numpy import *
import FacilityData
import MILPSolverVarSel

MILPSolverVarSel.DFSSolver(FacilityData.c,FacilityData.d,FacilityData.A,FacilityData.G,FacilityData.b)
# MIPSSolverVarSel.BFSSolver(FacilityData.c,FacilityData.d,FacilityData.A,FacilityData.G,FacilityData.b)
# MIPSSolverVarSel.BestFirstSolver(FacilityData.c,FacilityData.d,FacilityData.A,FacilityData.G,FacilityData.b)
