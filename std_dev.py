import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
#Creating a list of sum of 2 dice, rolled 1000 times
dice_result = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)
#Calculating the mean and the standard deviation
mean = sum(dice_result) / len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([dice_result], ["result"], show_hist=False)
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.15],name="Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.15],name="Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.15],name="Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.15],name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],name="Mean"))
fig.show()

print("Mean is {}  Median is {}  Mode is {} ".format(mean,median,mode))

list_std_dev_1=[result for result in dice_result if result>first_std_deviation_start and result<first_std_deviation_end]
list_std_dev_2=[result for result in dice_result if result>second_std_deviation_start and result<second_std_deviation_end]
list_std_dev_3=[i for i in dice_result if i>third_std_deviation_start and i<third_std_deviation_end]

print('list_std_dev_1',len(list_std_dev_1)*100.0/len(dice_result))
print('list_std_dev_2',len(list_std_dev_2)*100.0/len(dice_result))
print('list_std_dev_3',len(list_std_dev_3)*100.0/len(dice_result))

