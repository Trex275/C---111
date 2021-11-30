import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

meanofPopulation = statistics.mean(data)
medianofPopulation = statistics.median(data)
modeofPopulation = statistics.mode(data)
stdevofPopulation = statistics.stdev(data)

print(meanofPopulation, medianofPopulation, modeofPopulation, stdevofPopulation)

#fig = ff.create_distplot([data], ["Marks"],show_hist = False)
#fig.show()

def experiment(): 
    samples = []
    for i in range(100): 
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        samples.append(value)
    meanofsamples = statistics.mean(samples)
    return(meanofsamples)

meanfromexperiments = []
for i in range(850):
    meanofsamples = experiment()
    meanfromexperiments.append(meanofsamples)

meanofSampling = statistics.mean(meanfromexperiments)
medianofSampling = statistics.median(meanfromexperiments)
modeofSampling = statistics.mode(meanfromexperiments)
stdevofSampling = statistics.stdev(meanfromexperiments)

print("the mean, median and mode of sampling distribution is ", meanofSampling, medianofSampling, modeofSampling)
print("the standard deviaiton of sampling distribution is ", stdevofSampling)

#fig = ff.create_distplot([meanfromexperiments], ["Sampling Distribution"],show_hist = False)
#fig.show()

#range of first, second and third standard deviation 

firststdevstart, firststdevend = meanofSampling - stdevofSampling, meanofSampling + stdevofSampling
secondstdevstart, secondstdevend = meanofSampling - (2*stdevofSampling), meanofSampling + (2*stdevofSampling)
thirdstdevstart, thirdstdevend = meanofSampling - (3*stdevofSampling), meanofSampling + (3 * stdevofSampling)

print("the first, second and third standard deviations are : ")
print(firststdevstart, firststdevend)
print(secondstdevstart, secondstdevend)
print(thirdstdevstart, thirdstdevend)

#studying the effect of intervention 1
df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()
mean1 = statistics.mean(data1)
print("The mean of intrevention 1 is ", mean1)

'''fig = ff.create_distplot([meanfromexperiments], ["Sampling Distribution"],show_hist = False)
fig.add_trace(go.Scatter(x = [meanofSampling, meanofSampling], y = [0, 0.17], mode = "lines", name = "Mean of sampling distribution" ))
fig.add_trace(go.Scatter(x = [firststdevend, firststdevend], y = [0, 0.17], mode = "lines", name = "First Standard Deviation" ))
fig.add_trace(go.Scatter(x = [secondstdevend, secondstdevend], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation" ))
fig.add_trace(go.Scatter(x = [thirdstdevend, thirdstdevend], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation" ))
fig.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.17], mode = "lines", name = "Mean of Intervention 1" ))
fig.show()'''

#studying the effect of intervention 2
df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()
mean2 = statistics.mean(data2)
print("The mean of intrevention 2 is ", mean2)

'''fig = ff.create_distplot([meanfromexperiments], ["Sampling Distribution"],show_hist = False)
fig.add_trace(go.Scatter(x = [meanofSampling, meanofSampling], y = [0, 0.17], mode = "lines", name = "Mean of sampling distribution" ))
fig.add_trace(go.Scatter(x = [firststdevend, firststdevend], y = [0, 0.17], mode = "lines", name = "First Standard Deviation" ))
fig.add_trace(go.Scatter(x = [secondstdevend, secondstdevend], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation" ))
fig.add_trace(go.Scatter(x = [thirdstdevend, thirdstdevend], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation" ))
fig.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 0.17], mode = "lines", name = "Mean of Intervention 1" ))
fig.show()'''

#studying the effect of intervention 3
df3 = pd.read_csv("data3.csv")
data3 = df3["Math_score"].tolist()
mean3 = statistics.mean(data3)
print("The mean of intrevention 3 is ", mean3)

fig = ff.create_distplot([meanfromexperiments], ["Sampling Distribution"],show_hist = False)
fig.add_trace(go.Scatter(x = [meanofSampling, meanofSampling], y = [0, 0.17], mode = "lines", name = "Mean of sampling distribution" ))
fig.add_trace(go.Scatter(x = [firststdevend, firststdevend], y = [0, 0.17], mode = "lines", name = "First Standard Deviation" ))
fig.add_trace(go.Scatter(x = [secondstdevend, secondstdevend], y = [0, 0.17], mode = "lines", name = "Second Standard Deviation" ))
fig.add_trace(go.Scatter(x = [thirdstdevend, thirdstdevend], y = [0, 0.17], mode = "lines", name = "Third Standard Deviation" ))
fig.add_trace(go.Scatter(x = [mean3, mean3], y = [0, 0.17], mode = "lines", name = "Mean of Intervention 3" ))
fig.show()

#zscore = (new sample mean - mean of sampling )/ standard deviation 

zscore = (meanofSampling - mean1) / stdevofSampling
print("The zscore for the first intervention is ", zscore)


