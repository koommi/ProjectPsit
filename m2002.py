import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('beobonus', '02p6asccbu')
data = Data([
    Scattergeo(
        lat=['4.34604', '13.179938', '-1.890793', '20.352561', '4.702613', '22.835942', '13.101607', '1.354541', '12.990648', '35.282137', '22.258337', '36.414396', '36.469294', '23.984748', '47.493935', '50.435589', '55.505669', '61.776083', '46.371033', '50.81525', '53.105627', '42.888231', '51.880182', '61.649893', '61.98577', '39.208426', '62.669473', '46.692043', '54.832647', '-35.969668', '-9.034497', '57.206831', '39.225402', '24.045923', '22.363109', '28.117783', '29.649924', '7.511006', '-25.702687', '-42.700348', '26.371795', '30.941204', '29.288954', '23.235338', '23.57715', '-31.28278'],
        latsrc='beobonus:259:4aa9b7',
        lon=['114.538134', '105.141616', '120.636619', '102.928087', '102.627115', '94.704193', '120.95319', '103.822287', '108.625361', '97.014943', '114.204739', '138.366124', '127.881784', '121.422846', '14.189775', '4.663739', '10.058591', '26.234745', '2.270866', '10.451916', '-8.081788', '12.5324', '5.707034', '9.354401', '99.164918', '-3.191513', '16.376332', '8.002429', '-2.472825', '-65.151983', '-52.979621', '-101.850427', '-101.402765', '90.16626', '79.691163', '83.930104', '69.321531', '80.710733', '134.340382', '172.305005', '29.819145', '34.848342', '47.488879', '45.163437', '54.087503', '24.224358'],
        lonsrc='beobonus:259:372fcc',
        text=['Brunei (10,129)', 'Cambodia(70,187)', 'Indonesia\n(164,645)', 'Lao\n(90,717)', 'Malaysia\n(1,332,355)', 'Myanmar \n(36,111)', 'Philippines\n(139,364)', 'Singapore\n(546,796)', 'Vietnam\n(84,219)', 'China\n(797,976)', 'Hong Kong\n(335,816)', 'Japan\n(1,239,421)', 'Korea\n(704,649)', 'Taiwan\n(674,366)', 'Austria\n(54,020)', 'Belgium\n(56,865)', 'Denmark\n(90,480)', 'Finland\n(66,772)', 'France\n(271,395)', 'Germany\n(411,049)', '  ', 'Italy\n(129,293)', 'Netherlands\n(150,138)', 'Norway\n(74,607)', 'Russia\n(70,692)', 'Spain\n(47,431)', 'Sweden\n(215,894)', '118,827', 'United Kingdom\n(704,416)', 'Argentina\n(3,398)', 'Brazil\n(8,960)', 'Canada\n(135,668)', 'USA\n(555,353)', 'Bangladesh\n(35,928)', 'India\n(280,641)', 'Nepal\n(19,933)', 'Pakistan\n(31,246)', 'Sri Lanka\n(31,649)', 'Australia\n(351,508)', 'New Zealand\n(73,710)', 'Egypt\n(7,719)', 'Israel\n(98,691)', 'Kuwait\n(25,251)', 'Saudi Arabia\n(6,886)', 'Emirates\n(26,565)', 'South Africa\n(39,262)'],
        textsrc='beobonus:252:8525dd',
        uid='2287d5'
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
