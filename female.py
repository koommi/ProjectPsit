import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
trace1 = Bar(
    x=['2000'],
    y=['3,822,787'],
    name='2000',
    text=['2000'],
    textsrc='beobonus:50:74ef1e?74ef1e="2000"',
    uid='c5efdc',
    xsrc='beobonus:50:74ef1e?74ef1e="2000"',
    ysrc='beobonus:50:2edaab?74ef1e="2000"'
)
trace2 = Bar(
    x=['2001'],
    y=['4,040,349'],
    name='2001',
    text=['2001'],
    textsrc='beobonus:50:74ef1e?74ef1e="2001"',
    uid='0b15c2',
    xsrc='beobonus:50:74ef1e?74ef1e="2001"',
    ysrc='beobonus:50:2edaab?74ef1e="2001"'
)
trace3 = Bar(
    x=['2002'],
    y=['4,372,085'],
    name='2002',
    text=['2002'],
    textsrc='beobonus:50:74ef1e?74ef1e="2002"',
    uid='246020',
    xsrc='beobonus:50:74ef1e?74ef1e="2002"',
    ysrc='beobonus:50:2edaab?74ef1e="2002"'
)
trace4 = Bar(
    x=['2003'],
    y=['3,835,330'],
    name='2003',
    text=['2003'],
    textsrc='beobonus:50:74ef1e?74ef1e="2003"',
    uid='827a2a',
    xsrc='beobonus:50:74ef1e?74ef1e="2003"',
    ysrc='beobonus:50:2edaab?74ef1e="2003"'
)
trace5 = Bar(
    x=['2004'],
    y=['4,948,162'],
    name='2004',
    text=['2004'],
    textsrc='beobonus:50:74ef1e?74ef1e="2004"',
    uid='af10ab',
    xsrc='beobonus:50:74ef1e?74ef1e="2004"',
    ysrc='beobonus:50:2edaab?74ef1e="2004"'
)
trace6 = Bar(
    x=['2005'],
    y=['4,752,441'],
    name='2005',
    text=['2005'],
    textsrc='beobonus:50:74ef1e?74ef1e="2005"',
    uid='03436f',
    xsrc='beobonus:50:74ef1e?74ef1e="2005"',
    ysrc='beobonus:50:2edaab?74ef1e="2005"'
)
trace7 = Bar(
    x=['2006'],
    y=['5,607,475'],
    name='2006',
    text=['2006'],
    textsrc='beobonus:50:74ef1e?74ef1e="2006"',
    uid='232216',
    xsrc='beobonus:50:74ef1e?74ef1e="2006"',
    ysrc='beobonus:50:2edaab?74ef1e="2006"'
)
trace8 = Bar(
    x=['2007'],
    y=['5,027,657'],
    name='2007',
    text=['2007'],
    textsrc='beobonus:50:74ef1e?74ef1e="2007"',
    uid='6befc6',
    xsrc='beobonus:50:74ef1e?74ef1e="2007"',
    ysrc='beobonus:50:2edaab?74ef1e="2007"'
)
trace9 = Bar(
    x=['2008'],
    y=['5,767,272'],
    name='2008',
    text=['2008'],
    textsrc='beobonus:50:74ef1e?74ef1e="2008"',
    uid='82d4f4',
    xsrc='beobonus:50:74ef1e?74ef1e="2008"',
    ysrc='beobonus:50:2edaab?74ef1e="2008"'
)
trace10 = Bar(
    x=['2009'],
    y=['5,222,799'],
    name='2009',
    text=['2009'],
    textsrc='beobonus:50:74ef1e?74ef1e="2009"',
    uid='39897c',
    xsrc='beobonus:50:74ef1e?74ef1e="2009"',
    ysrc='beobonus:50:2edaab?74ef1e="2009"'
)
trace11 = Bar(
    x=['2010'],
    y=['5,848,630'],
    name='2010',
    text=['2010'],
    textsrc='beobonus:50:74ef1e?74ef1e="2010"',
    uid='a4ec50',
    xsrc='beobonus:50:74ef1e?74ef1e="2010"',
    ysrc='beobonus:50:2edaab?74ef1e="2010"'
)
trace12 = Bar(
    x=['2011'],
    y=['7,822,906'],
    name='2011',
    text=['2011'],
    textsrc='beobonus:50:74ef1e?74ef1e="2011"',
    uid='85d04b',
    xsrc='beobonus:50:74ef1e?74ef1e="2011"',
    ysrc='beobonus:50:2edaab?74ef1e="2011"'
)
trace13 = Bar(
    x=['2012'],
    y=['9,306,403'],
    name='2012',
    text=['2012'],
    textsrc='beobonus:50:74ef1e?74ef1e="2012"',
    uid='a5442d',
    xsrc='beobonus:50:74ef1e?74ef1e="2012"',
    ysrc='beobonus:50:2edaab?74ef1e="2012"'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13])
layout = Layout(
    autosize=True,
    barmode='group',
    height=514,
    title='FEMALE',
    width=1121,
    xaxis=XAxis(
        autorange=False,
        range=[1998.280512662898, 2011.280512662898],
        title='Years',
        type='linear'
    ),
    yaxis=YAxis(
        autorange=False,
        range=[1993577.784034904, 11789791.468245428],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
