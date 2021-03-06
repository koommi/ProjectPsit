import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('SandChuenchuphol', 'xyg0nuli7p')
trace1 = Scatter(
    x=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['1,455,214', '1,523,952', '1,552,337', '1,300,768', '1,593,188', '1,643,355', '1,939,255', '2,153,908', '2,435,212', '1,764,455', '1,676,484', '2,426,057', '2,910,605'],
    name='25Or Lower',
    uid='637d48',
    xsrc='SandChuenchuphol:26:e65984',
    ysrc='SandChuenchuphol:26:2db0ed'
)
trace2 = Scatter(
    x=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['2,537,639', '2,726,812', '2,830,547', '2,489,810', '2,899,663', '2,943,762', '3,628,174', '3,851,347', '3,671,068', '3,889,731', '4,395,345', '5,422,072', '5,933,709'],
    name='25-34 Years Old',
    uid='c46b29',
    xsrc='SandChuenchuphol:26:e65984',
    ysrc='SandChuenchuphol:26:6b4bc9'
)
trace3 = Scatter(
    x=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['2,270,566', '2,414,170', '2,605,227', '2,564,250', '2,960,953', '2,852,566', '3,375,882', '3,432,234', '3,282,715', '3,514,041', '4,132,223', '4,846,224', '5,504,458'],
    name='35 - 44  Years Old',
    uid='39638a',
    xsrc='SandChuenchuphol:26:e65984',
    ysrc='SandChuenchuphol:26:d1bc2f'
)
trace4 = Scatter(
    x=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['1,822,708', '1,893,820', '2,099,828', '2,039,752', '2,357,021', '2,275,911', '2,758,816', '2,767,578', '2,718,785', '2,772,824', '3,222,829', '3,669,314', '4,328,028'],
    name='45 - 54 Years Old',
    uid='66bfc7',
    xsrc='SandChuenchuphol:26:e65984',
    ysrc='SandChuenchuphol:26:7f3beb'
)
trace5 = Scatter(
    x=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['996,057', '1,060,440', '1,228,238', '1,178,195', '1,373,279', '1,348,016', '1,583,504', '1,663,221', '1,759,277', '1,634,889', '1,893,874', '2,119,860', '2,604,599'],
    name='55- 64 Years Old',
    uid='c33d5a',
    xsrc='SandChuenchuphol:26:e65984',
    ysrc='SandChuenchuphol:26:61ab54'
)
trace6 = Scatter(
    x=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'],
    y=['426,439', '442,756', '482,890', '431,718', '466,599', '453,326', '536,171', '595,940', '717,163', '573,901', '615,645', '746,943', '1,072,504'],
    name='65 or Over',
    uid='0ea3b7',
    xsrc='SandChuenchuphol:26:e65984',
    ysrc='SandChuenchuphol:26:fa7819'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
layout = Layout(
    autosize=True,
    height=816,
    width=1620,
    xaxis=XAxis(
        autorange=True,
        range=[1999.1079286010793, 2014.8920713989207],
        type='linear'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[30032.774827403133, 7121857.225172597]
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
