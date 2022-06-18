import streamlit as st
from funksjoner import Input, Forside, Innstillinger, Forklaringer
from app import beregning
 
def forside():
    st.title('Kalkuler din gevinst ved å hente energi fra grunnen')
    st.header('Start kalkulator ved å fylle inn i feltene under')
    input = Input()
    if input.lat == float:
        st.markdown("""---""")
        if 'key' not in st.session_state:
            st.session_state['key'] = 'value'
            st.header('Hva er bergvarme?')
            Forside()
    else:
        beregning(input.long, input.lat, input.boligareal)

def side_1():
    st.title('Lær mer')
    with st.expander('Hva er bergvarme?'):
        Forside()
    Forklaringer()

def side_2():
    st.title("Om oss")
    st.header("Asplan Viak")
    st.write("...")

    st.header("Norsk Varmepumpeforening (NOVAP)")
    st.write("...")

def side_3():
    st.title("Andre tjenester")
    st.header('Lønnsom solenergi')
    st.write (""" AV- Lønnsom solenergi er et verktøy for kartlegging, 
    lønnsomhetsanalyser og planlegging av muligheter for solcelleanlegg 
    på nye og eksisterende bygg.
    """ )
    st.write('https://av-solenergi.no/')

    st.header('Ombruk')
    st.write('f')


def main():
    page_names_to_funcs = {
        "Kalkulatoren": forside,
        "Lær mer" : side_1,
        "Om oss": side_2,
        "Andre tjenester" : side_3}  
    with st.sidebar:
        Innstillinger().egen_logo()
    selected_page = st.sidebar.radio("", page_names_to_funcs.keys(), horizontal=False, index=0)
    st.sidebar.markdown("""---""")
    page_names_to_funcs[selected_page]()

if __name__ == '__main__':
    main()
