import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
data = Data([
    Scatter(
        x=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
        y=['9,508,623', '10,061,950', '10,799,067', '10,004,453', '11,650,703', '11,516,936', '13,821,802', '14,464,228', '14,584,220', '14,149,841', '15,936,400', '19,230,470', '22,353,903'],
        name='y',
        uid='4d1eb3',
        xsrc='beobonus:43:72c335',
        ysrc='beobonus:43:327c3c'
    )
])
layout = Layout(
    autosize=True,
    height=514,
    title='Total of foreign tourists in Thailand.',
    width=1121,
    xaxis=XAxis(
        autorange=False,
        range=[1997.0353569503766, 2015.3748335185567],
        title='Years',
        type='linear'
    ),
    yaxis=YAxis(
        autorange=False,
        range=[8184045.994554231, 34895242.829630025],
        title='Number of people.'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
