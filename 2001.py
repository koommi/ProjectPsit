import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['East Asia'],
    y=['5,786,403'],
    name='East Asia',
    uid='376290',
    xsrc='beobonus:88:01908d?01908d="East Asia"',
    ysrc='beobonus:88:b633ff?01908d="East Asia"'
)
trace2 = Bar(
    x=['Europe'],
    y=['2,508,566'],
    name='Europe',
    uid='096e08',
    xsrc='beobonus:88:01908d?01908d="Europe"',
    ysrc='beobonus:88:b633ff?01908d="Europe"'
)
trace3 = Bar(
    x=['Amercica'],
    y=['682,995'],
    name='Amercica',
    uid='51f399',
    xsrc='beobonus:88:01908d?01908d="Amercica"',
    ysrc='beobonus:88:b633ff?01908d="Amercica"'
)
trace4 = Bar(
    x=['South Asia'],
    y=['350,874'],
    name='South Asia',
    uid='55b2ab',
    xsrc='beobonus:88:01908d?01908d="South Asia"',
    ysrc='beobonus:88:b633ff?01908d="South Asia"'
)
trace5 = Bar(
    x=['Oceania'],
    y=['420,551'],
    name='Oceania',
    uid='0a034e',
    xsrc='beobonus:88:01908d?01908d="Oceania"',
    ysrc='beobonus:88:b633ff?01908d="Oceania"'
)
trace6 = Bar(
    x=['Middle East'],
    y=['215,148'],
    name='Middle East',
    uid='112633',
    xsrc='beobonus:88:01908d?01908d="Middle East"',
    ysrc='beobonus:88:b633ff?01908d="Middle East"'
)
trace7 = Bar(
    x=['Africa'],
    y=['97,413'],
    name='Africa',
    uid='df173f',
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
        range=[0, 6090950.52631579],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
