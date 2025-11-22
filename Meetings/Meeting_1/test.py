import numpy as np, polyscope as ps
V = np.array([[0.,0.], [1.,0.], [0.,1.]])
F = np.array([[0, 1, 2]])
ps.init()
ps.register_surface_mesh("mesh", V, F)
ps.show()
