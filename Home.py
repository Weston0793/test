import streamlit as st

def main():
    st.title("Üdvözöljük az Orvosi Röntgenkép Adatbázisban!")
    
    st.markdown("""
    ### Az alkalmazás célja
    Az alkalmazás célja, hogy segítséget nyújtson orvosi röntgenképek kezelésében, feltöltésében, keresésében és státuszuk nyomon követésében.

    ### Funkciók
    - **Kép feltöltése**: Új röntgenképeket tölthet fel az adatbázisba.
    - **Képek keresése**: Kereshet az adatbázisban található röntgenképek között különböző kritériumok alapján.
    - **Státusz**: Megtekintheti a feltöltött röntgenképek állapotát és statisztikáit.
    - **Elérhetőség**: Kapcsolatba léphet a fejlesztőkkel vagy támogatást kérhet.

    ### Használati útmutató
    1. **Kép feltöltése**: Válassza a "Kép feltöltése" menüpontot, adja meg a beteg azonosítóját és töltse fel a röntgenképet. Töltse ki a szükséges adatokat és kattintson a "Feltöltés" gombra.
    2. **Képek keresése**: Válassza a "Képek keresése" menüpontot, adja meg a keresési feltételeket és kattintson a "Keresés" gombra. A találatok listáját megtekintheti és letöltheti.
    3. **Státusz**: Válassza a "Státusz" menüpontot, hogy megtekintse a röntgenképek feltöltési statisztikáit és aktuális állapotát.
    4. **Elérhetőség**: Válassza az "Elérhetőség" menüpontot, ha segítségre van szüksége vagy kapcsolatba szeretne lépni velünk.

    ### Támogatás
    Ha bármilyen kérdése vagy problémája van, kérjük, vegye fel velünk a kapcsolatot az "Elérhetőség" menüponton keresztül.
    
    Köszönjük, hogy használja az alkalmazásunkat!
    """)

if __name__ == "__main__":
    main()
