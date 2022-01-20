from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
#
P = set(['A', 'B', 'C', 'D',])
I = set(['D', 'E', 'F'])
CA = list(P).copy()
CA.extend( set(I).intersection(set(I)) )
N = set(list(CA))
v=venn3_circles(subsets = [P, I, N],#subs,
    linestyle='dashed',
    linewidth=1,
    alpha = 0.5,
    color="grey")
c = venn3(
    subsets = [P, I, N],#subs,
    set_labels = ('Conjunto P', 'Conjunto I', 'Conjunto N'),)
c.hide_zeroes
#
plt.show()
