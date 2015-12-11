import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['East Asia'],
    y=[' 7,076,190 '],
    name='East Asia',
    uid='80bb93',
    xsrc='beobonus:88:01908d?01908d="East Asia"',
    ysrc='beobonus:88:b633ff?01908d="East Asia"'
)
trace2 = Bar(
    x=['Europe'],
    y=[' 4,059,988 '],
    name='Europe',
    uid='09d12d',
    xsrc='beobonus:88:01908d?01908d="Europe"',
    ysrc='beobonus:88:b633ff?01908d="Europe"'
)
trace3 = Bar(
    x=['Amercica'],
    y=[' 853,380 '],
    name='Amercica',
    uid='759cee',
    xsrc='beobonus:88:01908d?01908d="Amercica"',
    ysrc='beobonus:88:b633ff?01908d="Amercica"'
)
trace4 = Bar(
    x=['South Asia'],
    y=[' 826,437 '],
    name='South Asia',
    uid='72b365',
    xsrc='beobonus:88:01908d?01908d="South Asia"',
    ysrc='beobonus:88:b633ff?01908d="South Asia"'
)
trace5 = Bar(
    x=['Oceania'],
    y=[' 737,460 '],
    name='Oceania',
    uid='3fb06d',
    xsrc='beobonus:88:01908d?01908d="Oceania"',
    ysrc='beobonus:88:b633ff?01908d="Oceania"'
)
trace6 = Bar(
    x=['Middle East'],
    y=[' 483,983 '],
    name='Middle East',
    uid='327952',
    xsrc='beobonus:88:01908d?01908d="Middle East"',
    ysrc='beobonus:88:b633ff?01908d="Middle East"'
)
trace7 = Bar(
    x=['Africa'],
    y=[' 112,403 '],
    name='Africa',
    uid='7e8986',
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
        range=[0, 7448621.052631579],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
