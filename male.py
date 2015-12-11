import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['2000'],
    y=['5,685,836'],
    name='2000',
    text=['2000'],
    textsrc='beobonus:50:74ef1e?74ef1e="2000"',
    uid='732c76',
    xsrc='beobonus:50:74ef1e?74ef1e="2000"',
    ysrc='beobonus:50:2edaab?74ef1e="2000"'
)
trace2 = Bar(
    x=['2001'],
    y=['6,021,601'],
    name='2001',
    text=['2001'],
    textsrc='beobonus:50:74ef1e?74ef1e="2001"',
    uid='1d6833',
    xsrc='beobonus:50:74ef1e?74ef1e="2001"',
    ysrc='beobonus:50:2edaab?74ef1e="2001"'
)
trace3 = Bar(
    x=['2002'],
    y=['6,426,982'],
    name='2002',
    text=['2002'],
    textsrc='beobonus:50:74ef1e?74ef1e="2002"',
    uid='d8dd87',
    xsrc='beobonus:50:74ef1e?74ef1e="2002"',
    ysrc='beobonus:50:2edaab?74ef1e="2002"'
)
trace4 = Bar(
    x=['2003'],
    y=['6,169,123'],
    name='2003',
    text=['2003'],
    textsrc='beobonus:50:74ef1e?74ef1e="2003"',
    uid='48a0ac',
    xsrc='beobonus:50:74ef1e?74ef1e="2003"',
    ysrc='beobonus:50:2edaab?74ef1e="2003"'
)
trace5 = Bar(
    x=['2004'],
    y=['6,702,541'],
    name='2004',
    text=['2004'],
    textsrc='beobonus:50:74ef1e?74ef1e="2004"',
    uid='6c6e81',
    xsrc='beobonus:50:74ef1e?74ef1e="2004"',
    ysrc='beobonus:50:2edaab?74ef1e="2004"'
)
trace6 = Bar(
    x=['2005'],
    y=['6,764,495'],
    name='2005',
    text=['2005'],
    textsrc='beobonus:50:74ef1e?74ef1e="2005"',
    uid='0b82ac',
    xsrc='beobonus:50:74ef1e?74ef1e="2005"',
    ysrc='beobonus:50:2edaab?74ef1e="2005"'
)
trace7 = Bar(
    x=['2006'],
    y=['8,214,327'],
    name='2006',
    text=['2006'],
    textsrc='beobonus:50:74ef1e?74ef1e="2006"',
    uid='ba4cb9',
    xsrc='beobonus:50:74ef1e?74ef1e="2006"',
    ysrc='beobonus:50:2edaab?74ef1e="2006"'
)
trace8 = Bar(
    x=['2007'],
    y=['9,436,571'],
    name='2007',
    text=['2007'],
    textsrc='beobonus:50:74ef1e?74ef1e="2007"',
    uid='ba578b',
    xsrc='beobonus:50:74ef1e?74ef1e="2007"',
    ysrc='beobonus:50:2edaab?74ef1e="2007"'
)
trace9 = Bar(
    x=['2008'],
    y=['8,816,948'],
    name='2008',
    text=['2008'],
    textsrc='beobonus:50:74ef1e?74ef1e="2008"',
    uid='82c689',
    xsrc='beobonus:50:74ef1e?74ef1e="2008"',
    ysrc='beobonus:50:2edaab?74ef1e="2008"'
)
trace10 = Bar(
    x=['2009'],
    y=['8,927,042'],
    name='2009',
    text=['2009'],
    textsrc='beobonus:50:74ef1e?74ef1e="2009"',
    uid='9e202f',
    xsrc='beobonus:50:74ef1e?74ef1e="2009"',
    ysrc='beobonus:50:2edaab?74ef1e="2009"'
)
trace11 = Bar(
    x=['2010'],
    y=['10,087,770'],
    name='2010',
    text=['2010'],
    textsrc='beobonus:50:74ef1e?74ef1e="2010"',
    uid='81bd91',
    xsrc='beobonus:50:74ef1e?74ef1e="2010"',
    ysrc='beobonus:50:2edaab?74ef1e="2010"'
)
trace12 = Bar(
    x=['2011'],
    y=['11,407,564'],
    name='2011',
    text=['2011'],
    textsrc='beobonus:50:74ef1e?74ef1e="2011"',
    uid='5ac689',
    xsrc='beobonus:50:74ef1e?74ef1e="2011"',
    ysrc='beobonus:50:2edaab?74ef1e="2011"'
)
trace13 = Bar(
    x=['2012'],
    y=['13,047,500'],
    name='2012',
    text=['2012'],
    textsrc='beobonus:50:74ef1e?74ef1e="2012"',
    uid='bb4a5d',
    xsrc='beobonus:50:74ef1e?74ef1e="2012"',
    ysrc='beobonus:50:2edaab?74ef1e="2012"'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13])
layout = Layout(
    autosize=True,
    barmode='group',
    height=514,
    title='MALE',
    width=1121,
    xaxis=XAxis(
        autorange=True,
        range=[1999.5, 2012.5],
        type='linear'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 13734210.52631579]
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
