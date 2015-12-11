import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['East Asia'],
    y=[' 8,167,164 '],
    name='East Asia',
    uid='196b3b',
    xsrc='beobonus:88:01908d?01908d="East Asia"',
    ysrc='beobonus:88:b633ff?01908d="East Asia"'
)
trace2 = Bar(
    x=['Europe'],
    y=[' 4,442,375 '],
    name='Europe',
    uid='631da6',
    xsrc='beobonus:88:01908d?01908d="Europe"',
    ysrc='beobonus:88:b633ff?01908d="Europe"'
)
trace3 = Bar(
    x=['Amercica'],
    y=[' 844,644 '],
    name='Amercica',
    uid='44342c',
    xsrc='beobonus:88:01908d?01908d="Amercica"',
    ysrc='beobonus:88:b633ff?01908d="Amercica"'
)
trace4 = Bar(
    x=['South Asia'],
    y=[' 995,321 '],
    name='South Asia',
    uid='8f90c7',
    xsrc='beobonus:88:01908d?01908d="South Asia"',
    ysrc='beobonus:88:b633ff?01908d="South Asia"'
)
trace5 = Bar(
    x=['Oceania'],
    y=[' 789,632 '],
    name='Oceania',
    uid='3f247c',
    xsrc='beobonus:88:01908d?01908d="Oceania"',
    ysrc='beobonus:88:b633ff?01908d="Oceania"'
)
trace6 = Bar(
    x=['Middle East'],
    y=[' 569,334 '],
    name='Middle East',
    uid='2d0f46',
    xsrc='beobonus:88:01908d?01908d="Middle East"',
    ysrc='beobonus:88:b633ff?01908d="Middle East"'
)
trace7 = Bar(
    x=['Africa'],
    y=[' 127,930 '],
    name='Africa',
    uid='f8f8d7',
    xsrc='beobonus:88:01908d?01908d="Africa"',
    ysrc='beobonus:88:b633ff?01908d="Africa"'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
layout = Layout(
    autosize=True,
    barmode='group',
    height=514,
    title='Number of foreign tourists in other continent.',
    width=1121,
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 6.5],
        title='Name of continent.',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 8597014.736842105],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
