# assignment_q2_fixed.py
# Polynomial (cubic) regression fit and plot
# Fixes applied relative to the provided script:
#   1) DESIGN MATRIX: included x^3 term in X (previously stopped at x^2).
#   2) ESTIMATOR: use np.linalg.lstsq for numerical stability (ok for X'X inversion too).
#   3) PREDICTIONS: compute Y_pred = X @ beta (previous code sliced beta and X incorrectly).
#   4) PLOT: show scatter and fitted curve (sorted by x) in one figure.
#   5) COMMENTS: added to explain each step clearly.

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

# Reproducibility
gen = default_rng(1)

N = 500
x = gen.uniform(-3, 3, N)
x.sort()

# True DGP: cubic with noise
Y = -0.4 + (-2)*x + 1.5*(x**2) + 1*(x**3) + 2*gen.standard_normal(N)

# --- Build design matrix up to x^3 and fit OLS ---
I = np.ones((N, 1))
X = np.column_stack((I, x, x**2, x**3))   # include x^3

# beta = (X'X)^(-1) X'Y  # mathematically
# Use lstsq (more stable and handles singular matrices gracefully):
beta, *_ = np.linalg.lstsq(X, Y, rcond=None)

# Fitted values
Y_pred = X @ beta

# --- Plot ---
fig = plt.figure()
plt.scatter(x, Y, label='Data', s=12)
plt.plot(x, Y_pred, label='Fitted cubic')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic polynomial fit via OLS')
plt.legend()
plt.tight_layout()
# If running as a script, show the plot window; when run headless, consider saving.
# plt.show()
fig.savefig('q2_cubic_fit.png', dpi=150, bbox_inches='tight')
print("Estimated beta (b0,b1,b2,b3):", beta)
print("Saved figure: q2_cubic_fit.png")
