# Day_02_02_matplotlib.colormap.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_1():
    x = np.random.rand(100)
    y = np.random.rand(100)
    t = np.arange(100)


    # plt.plot(x, y, 'ro')
    # plt.scatter(x, y)       # 점의 option을 주기 쉽다
    plt.scatter(x, y, c=t)      # 데이터의 개수와 c의 개수가 같아야 한다.
    plt.show()

def plot_2():
    # x = np.random.rand(100)
    x = np.arange(100)
    y = t = x

    # plt.plot(x, y, 'ro')
    # plt.scatter(x, y)       # 점의 option을 주기 쉽다
    # plt.scatter(x, -y, c=t, cmap = 'jet')      # 데이터의 개수와 c의 개수가 같아야 한다.
    # plt.scatter(x, -y, c=t, cmap = 'viridis')      # 데이터의 개수와 c의 개수가 같아야 한다.
    plt.scatter(x, -y, c=cm.viridis(0))
    plt.scatter(x, -y, c=[cm.viridis(0)]*50 + [cm.viridis(255)]*50)
    # color map은 색을 다채롭게 쓸 수 있는 방법
    plt.show()


print(plt.colormaps())
# ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Vega10', 'Vega10_r', 'Vega20', 'Vega20_r', 'Vega20b', 'Vega20b_r', 'Vega20c', 'Vega20c_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spectral', 'spectral_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
print(len(plt.colormaps()))     # 168개 있음


jet = cm.get_cmap('jet')        # red green yellow alpha(투명도)

print(jet(-10))
print(jet(0))           # 0~255범위에서 섞어서 만들어서 색을 만듬
print(jet(255))
print(jet(256))
print(jet(1.0))         # 정수와 실수로 줄수 있고. 1.0 은 255와 같다.
print('-' * 50)

print(jet(127))         # 아래는 같은 값
print(jet(127/255))
print('-' * 50)

# 문제
# jet에서 8가지 색상을 뽑아주세요.
print(jet([0, 255]))        # 배열로 뽑아 줌

print(jet(range(0, 256, 32)))
print(jet(np.linspace(0,  1, 8)))







