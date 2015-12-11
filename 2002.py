import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['East Asia'],
    y=[' 6,236,246 '],
    name='East Asia',
    uid='e270f5',
    xsrc='beobonus:88:01908d?01908d="East Asia"',
    ysrc='beobonus:88:b633ff?01908d="East Asia"'
)
trace2 = Bar(
    x=['Europe'],
    y=[' 2,650,992 '],
    name='Europe',
    uid='fdca37',
    xsrc='beobonus:88:01908d?01908d="Europe"',
    ysrc='beobonus:88:b633ff?01908d="Europe"'
)
trace3 = Bar(
    x=['Amercica'],
    y=[' 730,402 '],
    name='Amercica',
    uid='1f1790',
    xsrc='beobonus:88:01908d?01908d="Amercica"',
    ysrc='beobonus:88:b633ff?01908d="Amercica"'
)
trace4 = Bar(
    x=['South Asia'],
    y=['350,874'],
    name='South Asia',
    uid='9ca8b2',
    xsrc='beobonus:88:01908d?01908d="South Asia"',
    ysrc='beobonus:88:b633ff?01908d="South Asia"'
)
trace5 = Bar(
    x=['Oceania'],
    y=[' 427,109 '],
    name='Oceania',
    uid='724979',
    xsrc='beobonus:88:01908d?01908d="Oceania"',
    ysrc='beobonus:88:b633ff?01908d="Oceania"'
)
trace6 = Bar(
    x=['Middle East'],
    y=[' 245,822 '],
    name='Middle East',
    uid='710814',
    xsrc='beobonus:88:01908d?01908d="Middle East"',
    ysrc='beobonus:88:b633ff?01908d="Middle East"'
)
trace7 = Bar(
    x=['Africa'],
    y=[' 98,290 '],
    name='Africa',
    uid='927092',
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
        range=[0, 6564469.47368421],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
