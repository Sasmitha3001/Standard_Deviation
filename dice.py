import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result=[]

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum=dice1+dice2
    dice_result.append(sum)

mean=int(sum(dice_result))/1000
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
std_dev=statistics.stdev(dice_result)

first_std_dev_start=mean-std_dev
first_std_dev_end=mean+std_dev

second_std_dev_start=mean-2*std_dev
second_std_dev_end=mean+2*std_dev

third_std_dev_start=mean-3*std_dev
third_std_dev_end=mean+3*std_dev

figure=ff.create_distplot([dice_result],['Dice Result'],show_hist=False)
figure.show()

