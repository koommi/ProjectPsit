import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['East Asia'],
    y=[' 7,622,244 '],
    name='East Asia',
    uid='d2f618',
    xsrc='beobonus:88:01908d?01908d="East Asia"',
    ysrc='beobonus:88:b633ff?01908d="East Asia"'
)
trace2 = Bar(
    x=['Europe'],
    y=[' 3,490,779 '],
    name='Europe',
    uid='81822f',
    xsrc='beobonus:88:01908d?01908d="Europe"',
    ysrc='beobonus:88:b633ff?01908d="Europe"'
)
trace3 = Bar(
    x=['Amercica'],
    y=[' 923,382 '],
    name='Amercica',
    uid='662bcd',
    xsrc='beobonus:88:01908d?01908d="Amercica"',
    ysrc='beobonus:88:b633ff?01908d="Amercica"'
)
trace4 = Bar(
    x=['South Asia'],
    y=[' 631,208 '],
    name='South Asia',
    uid='f2fc28',
    xsrc='beobonus:88:01908d?01908d="South Asia"',
    ysrc='beobonus:88:b633ff?01908d="South Asia"'
)
trace5 = Bar(
    x=['Oceania'],
    y=[' 651,262 '],
    name='Oceania',
    uid='2b7cbe',
    xsrc='beobonus:88:01908d?01908d="Oceania"',
    ysrc='beobonus:88:b633ff?01908d="Oceania"'
)
trace6 = Bar(
    x=['Middle East'],
    y=[' 392,416 '],
    name='Middle East',
    uid='38ce37',
    xsrc='beobonus:88:01908d?01908d="Middle East"',
    ysrc='beobonus:88:b633ff?01908d="Middle East"'
)
trace7 = Bar(
    x=['Africa'],
    y=[' 110,511 '],
    name='Africa',
    uid='d651de',
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
        range=[0, 6733891.578947368],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
