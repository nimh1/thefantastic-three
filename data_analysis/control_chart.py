import spc
import matplotlib.pyplot as plt


def control_chart():
    x = [25,19,14,17,25,39,49,6,11,19,13,26,24,32,14,19]
    cc = spc.Spc(x, spc.CHART_X_MR_X)
    cc.get_chart()
    plt.show()