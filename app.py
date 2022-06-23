import streamlit as st
from funksjoner import Dimensjonering, Gis, Energibronn, Strompriser, Temperaturdata, Energibehov, Kostnader, Co2, Stromregion, Forklaringer, load_lottie
import numpy as np
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div


def beregning(adresse_lat, adresse_long, bolig_areal, navn):
    if adresse_long:
        energibronn_obj = Energibronn(adresse_lat, adresse_long)
        temperaturdata_obj = Temperaturdata(adresse_lat, adresse_long)
        stromregion_obj = Stromregion(adresse_lat, adresse_long)

        with st.sidebar:
            st.header("Forutsetninger")

        energibehov_obj = Energibehov(bolig_areal, temperaturdata_obj.stasjon_id)
        energibehov_obj.hent_behov_fra_fil()
        energibehov_obj.aarlig_behov()

        dhw_arr = energibehov_obj.dhw_arr
        romoppvarming_arr = energibehov_obj.romoppvarming_arr
        dhw_sum = energibehov_obj.dhw_sum
        romoppvarming_sum = energibehov_obj.romoppvarming_sum
        energibehov_sum = energibehov_obj.energibehov_sum
        gjennomsnittstemperatur = temperaturdata_obj.gjsnitt
        tekst = temperaturdata_obj.gjsnitt_tekst
        region = stromregion_obj.region
        dybde_til_fjell = energibronn_obj.dybde_til_fjell
        energibronn_lat = energibronn_obj.energibronn_lat
        energibronn_long = energibronn_obj.energibronn_long
        stasjon_lat = temperaturdata_obj.stasjon_lat
        stasjon_long = temperaturdata_obj.stasjon_long
        stasjon_id = temperaturdata_obj.stasjon_id
        
        #--Sidebar--
        with st.sidebar:
            with st.expander('Oppvarmingsbehov'):
                #st.caption("""Oppvarmingsbehovet er estimert ut ifra oppgitt areal og adresse. 
                #Estimerte verdier vises i boksene under. Du kan fritt justere verdiene. """)
            
                #energibehov_obj.resultater(dhw_sum, romoppvarming_sum, energibehov_sum)
                dhw_sum, romoppvarming_sum, dhw_arr, romoppvarming_arr = energibehov_obj.juster_behov(dhw_sum, romoppvarming_sum, dhw_arr, romoppvarming_arr)
                energibehov_obj.plot(dhw_arr, romoppvarming_arr)

        #--Sidebar--

        energibehov_arr = (dhw_arr + romoppvarming_arr).reshape(-1)
        energibehov_sum = np.sum(energibehov_arr)
        dimensjonering_obj = Dimensjonering()

        #--Sidebar--
        with st.sidebar:
            with st.expander('Dekningsgrad og årsvarmefaktor'):       
                dekningsgrad = dimensjonering_obj.angi_dekningsgrad()
                cop = dimensjonering_obj.angi_cop()
        #--Sidebar--

        energibehov_arr_gv, energibehov_sum_gv, varmepumpe_storrelse = dimensjonering_obj.energi_og_effekt_beregning(dekningsgrad, energibehov_arr, energibehov_sum)
        levert_fra_bronner_arr, kompressor_arr, spisslast_arr, levert_fra_bronner_sum, kompressor_sum, spisslast_sum = dimensjonering_obj.dekning(energibehov_arr_gv, energibehov_arr, cop)
        antall_meter = dimensjonering_obj.antall_meter(varmepumpe_storrelse, levert_fra_bronner_sum, cop, gjennomsnittstemperatur)
        antall_bronner = dimensjonering_obj.antall_bronner (antall_meter)

    

        strompriser_obj = Strompriser(region)

        #--Sidebar--
        with st.sidebar:   
            with st.expander('Strømpris'):
                strompriser_obj.input()
        #--Sidebar--

        el_pris = strompriser_obj.beregn_el_pris()
        kostnader_obj = Kostnader(dybde_til_fjell, varmepumpe_storrelse, antall_meter, kompressor_arr, energibehov_arr_gv, el_pris)
        
        #--Sidebar--
        with st.sidebar:
            with st.expander('Dybde til fjell'):   
                kostnader_obj.oppdater_dybde_til_fjell()
        #--Sidebar--
        #energibehov_obj.resultater(dhw_sum, romoppvarming_sum, energibehov_sum)
        #st.markdown("""---""")
        st.title("""Resultater""")
        st.markdown(""" **_Resultatene fra bergvarmekalkulatoren er å anse som estimater, og skal ikke brukes for endelig dimensjonering av energibrønn med varmepumpe. 
            Dimensjonering må tilpasses de stedlige forholdene av leverandør._** """)

        st.markdown(""" *_Trykk på boksene under for å se resultatene. Du kan endre forutsetningene for beregningene i menyen til venstre.
        Oppvarmingsbehovet er den viktigste forutsetningen og er estimert ut ifra oppgitt oppvarmet areal og adresse._* """)
        
        with st.sidebar:
            with st.expander('Kart'):
                Gis().kart(stasjon_lat, adresse_lat, energibronn_lat, stasjon_long, adresse_long, energibronn_long)
                st.write (f""" Kartet viser adresse (mørkegrønn farge), nærmeste eksisterende energibrønn (grønn farge) 
                og nærmeste værstasjon, {stasjon_id}, med fullstendige temperaturdata (solgul farge). 
                Nærmeste eksisterende energibrønn brukes til å estimere dybde til fjell i området. Fra værstasjonen hentes det 
                inn målt temperatur per time for de siste 30 år. Gjennomsnittstemperaturen
                er målt til å være {gjennomsnittstemperatur} \u2103. {tekst} Strømregionen er {region}. """)
        
        investeringskostnad = kostnader_obj.investeringskostnad()
        with st.sidebar:
            with st.expander('Investering'):
                investeringskostnad = kostnader_obj.juster_investeringskostnad(investeringskostnad)
                nedbetalingtid, effektiv_rente = kostnader_obj.fyring_input()
        #st.header('Kostnader')
        with st.expander('Kostnader'):
            st.subheader("Drift")
            kostnad_gv_monthly, kostnad_el_monthly = kostnader_obj.monthly_costs()
            kostnader_obj.fyring_costs_plot(kostnad_gv_monthly, kostnad_el_monthly)
            st.markdown("""---""")
            st.subheader("Investering og drift over 20 år")
            st.write(f"""Figuren under viser årlige kostnader til oppvarming inkl. investeringskostnad. 
            Det er forutsatt at investeringen nedbetales i løpet av {int(nedbetalingtid)} år 
            med en effektiv rente på {float("{:.4f}".format(effektiv_rente * 100)) } %. """)            
            kostnad_gv_monthly, kostnad_el_monthly, total_besparelse = kostnader_obj.fyring_costs(investeringskostnad, nedbetalingtid, effektiv_rente)
            kostnader_obj.fyring_costs_plot(kostnad_gv_monthly, kostnad_el_monthly)
            if total_besparelse < 0:
                st.warning('Bergvarme er ikke lønnsomt etter 20 år ut ifra oppgitte forutsetninger.')
            else:
                st.write(f"""_Etter 20 år vil du ha spart til sammen **{total_besparelse} kr** på varme opp boligen med bergvarme istedenfor elektrisk oppvarming._ """)
            st.markdown("""---""")
            st.subheader("Investering")
            st.write("""Investeringskostnaden omfatter en komplett installsjon av bergvarme inkl. varmepumpe, montering og energibrønn. 
            Merk at dette er et estimat, og endelig pris må fastsettes av leverandør. """)
            st.metric('Investeringskostnad bergvarme', str(investeringskostnad) + ' kr')
        co2 = Co2()
        with st.sidebar:
            with st.expander('Klimagassutslipp'):
                co2.juster_input()
        #st.header('Klimagassutslipp'):
        with st.expander('Klimagassutslipp'):
            co2_gv_yearly, co2_el_yearly, flyreiser = co2.beregning(energibehov_arr, kompressor_sum)
            #with st.expander('Se graf'):
            co2.plotting(co2_gv_yearly, co2_el_yearly)
            st.write(f"""_CO\u2082 besparelsen med bergvarme tilsvarer **{flyreiser} flyreiser** mellom Oslo og Trondheim._ """)

        #st.header('Dimensjonering')
        with st.expander('Dimensjonering'):
            st.markdown(""" Vi har dimensjonert et _bergvarmeanlegg for din bolig_ ut ifra oppgitte forutsetninger. 
            Merk at dette er et estimat, og endelig dimensjonering skal utføres av leverandør.""")

            #with st.expander('Se graf'):
            dimensjonering_obj.bronn_resultater(antall_meter, varmepumpe_storrelse, antall_bronner)
            dimensjonering_obj.varighetsdiagram(energibehov_arr, energibehov_arr_gv, kompressor_arr)
        
        st.markdown(""" --- """)
        url = 'https://www.varmepumpeinfo.no/varmepumpe'
        st.header("[Trykk her for å finne leverandør av bergvarmeanlegg!](%s)" % url)

        
#        if st.button('Trykk her for å finne nærmeste leverandør av bergvarmeanlegg!'):
#            js = "window.open('https://www.varmepumpeinfo.no/varmepumpe')"  # New tab or window
#            html = '<img src onerror="{}">'.format(js)
#            div = Div(text=html)
#            st.bokeh_chart(div)
    

    #st_lottie(load_lottie('https://assets5.lottiefiles.com/packages/lf20_l22gyrgm.json'))  
    #st.caption('Et verktøy fra Asplan Viak AS | 📧 magne.syljuasen@asplanviak.no')



    