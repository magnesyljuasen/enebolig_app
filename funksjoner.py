import streamlit as st
import pandas as pd
import numpy as np
import mpu
import math
import pydeck as pdk
from PIL import Image
from streamlit_folium import folium_static
from streamlit_lottie import st_lottie
import requests
import altair as alt
import base64
import json
from shapely.geometry import Point, shape
import streamlit as st
import requests

#Forbedring

#Behovsklasser
#class grunnlag   
#class kostnader
#arve fra input 
#class klimagassutslipp
#arve fra kostnader
#class dimensjonering
#arve fra dimensjonering

#variabler initialiseres i konstruktøren til klassen

#klasse kjøres -> oppdaterer en self.variabel -> henter ut self.variabel fra arvet klasse -> bruker i en annen (muligens oppdater self.variabel igjen) ->

#--OK--
class Forklaringer:
    def __init__(self) -> None:
        self.forklaringer()

    def forklaringer(self):

        with st.expander('Finansiering'):
            url = 'https://www.enova.no/privat/alle-energitiltak/varmepumper/vaske-til-vann-varmepumpe-/'
            st.write(""" Du får inntil 10 000,- i støtte fra [ENOVA](%s) når du skaffer deg en væske-til-vann-varmepumpe. """ % url)
            
            url = 'https://www.enova.no/privat/alle-energitiltak/tiltaksbonus---vannbarent-anlegg/'
            st.write(""" Dersom du i tillegg installerer akkumulatortank og vannbåren varme kan du få inntil 40 000,- i [tiltaksbonus](%s).""" % url)

            url = "https://www.smartepenger.no/lan/3408-gronne-boliglan"
            st.write("""Mange banker har begynt å tilby billigere 
            boliglån hvis boligen regnes som miljøvennlig; et såkalt [grønt boliglån](%s). Med et bergvarmeanlegg 
            vil din bolig havne i energiklasse A eller B, som gjør at boligen kvalifiserer for et slikt lån. """ % url)
            
        with st.expander('Hvorfor bergvarme?'):
            st.write(""" Bergvarme er både miljøvennlig, kortreist og fornybar energi, 
                        og blir stadig mer populært blant norske byggeiere. Et bergvarmeanlegg gir den 
                        beste strømbesparelsen og kan redusere din strømregning med en faktor på 3 – 4. """)

            st.write(""" Om sommeren, når det er behov for kjøling, er temperaturen i brønnen i seg selv
                            lav nok til å kjøle bygningen. Da trengs viftekonvektorer som kan 
                            fordele kjøling i bygningen på en komfortabel måte. """)

        with st.expander('Hva gjør bergvarmekalkulatoren?'):
            st.write(""" Kalkulatoren er utviklet av Asplan Viak, og utfører en enkel dimensjonering av en energibrønn 
            med bergvarmepumpe for din bolig. Den regner så ut kostnader og miljøgevinst for det aktuelle anlegget. Det er mulig 
            å justere parameterene som ligger til grunn for beregningen i menyen til venstre som dukker opp når du skriver inn din adresse. """)
            st.write(""" Resultatene fra kalkulatoren er å anse som et estimat, og endelig dimensjonering av energibrønnen med varmepumpe
            må tilpasses de stedlige forholdene av leverandør. """)
            
#--OK--
class Forside:
    def __init__(self) -> None:
        self.tekst()
    
    def tekst(self):
        c1, c2 = st.columns(2)
        with c1:
            st.header('1) Energibrønn')
            st.write(""" Bergvarme er i hovedsak lagret solenergi med en stabil temperatur i størrelsesorden rundt 5 - 7 °C. """ )
            st.write(""" For å hente ut bergvarmen må det bores en energibrønn med 
            en dybde på mellom 80 - 300 meter. Dette gjøres med en borerigg.""")
            st.write(""" Inne i energibrønnen monteres det en U-formet slange
            som sirkulerer frostsikker væske ned i 
            energibrønnen og videre opp igjen til overflaten. """)
        with c2:
            image = Image.open('Grunnlagsdata/Bilder/Construction-bro.png')
            st.image(image)         

        c2, c1 = st.columns(2)
        with c1:
            image = Image.open('Grunnlagsdata/Bilder/Pipeline maintenance-amico.png')
            st.image(image)
        with c2:
            st.header('2) Bergvarmepumpe')
            st.write(""" En væske-vann-varmepumpe (ofte kalt bergvarmepumpe) installeres i boligen, 
            og endene på kollektorslangen kobles til varmepumpen. """)
            st.write(""" 
            For oppvarmingsformål kan nå varmepumpen hente varmeenergi med en stabil lav temperatur 
            fra berggrunnen og levere varmeenergi med en høy temperatur til boligens 
            vannbårne varmesystem. For å utføre dette arbeidet bruker varmepumpen strøm, 
            men siden berggrunnen har en mye jevnere temperatur enn uteluft vil strømforbruket 
            være lavere sammenlignet med en luft-luft-varmepumpe. """)
        c1, c2 = st.columns(2)
        with c1:
            st.header('3) Miljøvennlig og lønnsom oppvarming')
            st.write(""" Du kan nå nyte en perfekt temperert bolig med en 
            energibesparende, fornybar og lønnsom teknologi. """)

            st.write(""" Har du bergvarmepumpe med energibrønn, 
            kan du få tilnærmet gratis kjøling. Om sommeren når det er behov for kjøling, 
            er temperaturen i brønnen i seg selv lav nok til å kjøle bygningen. 
            Dette kalles frikjøling. Da trenger vi som regel viftekonvektorer 
            som kan fordele kjøling på en komfortabel måte. 
            En slik konvektor er i prinsippet en radiator med vifte som effektivt sprer varm eller kald luft ut i rommet. """)

        with c2:
            image = Image.open('Grunnlagsdata/Bilder/Smart home-pana.png')
            st.image(image)
#----

#--OK--
class Innstillinger:
    def __init__(self):
        self.innstillinger()

    def egen_logo(self):
        image = Image.open('Grunnlagsdata/Bilder/egen_logo3.PNG')
        st.image(image)

    def tittel(self):
        return 'Bergvarmekalkulatoren'

    def favicon(self):
        return Image.open('Grunnlagsdata/Bilder/AsplanViak_Favicon_16x16.png')

    def forsidebilde(self):
        image = Image.open('Grunnlagsdata/Bilder/hovedlogo.png')
        st.image(image)

    def innstillinger(self):
        st.set_page_config(page_title=self.tittel(),page_icon=self.favicon(),layout="centered")
        hide_menu_style = """
                        <style>
                        #MainMenu {visibility: hidden; }
                        footer {visibility: hidden; }
                        </style>
        """
        st.markdown(hide_menu_style,unsafe_allow_html=True)

#--OK-- 
class Input:
    def __init__(self):
        self.lat = float
        self.long = float
        self.navn = str
        self.boligareal = int
        self.velg_boligareal()
        self.velg_postnummer()

    @st.cache
    def importer_postnummer(self):
        postnummer_df = pd.read_csv('Grunnlagsdata/Adresse/alle_postnummer.csv', sep=',', low_memory=False)
        return postnummer_df.iloc[:,1].to_numpy()

    def velg_postnummer(self):
        postnummer_liste = self.importer_postnummer()
        postnummer_liste = np.sort(postnummer_liste)
        valgt = st.multiselect('Skriv inn postnummer', postnummer_liste, 
        help=""" Adressen brukes til å hente inn nøyaktige temperaturdata 
        og nærliggende energibrønner. """)
        if len(valgt) > 1:
            st.error('Du må velge ett postnummer')
            st.stop()
        if valgt:
            self.valgt = valgt[0] 
            self.velg_adresse()

    @st.cache
    def importer_adresse(self):
        filnavn = 'Grunnlagsdata/Adresse/' + self.valgt + '.csv'
        adresse_df = pd.read_csv(filnavn, sep=',', low_memory=False)
        return adresse_df, adresse_df.iloc[:,1].to_numpy()

    def velg_adresse(self):
        adresse_df, adresse_liste = self.importer_adresse()
        adresse_liste = np.sort(adresse_liste)
        valgt = st.multiselect('Skriv inn adresse', adresse_liste, 
        help=""" Adressen brukes til å hente inn nøyaktige temperaturdata 
        og nærliggende energibrønner. """)
        if len(valgt) > 1:
            st.error('Du må velge en adresse')
            st.stop()
        if len(valgt) == 1:
            i=adresse_df[adresse_df['Navn']==valgt[0]]
            self.lat, self.long, self.navn = i.iat[0,3], i.iat[0,2], valgt[0]

    def velg_boligareal(self):
        self.boligareal = st.number_input('Oppgi oppvarmet areal [m\u00b2]?', min_value=100, value=150, max_value=1000, step=10, 
        help='Oppvarmet bruksareal er den delen av bruksarealet (BRA) som tilføres varme fra bygnings varmesystem')

#----

#--OK--
class Energibronn:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.les_csv(self.importer_csv())
        self.beregning()
        #self.dybde_til_fjell
        #self.energibronn_lat 
        #self.energibronn_long 

    @st.cache
    def importer_csv(self):
        energibronner_df = pd.read_csv('Grunnlagsdata/CSV/energibronner.csv', sep=';', on_bad_lines='skip', low_memory=False)
        return energibronner_df

    def les_csv(self, energibronner_df):
        self.energibronner_boret_lengde_til_berg = energibronner_df.iloc[:, 10]
        self.energibronner_lat = energibronner_df.iloc[:, -2]
        self.energibronner_long = energibronner_df.iloc[:, -3]

    def beregning(self):
        minste_distanse = 100000
        for i in range(0, len(self.energibronner_long)):
            distanse = mpu.haversine_distance((self.energibronner_lat.iloc[i], self.energibronner_long.iloc[i]),
                                              (self.lat, self.long))
            if minste_distanse > distanse:
                minste_distanse = distanse
                minste_i = i

        distanse_til_energibronn = round(distanse)
        dybde_til_fjell = round(self.energibronner_boret_lengde_til_berg.iloc[minste_i])
        energibronn_long = self.energibronner_long.iloc[minste_i]
        energibronn_lat = self.energibronner_lat.iloc[minste_i]
        if dybde_til_fjell > 50:
            dybde_til_fjell = 50
        self.dybde_til_fjell = dybde_til_fjell
        self.energibronn_lat = energibronn_lat
        self.energibronn_long = energibronn_long
#----

#--OK--
class Temperaturdata ():
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.stasjon_id, self.stasjon_lat, self.stasjon_long, self.distanse_min = self.nearmeste_stasjon()
        self.gjennomsnittstemperatur()
        #self.stasjon_id
        #self.stasjon_lat
        #self.stasjon_long
        #self.distanse_min
        #self.gjennomsnittstemperatur
        #self.gjsnitt_tekst

    @st.cache
    def temperaturserie_fra_fil(self):
        serie = 'Grunnlagsdata/Database/' + self.stasjon_id + '_temperatur.csv'
        temperatur_arr = pd.read_csv(serie, sep=',', on_bad_lines='skip').to_numpy()
        return temperatur_arr

    def gjennomsnittstemperatur(self):
        arr = self.temperaturserie_fra_fil()
        gjsnitt = float("{:.2f}".format(np.average(arr)))
        tekst = ''
        if gjsnitt < 3:
            tekst = """ Ettersom gjennomsnittstemperaturen er lav kan det være en 
            driftsstrategi å fryse grunnvannet i energibrønnen (merk at dette ikke 
            må gjøres hvis det er sensitive løsmasser / kvikkleire i området). """
        self.gjsnitt = gjsnitt
        self.gjsnitt_tekst = tekst

    @st.cache
    def importer_csv (self):
        stasjonsliste = pd.read_csv('Grunnlagsdata/Database/Stasjoner.csv', sep=',',on_bad_lines='skip')
        return stasjonsliste

    def nearmeste_stasjon (self):
        distanse_min = 1000000
        df = self.importer_csv()
        for i in range (0, len (df)):
            distanse = mpu.haversine_distance((df.iat [i,1], df.iat [i,2]), (self.lat, self.long))
            if distanse != 0 and distanse < distanse_min:
                distanse_min = distanse
                stasjon_id = df.iat [i,0]
                stasjon_lat = df.iat [i,1]
                stasjon_long = df.iat [i,2]
            
        return stasjon_id, stasjon_lat, stasjon_long, distanse_min
#----

#--OK--
class Stromregion:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.finn_region()
        #self.region

    def importer_fil(self):
        with open('Grunnlagsdata/CSV/regioner.geojson') as f:
            js = json.load(f)
        f.close()
        return js

    def finn_region(self):
        punkt = Point(self.long, self.lat)
        js = self.importer_fil()
        region = 0 #hvis den ikke finner noen
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(punkt):
                region = feature['properties']['ElSpotOmr']
                if region == 'NO 1':
                    region = 'Sørøst-Norge (NO1)'
                if region == 'NO 2':
                    region = 'Sørvest-Norge (NO2)'
                if region == 'NO 3':
                    region = 'Midt-Norge (NO3)'
                if region == 'NO 4':
                    region = 'Nord-Norge (NO4)'
                if region == 'NO 5':
                    region = 'Vest-Norge (NO5)'
        self.region = region
#----

#--OK--
class Energibehov():
    def __init__(self, bolig_areal, stasjon_id):
        self.bolig_areal = bolig_areal
        self.stasjon_id = stasjon_id
        #self.aarlig_behov()

        #self.dhw_sum
        #self.romoppvarming_sum
        #self.energibheov_sum

    #@st.cache
    def hent_behov_fra_fil(self):
        faktor = 1.25
        dhw = 'Grunnlagsdata/Database/' + self.stasjon_id + '_dhw.csv'
        romoppvarming = 'Grunnlagsdata/Database/' + self.stasjon_id + '_romoppvarming.csv'
        self.dhw_arr = (pd.read_csv(dhw, sep=',', on_bad_lines='skip').to_numpy() * self.bolig_areal) * faktor
        self.romoppvarming_arr = (pd.read_csv(romoppvarming, sep=',', on_bad_lines='skip').to_numpy() * self.bolig_areal) * faktor

    def behov(self):
        dhw_arr, romoppvarming_arr = self.hent_behov_fra_fil()

    def aarlig_behov(self):
        self.dhw_sum = int(sum(self.dhw_arr))
        self.romoppvarming_sum = int(sum(self.romoppvarming_arr))
        self.energibehov_sum = self.dhw_sum + self.romoppvarming_sum

    def resultater(self, dhw_sum, romoppvarming_sum, energibehov_sum):
        st.caption(""" Oppvarmingsbehovet er estimert ut ifra boligareal og adresse. Dette er den viktigste forutsetningen for beregningen av ditt bergvarmeanlegg. 
        Du kan justere oppvarmingsbehovet for din bolig i menyen til venstre.""")
        column_1, column_2, column_3 = st.columns(3)
        with column_1:
            st.metric(label="Årlig varmtvannsbehov", value=(str(int(round (dhw_sum,-1))) + " kWh"))
        with column_2:
            st.metric(label="Årlig romoppvarmingsebehov", value=(str(int(round(romoppvarming_sum, -1))) + " kWh"))
        with column_3:
            st.metric(label="Årlig oppvarmingsbehov", value=(str(int(round ((dhw_sum + romoppvarming_sum), -1))) + " kWh"))

    def plot(self, dhw_arr, romoppvarming_arr):
        dhw_arr = hour_to_month (dhw_arr)
        romoppvarming_arr = hour_to_month (romoppvarming_arr)
        months = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']
        x_axis = np.arange(len(months))

        data = pd.DataFrame({'Måneder' : months, 'Romoppvarmingsbehov' : romoppvarming_arr, 'Varmtvannsbehov' : dhw_arr, })
        c = alt.Chart(data).transform_fold(
            ['Romoppvarmingsbehov', 'Varmtvannsbehov'],
            as_=['Forklaring', 'Oppvarmingsbehov (kWh)']).mark_bar().encode(
            x=alt.X('Måneder:N', sort=months, title=None),
            y='Oppvarmingsbehov (kWh):Q',
            color=alt.Color('Forklaring:N', scale=alt.Scale(domain=['Romoppvarmingsbehov', 'Varmtvannsbehov'], 
            range=['#4a625c', '#8e9d99']), legend=alt.Legend(orient='top', direction='vertical', title=None)))
        st.altair_chart(c, use_container_width=True)
        
    def juster_behov(self, dhw_sum, romoppvarming_sum, dhw_arr, romoppvarming_arr):
        dhw_sum_ny = st.number_input('Varmtvann [kWh]', min_value = int(1000), 
        max_value = int(50000), value = round(dhw_sum, -1), step = int(500), help="""
        Erfaring viser at varmtvannsbehovet er avhengig av antall forbrukere og bør justeres etter dette. 
        Bor det mange i boligen bør det altså justeres opp. """)

        romoppvarming_sum_ny = st.number_input('Romoppvarming [kWh]', min_value = int(10000), 
        max_value = int(100000), value = round (romoppvarming_sum, -1), step = int(500), help= """
        Romoppvarmingsbehovet er beregnet basert på oppgitt oppvarmet areal og temperaturdata fra nærmeste værstasjon
        for de 30 siste år. """)
        dhw_prosent = dhw_sum_ny / dhw_sum
        romoppvarming_prosent = romoppvarming_sum_ny / romoppvarming_sum

        dhw_arr = dhw_arr * dhw_prosent
        romoppvarming_arr = romoppvarming_arr * romoppvarming_prosent

        return dhw_sum_ny, romoppvarming_sum_ny, dhw_arr, romoppvarming_arr
#----














    

@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-repeat: no-repeat;
        background-size: 1500px 350px;
        background-attachment : fixed;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

def hour_to_month (hourly_array):
    monthly_array = []
    summert = 0
    for i in range(0, len(hourly_array)):
        verdi = hourly_array[i]
        if np.isnan(verdi):
            verdi = 0
        summert = verdi + summert
        if i == 744 or i == 1416 or i == 2160 or i == 2880 \
                or i == 3624 or i == 4344 or i == 5088 or i == 5832 \
                or i == 6552 or i == 7296 or i == 8016 or i == 8759:
            monthly_array.append(int(summert))
            summert = 0
    return monthly_array  


class Veienvidere:
    def __init__(self):
        c1, c2 = st.columns(2)
        with st.expander('Forhandlersøk'):
            with c1:
                url = "https://www.varmepumpeinfo.no/forhandlersok"
                st.subheader("◈ [Finn leverandør](%s)" % url)

                url = "https://www.enova.no/privat/alle-energitiltak/varmepumper/vaske-til-vann-varmepumpe-/"
                st.subheader("◈ [ENOVA støtte](%s)" % url)

                url = "https://www.sparebank1.no/nb/ostlandet/privat/lan/boliglan/gront-boliglan/gront-energilan.html"
                st.subheader("◈ [Grønt energilån](%s)" % url)

        with c2:
            url4 = "https://share.streamlit.io/magnesyljuasen/bergvarmekalkulatoren_v2/main/main.py"
            st.subheader("◇ [Lær mer](%s)" % url4)

            url5 = "https://www.asplanviak.no/tjenester/grunnvarme/"
            st.subheader("◇ [Rådgivning](%s)" % url5)

        with st.expander('Du kan få billigere boliglån'):
            url = "https://www.smartepenger.no/lan/3408-gronne-boliglan"
            st.write("""Mange banker har begynt å tilby billigere 
            boliglån hvis boligen regnes som miljøvennlig; et såkalt [grønt boliglån](%s). For at boligen skal regnes som miljøvennlig
            må den være i energiklasse A) eller B) som er definert slik:
            """ % url)
            c1, c2 = st.columns(2)
            with c1:
                st.caption (""" A) Boligen har varmepumpe eller solenergi, i tillegg til 
                            bedre isolering og bedre vinduer enn hva som er standard eller 
                """)
            with c2:
                st.caption (""" B) Boligen har varmepumpe eller solenergi og/eller har bedre
                            isolasjon og vinduer enn kravene i byggeforskriftene. I tillegg til oppvarming og isolasjon vil type bolig,
                            byggeår og bruksareal påvirke energiklassen. 
            """)

            st.write(""" Å installere en energibrønn med varmepumpe vil altså plassere boligen din i energiklasse A) eller B) som igjen gir
            grunnlag for å søke om billigere boliglån. 
            """)


class Co2:
    def __init__(self):
        pass

    def juster_input(self):
        tekst = """ NVE publiserer hvert år klimadeklarasjon for fysisk levert strøm i Norge. Det 
            gjennomsnittlige direkte klimagassutslippet knyttet til bruk av strøm i Norge
            var 8 gram CO\u2082-ekvivalenter per kilowattime i 2020. Det er også andre tall som benyttes. """
        valgmuligheter = ['Norsk energimiks', 'Norsk-europeisk energimiks', 'Europeisk energimiks ']
        valg = st.selectbox('Klimagassutslipp knyttet til bruk av strøm', valgmuligheter, help=tekst, index=1) 
        if valg == valgmuligheter[0]:
            self.co2_per_kwh = 16.2 / 100000
        elif valg == valgmuligheter[1]:
            self.co2_per_kwh = 116.93 / 100000
        elif valg == valgmuligheter[2]:
            self.co2_per_kwh = 123 / 100000

        st.caption(f"""{int(self.co2_per_kwh * 100000)} gram CO\u2082-ekvivalenter per kWh""")
            

    def beregning(self, energibehov_hourly, kompressor_energi_y):
        co2_el_yearly = round(np.sum(energibehov_hourly) * self.co2_per_kwh)
        co2_gv_yearly = kompressor_energi_y * self.co2_per_kwh

        x_axis = np.array(range(1, 21))
        co2_el_ligning = co2_el_yearly * x_axis
        co2_gv_ligning = co2_gv_yearly * x_axis

        besparelse = round (co2_el_ligning[-1] - co2_gv_ligning[-1])

        st.caption('Forbrukt CO\u2082 etter 20 år:')
        res_column_1, res_column_2, res_column_3 = st.columns(3)
        with res_column_2:
            st.metric('Bergvarme', str(round (co2_gv_ligning[-1])) + ' tonn')
        with res_column_3:
            st.metric('Elektrisk oppvarming', str(round (co2_el_ligning[-1])) + ' tonn')
        with res_column_1:
            st.metric('Besparelse med bergvarme', str(besparelse) + ' tonn', delta='Miljøvennlig')

        flyreiser = int(round(besparelse * 1000 / 103,0)) 
        tekst = f""" CO\u2082 besparelsen med bergvarme tilsvarer {flyreiser} flyreiser mellom Oslo og Trondheim. """
        st.write(tekst)

        return co2_gv_yearly, co2_el_yearly

    def plotting(self, co2_gv_yearly, co2_el_yearly):
#        x_axis = np.array(range(1, 26))
#        co2_gv_ligning = co2_gv_yearly * x_axis
#        co2_el_ligning = co2_el_yearly * x_axis
#        data = pd.DataFrame({'År' : x_axis, 'Bergvarme' : co2_gv_ligning, 'Elektrisk oppvarming' : co2_el_ligning})
#        c = alt.Chart(data).transform_fold(
#            ['Bergvarme', 'Elektrisk oppvarming'],
#            as_=['Forklaring', 'CO2 utslipp (tonn)']).mark_line().encode(
#            x=alt.X('År:N', sort=x_axis),
#            y=alt.Y('CO2 utslipp (tonn):Q', title='CO\u2082 utslipp (tonn)'),
#            color=alt.Color('Forklaring:N', scale=alt.Scale(domain=['Bergvarme', 'Elektrisk oppvarming'], 
#            range=['#48a23f', '#880808']), legend=alt.Legend(orient='top', direction='vertical', title=None)))
#        st.altair_chart(c, use_container_width=True)

        co2_besparelse = co2_el_yearly - co2_gv_yearly

        
        #--1
        source = pd.DataFrame({"label" : ['CO\u2082 utslipp', 'CO\u2082 besparelse'], "value": [round(co2_gv_yearly*25), round(co2_besparelse*25)]})
        c1 = alt.Chart(source).mark_arc(innerRadius=35).encode(
            theta=alt.Theta(field="value", type="quantitative"),
            color=alt.Color(field="label", type="nominal", scale=alt.Scale(range=['#48a23f','#a23f47']), 
            legend=alt.Legend(orient='top', direction='vertical', title='Bergvarme'))).configure_view(strokeWidth=0)

        #--2
        source = pd.DataFrame({"label" : ['CO\u2082 utslipp'], "value": [co2_el_yearly*25]})
        c2 = alt.Chart(source).mark_arc(innerRadius=35).encode(
            theta=alt.Theta(field="value", type="quantitative"),
            color=alt.Color(field="label", type="nominal", scale=alt.Scale(range=['#a23f47']), 
            legend=alt.Legend(orient='top', direction='vertical', title='Elektrisk oppvarming'))).configure_view(strokeWidth=0)


        col1, col2 = st.columns(2)
        with col1:
            st.altair_chart(c1, use_container_width=True)
        with col2:
            st.altair_chart(c2, use_container_width=True)





class Kostnader:
    def __init__(self, dybde_til_fjell, varmepumpe_storrelse, antall_meter, kompressor, energibehov, el_pris):
        self.dybde_til_fjell = dybde_til_fjell
        self.varmepumpe_storrelse = varmepumpe_storrelse
        self.antall_meter = antall_meter
        self.kompressor_gv_hourly = kompressor
        self.energibehov_hourly = energibehov
        self.el_pris = el_pris

    def juster_investeringskostnad(self, investeringskostnad):
        return math.ceil(st.number_input('Komplett prisestimat for varmepumpe, montering og energibrønn [kr]', 
        min_value=1, value=investeringskostnad, max_value=750000, step=5000, help = 'Vannbåren varme er ikke tatt med i dette regnestykket'))


    def oppdater_dybde_til_fjell(self):
        tekst= (""" Dybde til fjell [m] er en viktig parameter for å beregne kostnaden for brønnboring. 
        Foreslått dybde til fjell er basert på målt dybde til fjell i nærmeste energibrønn. 
        Dybde til fjell har stor lokal variasjon og bør sjekkes mot Nasjonal database 
        for grunnundersøkelser (NADAG). Lenke: https://geo.ngu.no/kart/nadag-avansert/ """)
        #st.caption(tekst)
        self.dybde_til_fjell = st.number_input ('Oppgi dybde til fjell [m]', 
        value = self.dybde_til_fjell, min_value = 0, max_value = 150, help=tekst)
        
    def investeringskostnad (self):

        varmepumpe_pris = 141000
        if self.varmepumpe_storrelse > 12:
            varmepumpe_pris = math.ceil(varmepumpe_pris + (self.varmepumpe_storrelse - 12) * 10000)
            
        
        etablering_pris = 3500
        odex_sko_pris = 575
        bunnlodd_pris = 1000
        lokk_pris = 700
        odex_i_losmasser_pris = 700  # per meter
        fjellboring_pris = 170  # per meter
        kollektor_pris = 90  # per meter

        antall_meter = self.antall_meter
        dybde_til_fjell = self.dybde_til_fjell

        kollektor = (antall_meter - 1) * kollektor_pris
        boring = ((antall_meter - dybde_til_fjell) * fjellboring_pris) + (dybde_til_fjell * odex_i_losmasser_pris)
        boring_faste_kostnader = etablering_pris + odex_sko_pris + bunnlodd_pris + lokk_pris

        energibronn_pris = math.ceil(kollektor) + math.ceil(boring) + math.ceil(boring_faste_kostnader)

        komplett_pris = energibronn_pris + varmepumpe_pris

        return komplett_pris

    def plot_investeringskostnad(self, investeringskostnad):
        x_axis = np.array(range(1, 26))
        el_ligning = self.kostnad_el_yearly * x_axis
        gv_ligning = self.kostnad_gv_yearly * x_axis + investeringskostnad
        self.nedbetalingstid = round(investeringskostnad / (self.kostnad_el_yearly - self.kostnad_gv_yearly))
        self.besparelse = round (el_ligning [-1] - gv_ligning [-1], -2)

        data = pd.DataFrame({'År' : x_axis, 'Bergvarme' : gv_ligning, 'Elektrisk oppvarming' : el_ligning})
        c = alt.Chart(data).transform_fold(
            ['Bergvarme', 'Elektrisk oppvarming'],
            as_=['Forklaring', 'Kroner']).mark_line().encode(
            x=alt.X('År:N', sort=x_axis),
            y=alt.Y('Kroner:Q', title='Kostnader (kr)'),
            color=alt.Color('Forklaring:N', scale=alt.Scale(domain=['Bergvarme', 'Elektrisk oppvarming'], 
            range=['#48a23f', '#a23f47']), legend=alt.Legend(orient='top', direction='vertical', title=None)))
        st.altair_chart(c, use_container_width=True)
        
        res_column_1, res_column_2, res_column_3 = st.columns(3)
        with res_column_1:
            st.metric('Estimert investeringskostnad', str(investeringskostnad) + ' kr')
        with res_column_2:
            st.metric('Nedbetalingstid', str(self.nedbetalingstid) + ' år')
        with res_column_3:
            st.metric('Gevinst etter 25 år', str(self.besparelse) + ' kr')


    def monthly_costs (self):
        kostnad_el_hourly = self.energibehov_hourly * self.el_pris
        kostnad_gv_hourly = self.kompressor_gv_hourly * self.el_pris

        kostnad_el_monthly = hour_to_month(kostnad_el_hourly)
        kostnad_gv_monthly = hour_to_month(kostnad_gv_hourly)

        kostnad_el_yearly = int(np.nansum(kostnad_el_monthly))
        kostnad_gv_yearly = int(np.nansum(kostnad_gv_monthly))
        self.kostnad_el_yearly = kostnad_el_yearly
        self.kostnad_gv_yearly = kostnad_gv_yearly

        besparelse = round (kostnad_el_yearly - kostnad_gv_yearly, -2)
        if besparelse > 0:
            d = 'Lønnsomt'
            d_c = 'normal'
        elif besparelse < 0:
            d = 'Ikke lønnsomt'
            d_c = 'off'
                 
        st.caption("""Figuren under viser årlige driftskostnader med bergvarme kontra elektrisk oppvarming. 
        I dette regnestykket er ikke investeringskostnaden inkludert. Bergvarme gir en god strømbesparelse som reduserer din månedlige strømregning.""")
        cost_column_1, cost_column_2, cost_column_3 = st.columns(3)
        with cost_column_2:
            st.metric(label="Bergvarme", value=(str(round(kostnad_gv_yearly, -2)) + " kr/år"))
        with cost_column_3:
            st.metric(label="Elektrisk oppvarming", value=(str(round(kostnad_el_yearly, -2)) + " kr/år"))
        with cost_column_1:
            st.metric('Besparelse med bergvarme', str(round (kostnad_el_yearly - kostnad_gv_yearly, -2)) + ' kr/år', delta=d, delta_color=d_c)
        
        return kostnad_gv_monthly, kostnad_el_monthly

    def fyring_input(self):
        #nedbetalingstid = st.number_input('Nedbetalingstid [år]', value=20, min_value=1, max_value=25,step=1)
        nedbetalingstid = 20
        effektiv_rente = st.number_input('Effektiv rente [%]', value=2.44, min_value=1.00, max_value=10.00) / 100
        return nedbetalingstid, effektiv_rente

    def fyring_costs (self, investeringskostnad, nedbetalingtid, effektiv_rente):
            #pslag = (investeringskostnad / 20) / 8600
            kostnad_el_hourly = self.energibehov_hourly * self.el_pris
            kostnad_gv_hourly = self.kompressor_gv_hourly * self.el_pris #+ pslag

            kostnad_el_monthly = hour_to_month(kostnad_el_hourly)
            kostnad_gv_monthly = hour_to_month(kostnad_gv_hourly) 

            monthly_antall = nedbetalingtid * 12
            monthly_rente = effektiv_rente / 12
            termin_monthly = investeringskostnad / ((1 - (1 / (1 + monthly_rente) ** monthly_antall)) / monthly_rente)
            termin_yearly = termin_monthly * 12

            kostnad_el_yearly = int(np.nansum(kostnad_el_monthly))
            kostnad_gv_yearly = int(np.nansum(kostnad_gv_monthly)) + int(termin_yearly)
            self.kostnad_el_yearly = kostnad_el_yearly
            self.kostnad_gv_yearly = kostnad_gv_yearly

            besparelse = round (kostnad_el_yearly - kostnad_gv_yearly, -2)
            if besparelse > 0:
                d = 'Lønnsomt'
                d_c = 'normal'
            elif besparelse < 0:
                d = 'Ikke lønnsomt'
                d_c = 'off'

            cost_column_1, cost_column_2, cost_column_3 = st.columns(3)
            with cost_column_2:
                st.metric(label="Bergvarme", value=(str(round(kostnad_gv_yearly, -2)) + " kr/år"))
            with cost_column_3:
                st.metric(label="Elektrisk oppvarming", value=(str(round(kostnad_el_yearly, -2)) + " kr/år"))
            with cost_column_1:
                st.metric('Besparelse med bergvarme', str(round (kostnad_el_yearly - kostnad_gv_yearly, -2)) + ' kr/år', delta=d, delta_color=d_c)

            kostnad_gv_monthly = np.array(kostnad_gv_monthly) + termin_yearly/12
            return kostnad_gv_monthly, kostnad_el_monthly

    def fyring_costs_plot(self, kostnad_gv_monthly, kostnad_el_monthly):         
        months = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']
        wide_form = pd.DataFrame({
            'Måneder' : months,
            'Bergvarme' : kostnad_gv_monthly, 
            'Elektrisk oppvarming' : kostnad_el_monthly})

        c1 = alt.Chart(wide_form).transform_fold(
            ['Bergvarme', 'Elektrisk oppvarming'],
            as_=['key', 'Kostnader (kr)']).mark_bar(opacity=1).encode(
                x=alt.X('Måneder:N', sort=months, title=None),
                y=alt.Y('Kostnader (kr):Q',stack=None),
                color=alt.Color('key:N', scale=alt.Scale(domain=['Bergvarme'], 
                range=['#48a23f']), legend=alt.Legend(orient='top', direction='vertical', title=None))).configure_view(strokeWidth=0)

        c2 = alt.Chart(wide_form).transform_fold(
            ['Bergvarme', 'Elektrisk oppvarming'],
            as_=['key', 'Kostnader (kr)']).mark_bar(opacity=1).encode(
                x=alt.X('Måneder:N', sort=months, title=None),
                y=alt.Y('Kostnader (kr):Q',stack=None, title=None),
                color=alt.Color('key:N', scale=alt.Scale(domain=['Elektrisk oppvarming'], 
                range=['#880808']), legend=alt.Legend(orient='top', direction='vertical', title=None))).configure_view(strokeWidth=0)
        col1, col2 = st.columns(2)
        with col1:
            st.altair_chart(c1, use_container_width=True)  
        with col2:
            st.altair_chart(c2, use_container_width=True)  


    def gronne_laan (self):
        x_axis = np.array(range(1, 26))
        x_axis_laan = np.array(range(1, 27))
        c1, c2 = st.columns(2)
        with c1:
            nedbetalingstid = st.number_input('Nedbetalingstid energilån [år]', value=20, min_value=1, max_value=25,step=1)
        with c2:
            effektiv_rente = st.number_input('Effektiv rente [%]', value=2.44, min_value=1.00, max_value=10.00) / 100

        monthly_antall = nedbetalingstid * 12
        monthly_rente = effektiv_rente / 12
        termin_monthly = self.investeringskostnad() / ((1 - (1 / (1 + monthly_rente) ** monthly_antall)) / monthly_rente)
        termin_yearly = termin_monthly * 12

        el_ligning = self.kostnad_el_yearly * x_axis
        gv_ligning_1 = []
        gv_ligning_2 = []

        j = -1
        for i in range(1, len(x_axis_laan)):
            if i <= nedbetalingstid:
                verdi = (self.kostnad_gv_yearly + termin_yearly) * i
                gv_ligning_1.append(verdi)
            if i >= nedbetalingstid:
                j += 1
                x_axis_laan[i] = i
                gv_ligning_2.append(self.kostnad_gv_yearly * j + verdi)

        gv_ligning = gv_ligning_1 + gv_ligning_2

class Strompriser ():
    def __init__(self, region):
        self.region = region

    def input (self):
        self.year = st.selectbox('Hvilken årlig strømpris skal ligge til grunn?',('2021', '2020', '2019', '2018', 
        'Gjennomsnitt av de siste 4 år'), help="""
        Det er hentet inn historisk strømpris per time for de siste 4 år.
        Velg den som skal ligge til grunn for beregningen. 
        """)
        self.nettleie = st.number_input('Nettleie [øre/kWh]', value=float(27.9), step=0.25) / 100
        self.fastledd = st.number_input('Fastledd [kr/år]', value=int(1380), step=100) / 8600

    @st.cache
    def el_spot_pris (self):
        if self.year == '2018':
            el_spot_hourly = pd.read_csv('Grunnlagsdata/CSV/el_spot_hourly_2018.csv', sep=';', on_bad_lines='skip')
        if self.year == '2019':
            el_spot_hourly = pd.read_csv('Grunnlagsdata/CSV/el_spot_hourly_2019.csv', sep=';', on_bad_lines='skip')
        if self.year == '2020':
            el_spot_hourly = pd.read_csv('Grunnlagsdata/CSV/el_spot_hourly_2020.csv', sep=';', on_bad_lines='skip')
        if self.year == '2021':
            el_spot_hourly = pd.read_csv('Grunnlagsdata/CSV/el_spot_hourly_2021.csv', sep=';', on_bad_lines='skip')
        return el_spot_hourly

    def el_pris (self):
        elavgift = 16.69 / 100
        pslag = 0
        moms = 1.25
        nettleie = self.nettleie
        fastledd = self.fastledd

        if self.region == 'Sørøst-Norge (NO1)' or self.region == 0:
            el_pris_hourly = (self.el_spot_pris().iloc[:, 3] / 1000 + nettleie + elavgift + fastledd + pslag) * moms
        if self.region == 'Sørvest-Norge (NO2)':
            el_pris_hourly = (self.el_spot_pris().iloc[:, 4] / 1000 + nettleie + elavgift + fastledd + pslag) * moms
        if self.region == 'Midt-Norge (NO3)':
            el_pris_hourly = (self.el_spot_pris().iloc[:, 5] / 1000 + nettleie + elavgift + fastledd + pslag) * moms
        if self.region == 'Nord-Norge (NO4)':
            el_pris_hourly = (self.el_spot_pris().iloc[:, 6] / 1000 + nettleie + elavgift + fastledd + pslag) * moms
        if self.region == 'Vest-Norge (NO5)':
            el_pris_hourly = (self.el_spot_pris().iloc[:, 7] / 1000 + nettleie + elavgift + fastledd + pslag) * moms

        el_pris_hourly = np.array(el_pris_hourly)
        el_pris_hourly = np.resize(el_pris_hourly, 8760)

        return el_pris_hourly

    def beregn_el_pris (self):
        if self.year == 'Gjennomsnitt av de siste 4 år':
            gjennomsnitt_el_pris = 0
            for year in ['2018', '2019', '2020', '2021']:
                self.year = year
                el_pris_hourly = self.el_pris ()
                gjennomsnitt_el_pris += el_pris_hourly
            return gjennomsnitt_el_pris / 4
        else:
            return self.el_pris ()
        

class Dimensjonering:
    def __init__(self):
        pass

    @st.cache
    def energi_og_effekt_beregning(self, dekningsgrad, energibehov_arr, energibehov_sum):
        varmepumpe_storrelse = max(energibehov_arr)
        beregnet_dekningsgrad = 100.5
        if dekningsgrad == 100:
            return np.array(energibehov_arr), round(np.sum(energibehov_arr)), float("{:.1f}".format(varmepumpe_storrelse))

        while (beregnet_dekningsgrad / dekningsgrad) > 1:
            tmp_liste_h = np.zeros (8760)
            for i, timeverdi in enumerate (energibehov_arr):
                if timeverdi > varmepumpe_storrelse:
                    tmp_liste_h[i] = varmepumpe_storrelse
                else:
                    tmp_liste_h[i] = timeverdi
            
            beregnet_dekningsgrad = (sum (tmp_liste_h) / energibehov_sum) * 100

            varmepumpe_storrelse -= 0.05

        if varmepumpe_storrelse < 6:
            varmepumpe_storrelse == 6
        if varmepumpe_storrelse > 6 and varmepumpe_storrelse < 8:
            varmepumpe_storrelse = 8
        if varmepumpe_storrelse > 8 and varmepumpe_storrelse < 10:
            varmepumpe_storrelse = 10
        if varmepumpe_storrelse > 10 and varmepumpe_storrelse < 12:
            varmepumpe_storrelse = 12
        if varmepumpe_storrelse > 12 and varmepumpe_storrelse < 15:
            varmepumpe_storrelse = 15
        if varmepumpe_storrelse > 14 and varmepumpe_storrelse > 17:
            varmepumpe_storrelse = 17
        
        return np.array (tmp_liste_h), round (np.sum (tmp_liste_h)), float("{:.1f}".format(varmepumpe_storrelse))

    def angi_dekningsgrad(self):
        return st.number_input('Energidekningsgrad for bergvarme [%]', value=100, 
        min_value=80, max_value=100, step = 1, help='Vanligvis settes dekningsgraden til 100% ' 
        'som betyr at bergvarmeanlegget skal dekke hele energibehovet.' 
        ' Dersom dekningsgraden er mindre enn dette skal energikilder som vedfyring eller strøm dekke behovet de kaldeste dagene.')

    def angi_cop(self):
        return st.number_input('Årsvarmefaktor (SCOP) til varmepumpen', value=3.5, min_value=2.0, 
        max_value=4.0, step = 0.1, help='Årsvarmefaktoren avgjør hvor mye ' 
        'energi du sparer med et varmepumpeanlegg; den uttrykker hvor ' 
        'mye varmeenergi anlegget leverer i forhold til hvor mye elektrisk energi det bruker i løpet av et år.')

    def dekning(self, energibehov_arr_gv, energibehov_arr, cop):
        levert_fra_bronner_arr = energibehov_arr_gv - energibehov_arr_gv / cop
        kompressor_arr = energibehov_arr_gv - levert_fra_bronner_arr
        spisslast_arr = energibehov_arr - energibehov_arr_gv

        levert_fra_bronner_sum = int(sum(levert_fra_bronner_arr))
        kompressor_sum = int(sum(kompressor_arr))
        spisslast_sum = int(sum(spisslast_arr))

        return levert_fra_bronner_arr, kompressor_arr, spisslast_arr, levert_fra_bronner_sum, kompressor_sum, spisslast_sum

    def energi_resultater(self, levert_fra_bronner_sum, kompressor_sum, spisslast_sum):
        column_1, column_2, column_3 = st.columns(3)
        with column_1:
            st.metric(label="Levert energi fra brønner", value=(str(round (levert_fra_bronner_sum, -1)) + " kWh"))
        with column_2:
            st.metric(label="Strømforbruk varmepumpe", value=(str(round (kompressor_sum, -1)) + " kWh"))
        with column_3:
            st.metric(label="Spisslast", value=(str(round (spisslast_sum, -1)) + " kWh"))

    def varighetsdiagram(self, energibehov_arr, energibehov_arr_gv, kompressor_arr):

        wide_form = pd.DataFrame({
            'Varighet (timer)' : np.array(range(0, len(energibehov_arr))),
            'Spisslast (ikke bergvarme)' : np.sort(energibehov_arr)[::-1], 
            'Levert energi fra brønn(er)' : np.sort(energibehov_arr_gv)[::-1],
            'Strømforbruk varmepumpe' : np.sort(kompressor_arr)[::-1]
            })

        c = alt.Chart(wide_form).transform_fold(
            ['Spisslast (ikke bergvarme)', 'Levert energi fra brønn(er)', 'Strømforbruk varmepumpe'],
            as_=['key', 'Effekt (kW)']).mark_area().encode(
                x=alt.X('Varighet (timer):Q', scale=alt.Scale(domain=[0, 8760])),
                y='Effekt (kW):Q',
                color=alt.Color('key:N', scale=alt.Scale(domain=['Spisslast (ikke bergvarme)', 'Levert energi fra brønn(er)', 'Strømforbruk varmepumpe'], 
                range=['#ffdb9a', '#48a23f', '#1d3c34']), legend=alt.Legend(orient='top', direction='vertical', title=None))
            )

        st.altair_chart(c, use_container_width=True)

    def varighetsdiagram_bar(self, spisslast_arr, energibehov_arr_gv, kompressor_arr, levert_fra_bronner_arr):
        spisslast_arr = hour_to_month (spisslast_arr)
        energibehov_arr_gv = hour_to_month (energibehov_arr_gv)
        kompressor_arr = hour_to_month (kompressor_arr)
        levert_fra_bronner_arr = hour_to_month (levert_fra_bronner_arr)

        months = ['jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']
        x_axis = np.arange(len(months))

        data = pd.DataFrame({'Måneder' : months, 'Levert energi fra brønn(er)' : levert_fra_bronner_arr, 'Strømforbruk varmepumpe' : kompressor_arr, })
        c = alt.Chart(data).transform_fold(
            ['Levert energi fra brønn(er)', 'Strømforbruk varmepumpe'],
            as_=['Forklaring', 'Oppvarmingsbehov (kWh)']).mark_bar().encode(
            x=alt.X('Måneder:N', sort=months),
            y='Oppvarmingsbehov (kWh):Q',
            color=alt.Color('Forklaring:N', scale=alt.Scale(domain=['Levert energi fra brønn(er)', 'Strømforbruk varmepumpe'], 
            range=['#48a23f', '#1d3c34']), legend=alt.Legend(orient='top', direction='vertical', title=None)))
        st.altair_chart(c, use_container_width=True)

    def antall_meter(self, varmepumpe_storrelse, levert_fra_bronner, cop, gjennomsnittstemperatur):
        
        energi_per_meter = 0.0011*gjennomsnittstemperatur**4 - 0.0537*gjennomsnittstemperatur**3 + 1.0318*gjennomsnittstemperatur**2 + 6.2816*gjennomsnittstemperatur + 36.192
        if energi_per_meter > 120:
            energi_per_meter = 120
        if energi_per_meter < 50:
            energi_per_meter = 50
        
        #effekt_per_meter = 100  # kriterie 2

        #antall_meter_effekt = ((varmepumpe_storrelse - varmepumpe_storrelse / cop) * 1000) / effekt_per_meter
        antall_meter_energi = (levert_fra_bronner) / energi_per_meter

        #if antall_meter_effekt < antall_meter_energi:
        #    antall_meter_tot = antall_meter_energi
        #else:
        #    antall_meter_tot = antall_meter_effekt

        return math.ceil(antall_meter_energi)

    def antall_bronner(self, antall_meter):
        bronnlengde = 0
        for i in range(1,10):
            bronnlengde += 350
            if antall_meter <= bronnlengde:
                return i

    def bronn_resultater(self, antall_meter, varmepumpe_storrelse, antall_bronner):
        tekst = " brønn"
        if antall_bronner > 1:
            tekst = " brønner"
        column_1, column_2, column_3 = st.columns(3)
        with column_1:
            st.metric(label="Brønndybde", value=str(antall_meter) + " m")
        with column_2:
            st.metric(label="Varmepumpestørrelse", value=str(math.ceil(varmepumpe_storrelse)) + " kW")
        with column_3:
            st.metric(label='Antall brønner', value = str(antall_bronner) + tekst)

















#--





class Gis:
    def __init__(self):
        pass

    def adresse_til_koordinat (self, adresse):
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(adresse, timeout=None, country_codes='NO', exactly_one=True)
        if location is None:
            st.error ('Ugyldig adresse. Prøv igjen!')
            #lott = load_lottie('https://assets2.lottiefiles.com/packages/lf20_i0hpsr18.json')
            #st_lottie(lott)
            st.stop()
        lat = location.latitude
        long = location.longitude
        return lat, long

    def kart(self, stasjon_lat, adresse_lat, energibronn_lat, stasjon_long, adresse_long, energibronn_long):
        df1 = pd.DataFrame({'latitude': [stasjon_lat],'longitude': [stasjon_long]})
        df2 = pd.DataFrame({'latitude': [adresse_lat],'longitude': [adresse_long]})
        df3 = pd.DataFrame({'latitude': [energibronn_lat],'longitude': [energibronn_long]})
    
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/streets-v11',
            initial_view_state=pdk.ViewState(
                latitude=adresse_lat,
                longitude=adresse_long,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    type='ScatterplotLayer',
                    data=df1,
                    get_position='[longitude, latitude]',
                    pickable=True,
                    stroked=True,
                    radius_max_pixels=10,
                    radius_min_pixels=500,
                    filled=True,
                    line_width_scale=25,
                    line_width_max_pixels=5,
                    get_fill_color=[255, 195, 88],
                    get_line_color=[0, 0, 0]
                ),
                pdk.Layer(
                    type='ScatterplotLayer',
                    data=df2,
                    get_position='[longitude, latitude]',
                    pickable=True,
                    stroked=True,
                    radius_max_pixels=20,
                    radius_min_pixels=500,
                    filled=True,
                    line_width_scale=25,
                    line_width_max_pixels=5,
                    get_fill_color=[29, 60, 52],
                    get_line_color=[29, 60, 52],
                ),
                pdk.Layer(
                    type='ScatterplotLayer',
                    data=df3,
                    get_position='[longitude, latitude]',
                    pickable=True,
                    stroked=True,
                    radius_max_pixels=10,
                    radius_min_pixels=500,
                    filled=True,
                    line_width_scale=25,
                    line_width_max_pixels=5,
                    get_fill_color=[183, 220, 143],
                    get_line_color=[0, 0, 0]
                ),
            ],
        ))





