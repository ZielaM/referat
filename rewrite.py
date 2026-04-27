import re

file_path = "referat.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "<h1>Jak napisać dobry<br>scenariusz testowy?</h1>",
        "<h1>Jak stworzyć skuteczny<br>scenariusz testowy?</h1>"
    ),
    (
        '<h2 class="subtitle">Referat merytoryczno-dydaktyczny</h2>',
        '<h2 class="subtitle">Opracowanie merytoryczno-dydaktyczne</h2>'
    ),
    (
        '<h2 class="section-title">1. Wstęp i kontekst rynkowy</h2>',
        '<h2 class="section-title">1. Wprowadzenie i uwarunkowania rynkowe</h2>'
    ),
    (
        '<p>W historii inżynierii oprogramowania istnieje wiele przykładów katastrof, których można by łatwo uniknąć dzięki zastosowaniu rzetelnych scenariuszy testowych. Jednym z najbardziej spektakularnych i kosztownych incydentów była utrata sondy Mars Climate Orbiter we wrześniu 1999 roku. Statek kosmiczny warty 125 milionów dolarów spłonął w atmosferze Marsa z powodu absurdalnego błędu integracyjnego: jeden zespół inżynierów używał w oprogramowaniu systemu metrycznego (niutonosekundy), a drugi systemu imperialnego (funty siły). Wystarczyłby jeden odpowiednio udokumentowany scenariusz testujący przesył i konwersję danych nawigacyjnych między modułami, aby ocalić całą misję.</p>',
        '<p>Dzieje inżynierii oprogramowania obfitują w przykłady porażek, którym można było zapobiec poprzez wdrożenie rzetelnych scenariuszy testowych. Jedną z najbardziej głośnych i kosztownych katastrof była utrata sondy Mars Climate Orbiter we wrześniu 1999 roku. Warty 125 milionów dolarów statek kosmiczny uległ zniszczeniu w marsjańskiej atmosferze wskutek trywialnego błędu integracji: jedna grupa inżynierów posługiwała się w kodzie systemem metrycznym (niutonosekundy), podczas gdy inna stosowała system imperialny (funty siły). Żeby uratować tę misję, wystarczyłoby przygotować i wykonać pojedynczy, dobrze opisany scenariusz testujący przesyłanie oraz konwersję informacji nawigacyjnych pomiędzy komponentami.</p>'
    ),
    (
        '<p>Globalny rynek testowania oprogramowania został wyceniony na 60 miliardów USD w 2025 roku, a prognozy wskazują na jego dynamiczny wzrost do poziomu 112 miliardów USD do roku 2034. Choć liczby te robią wrażenie, stanowią one zaledwie około 9% całego sektora tworzenia oprogramowania, którego wartość szacuje się na 1 bilion USD. Ta relatywnie mała część rynku odpowiada jednak za stabilność i niezawodność całej światowej infrastruktury cyfrowej – od systemów bankowych, przez logistykę, aż po aparaturę medyczną podtrzymującą życie.</p>',
        '<p>Wartość światowego rynku testowania oprogramowania w 2025 roku oszacowano na 60 miliardów dolarów, a przewidywania sugerują jego szybki rozwój do wartości 112 miliardów dolarów w 2034 roku. Mimo że te kwoty wydają się ogromne, odpowiadają one ledwie za blisko 9% całkowitej branży wytwarzania oprogramowania, wycenianej na około bilion dolarów. Niemniej jednak, ten stosunkowo niewielki wycinek rynku gwarantuje bezawaryjność i ciągłość działania globalnej infrastruktury cyfrowej – począwszy od rozwiązań finansowych, poprzez systemy logistyczne, a na sprzęcie medycznym ratującym ludzkie życie kończąc.</p>'
    ),
    (
        '<p>Niniejszy referat stawia sobie za cel dogłębną analizę procesu tworzenia scenariuszy testowych jako fundamentu zapewniania jakości. W dobie wykładniczego postępu Sztucznej Inteligencji i automatyzacji postawione zostanie również kluczowe pytanie badawcze: <strong>Czy w świecie autonomicznych agentów AI tester jest w ogóle jeszcze potrzebny?</strong></p>',
        '<p>Głównym celem tego referatu jest szczegółowe omówienie procedury przygotowywania scenariuszy testowych, stanowiących bazę dla zapewnienia jakości oprogramowania (Quality Assurance). W epoce błyskawicznego rozwoju Sztucznej Inteligencji oraz mechanizmów automatyzacji sformułowano także zasadnicze pytanie analityczne: <strong>Czy w erze samodzielnych agentów AI obecność testera jest nadal konieczna?</strong></p>'
    ),
    (
        '<h2 class="section-title">2. Czym jest scenariusz testowy?</h2>',
        '<h2 class="section-title">2. Definicja i cel scenariusza testowego</h2>'
    ),
    (
        '<p>Definiowanie scenariusza testowego należy przeprowadzić od ogółu do szczegółu, skupiając się na jego funkcjonalnym znaczeniu. W najprostszym ujęciu, scenariusz to dokładny „przepis” na sprawdzenie konkretnej funkcji systemu lub przypadku jego użycia. Dokumentuje on przebieg testowania całego procesu biznesowego w odpowiedniej, z góry ustalonej kolejności. Zgodnie z międzynarodowymi standardami ISTQB (International Software Testing Qualifications Board), proces tworzenia dokumentacji testowej dzieli się na dwa nierozerwalne etapy:</p>',
        '<p>Określanie pojęcia scenariusza testowego warto rozpocząć od perspektywy ogólnej i przechodzić do detali, koncentrując się na jego roli użytkowej. Najprościej rzecz ujmując, scenariusz jest precyzyjną instrukcją pozwalającą zweryfikować określoną funkcjonalność aplikacji lub dany przypadek użycia. Utrwala on ścieżkę weryfikacji kompletnego procesu biznesowego w logicznym, zaplanowanym wcześniej porządku. Według globalnych wytycznych ISTQB (International Software Testing Qualifications Board), przygotowywanie tego rodzaju dokumentacji testowej obejmuje dwa nieodłączne kroki:</p>'
    ),
    (
        '<li><strong>Projektowanie (Przypadek Testowy):</strong> Na tym etapie powstaje atomowy <i>przypadek testowy (Test Case)</i>, określający konkretne dane wejściowe i oczekiwane wyniki. Odpowiada on na pytanie: <i>„co dokładnie chcemy sprawdzić?”</i> (np. logowanie przy użyciu niepoprawnego hasła).</li>',
        '<li><strong>Faza projektowania (Przypadek Testowy):</strong> W tym kroku tworzony jest niepodzielny <i>przypadek testowy (Test Case)</i>, który precyzuje określone parametry wejściowe oraz zakładane rezultaty. Udziela on odpowiedzi na pytanie: <i>„jaki konkretnie element podlega weryfikacji?”</i> (przykładowo: próba zalogowania z błędnym hasłem).</li>'
    ),
    (
        '<li><strong>Implementacja (Scenariusz Testowy):</strong> Na tym etapie tworzony jest właściwy <i>scenariusz testowy (Test Scenario / Procedura Testowa)</i>, który układa wcześniej zaprojektowane przypadki w logiczną, wykonywalną kolejność kroków, tworząc spójną ścieżkę przejścia przez aplikację. Odpowiada on na pytanie: <i>„jak krok po kroku należy to sprawdzić?”</i>.</li>',
        '<li><strong>Faza implementacji (Scenariusz Testowy):</strong> W tym momencie powstaje finalny <i>scenariusz testowy (Test Scenario / Procedura Testowa)</i>. Organizuje on przygotowane wcześniej przypadki w racjonalną, możliwą do odtworzenia sekwencję akcji, formując logiczny ciąg operacji w systemie. Stanowi on odpowiedź na pytanie: <i>„w jaki sposób, krok po kroku, zrealizować test?”</i>.</li>'
    ),
    (
        '<p>Dla przykładu: scenariusz „Rejestracja nowego użytkownika” będzie składał się z wielu mniejszych przypadków testowych, takich jak: próba wysłania pustego formularza, walidacja siły hasła oraz poprawne założenie konta. Dlaczego tworzenie tak ustrukturyzowanych scenariuszy jest absolutnie niezbędne w profesjonalnym projekcie IT?</p>',
        '<p>Tytułem przykładu: scenariusz zatytułowany „Rejestracja nowego użytkownika” obejmie zbiór mniejszych przypadków testowych, m.in.: przesłanie formularza bez wypełnionych pól, weryfikację złożoności hasła czy też zakończone sukcesem utworzenie profilu. Z jakiego powodu opracowywanie tak uporządkowanych scenariuszy uważa się za krytyczne w komercyjnych przedsięwzięciach IT?</p>'
    ),
    (
        '''<ol>
            <li><strong>Powtarzalność i namierzanie defektów:</strong> Nawet jeśli tester wykryje krytyczny błąd, ale nie potrafi go później odtworzyć (np. dlatego, że zapomniał, jakich danych wejściowych użył), dla programisty ten błąd w praktyce nie istnieje. Scenariusz rygorystycznie dokumentuje stan środowiska i kroki testowe. Pozwala to na błyskawiczne zrekonstruowanie awarii, ułatwiając zespołowi deweloperskiemu jej naprawę.</li>
            <li><strong>Praca zespołowa i transfer wiedzy:</strong> Jasno zdefiniowana dokumentacja zabezpiecza płynność projektu. W przypadku nagłej nieobecności głównego testera, który zna dany moduł „na pamięć”, każda inna osoba z zespołu (nawet nowy pracownik) może natychmiast przejąć jego obowiązki. Scenariusze chronią wiedzę domenową przed zniknięciem wraz z odejściem pracownika.</li>
            <li><strong>Fundament pod automatyzację:</strong> Współczesne agenty testujące oraz skrypty automatyczne (np. w Selenium czy Cypress) wymagają bezwzględnie precyzyjnych i ustrukturyzowanych instrukcji. Bez dobrze napisanego scenariusza manualnego, proces pisania testów automatycznych staje się chaotyczny i jest wysoce podatny na błędy logiczne.</li>
        </ol>''',
        '''<ol>
            <li><strong>Możliwość reprodukcji i lokalizacja błędów:</strong> Nawet w sytuacji, gdy tester zidentyfikuje awarię krytyczną, lecz nie będzie w stanie jej ponownie wywołać (ponieważ np. nie pamięta wprowadzonych danych), taki defekt z perspektywy programisty niemalże nie występuje. Scenariusz ściśle utrwala kondycję systemu oraz podjęte działania. Umożliwia to natychmiastowe odtworzenie usterki, co znacznie usprawnia pracę programistom.</li>
            <li><strong>Działanie grupowe i przekazywanie informacji:</strong> Precyzyjnie przygotowana dokumentacja chroni ciągłość prac projektowych. W razie niespodziewanego urlopu kluczowego testera, doskonale obeznanego z daną funkcjonalnością, ktokolwiek inny w teamie (włączając w to nowo zatrudnionych) jest w stanie z marszu kontynuować zadania. Scenariusze pełnią rolę tarczy chroniącej know-how przed jego utratą w wyniku rotacji kadr.</li>
            <li><strong>Baza dla procesów automatyzacji:</strong> Dzisiejsze narzędzia i skrypty automatyzujące (jak choćby Selenium albo Cypress) bezwarunkowo potrzebują dokładnych, zorganizowanych algorytmów postępowania. Pozbawiony jakościowego scenariusza testów manualnych, proces tworzenia kodu dla automatów bywa nieuporządkowany i bardzo narażony na defekty logiczne.</li>
        </ol>'''
    ),
    (
        '''<div class="annotation">
            <strong>Adnotacja:</strong> Dobry scenariusz pełni funkcję „mapy”, która prowadzi testera przez konkretny obszar funkcjonalny systemu, chroniąc zespół przed chaosem wynikającym z intuicyjnego, nieudokumentowanego testowania (tzw. testowania ad-hoc, które sprawdza się tylko jako technika uzupełniająca).
        </div>''',
        '''<div class="annotation">
            <strong>Ważna uwaga:</strong> Wysokiej jakości scenariusz przypomina swoistą „mapę drogową”, asystującą testerowi w obrębie danego modułu aplikacji. Chroni to całą grupę przed dezinformacją związaną ze swobodnym, nieformalnym podejściem (znanym jako testowanie ad-hoc, które powinno być traktowane wyłącznie jako czynność poboczna).
        </div>'''
    ),
    (
        '<h2 class="section-title">3. Budowa scenariusza testowego</h2>',
        '<h2 class="section-title">3. Struktura scenariusza testowego</h2>'
    ),
    (
        '<p>W podejściu klasycznym scenariusz przyjmuje formę ustrukturyzowanej tabeli składającej się z dwóch głównych warstw.</p>',
        '<p>W standardowym modelu, scenariusz przybiera postać zorganizowanej tabeli, bazującej na dwóch nadrzędnych sekcjach.</p>'
    ),
    (
        '<h3>3.1. Warstwa informacyjno-środowiskowa</h3>',
        '<h3>3.1. Sekcja konfiguracyjna i informacyjna</h3>'
    ),
    (
        '<p>Określa kontekst sprzętowy i systemowy. Ten sam test może dać inne wyniki w zależności od konfiguracji zasobów pamięci czy wersji platformy .NET.</p>',
        '<p>Definiuje otoczenie urządzeń oraz oprogramowania. Identyczny przypadek testowy może skutkować odmiennym rezultatem w oparciu o dostępne pokłady pamięci operacyjnej lub zastosowaną generację środowiska .NET.</p>'
    ),
    (
        '<th>Dane systemowe</th>\n                <th>Przykładowa wartość (wg specyfikacji)</th>',
        '<th>Parametry środowiska</th>\n                <th>Wartość ilustracyjna (zgodnie ze specyfikacją)</th>'
    ),
    (
        '<h3>3.2. Matryca wykonawcza</h3>',
        '<h3>3.2. Część wykonawcza (Matryca)</h3>'
    ),
    (
        '<p>Zawiera kluczowe pola umożliwiające śledzenie postępu testów:</p>',
        '<p>Obejmuje najważniejsze atrybuty pozwalające na weryfikację zaawansowania testów:</p>'
    ),
    (
        '''<ul>
            <li><strong>ID:</strong> Unikalny identyfikator testu ułatwiający śledzenie.</li>
            <li><strong>Warunki wstępne:</strong> Rygorystycznie zdefiniowany stan systemu przed testem (np. saldo konta wynosi 11,99).</li>
            <li><strong>Kroki testowe:</strong> Algorytmiczny opis działań do wykonania krok po kroku.</li>
            <li><strong>Oczekiwany wynik:</strong> Mierzalna odpowiedź (np. „wyrzuć wyjątek ArgumentOutOfRangeException”). Musi być określona PRZED testem.</li>
            <li><strong>Waga:</strong> Priorytet testu (Niska, Wysoka, Krytyczna).</li>
        </ul>''',
        '''<ul>
            <li><strong>Identyfikator (ID):</strong> Niepowtarzalne oznaczenie testu pomagające w jego ewidencji.</li>
            <li><strong>Stan początkowy (Preconditions):</strong> Precyzyjnie opisana kondycja aplikacji przed uruchomieniem testu (np. stan środków na koncie to 11,99).</li>
            <li><strong>Kroki operacyjne:</strong> Konsekwentna sekwencja akcji do zrealizowania przez testera.</li>
            <li><strong>Zakładany rezultat:</strong> Spodziewana i obiektywna reakcja programu (np. „zgłoszenie błędu ArgumentOutOfRangeException”). Należy ją sformułować ZANIM test zostanie wykonany.</li>
            <li><strong>Priorytet (Waga):</strong> Ranga istotności sprawdzanego przypadku (Niski, Wysoki, Krytyczny).</li>
        </ul>'''
    ),
    (
        '<h2 class="section-title">4. Zasady projektowania i techniki ISTQB</h2>',
        '<h2 class="section-title">4. Dobre praktyki projektowe i metodologie ISTQB</h2>'
    ),
    (
        '<h3>4.1. Podstawowe zasady</h3>',
        '<h3>4.1. Fundamentalne reguły</h3>'
    ),
    (
        '''<ul>
            <li><strong>Czytelność i język biznesowy:</strong> Scenariusz to „kontrakt” między technologią a biznesem. Zamiast pisać „wyślij payload JSON”, należy napisać „zatwierdź formularz poprawnymi danymi”.</li>
            <li><strong>Atomowość:</strong> Jeden scenariusz weryfikuje jeden wyizolowany proces. Testy muszą być niezależne od siebie.</li>
            <li><strong>Pułapka 100% pokrycia:</strong> Pokrycie kodu nie oznacza poprawnej logiki. Liczy się jakość asercji walidacyjnych, a nie sama liczba uruchomionych linii kodu.</li>
        </ul>''',
        '''<ul>
            <li><strong>Przejrzystość oraz nomenklatura biznesowa:</strong> Dokumentacja testowa przypomina pomost pomiędzy światem IT a biznesem. Lepiej unikać zwrotów w stylu „wyślij payload JSON”, zastępując je sformułowaniami typu „prześlij formularz z ważnymi danymi”.</li>
            <li><strong>Niezależność (Atomowość):</strong> Pojedynczy przypadek ma za zadanie zweryfikować jeden odrębny mechanizm. Poszczególne scenariusze nie mogą na siebie wpływać.</li>
            <li><strong>Iluzja pełnego pokrycia kodu:</strong> Fizyczne przejście przez wszystkie linie kodu (Code Coverage) nie gwarantuje braku wad w logice biznesowej. Decyduje wartość weryfikacyjna testów, a nie wyłącznie objętość przetestowanego tekstu źródłowego.</li>
        </ul>'''
    ),
    (
        '<h3>4.2. Kluczowe techniki doboru przypadków</h3>',
        '<h3>4.2. Główne strategie selekcji przypadków testowych</h3>'
    ),
    (
        '<p>Dobry scenariusz musi wykorzystywać techniki czarnoskrzynkowe (black-box), które weryfikują system z perspektywy użytkownika końcowego:</p>',
        '<p>Solidny zestaw testów powinien bazować na metodach czarnoskrzynkowych (black-box testing), oceniających oprogramowanie z punktu widzenia ostatecznego klienta:</p>'
    ),
    (
        '''<ul>
            <li><strong>Analiza wartości brzegowych (BVA):</strong> Sprawdzanie skrajnych wartości (np. dla dopuszczalnego zakresu 1-100 sprawdzamy zachowanie dla 0, 1, 100 oraz 101).</li>
            <li><strong>Podział na klasy równoważności:</strong> Grupowanie danych, dla których system reaguje tak samo, by uniknąć setek powtarzających się kroków.</li>
            <li><strong>Ścieżki negatywne (Negative Testing):</strong> Sprawdzanie reakcji systemu na znaki specjalne, wstrzyknięcie złośliwego kodu SQL czy błędne hasła.</li>
            <li><strong>Przewidywanie błędów (Error Guessing):</strong> Wykorzystanie doświadczenia testera do wyłapywania typowych problemów (np. błędna obsługa lat przestępnych).</li>
        </ul>''',
        '''<ul>
            <li><strong>Weryfikacja wartości brzegowych (BVA):</strong> Testowanie ekstremalnych granic (przykładowo, gdy dozwolony przedział to 1-100, podajemy wartości 0, 1, 100 i 101).</li>
            <li><strong>Partycjonowanie na klasy równoważności:</strong> Zbieranie argumentów wywołujących taką samą reakcję programu w zbiory. Ma to na celu ominięcie konieczności pisania nadmiarowych testów dla każdej możliwej liczby z osobna.</li>
            <li><strong>Scenariusze negatywne (Negative Testing):</strong> Obserwacja zachowania oprogramowania w przypadku wprowadzania niedozwolonych znaków, ataków typu SQL Injection lub niepoprawnych poświadczeń.</li>
            <li><strong>Zgadywanie defektów (Error Guessing):</strong> Poleganie na intuicji i wiedzy specjalisty w celu odnajdywania charakterystycznych niedociągnięć (chociażby wadliwe kalkulowanie lat przestępnych).</li>
        </ul>'''
    ),
    (
        '<h2 class="section-title">5. Rola Sztucznej Inteligencji (AI) w tworzeniu testów</h2>',
        '<h2 class="section-title">5. Wpływ Sztucznej Inteligencji (AI) na proces testowania</h2>'
    ),
    (
        '''<p>Wkroczenie narzędzi opartych na dużych modelach językowych (LLM) – takich jak ChatGPT, Gemini, Claude, czy inteligentnych środowisk IDE (Cursor, Windsurf) – bezpowrotnie zmieniło krajobraz pracy inżynierów jakości. Sztuczna inteligencja potrafi błyskawicznie przeanalizować obszerną dokumentację biznesową (User Story) i na jej podstawie w kilka sekund wygenerować propozycje scenariuszy testowych. Co więcej, AI jest nieocenione przy generowaniu tzw. danych testowych (mock data) – z łatwością stworzy skomplikowane obiekty JSON, adresy e-mail czy fałszywe numery kart kredytowych potrzebne do walidacji formularzy.</p>
        <p>Należy jednak z całą stanowczością podkreślić, że AI pełni rolę <strong>asystenta, a nie autora ostatecznego</strong>. Bezkrytyczne kopiowanie wyników pracy sztucznej inteligencji niesie ze sobą poważne i kosztowne ryzyka:</p>''',
        '''<p>Adaptacja platform napędzanych dużymi modelami językowymi (LLM) – do których zalicza się m.in. ChatGPT, Gemini, Claude, a także nowoczesne edytory programistyczne (np. Cursor, Windsurf) – na zawsze odmieniła sposób funkcjonowania specjalistów ds. jakości. AI jest w stanie momentalnie prześledzić rozbudowane wymagania biznesowe (User Stories) i w oparciu o nie, w przeciągu chwili, zaproponować wstępne zarysy scenariuszy testowych. Ponadto, algorytmy te doskonale radzą sobie z przygotowywaniem danych testowych (tzw. mock data) – potrafią szybko wygenerować wielopoziomowe struktury JSON, adresy skrzynek pocztowych lub fikcyjne numery kart płatniczych, niezbędne podczas testowania interfejsów.</p>
        <p>Warto mimo wszystko wyraźnie zaznaczyć, iż AI odgrywa tu rolę <strong>wspierającą, a nie ostatecznego twórcy</strong>. Ślepe ufanie rezultatom wygenerowanym przez sztuczną inteligencję wiąże się z ogromnymi i bolesnymi konsekwencjami:</p>'''
    ),
    (
        '''<ul>
            <li><strong>Zjawisko „uprzejmego kodu” (Polite Code):</strong> Modele AI mają naturalną tendencję do generowania kodu i testów, które próbują za wszelką cenę zapobiec "wysypaniu się" aplikacji. Owijają one wrażliwą logikę w obszerne bloki <code>try-catch</code>, co powoduje wyciszanie błędów. Stoi to w jaskrawej sprzeczności z fundamentem testowania, czyli zasadą <i>fail-fast</i> – system powinien natychmiast i głośno sygnalizować każdą nieprawidłowość.</li>
            <li><strong>Syndrom powierzchowności i halucynacje:</strong> Jak zauważają wybitni eksperci (m.in. James Bach i Michael Bolton), AI potrafi stworzyć dokumentację, która wygląda niezwykle profesjonalnie, lecz jest merytorycznie bezużyteczna. Model językowy zgaduje kolejne słowa, nie rozumiejąc głębokiej logiki biznesowej ani ukrytych zależności w architekturze systemu. Może testować powierzchowne ścieżki, całkowicie ignorując krytyczne luki w zabezpieczeniach.</li>
            <li><strong>Pomijanie ograniczeń zakresu:</strong> AI regularnie rezygnuje ze stosowania silnego typowania zmiennych, przepuszczając nielogiczne dane wejściowe (np. ujemny wiek użytkownika) ze statusem testu "pozytywny".</li>
            <li><strong>Generowanie długu technicznego:</strong> Testy napisane przez AI są często rozwlekłe i nadmiarowe. Model rozwiązuje problem lokalnie („tu i teraz”), nie przejmując się tym, że za rok inny zespół będzie musiał ten kod utrzymywać. Prowadzi to do ogromnego długu technicznego przy próbie skalowania projektu.</li>
        </ul>''',
        '''<ul>
            <li><strong>Efekt „uprzejmego kodu” (Polite Code):</strong> Narzędzia LLM wykazują predyspozycję do pisania asercji ukierunkowanych na ukrywanie błędów oprogramowania. Zamykają one potencjalnie wadliwe instrukcje w bloki <code>try-catch</code>, ignorując pojawiające się wyjątki. Działanie takie narusza bazową filozofię testowania <i>fail-fast</i>, mówiącą, że aplikacja musi momentalnie oraz wyraźnie alarmować o każdym zakłóceniu.</li>
            <li><strong>Iluzja profesjonalizmu i zmyślanie (halucynacje):</strong> Jak argumentują autorytety w branży (tacy jak James Bach czy Michael Bolton), AI potrafi dostarczyć materiały prezentujące się imponująco od strony formalnej, jednakże całkowicie chybione merytorycznie. Mechanizm generujący przewiduje następne tokeny, zupełnie nie pojmując sedna procesów biznesowych i zawiłości architektury oprogramowania. Często skupia się na trywialnych przepływach pracy, omijając kluczowe dziury w bezpieczeństwie.</li>
            <li><strong>Lekceważenie restrykcji walidacyjnych:</strong> Sztuczna inteligencja miewa kłopoty z egzekwowaniem restrykcyjnych typów dla zmiennych, akceptując np. ujemne wartości dla wieku i oznaczając test jako "zaliczony".</li>
            <li><strong>Kumulowanie długu technicznego:</strong> Scenariusze tworzone za sprawą AI bywają przegadane i zbędnie obszerne. Model radzi sobie z wyzwaniem doraźnie („na tu i teraz”), bez refleksji nad tym, kto za jakiś czas będzie zmuszony czytać i refaktoryzować ten kod. Generuje to niebezpieczny dług technologiczny podczas późniejszego rozwoju produktu.</li>
        </ul>'''
    ),
    (
        '''<div class="annotation">
            <strong>Najlepsze praktyki pracy z AI (Prompt Engineering & Chain of Thought):</strong><br>
            Aby zminimalizować halucynacje, tester musi umiejętnie kierować modelem. Zamiast ogólnikowego „napisz testy logowania”, należy użyć precyzyjnego promptu: <i>„Jesteś inżynierem QA. Wygeneruj 5 scenariuszy brzegowych dla endpointu /api/auth, skupiając się na walidacji kodów statusu HTTP”</i>. Warto stosować technikę myślenia krokowego (Chain of Thought), instruując AI: 1. Najpierw przeanalizuj kod źródłowy &rarr; 2. Wypisz wszystkie możliwe ścieżki decyzyjne &rarr; 3. Dopiero teraz sformułuj oczekiwany rezultat i napisz asercję.
        </div>''',
        '''<div class="annotation">
            <strong>Dobre praktyki wykorzystania AI (Prompt Engineering i Chain of Thought):</strong><br>
            W celu redukcji występowania halucynacji, specjalista musi sprawnie nakierowywać algorytm. Zamiast używać ogólnikowego zapytania „przygotuj testy ekranu logowania”, lepiej zastosować precyzyjną komendę: <i>„Jesteś inżynierem QA. Stwórz 5 granicznych scenariuszy testowych dla punktu końcowego /api/auth, przywiązując wagę do weryfikacji kodów odpowiedzi HTTP”</i>. Rekomenduje się również użycie metodologii rozbijania problemu na mniejsze etapy (Chain of Thought), podając AI ramy działania: 1. Przeczytaj dostarczony kod źródłowy &rarr; 2. Zidentyfikuj wszelkie dozwolone ścieżki w logice programu &rarr; 3. W ostatnim kroku określ spodziewane wyjście i zapisz regułę asercji.
        </div>'''
    ),
    (
        '<h2 class="section-title">6. Czy w erze autonomicznych agentów AI tester jest jeszcze potrzebny?</h2>',
        '<h2 class="section-title">6. Zasadność utrzymania roli testera w czasach sztucznej inteligencji</h2>'
    ),
    (
        '''<p>Obserwując możliwości generatywnej sztucznej inteligencji, w mediach branżowych wielokrotnie wieszczono "śmierć zawodu testera". Jednak dogłębna analiza natury testowania oprogramowania oraz publikacje na portalach takich jak <i>testerzy.pl</i> wskazują jasno: <strong>sztuczna inteligencja nie zastąpi człowieka, szum wokół tego tematu jest mocno przesadzony, ale sama rola testera ulegnie głębokiej ewolucji</strong>.</p>
        <p>Złożoność dzisiejszych systemów wymaga kompetencji, których maszyny cyfrowe po prostu nie posiadają. Człowiek pozostaje niezastąpiony z czterech kluczowych powodów:</p>''',
        '''<p>Mając na uwadze potencjał wnoszony przez generatywną AI, na łamach pism technologicznych nieraz już ogłaszano "koniec profesji inżyniera QA". Wnikliwa ewaluacja specyfiki QA oraz artykuły branżowe publikowane m.in. na portalu <i>testerzy.pl</i> dają jednak do zrozumienia: <strong>algorytmy nie wyeliminują pracowników z krwi i kości, histeria w tej materii bywa wyolbrzymiona, aczkolwiek obowiązki testera bez wątpienia przejdą dużą transformację</strong>.</p>
        <p>Skomplikowanie współczesnych rozwiązań technologicznych wymusza posiadanie umiejętności, których procesory po prostu są pozbawione. Specjalista pozostanie koniecznym elementem układanki z czterech głównych przyczyn:</p>'''
    ),
    (
        '''<ul>
            <li><strong>Głębokie zrozumienie kontekstu biznesowego:</strong> AI może sprawdzić, czy przycisk „Kup teraz” poprawnie zmienia kolor i wysyła odpowiedni request do serwera. Nie wie jednak, czy ten przycisk w ogóle powinien znajdować się w tym miejscu, czy jest zgodny ze strategią marketingową firmy oraz czy nie wprowadza klienta w błąd w świetle obowiązującego prawa (np. dyrektywy Omnibus).</li>
            <li><strong>Empatia i User Experience (UX):</strong> Maszyna wykonuje instrukcje w ułamku sekundy, nie odczuwając żadnych emocji. Nie poczuje frustracji, gdy nawigacja na stronie mobilnej okaże się „toporna”, animacje zbyt długie, a interfejs po prostu irytujący. Tester, będąc pierwszym prawdziwym użytkownikiem, ocenia aplikację przez pryzmat ludzkiego komfortu i ergonomii.</li>
            <li><strong>Kreatywność i nielogiczność w testach negatywnych:</strong> Algorytmy uczą się na poprawnych wzorcach, dlatego ich propozycje testów są zazwyczaj bardzo „książkowe” i przewidywalne. Praktyka inżynierska pokazuje tymczasem, że najbardziej krytyczne awarie na produkcji wynikają z działań skrajnie nielogicznych i nieprzewidywalnych – np. gdy spanikowany użytkownik wciśnie klawisz „Wstecz” w przeglądarce podczas przetwarzania płatności. AI rzadko potrafi symulować prawdziwy, ludzki chaos.</li>
            <li><strong>Odpowiedzialność moralna i prawna:</strong> Jest to argument ostateczny. Algorytm LLM jest w stanie w kilka sekund wygenerować kod pokrywający aplikację bankową testami. Jednakże w przypadku wdrożenia wadliwej wersji na produkcję, co skutkowałoby wyciekiem danych osobowych lub zablokowaniem środków klientów, maszyna nie poniesie żadnych konsekwencji prawnych, finansowych ani wizerunkowych. Ciężar odpowiedzialności za to, czy system nadaje się do wdrożenia (tzw. <i>Go/No-Go decision</i>), zawsze musi spoczywać na barkach żywego, wykwalifikowanego inżyniera jakości.</li>
        </ul>''',
        '''<ul>
            <li><strong>Szerokie pojęcie o otoczeniu biznesowym:</strong> AI zweryfikuje, czy guzik „Zamawiam i płacę” odpowiednio animuje się po najechaniu kursorem i prawidłowo emituje zapytanie sieciowe. Nie oceni natomiast, czy umiejscowienie tego kontrolera jest sensowne z punktu widzenia konwersji, czy wpasowuje się w identyfikację wizualną przedsiębiorstwa i czy nie narusza wytycznych prawnych (takich jak dyrektywa Omnibus).</li>
            <li><strong>Wyrozumiałość i odbiór przez użytkownika (UX):</strong> Komputer realizuje polecenia w mgnieniu oka, będąc całkowicie wyzutym z uczuć. Nie zdenerwuje się, jeśli poruszanie się po interfejsie mobilnym okaże się uciążliwe, wczytywanie ekranów potrwa wieki, a cały design będzie odpychający. To inżynier jakości, wcielając się w rolę realnego klienta, diagnozuje aplikację pod kątem przyjazności i wygody obsługi.</li>
            <li><strong>Nieszablonowość w weryfikacji negatywnej:</strong> Modele sztucznej inteligencji były trenowane na idealnych zbiorach danych, stąd ich koncepcje testowania bywają szkolne i łatwe do odgadnięcia. Doświadczenie dowodzi z kolei, że najbardziej destrukcyjne błędy na systemach produkcyjnych są następstwem akcji chaotycznych i absurdalnych – np. kiedy zdezorientowany internauta klika kilkukrotnie przycisk „Cofnij” w trakcie autoryzacji przelewu. Systemom AI ciężko jest podrobić unikalny, ludzki przypadek użycia.</li>
            <li><strong>Aspekt prawno-etyczny:</strong> Powód ten zdaje się być kluczowy. Choć silnik LLM potrafi w okamgnieniu wyrzucić z siebie tysiące linii kodu testującego dla platformy finansowej, to w razie wydania felernej aktualizacji, zagrażającej bezpieczeństwu oszczędności klientów czy naruszającej RODO, program komputerowy nie zostanie pociągnięty do żadnej formy odpowiedzialności karnej, biznesowej lub wizerunkowej. Ciężar decyzyjny odnośnie dopuszczenia danej kompilacji do użytku publicznego (tzw. proces <i>Go/No-Go decision</i>) nieprzerwanie należy do żywego specjalisty.</li>
        </ul>'''
    ),
    (
        '<h2 class="section-title">7. Podsumowanie i wnioski</h2>',
        '<h2 class="section-title">7. Podsumowanie i przemyślenia końcowe</h2>'
    ),
    (
        '''<p>Tworzenie oprogramowania to proces obarczony ogromnym ryzykiem błędu, a rola testowania systemów IT jest dziś absolutnie krytyczna. Jak dowiódł przywołany we wstępie przykład misji Mars Climate Orbiter, nawet najbardziej zaawansowane projekty inżynieryjne mogą lec w gruzach z powodu braku prostej weryfikacji warunków brzegowych. Rygorystyczna i przemyślana dokumentacja testowa, ujęta w formę scenariuszy, jest fundamentem bezpieczeństwa globalnej infrastruktury.</p>
        <p>Dobrze skonstruowany scenariusz testowy nie jest dokumentem biurokratycznym ani techniczną „sztuką dla sztuki”. <strong>To formalny kontrakt zawarty między analitykiem, biznesem a inżynierem oprogramowania.</strong> Zastosowanie ustrukturyzowanych technik zdefiniowanych przez ISTQB (np. analiza wartości brzegowych czy klasy równoważności) pozwala stworzyć sieć bezpieczeństwa, która chroni projekt przed stratą wiedzy z powodu rotacji pracowników i stanowi stabilną bazę pod automatyzację.</p>''',
        '''<p>Produkcja oprogramowania jest przedsięwzięciem nierozerwalnie połączonym z ryzykiem pomyłek, wobec czego waga testowania systemów IT urasta obecnie do rangi krytycznej. Podobnie jak w przypadku zacytowanej na wstępie tragedii orbitera marsjańskiego, nawet wysoce skomplikowane i drogie projekty mają szansę runąć jak domek z kart, jeśli zabraknie banalnego sprawdzenia interfejsów łączących dany moduł. Ścisła, logicznie zaprojektowana dokumentacja QA, zorganizowana jako zbiór scenariuszy, gwarantuje spokój i bezpieczeństwo w światowej sieci informatycznej.</p>
        <p>Profesjonalny przypadek testowy zdecydowanie nie stanowi jedynie formalności biurokratycznej lub „pisania dla samego pisania”. <strong>Jest on swego rodzaju cyfrową ugodą spisaną na linii dział biznesowy, analityk a zespół wytwórczy.</strong> Wdrażanie systematycznych koncepcji certyfikowanych przez ISTQB (jak choćby analiza danych na krawędziach przedziałów czy techniki klasyfikacyjne) przyczynia się do budowy tarczy ochronnej, zachowującej merytorykę projektu pomimo fluktuacji personalnych oraz torującej drogę dla skutecznej automatyzacji procesów testowych.</p>'''
    ),
    (
        '<p><strong>Z przeprowadzonych w referacie rozważań płyną trzy główne wnioski końcowe:</strong></p>',
        '<p><strong>Z przedstawionych w opracowaniu argumentów wyłaniają się trzy decydujące konkluzje:</strong></p>'
    ),
    (
        '''<ol>
            <li><strong>Sztuczna Inteligencja to potężne narzędzie wspomagające, ale fatalny decydent.</strong> AI uwalnia testera od żmudnej i powtarzalnej pracy, ale ma tendencję do maskowania błędów („uprzejmy kod”) i halucynacji. Wymaga zatem ciągłej, krytycznej analizy i stosowania zaawansowanych technik Prompt Engineeringu.</li>
            <li><strong>Rola testera nie umiera, lecz dynamicznie ewoluuje.</strong> Z klasycznego „klikacza” wykonującego skrypty manualne, inżynier jakości staje się <i>architektem jakości</i>. Jego głównym zadaniem będzie teraz strategiczne zarządzanie procesem weryfikacji i ocena merytoryczna tego, co wyprodukowały maszyny.</li>
            <li><strong>Ostateczna odpowiedzialność pozostaje przy człowieku.</strong> Brak intuicji, brak empatii względem doświadczeń użytkownika (UX) oraz niezdolność do przewidzenia nielogicznych ludzkich działań sprawiają, że to człowiek musi podjąć ostateczną decyzję o gotowości oprogramowania do wdrożenia na rynek.</li>
        </ol>
        <p>Podsumowując, rozwój technologii oraz AI zrewolucjonizuje sposób, w jaki mechanicznie piszemy scenariusze testowe, jednak to analityczne myślenie, kreatywność oraz poczucie odpowiedzialności człowieka wciąż będą decydować o ostatecznym sukcesie i użyteczności każdego produktu IT.</p>''',
        '''<ol>
            <li><strong>Algorytmy AI to fenomenalni pomocnicy, ale tragiczni przełożeni.</strong> Automatyzacja wspiera pracownika w zadaniach monotonnych, aczkolwiek cierpi na wymyślanie nieprawdziwych informacji oraz celowe tuszowanie problemów („Polite Code”). Zmusza to nas do nieustannego recenzowania jej poczynań i używania zmyślnych form Prompt Engineeringu.</li>
            <li><strong>Zawód QA nie kończy się, lecz adaptuje do nowych realiów.</strong> Odchodząc od wizerunku „osoby przeklikującej aplikację”, nowoczesny specjalista ewoluuje w stronę <i>architekta ds. jakości</i>. Do jego priorytetów należeć będzie od teraz dbanie o strategię jakościową produktu i nadzór nad skryptami wytworzonymi przez boty.</li>
            <li><strong>Ostatnie słowo zawsze należy do człowieka.</strong> Pozbawienie maszyn szóstego zmysłu, wrażliwości na doznania klienta (obszar UX) i trudności w symulowaniu irracjonalnych zachowań decydują o tym, iż wyłącznie ekspert może wziąć na siebie ciężar publikacji aplikacji na środowisko produkcyjne.</li>
        </ol>
        <p>Kończąc, upowszechnianie się inteligentnych modeli gruntownie zmieni rutynę samego pisania procedur testowych. Mimo to trzeźwe rozumowanie analityczne, wena twórcza a nade wszystko waga odpowiedzialności spoczywającej na ludzkich barkach, ani na chwilę nie przestaną być najważniejszymi filarami w dążeniu do sukcesu każdego nowoczesnego rozwiązania IT.</p>'''
    )
]

for orig, new in replacements:
    if orig not in content:
        print(f"FAILED TO FIND:\n{orig}\n")
    content = content.replace(orig, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Rewrites complete.")
