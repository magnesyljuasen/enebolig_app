import streamlit as st
from funksjoner import Dimensjonering, Gis, Energibronn, Strompriser, Temperaturdata, Energibehov, Kostnader, Co2, Stromregion, Forklaringer
import numpy as np

def beregning(adresse_lat, adresse_long, bolig_areal):
    if adresse_long:
        energibronn_obj = Energibronn(adresse_lat, adresse_long)
        temperaturdata_obj = Temperaturdata(adresse_lat, adresse_long)
        stromregion_obj = Stromregion(adresse_lat, adresse_long)

        with st.sidebar:
            with st.expander('Forutsetninger'):
                st.write(""" For mest mulig nøyaktig dimensjonering av ditt bergvarmeanlegg kan du justere 
                verdiene. Alle resultatene oppdateres automatisk. """)

                st.write(""" Trykk på boksene under for å justere forutsetningene.""")



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
                st.caption("""Oppvarmingsbehovet er estimert ut ifra oppgitt areal og adresse. 
                Estimerte verdier vises i boksene under. Du kan fritt justere verdiene. """)
            
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
        energibehov_obj.resultater(dhw_sum, romoppvarming_sum, energibehov_sum)
        st.markdown("""---""")
        st.title("""Resultater""")
        
        with st.sidebar:
            with st.expander('Se kart'):
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
        st.header('Kostnader')
        valg = st.radio('Visningsvalg', ['Drift', 'Investering', 'Investering og drift over 20 år'], horizontal=True)
        if valg == "Investering og drift over 20 år":
            st.caption(f"""Figuren under viser årlige kostnader til oppvarming inkl. investeringskostnad. 
            Det er forutsatt at investeringen nedbetales i løpet av {int(nedbetalingtid)} år 
            med en effektiv rente på {float("{:.4f}".format(effektiv_rente * 100)) } %. Dette kan justeres i menyen til venstre. """)            
            kostnad_gv_monthly, kostnad_el_monthly = kostnader_obj.fyring_costs(investeringskostnad, nedbetalingtid, effektiv_rente)
            kostnader_obj.fyring_costs_plot(kostnad_gv_monthly, kostnad_el_monthly)
        if valg == "Drift":
            kostnad_gv_monthly, kostnad_el_monthly = kostnader_obj.monthly_costs()
            kostnader_obj.fyring_costs_plot(kostnad_gv_monthly, kostnad_el_monthly)
        if valg == "Investering":
            st.caption("""Investeringskostnaden omfatter en komplett installsjon av bergvarme inkl. varmepumpe, montering og energibrønn. 
            Merk at dette er et estimat, og endelig pris må fastsettes av leverandør. """)
            st.metric('Investeringskostnad bergvarme', str(int(investeringskostnad)) + ' kr')
        co2 = Co2()
        with st.sidebar:
            with st.expander('Klimagassutslipp'):
                co2.juster_input()
        st.header('Klimagassutslipp')
        co2_gv_yearly, co2_el_yearly = co2.beregning(energibehov_arr, kompressor_sum)
        #with st.expander('Se graf'):
        co2.plotting(co2_gv_yearly, co2_el_yearly)

        st.header('Dimensjonering')
        st.caption('Ditt bergvarmeanlegg:')
        #with st.expander('Se graf'):
        dimensjonering_obj.bronn_resultater(antall_meter, varmepumpe_storrelse, antall_bronner)
        dimensjonering_obj.varighetsdiagram(energibehov_arr, energibehov_arr_gv, kompressor_arr)
        
        
        url = 'https://www.varmepumpeinfo.no/'
        st.title('Finn nærmeste [forhandler](%s)' %url)


        