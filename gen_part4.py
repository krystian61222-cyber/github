"""Part 4: Sections 7-8 of the GitHub case study."""


def build_sections_7_to_8(doc):
    from gen_part1 import add_body, add_bullet, add_table_row_bold_first

    # Section 7
    doc.add_heading('7. Wyniki inwestycji', level=1)

    add_body(doc,
        'Inwestycja Series A okazala si\u0119 dla a16z spektakularnym sukcesem zar\u00f3wno '
        'na poziomie mno\u017cnika, jak i warto\u015bci absolutnej:')

    table = doc.add_table(rows=4, cols=2, style='Table Grid')
    data = [
        ('Moment', 'Wycena GitHub'),
        ('Wej\u015bcie a16z (lipiec 2012, Series A)', 'ok. 750 mln USD'),
        ('Series B (lipiec 2015)', 'ok. 2 mld USD (+167%)'),
        ('Exit \u2013 przej\u0119cie Microsoft (pa\u017adziernik 2018)', '7,5 mld USD (+900%)'),
    ]
    for i, (param, val) in enumerate(data):
        row = table.rows[i]
        for j, text in enumerate([param, val]):
            cell = row.cells[j]
            cell.text = ''
            p = cell.paragraphs[0]
            run = p.add_run(text)
            if i == 0:
                run.bold = True

    add_body(doc,
        'A16z zainwestowa\u0142 100 mln USD przy wycenie post-money 750 mln USD, obejmuj\u0105c '
        'ok. 13,3% udzia\u0142\u00f3w. Po uczestnictwie w Series B i cz\u0119\u015bciowym rozwodnieniu '
        'fundusz utrzyma\u0142 udzia\u0142 na poziomie ok. 10\u201312% na moment exitu. Przy wycenie '
        'exitu 7,5 mld USD szacowany zwrot a16z wyni\u00f3s\u0142 ok. 750 mln\u20131 mld USD, '
        'co odpowiada mno\u017cnikowi ok. 7,5\u201310\u00d7 na zagregowanym kapitale (Series A + follow-on). '
        'Na samej Series A (100 mln USD) mno\u017cnik wyni\u00f3s\u0142 ok. 10\u00d7.')

    add_body(doc,
        'Okres inwestycyjny (hold period): 6 lat (lipiec 2012 \u2013 pa\u017adziernik 2018). '
        'Exit by\u0142 pe\u0142ny \u2013 Microsoft naby\u0142 100% akcji GitHub za akcje MSFT, '
        'a wszyscy dotychczasowi udzia\u0142owcy (w tym a16z) otrzymali p\u0142atno\u015b\u0107 '
        'w formie akcji Microsoftu, kt\u00f3re mogli nast\u0119pnie up\u0142ynni\u0107 na rynku '
        'publicznym.')

    add_body(doc,
        'Dynamika wzrostu u\u017cytkownik\u00f3w potwierdza si\u0142\u0119 efekt\u00f3w sieciowych '
        'platformy: 3,5 mln u\u017cytkownik\u00f3w (2012) \u2192 10 mln (2014) \u2192 20 mln (2017) '
        '\u2192 28 mln+ (2018, moment exitu). GitHub sta\u0142 si\u0119 w tym czasie infrastruktur\u0105 '
        'krytyczn\u0105 dla globalnej bran\u017cy oprogramowania.')

    # Subsection 7.1
    doc.add_heading('7.1. GitHub w portfelu a16z (kontekst power law)', level=2)

    add_body(doc,
        'Venture capital funkcjonuje w logice power law: wi\u0119kszo\u015b\u0107 inwestycji traci '
        'pieni\u0105dze lub generuje niski zwrot, a ca\u0142y wynik funduszu zale\u017cy od kilku '
        'spektakularnych wygr\u00f3w. GitHub jest jednym z g\u0142\u00f3wnych driver\u00f3w wynik\u00f3w '
        'a16z Fund III, kt\u00f3ry wed\u0142ug raportowanych danych z 2025 r. osi\u0105gn\u0105\u0142 '
        'Net TVPI na poziomie ok. 11,3\u00d7.')

    add_body(doc,
        'Kluczowe pozycje Fund III obok GitHub to:')

    add_bullet(doc,
        'Coinbase \u2013 wielokrotne rundy, ok. 15% udzia\u0142, zwrot ok. 60\u00d7 zagregowany '
        'na moment direct listingu (2021).')
    add_bullet(doc,
        'Lyft \u2013 Series C (maj 2013, 60 mln USD), 6,3% na IPO, zwrot ok. 88\u00d7 papierowy.')
    add_bullet(doc,
        'Pinterest \u2013 wczesna inwestycja, znacz\u0105cy zwrot na IPO (2019).')
    add_bullet(doc,
        'Databricks \u2013 inwestycja wzrostowa, wycena przekraczaj\u0105ca 40 mld USD w 2023 r.')

    add_body(doc,
        'Dla pe\u0142nego obrazu warto zestawi\u0107 GitHub z udokumentowanymi pora\u017ckami a16z '
        'z analogicznego okresu:')

    add_bullet(doc,
        'Jawbone \u2013 ok. 49 mln USD zaanga\u017cowania, likwidacja w 2017 r., ca\u0142kowita strata.')
    add_bullet(doc,
        'Basis/Basecoin \u2013 uczestnictwo w rundzie 133 mln USD, zamkni\u0119cie projektu '
        'w 2018 r. z powodu bariery regulacyjnej, ca\u0142kowita strata.')

    add_body(doc,
        'Pojedyncza wygrana na GitHubie (ok. 1 mld USD zwrotu) z \u0142atwo\u015bci\u0105 pokrywa '
        'obie te straty. To potwierdza, \u017ce strategia a16z polega nie na unikaniu pora\u017cek, '
        'lecz na zapewnieniu, \u017ce pojedyncze wygrane (GitHub, Coinbase, Lyft, Instagram) s\u0105 '
        'na tyle du\u017ce, by pokry\u0107 ca\u0142y portfel i wygenerowa\u0107 ponadprzeci\u0119tny '
        'zwrot dla LP.')

    # Section 8
    doc.add_heading('8. Ryzyka inwestycyjne i wnioski', level=1)

    # 8.1
    doc.add_heading('8.1. G\u0142\u00f3wne ryzyka identyfikowane w momencie inwestycji', level=2)

    add_bullet(doc,
        'Ryzyko konkurencyjne \u2013 Bitbucket (Atlassian) oferowa\u0142 darmowe repozytoria '
        'prywatne, GitLab rozwija\u0142 zintegrowan\u0105 platform\u0119 DevOps (CI/CD, registry, '
        'monitoring). Istnia\u0142o ryzyko, \u017ce konkurenci zaoferuj\u0105 wi\u0119cej za mniej '
        'i podwa\u017c\u0105 pozycj\u0119 GitHub.')
    add_bullet(doc,
        'Ryzyko zale\u017cno\u015bci od spo\u0142eczno\u015bci open source \u2013 lojalno\u015b\u0107 '
        'developer\u00f3w opiera\u0142a si\u0119 na goodwill i przyzwyczajeniu, nie na lock-in '
        'technologicznym. Decyzja Microsoftu o przej\u0119ciu (2018) pokaza\u0142a, jak szybko '
        'spo\u0142eczno\u015b\u0107 mo\u017ce rozwa\u017ca\u0107 migracj\u0119 (fala przej\u015b\u0107 '
        'na GitLab po og\u0142oszeniu akwizycji).')
    add_bullet(doc,
        'Ryzyko CEO / zarz\u0105dzania \u2013 Tom Preston-Werner jako za\u0142o\u017cyciel-CEO '
        'by\u0142 kluczowy dla kultury firmy. Jego rezygnacja w kwietniu 2014 r. (kontrowersje '
        'dot. mobbingu) stanowi\u0142a istotne ryzyko operacyjne.')
    add_bullet(doc,
        'Ryzyko monetyzacji \u2013 zdecydowana wi\u0119kszo\u015b\u0107 u\u017cytkownik\u00f3w '
        'korzysta\u0142a z darmowego planu (repozytoria publiczne). Konwersja na p\u0142atne plany '
        'i GitHub Enterprise by\u0142a wolna, a model przychod\u00f3w nie by\u0142 jeszcze '
        'w pe\u0142ni zweryfikowany w 2012 r.')
    add_bullet(doc,
        'Ryzyko jednego produktu \u2013 GitHub by\u0142 g\u0142\u00f3wnie hostem repozytori\u00f3w '
        'Git. Istnia\u0142o ryzyko disrupcji technologicznej (nowy system kontroli wersji, '
        'alternatywne modele wsp\u00f3\u0142pracy) lub kommodytyzacji hostingu.')
    add_bullet(doc,
        'Ryzyko adopcji enterprise \u2013 programi\u015bci kochali GitHub, ale pytanie brzmia\u0142o: '
        'czy CIO i CISO korporacji zaakceptuj\u0105 hostowanie krytycznego kodu \u017ar\u00f3d\u0142owego '
        'na zewn\u0119trznej platformie? Bezpiecze\u0144stwo, compliance (SOC 2, HIPAA) i kontrola '
        'danych by\u0142y g\u0142\u00f3wnymi barierami.')

    # 8.2
    doc.add_heading('8.2. Materializacja ryzyk ex-post', level=2)

    add_body(doc,
        'Krytyczna ocena trafno\u015bci identyfikacji ryzyk wymaga zestawienia ich z faktycznymi '
        'wydarzeniami w latach 2012\u20132018:')

    table2 = doc.add_table(rows=7, cols=3, style='Table Grid')
    # Header row
    headers = ['Ryzyko ex-ante', 'Materializacja ex-post', 'Ocena']
    for i, h in enumerate(headers):
        cell = table2.rows[0].cells[i]
        cell.text = ''
        run = cell.paragraphs[0].add_run(h)
        run.bold = True

    risks = [
        ('Konkurencja (Bitbucket, GitLab)',
         'Cz\u0119\u015bciowa \u2013 GitLab wyros\u0142 na znacz\u0105cego konkurenta (IPO 2021, '
         'wycena 15 mld USD), ale GitHub utrzyma\u0142 dominacj\u0119 (>90% rynku hostingu open source '
         'na moment exitu). Bitbucket pozosta\u0142 niszowy.',
         'Materializacja cz\u0119\u015bciowa, ale bez utraty pozycji lidera'),
        ('Zmiana CEO',
         'Pe\u0142na \u2013 Preston-Werner zrezygnowa\u0142 kwiecie\u0144 2014. Wanstrath okaza\u0142 '
         'si\u0119 kompetentnym nast\u0119pc\u0105, prowadz\u0105c firm\u0119 do exitu przy 7,5 mld USD.',
         'Pe\u0142na materializacja, ale skutecznie opanowana'),
        ('Monetyzacja',
         'Cz\u0119\u015bciowa \u2013 konwersja na p\u0142atne plany by\u0142a wolna, ale GitHub '
         'Enterprise osi\u0105gn\u0105\u0142 >200 mln USD ARR do 2018 r. Wystarczaj\u0105co, by '
         'uzasadni\u0107 wycen\u0119 7,5 mld USD.',
         'Materializacja cz\u0119\u015bciowa, ale bez zagro\u017cenia dla exitu'),
        ('Jeden produkt / disrupcja technologiczna',
         'Nie zmaterializowa\u0142o si\u0119 \u2013 Git umocni\u0142 pozycj\u0119 standardu, '
         'a GitHub rozszerzy\u0142 ofert\u0119 (Actions, Packages, Security, Copilot po exicie).',
         'Brak materializacji'),
        ('Adopcja enterprise',
         'Nie zmaterializowa\u0142o si\u0119 \u2013 Fortune 500 masowo przyj\u0119\u0142o GitHub '
         'Enterprise. Google, Microsoft, Facebook, Amazon, banki inwestycyjne \u2013 wszystkie '
         'zosta\u0142y klientami.',
         'Brak materializacji'),
        ('Zale\u017cno\u015b\u0107 od spo\u0142eczno\u015bci OSS',
         'Cz\u0119\u015bciowa \u2013 po og\u0142oszeniu przej\u0119cia przez Microsoft (2018) '
         'wyst\u0105pi\u0142a kr\u00f3tkotrwa\u0142a fala migracji na GitLab, ale szybko wygas\u0142a. '
         'Spo\u0142eczno\u015b\u0107 zaakceptowa\u0142a akwizycj\u0119.',
         'Materializacja kr\u00f3tkotrwa\u0142a, szybko opanowana'),
    ]
    for i, (risk, mat, assessment) in enumerate(risks):
        row = table2.rows[i + 1]
        row.cells[0].text = risk
        row.cells[1].text = mat
        row.cells[2].text = assessment

    add_body(doc,
        'Wniosek metodologiczny: zesp\u00f3\u0142 inwestycyjny a16z trafnie zidentyfikowa\u0142 '
        'kluczowe ryzyka ex-ante. Najistotniejsze ryzyko (zmiana CEO) zmaterializowa\u0142o si\u0119 '
        'w pe\u0142ni, ale zosta\u0142o skutecznie opanowane dzi\u0119ki wsparciu a16z w procesie '
        'tranzycji. Ryzyka konkurencyjne i monetyzacyjne zmaterializowa\u0142y si\u0119 cz\u0119\u015bciowo, '
        'ale nie zagro\u017ai\u0142y exitowi. Ryzyka technologiczne i enterprise adopcji nie '
        'zmaterializowa\u0142y si\u0119 \u2013 co potwierdza trafno\u015b\u0107 tezy inwestycyjnej Levine\u2019a.')

    # 8.3
    doc.add_heading('8.3. Wnioski o skuteczno\u015bci strategii a16z', level=2)

    add_body(doc,
        'Case GitHub ilustruje wczesno-wzrostow\u0105 strategi\u0119 a16z opart\u0105 na trzech filarach:')

    add_bullet(doc,
        'Wej\u015bcie w sp\u00f3\u0142k\u0119 z udowodnionym product-market fit, ale przed '
        'pe\u0142n\u0105 monetyzacj\u0105 enterprise \u2013 GitHub w 2012 r. mia\u0142 3,5 mln '
        'u\u017cytkownik\u00f3w i dominuj\u0105c\u0105 pozycj\u0119 w hostingu Git, ale dopiero '
        'zaczyna\u0142 budowa\u0107 przychody enterprise. A16z wszed\u0142 w momencie, gdy spo\u0142eczno\u015b\u0107 '
        'by\u0142a ju\u017c zbudowana, ale warto\u015b\u0107 biznesowa jeszcze nie w pe\u0142ni skomercjalizowana.')
    add_bullet(doc,
        'Lewarowanie sieci operacyjnej funduszu jako g\u0142\u00f3wnego differentiatora \u2013 '
        'rekrutacja (70+ os\u00f3b), strategia enterprise GTM, mentoring boardowy, wprowadzenia '
        'do Fortune 500. Te dzia\u0142ania mia\u0142y bezpo\u015bredni wp\u0142yw na wzrost '
        'przychod\u00f3w GitHub Enterprise.')
    add_bullet(doc,
        'Konsekwentne pozycjonowanie narracyjne \u2013 publikacje Levine\u2019a budowa\u0142y '
        'postrzeganie GitHub jako \u201ekrytycznej infrastruktury developerskiej\u201d, co '
        'u\u0142atwia\u0142o rozmowy sprzeda\u017cowe z CIO korporacji i budowa\u0142o wycen\u0119 '
        'w oczach potencjalnych nabywc\u00f3w strategicznych.')

    add_body(doc,
        'Zwrot ok. 10\u00d7 na 100 mln USD kapita\u0142u (absolutny zwrot ok. 1 mld USD) '
        'w 6 lat potwierdza skuteczno\u015b\u0107 tej strategii w segmencie developer infrastructure. '
        'Forma exitu (przej\u0119cie strategiczne przez Microsoft) by\u0142a optymalna dla sp\u00f3\u0142ki '
        'prywatnej \u2013 zapewni\u0142a pewno\u015b\u0107 i p\u0142ynno\u015b\u0107 zwrotu bez ryzyk '
        'zwi\u0105zanych z IPO i lock-upem (por. Lyft, gdzie papierowy 88\u00d7 zosta\u0142 '
        'istotnie ograniczony przez spadki kursu po debiucie).')

    add_body(doc,
        'S\u0142abo\u015bci\u0105 strategii by\u0142o ograniczone upside: gdyby GitHub pozosta\u0142 '
        'niezale\u017cny i wszed\u0142 na gie\u0142d\u0119 w 2020\u20132021 r. (w okresie boomu wycen '
        'tech), wycena mog\u0142aby przekroczy\u0107 20\u201330 mld USD (por. GitLab: 15 mld USD '
        'na IPO w 2021 r., przy znacznie mniejszej bazie u\u017cytkownik\u00f3w). Jednak ryzyko '
        'utrzymania sp\u00f3\u0142ki prywatnej przez kolejne 2\u20133 lata (zale\u017cno\u015b\u0107 '
        'od jednego za\u0142o\u017cyciela-CEO, rosnaca konkurencja GitLab, brak publicznej '
        'p\u0142ynno\u015bci) czyni\u0142o decyzj\u0119 o exicie przy 7,5 mld USD racjonaln\u0105 '
        'z perspektywy zarz\u0105dzania ryzykiem portfelowym.')

    return doc
