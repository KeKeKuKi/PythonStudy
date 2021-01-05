'''
介绍

Matplotlib 可能是 Python 2D-绘图领域使用最广泛的套件。
它能让使用者很轻松地将数据图形化，并且提供多样化的输出格式。

IPython 以及 pylab 模式
IPython 是 Python 的一个增强版本。它在下列方面有所增强：
命名输入输出、使用系统命令（shell commands）、排错（debug）能力。
我们在命令行终端给 IPython 加上参数 -pylab （0.12 以后的版本是 --pylab）之后，
就可以像 Matlab 或者 Mathematica 那样以交互的方式绘图。
pylab
pylab 是 matplotlib 面向对象绘图库的一个接口。
它的语法和 Matlab 十分相近。
也就是说，它主要的绘图命令和 Matlab 对应的命令有相似的参数。
'''
#  初级绘制
# 这一节中，我们将从简到繁：先尝试用默认配置在同一张图上绘制正弦和余弦函数图像，然后逐步美化它。
# 第一步，是取得正弦函数和余弦函数的值：
from pylab import *

# X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。
# C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X), np.sin(X)
'''
 使用默认配置[源码文件]
Matplotlib 的默认配置都允许用户自定义。
你可以调整大多数的默认配置：图片大小和分辨率（dpi）、
线宽、颜色、风格、坐标轴、坐标轴以及网格的属性、文字与字体属性等。
不过，matplotlib 的默认配置在大多数情况下已经做得足够好，
你可能只在很少的情况下才会想更改这些默认配置。
'''
# plt.plot(X, C)
# plt.plot(X, S)
# plt.show()


# 下面的代码中，我们展现了 matplotlib 的默认配置并辅以注释说明，这部分配置包含了有关绘图样式的所有配置。代码中的配置与默认配置完全相同，你可以在交互模式中修改其中的值来观察效果。
# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)
# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C, S = np.cos(X), np.sin(X)
# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
# linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# 我们在图的左上角添加一个图例。为此，我们只需要在 plot 函数里以「键 - 值」的形式增加一个参数。
plot(X, C, color="blue", linewidth=1.5, linestyle="--", label="cos")
# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.5, linestyle="-", label="sin")

legend(loc='upper left')
# 设置横轴的上下限
xlim(-4.0, 4.0)
# 设置纵轴的上下限
ylim(-1.1, 1.1)

# # 设置横轴记号
# xticks(np.linspace(-4, 4, 9, endpoint=True))
# # 设置纵轴记号
# yticks(np.linspace(-1, 1, 5, endpoint=True))

xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)
# 在屏幕上显示

'''
移动脊柱[源码文件]
坐标轴线和上面的记号连在一起就形成了脊柱（Spines，一条线段上有一系列的凸起，是不是很像脊柱骨啊~），
它记录了数据区域的范围。它们可以放在任意位置，不过至今为止，我们都把它放在图的四边。
实际上每幅图有四条脊柱（上下左右），为了将脊柱放在图的中间，我们必须将其中的两条（上和右）
设置为无色，然后调整剩下的两条到合适的位置——数据空间的 0 点。
'''
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

'''
我们希望在 2π/3 的位置给两条函数曲线加上一个注释。
首先，我们在对应的函数图像位置上画一个点；
然后，向横轴引一条垂线，以虚线标记；最后，写上标签。
'''
t = 2*np.pi/3
plot([t, t], [0,np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
scatter([t, ], [np.cos(t), ], 50, color ='blue')

annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plot([t, t], [0,np.sin(t)], color='red', linewidth=2.5, linestyle="--")
scatter([t, ], [np.sin(t), ], 50, color='red')

annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

'''
坐标轴上的记号标签被曲线挡住了，作为强迫症患者（雾）这是不能忍的。
我们可以把它们放大，然后添加一个白色的半透明底色。这样可以保证标签和曲线同时可见。
'''
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

show()
