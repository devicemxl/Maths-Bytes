from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
# 
P = set(['A', 'B', 'C', 'D',])
I = set(['D', 'E'])
N = set(['D', 'F', 'G'])
v=venn3_circles(subsets = [P, I, N],#subs,
    linestyle='dashed',
    linewidth=1,
    alpha = 0.5,
    color="grey")
c = venn3(
    subsets = [P, I, N],#subs,
    set_labels = ('Conjunto P', 'Conjunto I', 'Conjunto N'),)
c.hide_zeroes
# Lo que hay entre de A, B y C juntos
if c.get_label_by_id('111') != None: c.get_label_by_id('111').set_text( 'INT')
#
plt.show()
