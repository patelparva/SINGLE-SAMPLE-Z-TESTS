import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

def handle_input():
    input_correct=False
    while input_correct!=True:
        school=int(input('Which School\'s data do you want to fetch? \nFor School 1, Type 1\nFor School 2, Type 2\nFor School 3, Type 3\nEnter the number... '))

        if school==1:
            input_correct=True
            return 'School1'
        
        if school==2:
            input_correct=True
            return 'School2'
        
        if school==3:
            input_correct=True
            return 'School3'

        else:
            print('Invalid Input')

def fetch_data(school):
    df=pd.read_csv(school+'.csv')
    data=df['Math_score'].tolist()

    mean=statistics.mean(data)
    mean_dataset=[]

    for i in range(0,1000):
        temp_dataset=[]
        for i in range(0,100):
            temp_dataset.append(data[random.randrange(0,len(data))])
    
        mean=statistics.mean(temp_dataset)
    
        mean_dataset.append(mean)

    mean_sample=statistics.mean(mean_dataset)
    stdev_sample=statistics.stdev(mean_dataset)

    return mean_sample,stdev_sample,mean_dataset

def fetch_data_after_intervention(school):
    if school=='School1':
        
        df1=pd.read_csv('School_1_Sample.csv')
        data1=df1['Math_score'].tolist()
    
        mean1=statistics.mean(data1)
    
        return mean1
    
    if school=='School2':
        
        df1=pd.read_csv('School_2_Sample.csv')
        data1=df1['Math_score'].tolist()

        mean1=statistics.mean(data1)

        return mean1
    
    if school=='School3':
        
        df1=pd.read_csv('School_3_Sample.csv')
        data1=df1['Math_score'].tolist()

        mean1=statistics.mean(data1)

        return mean1

def find_z_score(mean_sample,mean1,stdev,school):
    z_score=(mean1-mean_sample)/stdev

    print('z Score for '+school+'is {}'.format(z_score))

def display_graph(data,mean,stdev,mean1):
    first_stdev_start,first_stdev_end=mean-stdev,mean+stdev
    second_stdev_start,second_stdev_end=mean-(stdev*2),mean+(stdev*2)
    third_stdev_start,third_stdev_end=mean-(stdev*3),mean+(stdev*3)
    
    fig=ff.create_distplot([data],['Sample Distribution'],show_hist=False)
    
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode='lines',name='Mean of Sample Distribution'))
    fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.2],mode='lines',name='Mean after Intervention'))
    
    fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.2],mode='lines',name='First Standard Deviation Start'))
    fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name='First Standard Deviation End'))
    
    fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.2],mode='lines',name='Second Standard Deviation Start'))
    fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode='lines',name='Second Standard Deviation End'))
    
    fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.2],mode='lines',name='Third Standard Deviation Start'))
    fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode='lines',name='Third Standard Deviation End'))

    fig.show()

def handle_data(school):
    mean,stdev,data=fetch_data(school)
    mean1=fetch_data_after_intervention(school)
    find_z_score(mean,mean1,stdev,school)
    display_graph(data,mean,stdev,mean1)

def main():
    input=handle_input()
    handle_data(input)

if __name__ == '__main__':
    main()
    