import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
data = Data([
    Scattergeo(
        lat=['4.34604', '13.179938', '-1.890793', '20.352561', '4.702613', '22.835942', '13.101607', '1.354541', '12.990648', '35.282137', '22.258337', '36.414396', '36.469294', '23.984748', '47.493935', '50.435589', '55.505669', '61.776083', '46.371033', '50.81525', '53.105627', '42.888231', '51.880182', '61.649893', '61.98577', '39.208426', '62.669473', '46.692043', '54.832647', '-35.969668', '-9.034497', '57.206831', '39.225402', '24.045923', '22.363109', '28.117783', '29.649924', '7.511006', '-25.702687', '-42.700348', '26.371795', '30.941204', '29.288954', '23.235338', '23.57715', '-31.28278'],
        latsrc='beobonus:255:e27577',
        lon=['114.538134', '105.141616', '120.636619', '102.928087', '102.627115', '94.704193', '120.95319', '103.822287', '108.625361', '97.014943', '114.204739', '138.366124', '127.881784', '121.422846', '14.189775', '4.663739', '10.058591', '26.234745', '2.270866', '10.451916', '-8.081788', '12.5324', '5.707034', '9.354401', '99.164918', '-3.191513', '16.376332', '8.002429', '-2.472825', '-65.151983', '-52.979621', '-101.850427', '-101.402765', '90.16626', '79.691163', '83.930104', '69.321531', '80.710733', '134.340382', '172.305005', '29.819145', '34.848342', '47.488879', '45.163437', '54.087503', '24.224358'],
        lonsrc='beobonus:255:1f7657',
        text=['Brunei (8,863)', 'Cambodia(65,502)', 'Indonesia(168,568)', 'Lao(100,747)', 'Malaysia(1,354,295)', 'Myanmar(32,702)', 'Philippines(140,371)', 'Singapore(515,630)', 'Vietnam(117,553)', 'China(606,635)', 'Hong Kong(411,242)', 'Japan(1,042,349)', 'Korea(695,313)', 'Taiwan(501,573)', 'Austria(53,646)', 'Belgium(52,052)', 'Denmark(82,828)', 'Finland(66,513)', 'France(237,690)', 'Germany(386,532)', '', 'Italy(97,526)', 'Netherlands(138,839)', 'Norway(71,885)', 'Russia(89,329)', 'Spain(31,526)', 'Sweden(204,002)', 'Switzerland(107,896)', 'United Kingdom(736,520)', 'Argentina(2,348)', 'Brazil(6,784)', 'Canada(137,963)', 'USA(514,863)', 'Bangladesh(53,421)', 'India(253,752)', 'Nepal(19,909)', 'Pakistan(31,315)', 'Sri Lanka(38,483)', 'Australia(291,872)', 'New Zealand(69,387)', 'Egypt(5,264)', 'Israel(69,837)', 'Kuwait(19,977)', 'Saudi Arabia(4,849)', 'Emirates(22,914)', 'South Africa(35,560)'],
        textsrc='beobonus:252:dff47f',
        uid='8157ad'
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