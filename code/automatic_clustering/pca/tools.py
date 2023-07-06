from collections import Counter
import plotly.graph_objects as go

def show_results_frecuencies(results_data, nclasses, name='', scale=100):
    info = dict(Counter(results_data))
    info_list = list(dict(info).items())
    info_list.sort()
    xs = [k for k, v in info_list]
    classes_xs = ['Class ' + str(k) + '<br />' + 'items: ' + str(v) for k, v in info_list]
    ys = [v / scale for k, v in info_list]

    fig = go.Figure(data=[
        go.Scatter(
            x=xs, y=[10] * nclasses,
            mode='markers',
            text=classes_xs,
            marker=dict(
                color=['rgb(93, 164, 214)',
                       'rgb(255, 144, 14)',
                       'rgb(44, 160, 101)',
                       'rgb(255, 65, 54)'],
                size=ys, ))
    ])

    fig.update_layout(title='Classes Frequency ' + name,
                      xaxis=dict(title='Class',
                                 type='category'),
                      yaxis=dict(showticklabels=False,
                                 showgrid=False))

    fig.show()
