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
            with st.expander('Dekningsgrad og ??rsvarmefaktor'):       
                dekningsgrad, cop = dimensjonering_obj.angi_dekningsgrad_og_cop()
        #--Sidebar--

        energibehov_arr_gv, energibehov_sum_gv, varmepumpe_storrelse = dimensjonering_obj.energi_og_effekt_beregning(dekningsgrad, energibehov_arr, energibehov_sum)
        levert_fra_bronner_arr, kompressor_arr, spisslast_arr, levert_fra_bronner_sum, kompressor_sum, spisslast_sum = dimensjonering_obj.dekning(energibehov_arr_gv, energibehov_arr, cop)
        antall_meter = dimensjonering_obj.antall_meter(varmepumpe_storrelse, levert_fra_bronner_sum, cop, gjennomsnittstemperatur)
        antall_bronner = dimensjonering_obj.antall_bronner (antall_meter)

    

        strompriser_obj = Strompriser(region)

        #--Sidebar--
        with st.sidebar:   
            with st.expander('Str??mpris'):
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
        st.markdown(""" **_Resultatene fra bergvarmekalkulatoren er ?? anse som estimater, og skal ikke brukes for endelig dimensjonering av energibr??nn med varmepumpe. 
            Dimensjonering m?? tilpasses de stedlige forholdene av leverand??r._** """)

        st.markdown(""" *_Trykk p?? boksene under for ?? se resultatene. Du kan endre forutsetningene for beregningene i menyen til venstre.
        Oppvarmingsbehovet er den viktigste forutsetningen og er estimert ut ifra oppgitt oppvarmet areal og adresse._* """)
        
        investeringskostnad = kostnader_obj.investeringskostnad()
        with st.sidebar:
            with st.expander('Investering'):
                nedbetalingtid, effektiv_rente, investeringskostnad = kostnader_obj.juster_investeringskostnad(investeringskostnad)
        
        with st.expander('Kostnader'):
            st.subheader("Drift")
            kostnad_gv_monthly, kostnad_el_monthly = kostnader_obj.monthly_costs()
            kostnader_obj.fyring_costs_plot(kostnad_gv_monthly, kostnad_el_monthly)
            st.markdown("""---""")
            st.subheader("Investering og drift over 20 ??r")
            st.write(f"""Figuren under viser ??rlige kostnader til oppvarming inkl. investeringskostnad. 
            Det er forutsatt at investeringen nedbetales i l??pet av {int(nedbetalingtid)} ??r 
            med en effektiv rente p?? {float("{:.4f}".format(effektiv_rente * 100)) } %. """)            
            kostnad_gv_monthly, kostnad_el_monthly, total_besparelse = kostnader_obj.fyring_costs(investeringskostnad, nedbetalingtid, effektiv_rente)
            kostnader_obj.fyring_costs_plot(kostnad_gv_monthly, kostnad_el_monthly)
            if total_besparelse < 0:
                st.warning('Bergvarme er ikke l??nnsomt etter 20 ??r ut ifra oppgitte forutsetninger.')
            else:
                st.write(f"""_Etter 20 ??r vil du ha spart til sammen **{total_besparelse} kr** p?? varme opp boligen med bergvarme istedenfor elektrisk oppvarming._ """)
            st.markdown("""---""")
            st.subheader("Investering")
            st.write("""Investeringskostnaden omfatter en komplett installsjon av bergvarme inkl. varmepumpe, montering og energibr??nn. 
            Merk at dette er et estimat, og endelig pris m?? fastsettes av leverand??r. """)
            st.metric('Investeringskostnad bergvarme', str(investeringskostnad) + ' kr')
        co2 = Co2()
        with st.sidebar:
            with st.expander('Klimagassutslipp'):
                co2.juster_input()

        with st.sidebar:
            with st.expander('Kart'):
                Gis().kart(stasjon_lat, adresse_lat, energibronn_lat, stasjon_long, adresse_long, energibronn_long)
                st.write (f""" Kartet viser adresse (m??rkegr??nn farge), n??rmeste eksisterende energibr??nn (gr??nn farge) 
                og n??rmeste v??rstasjon, {stasjon_id}, med fullstendige temperaturdata (solgul farge). 
                N??rmeste eksisterende energibr??nn brukes til ?? estimere dybde til fjell i omr??det. Fra v??rstasjonen hentes det 
                inn m??lt temperatur per time for de siste 30 ??r. Gjennomsnittstemperaturen
                er m??lt til ?? v??re {gjennomsnittstemperatur} \u2103. {tekst} Str??mregionen er {region}. """)
        #st.header('Klimagassutslipp'):
        with st.expander('Klimagassutslipp'):
            co2_gv_yearly, co2_el_yearly, flyreiser = co2.beregning(energibehov_arr, kompressor_sum)
            #with st.expander('Se graf'):
            co2.plotting(co2_gv_yearly, co2_el_yearly)
            st.write(f"""_CO\u2082 besparelsen med bergvarme tilsvarer **{flyreiser} flyreiser** mellom Oslo og Trondheim._ """)

        #st.header('Dimensjonering')
        with st.expander('Dimensjonering'):
            st.markdown(""" Vi har dimensjonert et _bergvarmeanlegg for din bolig_ ut ifra oppgitte forutsetninger. 
            Merk at dette er et estimat, og endelig dimensjonering skal utf??res av leverand??r.""")

            #with st.expander('Se graf'):
            dimensjonering_obj.bronn_resultater(antall_meter, varmepumpe_storrelse, antall_bronner)
            dimensjonering_obj.varighetsdiagram(energibehov_arr, energibehov_arr_gv, kompressor_arr)
        
        st.markdown(""" --- """)
        url = 'https://www.varmepumpeinfo.no/varmepumpe'
        st.header("[Trykk her for ?? finne leverand??r av bergvarmeanlegg!](%s)" % url)

        
#        if st.button('Trykk her for ?? finne n??rmeste leverand??r av bergvarmeanlegg!'):
#            js = "window.open('https://www.varmepumpeinfo.no/varmepumpe')"  # New tab or window
#            html = '<img src onerror="{}">'.format(js)
#            div = Div(text=html)
#            st.bokeh_chart(div)
    

    #st_lottie(load_lottie('https://assets5.lottiefiles.com/packages/lf20_l22gyrgm.json'))  
    #st.caption('Et verkt??y fra Asplan Viak AS | ???? magne.syljuasen@asplanviak.no')



    