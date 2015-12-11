import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
data = Data([
    Scattergeo(
        lat=['4.346040', '13.179938', '-1.890793', '20.352561', '4.702613', '22.835942', '13.101607', '1.354541', '12.990648', '35.282137', '22.258337', '36.414396', '36.469294', '23.984748', '47.493935', '50.435589', '55.505669', '61.776083', '46.371033', '50.815250', '53.105627', '42.888231', '51.880182', '61.649893', '61.985770', '39.208426', '62.669473', '46.692043', '54.832647', '-35.969668', '-9.034497', '57.206831', '39.225402', '24.045923', '22.363109', '28.117783', '29.649924', '7.511006', '-25.702687', '-42.700348', '26.371795', '30.941204', '29.288954', '23.235338', '23.577150', '-31.282780'],
        latsrc='beobonus:211:0ef8d8',
        lon=['114.538134', '105.141616', '120.636619', '102.928087', '102.627115', '94.704193', '120.953190', '103.822287', '108.625361', '97.014943', '114.204739', '138.366124', '127.881784', '121.422846', '14.189775', '4.663739', '10.058591', '26.234745', '2.270866', '10.451916', '-8.081788', '12.532400', '5.707034', '9.354401', '99.164918', '-3.191513', '16.376332', '8.002429', '-2.472825', '-65.151983', '-52.979621', '-101.850427', '-101.402765', '90.166260', '79.691163', '83.930104', '69.321531', '80.710733', '134.340382', '172.305005', '29.819145', '34.848342', '47.488879', '45.163437', '54.087503', '24.224358'],
        lonsrc='beobonus:211:c2e442',
        text=['Brunei(9,499)', 'Cambodia(105,367)', 'Indonesia(186,259)', 'Lao(203,748 )', 'Malaysia(1,373,946)', 'Myanmar(53,769)', 'Philippines(186,529)', 'Singapore(650,559)', 'Vietnam(179,243)', 'China(776,792)', 'Hong Kong(274,402)', 'Japan(1,196,654)', 'Korea(816,407)', 'Taiwan(365,664)', 'Austria(58,978)', 'Belgium(57,466)', 'Denmark(103,787)', 'Finland(85,632)', 'France(276,840)', 'Germany(441,827)', '  ', 'Italy(120,237)', 'Netherlands(152,493)', 'Norway(85,551)', 'Russia(102,783)', 'Spain(51,135)', 'Sweden(222,932)', 'Switzerland(120,438)', 'United Kingdom(773,843)', 'Argentina(3,487)', 'Brazil(9,013)', 'Canada(156,618)', 'USA(639,658)', 'Bangladesh(42,739)', 'India(381,471)', 'Nepal(23,081)', 'Pakistan(42,069)', 'Sri Lanka(38,740)', 'Australia(428,521)', 'New Zealand(85,726)', 'Egypt(7,887)', 'Israel(98,380)', 'Kuwait(29,773)', 'Saudi Arabia(10,474)', 'Emirates(48,802)', 'South Africa(35,748)'],
        textsrc='beobonus:158:cabe9f',
        uid='67d061'
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
