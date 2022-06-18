#        with st.expander('Hva er bergvarme?'):
#            st.write(""" Bergvarme er i hovedsak lagret solenergi med en stabil temperatur i størrelsesorden rundt 5 - 7 °C.""")
#            st.write(""" 1) For å hente ut bergvarme fra grunnen må det bores en energibrønn.""")
#            st.write(""" 2) Inne i energibrønnen monteres det en U-formet plastslange som fylles med en sirkulerende frostsikker væske.""")
#            st.write(""" 3) Væsken varmes opp av berggrunnen, og varmeenergien kan nå utnyttes ved hjelp av en 
#                            væske-vann-varmepumpe for å levere høy temperatur til boligens vannbårne varmesystem.""")
#            
#        with st.expander('Hvorfor bergvarme?'):
#            st.write(""" Bergvarme er både miljøvennlig, kortreist og fornybar energi, 
#                        og blir stadig mer populært blant norske byggeiere. Siden et bergvarmeanlegg henter 
#                   ca. 70% av levert varme fra grunnen redusert din strømregning til oppvarming. """)
#
#            st.write(""" Om sommeren, når det er behov for kjøling, er temperaturen i brønnen i seg selv
#                            lav nok til å kjøle bygningen. Da trengs viftekonvektorer som kan 
#                            fordele kjøling i bygningen på en komfortabel måte. """)

#        with st.expander('Hva gjør bergvarmekalkulatoren?'):
#            st.write(""" Kalkulatoren er utviklet av Asplan Viak, og utfører en enkel dimensjonering av en energibrønn 
#            med bergvarmepumpe for din bolig. Den regner så ut kostnader og miljøgevinst for det aktuelle anlegget. Det er mulig 
#            å justere parameterene som ligger til grunn for beregningen i menyen til venstre som dukker opp når du skriver inn din adresse. """)
#            st.write(""" Resultatene fra kalkulatoren er å anse som et estimat, og endelig dimensjonering av energibrønnen med varmepumpe
#            må tilpasses de stedlige forholdene av leverandør. """)

#        st.header('Om Asplan Viak')
#        st.write(""" Asplan Viak er et av Norges ledende rådgivningsselskaper innen plan, 
#        arkitektur- og ingeniørfag. Vår kompetanse finner du fra Tromsø i nord til 
#        Kristiansand i sør, med 1200+ medarbeidere fordelt på 32 kontorer. """)

#        st.write(""" Asplan Viak har solid kompetanse på både lukkede systemer med energibrønner i fjell, 
#        åpne systemer med bruk av grunnvann som energikilde, og større energilager. 
#        Vi tilbyr en rekke tjenester innen disse fagområdene, alt fra større utredninger 
#        og utviklingsprosjekter til forundersøkelser og detaljprosjektering av energibrønnparker. 
#        Vår erfaring er at tidlig og god planlegging, gjennomtenkte løsninger, gode grunnlagsdata og fokus 
#        på oppfølging i bygge- og driftsfasen er de største suksesskriteriene for vellykkede grunnvarmeanlegg. """)

        #st_lottie(load_lottie('https://assets5.lottiefiles.com/packages/lf20_l22gyrgm.json'))  
        #st.caption('Et verktøy fra Asplan Viak AS og Norsk Varmepumpeforening (NOVAP) | 📧 magne.syljuasen@asplanviak.no')
    #--Forklaringer--




 #       st.header ('Bergvarme reduserer din månedlige strømregning')
 #       kostnader_obj.monthly_costs()
 #       with st.expander('Hvordan beregnes dette?'):
 #           st.write(""" Et bergvarmeanlegg gir en god energibesparelse som bestemmes av 
 #           årsvarmefaktoren til varmepumpen. Den faktiske besparelsen i kroner vil være avhengig av strømprisen.
 #           I denne beregningen er det lagt til grunn en fast strømpris per time i et år som kan velges i menyen til venstre.
 #           Vi vet ikke hvordan strømprisen kommer til å utvikle seg i fremtiden. """)
        #image = Image.open('Bilder/Business Plan-bro.png')
        #st.image(image) 



      #Veienvidere()

        
        
        
        #with st.expander('Hvordan beregnes dette?'):
        #    st.write(""" Et bergvarmeanlegg gir en god energibesparelse som bestemmes av 
        #    årsvarmefaktoren til varmepumpen. Den faktiske besparelsen i kroner vil være avhengig av strømprisen.
        #    I denne beregningen er det lagt til grunn en fast strømpris per time i et år som kan velges i menyen til venstre.
        #    Vi vet ikke hvordan strømprisen kommer til å utvikle seg i fremtiden. """)
        
 #       with st.expander('Prisestimat for installasjon'):
 #           st.write ("""
 #           Den største barrieren når det gjelder etablering av 
 #           bergvarmeanlegg er investeringskostnaden. Investeringskostnaden inkluderer 
 #           boring av energibrønn samt installasjon av varmepumpe. Det presiseres at 
 #           dette kun er et anslag, og endelig pris må bestemmes av leverandør. """)
 #           st.write(""" Enovatilskuddet er en støtteordning for private husholdninger der du
 #           kan få inntil 10 000 kr i støtte når du anskaffer en bergvarmepumpe (væske-vann-varmepumpe). """)
 #           st.write(""" Grønne energilån er lån til miljøvennlige og energibesparende tiltak. Med et slikt lån
 #           kan dermed investeringskostnaden fordeles utover flere år. I mange tilfeller vil den månedlige 
 #           besparelsen med drift av et bergvarmeanlegg kunne forrente et slikt lån. """)

 #       st.header ('Du sparer miljøet')
        
#        with st.expander ('Hvordan beregnes dette?'):
#            st.write(""" NVE publiserer hvert år klimadeklarasjon for fysisk levert strøm i Norge. Det 
#            gjennomsnittlige direkte klimagassutslippet knyttet til bruk av strøm i Norge
#            var 8 gram CO\u2082-ekvivalenter per kilowattime i 2020. Denne verdien ligger til grunn for beregningen. """)

        
        

#        st.title('Andre ford')
#        Veienvidere()
#        st.markdown("""---""")

        #--Appen--


#        st.header('Forutsetninger')

#        st.subheader('Oppvarmingsbehov for din bolig')
#        energibehov_obj.plot(dhw_arr, romoppvarming_arr)
#        energibehov_obj.resultater(dhw_sum, romoppvarming_sum, energibehov_sum)
#        with st.expander ('Hvordan beregnes dette?'):
#            st.write ("""  Gjennomsnittstemperatur fra de siste 4 år og oppgitt boligareal benyttes til å estimere 
#            oppvarmingsbehovet for din bolig. Beregningen gjøres ved hjelp av PROFet-verktøyet som er utviklet av Sintef. 
#            Verktøyet estimerer både det årlige behovet for romoppvarming- og varmtvann som til sammen
#            utgjør det totale årlige oppvarmingsbehovet for din bolig. """)

#        st.subheader('Dimensjonering av ditt bergvarmeanlegg') 
#        #dimensjonering_obj.varighetsdiagram_bar(spisslast_arr, energibehov_arr_gv, kompressor_arr, levert_fra_bronner_arr)
#        dimensjonering_obj.varighetsdiagram(energibehov_arr, energibehov_arr_gv, kompressor_arr)
#        dimensjonering_obj.bronn_resultater(antall_meter, varmepumpe_storrelse, antall_bronner)

#        with st.expander('Hva ligger til grunn for denne dimensjoneringen?'):
#            st.write(""" Effektvarighetsdiagrammet i figuren over viser hvor stor andel av energibehovet som dekkes av varmepumpen. 
#            Størrelsen på varmepumpen bestemmes ut ifra maksimumeffekten i dette diagrammet. """)
#            st.write(""" Totalt antall brønnmetere bestemmes ut ifra energibehovet. Denne beregningen
#            tar hensyn til målt gjennomsnittstemperatur og energibehovet til boligen. 
#            Energibrønner må aldri dimensjoneres etter effektutak. """)

        

#        st.subheader('Oversiktskart')
#        Gis().kart(stasjon_lat, adresse_lat, energibronn_lat, stasjon_long, adresse_long, energibronn_long)
        
#        with st.expander ('Hva viser kartet?'):
#            st.write (f""" Kartet viser adresse (mørkegrønn farge), nærmeste eksisterende energibrønn (grønn farge) 
#            og nærmeste værstasjon, {stasjon_id}, med fullstendige temperaturdata (solgul farge). 
#            Nærmeste eksisterende energibrønn brukes til å estimere dybde til fjell i området. Fra værstasjonen hentes det 
#            inn målt temperatur per time for de siste 4 år. Gjennomsnittstemperaturen
#            er målt til å være {gjennomsnittstemperatur} \u2103. {tekst} Strømregionen er {region}. """)

#        st.markdown("""---""")
#        image = Image.open('Bilder/AsplanViak_illustrasjoner-02.png')
#        st.image(image)

#        st.caption('Et verktøy fra Asplan Viak AS | 📧 magne.syljuasen@asplanviak.no')


        #adresse_lat, adresse_long = Gis().adresse_til_koordinat(adresse)

#--OK--
class Tittelside:
    def __init__ (self):
        col1, col2, col3 = st.columns(3)
        with col1:
            #st_lottie(load_lottie('https://assets9.lottiefiles.com/packages/lf20_9t0xr9f2.json'))  
            self.av_logo()  
        with col2:
            st.title("Bergvarmekalkulatoren")
            st.write('Kalkuler din gevinst ved å hente energi fra berggrunnen!')

    def av_logo(self):
        image = Image.open('Grunnlagsdata/Bilder/logo.png')
        st.image(image)
#----
