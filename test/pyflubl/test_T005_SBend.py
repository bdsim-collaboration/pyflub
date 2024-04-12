import pyflubl as _pfbl
import numpy as _np

def test_T005_SBend() :
    m = _pfbl.Builder.Machine(bakeTransforms=True)
    m.AddDrift(name="d1", length=1, beampipeMaterial = "G4_STAINLESS-STEEL",
               beampipeRadius=30, beampipeThickness=5)
    m.AddSamplerPlane(name="s1", length=1e-6, samplersize=1)
    m.AddSBend(name="sb1", length=2, angle=_np.pi/4)
    m.AddSamplerPlane(name="s2", length=1e-6, samplersize=1)
    m.AddDrift(name="d2", length=1, beampipeMaterial = "G4_STAINLESS-STEEL",
               beampipeRadius=30, beampipeThickness=5)
    m.Write("T005_SBend")

    return m
