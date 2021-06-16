import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

'''declare variable'''
data_path = './result/smart_factory_pivot_y.csv'
plot_title = '중소벤처기업부 공식 트위터 스마트공장 언급 빈도 및 비율 변화'
plot_save = './figure/result_figure_y.png'
titlesize = 15
labelsize = 12

'''data load'''
df = pd.read_csv(data_path)
df['True_ratio'] = df['True_ratio'] * 100
# print(df)

'''visualize'''
def plotting(yticks_step, annotation_loca, barwidth):
    # korean font
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

    # declare plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # bar plot of the smart_factory_True
    p1 = ax.bar(x=df['date'], height=df['smart_factory_True'], width=barwidth)

    # x ticks setting
    xticks = df['date'] # declare x ticks
    ax.set_xticks(ticks=xticks) # set x ticks
    ax.set_xticklabels(labels=xticks, rotation=90) # turn x ticks 90 degree

    # seperate second axes
    ax_r = ax.twinx()

    # line plot of the True ratio
    p2 = ax_r.plot(df['date'], df['True_ratio'], color='saddlebrown', lw=2)

    # line plot ticks setting
    ax_r_yticks = np.arange(
        start=math.floor(min(df['True_ratio'])),
        stop=math.ceil(max(df['True_ratio']))+yticks_step,
        step=yticks_step
    ) # declare second y ticks

    # annotate value
    for i in df.index:
        ax_r.text(
            x=df['date'].loc[i],
            y=df['True_ratio'].loc[i]+annotation_loca,
            s=f"{df['True_ratio'].loc[i]:0.0f}%",
            horizontalalignment='center',
            verticalalignment='top',
            fontsize=10,
            color='black'
        )

    ax_r.set_yticks(ticks=ax_r_yticks) # set second y ticks
    ax_r.set_yticklabels([f"{y}%" for y in ax_r_yticks]) # y tick labels formatting


    # set title
    ax.set_title(label=plot_title, size=titlesize)
    # ax.set_xlabel(xlabel='시기')
    ax.set_ylabel(ylabel='언급 횟수', size=labelsize)
    ax_r.set_ylabel(ylabel='전체 트윗 대비 언급 비율', size=labelsize)

    fig.tight_layout()
    plt.savefig(plot_save)
    plt.show()

if data_path[-5] == 'y':
    plotting(yticks_step=0.25, annotation_loca=0.07, barwidth=0.3)

else:
    plotting(yticks_step=5, annotation_loca=1, barwidth=0.8)