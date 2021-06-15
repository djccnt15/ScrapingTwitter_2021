import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

'''data load'''
df_f = pd.read_csv('./result/smart_factory_pivot_y.csv')
df_f['True_ratio'] = df_f['True_ratio'] * 100
# print(df_f)

# sns.barplot(x='date', y='smart_factory_True', data=df_f)
# plt.show()

'''visualize'''
# declare plot
fig, ax = plt.subplots(figsize=(12, 6))
# seperate second axes
ax_r = ax.twinx()

# bar plot of the smart_factory_True
ax.bar(x=df_f['date'], height=df_f['smart_factory_True'])

# bar plot ticks setting
xticks = df_f['date'] # declare x ticks
ax.set_xticks(ticks=xticks) # set x ticks
ax.set_xticklabels(labels=xticks, rotation=90) # turn x ticks 90 degree

# line plot of the True ratio
ax_r.plot(df_f['date'], df_f['True_ratio'], color='saddlebrown', lw=2)

# annotate value
# ax_r.annotate(
#     df_f['True_ratio'],
#     xy=(df_f.loc[0, 'date'], df_f.loc[0, 'True_ratio'])
# )

# for s in ["left", "right", "top"]:
#     ax.spines[s].set_visible(False)

fig.tight_layout()
plt.savefig('./result/test.png')
plt.show()