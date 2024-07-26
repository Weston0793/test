import streamlit as st

def set_background():
    st.markdown(
         """
         <style>
         @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
         
         .stApp {
             background: linear-gradient(to bottom right, #f0f4f7, #d9e2ec);
             background-attachment: fixed;
             color: #212121;
             font-family: 'Roboto', sans-serif;
         }
         .title {
             font-size: 48px;
             font-weight: 700;
             color: #ffffff;
             text-align: center;
             padding: 20px;
             background: rgba(0, 150, 136, 0.8);
             border-radius: 10px;
             margin-top: 20px;
             text-shadow: 2px 2px 4px #000000;
             animation: fadeInDown 1.5s;
         }
         .subheader {
             font-size: 28px;
             color: #ffffff;
             background: #00796B;
             padding: 10px;
             border-radius: 10px;
             margin-top: 30px;
             margin-bottom: 10px;
             animation: fadeInDown 1.5s;
         }
         .subsubheader {
             font-size: 22px;
             color: #ffffff;
             background: #004D40;
             padding: 8px;
             border-radius: 8px;
             margin-top: 20px;
             margin-bottom: 10px;
             animation: fadeIn 1.5s;
         }
         .content {
             font-size: 16px;
             line-height: 1.2;
             text-align: justify;
             margin: 20px;
             padding: 20px;
             background: #ffffff;
             border-radius: 10px;
             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
             animation: fadeIn 1.5s;
         }
         .content ul {
             margin-left: 20px;
         }
         .content li {
             margin-bottom: 10px;
             animation: fadeIn 1.5s;
         }
         .content p {
             margin-bottom: 10px;
         }
         .content a {
             color: #00796B;
             text-decoration: none;
         }
         .content a:hover {
             text-decoration: underline;
         }
         @keyframes fadeInDown {
             0% {
                 opacity: 0;
                 transform: translateY(-20px);
             }
             100% {
                 opacity: 1;
                 transform: translateY(0);
             }
         }
         @keyframes fadeIn {
             0% {
                 opacity: 0;
             }
             100% {
                 opacity: 1;
             }
         }
         </style>
         <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
         <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
         <script>
             AOS.init();
         </script>
         """,
         unsafe_allow_html=True
     )

def main():
    set_background()

    st.markdown('<div class="title" data-aos="fade-down">Üdvözöljük az Orvosi Röntgenkép Adatbázisban!</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content" data-aos="fade-up">
    <div class="subheader" data-aos="fade-down">Az alkalmazás célja</div>
    Az alkalmazás célja, hogy segítse az orvosi röntgenképek kezelését, feltöltését, keresését és állapotuk nyomon követését. A rendszer pontos és részletes adatokat gyűjt a röntgenképekről, hogy elősegítse az orvosi kutatást, oktatást valamint legfőképpen a traumatológiai diagnosztikai munkát, ezáltal javítva a betegek ellátását.
    
    <div class="subheader" data-aos="fade-down">Funkciók</div>
    <ul>
        <li data-aos="fade-up"><strong>Kép feltöltése</strong>: Új röntgenkép(ek)et tölthet fel az adatbázisba.</li>
        <li data-aos="fade-up"><strong>Képek keresése</strong>: Kereshet az adatbázisban található röntgenképek között különböző kritériumok alapján.</li>
        <li data-aos="fade-up"><strong>Státusz</strong>: Megtekintheti a feltöltött röntgenképek állapotát és statisztikáit.</li>
        <li data-aos="fade-up"><strong>Elérhetőség</strong>: Kapcsolatba léphet a fejlesztőkkel.</li>
    </ul>

    <div class="subheader" data-aos="fade-down">Használati útmutató</div>

    <div class="subsubheader" data-aos="fade-up">1. Kép feltöltése</div>
    <div class="content" data-aos="fade-up">
        <ul>
            <li data-aos="fade-up">Kérjük a feltöltésre szánt képekről bizonyosodjon meg hogy anonimizálva vannak! A képeken nem szerepelhet semmilyen betegazonosító!</li>
            <li data-aos="fade-up">Válassza a bal oldalsáv "Navigáció" menüjéből a "Kép feltöltése" pontot.</li>
            <li data-aos="fade-up">Húzza a "Drag and drop file here" mezőbe a képet vagy válassza ki a "Browse files" gombbal s töltse fel a röntgenkép(ek)et (Max 15 MB/file).</li>
            <li data-aos="fade-up"><strong>Több kép feltöltése</strong>: Ha egyszerre több képet szeretne feltölteni, pipálja ki a "Több kép feltöltése" lehetőséget. Figyelem: az összes kép ugyanazokat a címkéket kapja! (kivéve a betegazonosítót)</li>
            <li data-aos="fade-up">Kérem, adja meg a kötelező adatokat: korcsoport, röntgen nézet, normál vagy elváltozás típusa, melyik oldal (ha végtagról van szó), és a sérült régiók (fő régió, régió).</li>
            <li data-aos="fade-up">A részletesebb adatmegadás (alrégiók, komplikációk, társuló állapotok, osztályozások) nagyban segíti a kutatást és diagnosztikát.</li>
            <li data-aos="fade-up"><strong>Több régió jelölése</strong>: Ha több sérült régiót szeretne megadni, pipálja ki a "Több régió jelölése" opciót. Fontos: új régió hozzáadására csak mentés után van lehetőség, jelenlegi technikai korlátok miatt. Ha mentés nélkül több új régiót hozzáad, hibaüzenet fog keletkezni!</li>
            <li data-aos="fade-up">A választható súlyossági kategóriák folyamatosan bővülnek. A hosszú csöves csontoknál már elérhető a teljes AO klasszifikáció.</li>
            <li data-aos="fade-up">Kattintson a "Feltöltés" gombra a kíválasztott adatok újra összegzéséhez, majd a "Megerősítés és Feltöltés" gombbal véglegesítheti a feltöltést.</li>
            <li data-aos="fade-up">Kérjük várja meg a zöld "Sikeres feltöltés" feliratot mielött új képet tölt fel. Több kép feltöltésénél egyszerre, többet kell várni.</li>
        </ul>
    </div>

    <div class="subsubheader" data-aos="fade-up">2. Képek keresése</div>
    <div class="content" data-aos="fade-up">
        <ul>
            <li data-aos="fade-up">Válassza a "Képek keresése" menüpontot a bal oldalsáv "Navigáció" menüjéből.</li>
            <li data-aos="fade-up">Adja meg a keresési feltételeket (minimum: típus, nézet, főrégió).</li>
            <li data-aos="fade-up">Kattintson a "Keresés" gombra. A találatok listája megtekinthető és letölthető.</li>
            <li data-aos="fade-up">Várjon egy pár másodpercet amíg a szerver összeállítja a "Letöltés" gomb megnyomása után a .zip filet, majd kattintson a "Megerősítés s Letöltés" gombra ha le kívánja tölteni a képeket és a hozzájuk tartozó címkéket.</li>
        </ul>
    </div>

    <div class="subsubheader" data-aos="fade-up">3. Státusz</div>
    <div class="content" data-aos="fade-up">
        <ul>
            <li data-aos="fade-up">Válassza a "Státusz" menüpontot a bal oldalsáv "Navigáció" menüjéből.</li>
            <li data-aos="fade-up">Tekintse meg a feltöltött röntgenképek statisztikáit és a projekt aktuális fázisának állapotát.</li>
            <li data-aos="fade-up">Az adatok alapján nyomon követheti a projekt előrehaladását és a hiányzó elemeket.</li>
            <li data-aos="fade-up">Az első fázis lezárási kirétirumai: az összes különböző csontot tartalmazó régióból, legalább két nézetből, normál és törött röntgenképeket gyüjts felnőttektől, kombinációnként legalább 50 darabot.</li>
            <li data-aos="fade-up">A második fázis a különböző alrégiók feltöltése lesz előreláthatólag.</li>
            <li data-aos="fade-up">Fontos: egyelőre a státusz a gyermekkori röntgeneket is számba veszi!</li>
        </ul>
    </div>

    <div class="subsubheader" data-aos="fade-up">4. Elérhetőség</div>
    <div class="content" data-aos="fade-up">
        <ul>
            <li data-aos="fade-up">Válassza az "Elérhetőség" menüpontot a bal oldalsáv "Navigáció" menüjéből.</li>
            <li data-aos="fade-up">Ha bármilyen észrevétele van a honlappal kapcsolatban, segítségre van szüksége vagy kérdése van, lépjen nyugodtan kapcsolatba a fejlesztőkkel.</li>
        </ul>
    </div>

    <div class="subheader" data-aos="fade-down">Fontos Információk</div>
    <ul>
        <li data-aos="fade-up"><strong>Adatbiztonság</strong>: Az összes feltöltött adat biztonságos és titkosított környezetben kerül tárolásra.</li>
        <li data-aos="fade-up"><strong>Frissítések és Karbantartás</strong>: Az alkalmazás rendszeresen frissül, hogy biztosítsa a legújabb és egyre kényelmesebb funkciók és várják az ide látogatókat.</li>
    </ul>

    Köszönjük, hogy használja az alkalmazásunkat!
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
