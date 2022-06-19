import streamlit as st
from funksjoner import Input, Forside, Innstillinger, Forklaringer
from app import beregning
from PIL import Image
 
def forside():
    st.title('Kalkuler din gevinst ved å hente energi fra grunnen')
    st.header('Start kalkulator ved å fylle inn i feltene under')
    input = Input()
    if len(input.valg) == 0:
        st.markdown("""---""")
        if 'key' not in st.session_state:
            st.session_state['key'] = 'value'
        st.header('Hva er bergvarme?')
        Forside()
    else:
        input.prosess()
        st.markdown("""---""")
        if input.lat != float:
            beregning(input.long, input.lat, input.boligareal)
            

def side_1():
    st.title('Lær mer')
    Forklaringer()

def side_2():
    st.title("Om oss")
    st.header("Asplan Viak")
    st.write("...")

    st.header("Norsk Varmepumpeforening (NOVAP)")
    st.write("...")

def side_3():
    st.title("Andre tjenester")
    st.header('AV Solenergi')
    c1, c2 = st.columns(2)
    with c1:
        st.write(""" AV Solenergi er et rammeverk for kartlegging, 
        lønnsomhetsanalyser og planlegging av muligheter for 
        solcelleanlegg på nye og eksisterende bygg. """)

        st.write(""" Verktøyet benyttes av våre rådgivere i planlegging, 
        dimensjonering og budsjettering av solcelleanlegg på alle typer bygg, 
        og gjør at vi kan jobbe svært effektivt og målrettet.""")

        url = 'https://av-solenergi.no/'
        st.subheader("[Prøv det her!](%s)" % url)
    with c2:
        image = Image.open('Grunnlagsdata/Bilder/solenergi.PNG')
        st.image(image) 

    st.header('AV Ombruk')
    c1, c2 = st.columns(2)
    with c1:
        st.write(""" Alt som kan brukes, skal brukes på nytt. """)

        st.write(""" Med AV Ombruk registreres materialene som 
        finnes i eksisterende bygg, for senere ombruk i rehabiliterings- 
        og nye prosjekter. En egen app gjør det enkelt for byggherrer 
        å kartlegge tilgjengelige materialer.""")

        url = 'https://av-ombruk.no/'
        st.subheader("[Prøv det her!](%s)" % url)
    with c2:
        image = Image.open('Grunnlagsdata/Bilder/ombruk.PNG')
        st.image(image) 

    st.header('Into Zero')
    c1, c2 = st.columns(2)
    with c1:
        st.write(""" Verktøy er under arbeid... """)

        st.write(""" Asplan Viak leder 3-årig innovasjonsprosjekt som skal føre til 
        bedre verktøy for klimavennlig områdeutvikling. I løpet av prosjektet skal 
        Asplan Viak, sammen med sine 11 partnere, se nærmere på hva som 
        skal til for å utvikle områder med fokus på reduksjon av klimagassutslipp. 
        Prosjektet er tverrfaglig anlagt, og det skal sees på løsninger 
        innenfor bygg og materialbruk, mobilitet, infrastruktur og energiforsyning. 
        Samtidig skal det være høyt fokus på gode stedskvaliteter og 
        utvikling av attraktive områder hvor folk vil trives, og 
        løsningene skal være økonomisk bærekraftige.""")

        url = 'https://www.asplanviak.no/prosjekter/integrert-planlegging-av-nullutslippsomraader-into-zero/'
        st.subheader("[Les mer her](%s)" % url)
    with c2:
        image = Image.open('Grunnlagsdata/Bilder/intoZero.PNG')
        st.image(image) 


def main():
    page_names_to_funcs = {
        "Kalkulatoren": forside,
        "Lær mer" : side_1,
        "Om oss": side_2,
        "Andre tjenester" : side_3}  
    with st.sidebar:
        Innstillinger().egen_logo()
    selected_page = st.sidebar.radio("", page_names_to_funcs.keys(), index=0)
    st.sidebar.markdown("""---""")
    page_names_to_funcs[selected_page]()

if __name__ == '__main__':
    main()
