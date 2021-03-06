import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
data = Data([
    Scattergeo(
        lat=['4.346040', '13.179938', '-1.890793', '20.352561', '4.702613', '22.835942', '13.101607', '1.354541', '12.990648', '35.282137', '22.258337', '36.414396', '36.469294', '23.984748', '47.493935', '50.435589', '55.505669', '61.776083', '46.371033', '50.815250', '53.105627', '42.888231', '51.880182', '61.649893', '61.985770', '39.208426', '62.669473', '46.692043', '54.832647', '-35.969668', '-9.034497', '57.206831', '39.225402', '24.045923', '22.363109', '28.117783', '29.649924', '7.511006', '-25.702687', '-42.700348', '26.371795', '30.941204', '29.288954', '23.235338', '23.577150', '-31.282780'],
        latsrc='beobonus:215:2646a5',
        lon=['114.538134', '105.141616', '120.636619', '102.928087', '102.627115', '94.704193', '120.953190', '103.822287', '108.625361', '97.014943', '114.204739', '138.366124', '127.881784', '121.422846', '14.189775', '4.663739', '10.058591', '26.234745', '2.270866', '10.451916', '-8.081788', '12.532400', '5.707034', '9.354401', '99.164918', '-3.191513', '16.376332', '8.002429', '-2.472825', '-65.151983', '-52.979621', '-101.850427', '-101.402765', '90.166260', '79.691163', '83.930104', '69.321531', '80.710733', '134.340382', '172.305005', '29.819145', '34.848342', '47.488879', '45.163437', '54.087503', '24.224358'],
        lonsrc='beobonus:215:6f8e0d',
        text=['Brunei(9,418)', 'Cambodia(117,100)', 'Indonesia(219,783)', 'Lao(276,207)', 'Malaysia(1,591,328)', 'Myanmar(62,769)', 'Philippines(198,443)', 'Singapore(687,160)', 'Vietnam(227,134)', 'China(949,117)', 'Hong Kong(376,636)', 'Japan(1,311,987)', 'Korea(1,092,783)', 'Taiwan(475,117)', 'Austria(76,106)', 'Belgium(68,617)', 'Denmark(128,037)', 'Finland(110,502)', 'France(321,278)', 'Germany(516,659)', '  ', 'Italy(150,420)', 'Netherlands(180,830)', 'Norway(106,314)', 'Russia(187,658)', 'Spain(69,658)', 'Sweden(306,085)', 'Switzerland(140,741)', 'United Kingdom(850,685)', 'Argentina(4,327)', 'Brazil(11,841)', 'Canada(183,094)', 'USA(694,258)', 'Bangladesh(40,281)', 'India(459,795)', 'Nepal(21,180)', 'Pakistan(46,367)', 'Sri Lanka(46,557)', 'Australia(549,547)', 'New Zealand(98,786)', 'Egypt(11,882)', 'Israel(121,508)', 'Kuwait(33,934)', 'Saudi Arabia(20,804)', 'Emirates(69,509)', 'South Africa(47,228)'],
        textsrc='beobonus:158:8a5b65',
        uid='eb8269'
    )
])
layout = Layout(
    autosize=True,
    height=514,
    title='Number of Foreign Tourists in other country.',
    width=1121
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
 
 
 
 
