import streamlit as st

def main():
    st.title("Üdvözöljük az Orvosi Röntgenkép Adatbázisban!")

    st.markdown("""
    ### Az alkalmazás célja
    Az alkalmazás célja, hogy segítse az orvosi röntgenképek kezelését, feltöltését, keresését és állapotuk nyomon követését. A rendszer pontos és részletes adatokat gyűjt a röntgenképekről, hogy elősegítse az orvosi kutatást és a diagnosztikai munkát.

    ### Funkciók
    - **Kép feltöltése**: Új röntgenképeket tölthet fel az adatbázisba.
    - **Képek keresése**: Kereshet az adatbázisban található röntgenképek között különböző kritériumok alapján.
    - **Státusz**: Megtekintheti a feltöltött röntgenképek állapotát és statisztikáit.
    - **Elérhetőség**: Kapcsolatba léphet a fejlesztőkkel vagy támogatást kérhet.

    ### Használati útmutató

    #### 1. Kép feltöltése
    - Válassza a "Kép feltöltése" menüpontot.
    - Adja meg a beteg azonosítóját és töltse fel a röntgenképet (Max 15 MB).
    - **Több kép feltöltése**: Ha egyszerre több képet szeretne feltölteni, pipálja ki a "Több kép feltöltése" lehetőséget. Figyelem: az összes kép ugyanazokat a címkéket kapja!
    - Kérem, adja meg a kötelező adatokat: korcsoport, röntgen nézet, normál vagy elváltozás típusa, melyik oldal (ha végtagról van szó), és a sérült régiók (fő régió, alrégió).
    - A részletesebb adatmegadás (alrégiók, komplikációk, társuló állapotok, osztályozások) nagyban segíti a kutatást és diagnosztikát.
    - **Több régió jelölése**: Ha több sérült régiót szeretne megadni, pipálja ki a "Több régió jelölése" opciót. Fontos: új régió hozzáadására csak mentés után van lehetőség a jelenlegi technikai korlátok miatt.
    - Kattintson a "Feltöltés" gombra az adatok mentéséhez.

    #### 2. Képek keresése
    - Válassza a "Képek keresése" menüpontot.
    - Adja meg a keresési feltételeket (típus, nézet, régiók, komplikációk, társuló állapotok).
    - Kattintson a "Keresés" gombra. A találatok listája megtekinthető és letölthető.

    #### 3. Státusz
    - Válassza a "Státusz" menüpontot.
    - Tekintse meg a feltöltött röntgenképek statisztikáit és aktuális állapotát.
    - Az adatok alapján nyomon követheti a projekt előrehaladását és a hiányzó elemeket.

    #### 4. Elérhetőség
    - Válassza az "Elérhetőség" menüpontot.
    - Ha segítségre van szüksége vagy kérdése van, lépjen kapcsolatba a fejlesztőkkel.

    ### Első fázis célja
    Az első fázis célja, hogy egy átfogó adatbázist hozzunk létre a röntgenképekről, amely segíti az orvosi kutatásokat és diagnosztikát. A pontos és részletes adatmegadás lehetővé teszi az elemzések hatékonyságának növelését és a betegségek jobb megértését.

    ### Fontos Információk
    - **Adatbiztonság**: Az összes feltöltött adat biztonságos és titkosított környezetben kerül tárolásra.
    - **Adatvédelmi Szabályok**: Az alkalmazás megfelel az adatvédelmi jogszabályoknak, és az Ön adatait csak az Ön beleegyezésével használjuk fel.
    - **Frissítések és Karbantartás**: Az alkalmazás rendszeresen frissül, hogy biztosítsa a legújabb funkciók és biztonsági intézkedések elérhetőségét.

    Köszönjük, hogy használja az alkalmazásunkat!
    """)

if __name__ == "__main__":
    main()
