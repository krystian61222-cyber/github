"""Part 5: Section 9 - Analysis of fund representatives."""


def build_section_9(doc):
    from gen_part1 import add_body, add_bullet, add_table_row_bold_first

    doc.add_heading('9. Analiza przedstawicieli funduszu', level=1)

    add_body(doc,
        'Poni\u017cej przedstawiono analiz\u0119 kluczowych przedstawicieli a16z odpowiedzialnych '
        'za inwestycj\u0119 w GitHub oraz ich publicznych wyst\u0105pie\u0144 (wpisy blogowe, '
        'wywiady, wyk\u0142ady, eseje). \u0141\u0105cznie zidentyfikowano 7 materia\u0142\u00f3w '
        '\u017ar\u00f3d\u0142owych pozwalaj\u0105cych odtworzy\u0107 filozofi\u0119 inwestycyjn\u0105 '
        'funduszu i tezy dotycz\u0105ce GitHub oraz sektora developer tools / open source.')

    # 9.1 Peter Levine
    doc.add_heading('9.1. Peter Levine \u2013 General Partner (od 2010 r.)', level=2)

    p = doc.add_paragraph()
    run = p.add_run('Background: ')
    run.bold = True
    p.add_run(
        'Do\u0142\u0105czy\u0142 do a16z w 2010 r. jako General Partner. Wcze\u015bniej CEO '
        'XenSource (open-source\u2019owa platforma wirtualizacji sprzedana Citrix Systems '
        'w 2007 r.), nast\u0119pnie VP i GM w Citrix zarz\u0105dzaj\u0105cy pionem wirtualizacji. '
        'Doktorat (PhD) MIT Sloan School of Management. Specjalizacja: infrastruktura oprogramowania, '
        'developer tools, systemy enterprise, komercjalizacja open source.'
    )

    p2 = doc.add_paragraph()
    run2 = p2.add_run('Specjalizacja inwestycyjna: ')
    run2.bold = True
    p2.add_run(
        'Levine prowadzi\u0142 inwestycje a16z w sektorze developer tools i infrastruktury: '
        'GitHub, Mesosphere (D2iQ), Nicira (przej\u0119te przez VMware), Databricks (wsp\u00f3\u0142prowadzenie). '
        'Jego teza inwestycyjna konsekwentnie opiera si\u0119 na modelu \u201eopen source community '
        'jako silnik adopcji, enterprise jako silnik przychod\u00f3w\u201d \u2013 wypracowanym '
        'na podstawie do\u015bwiadczenia z XenSource.'
    )

    add_body(doc, 'Kluczowe materia\u0142y publiczne:')

    add_bullet(doc,
        '\u201eSoftware Eating Software Development\u201d \u2013 wpis blogowy a16z, 9 lipca 2012 r. '
        '\u2013 og\u0142oszenie inwestycji w GitHub. Teza: je\u015bli oprogramowanie zjada \u015bwiat, '
        'to narz\u0119dzia do jego tworzenia s\u0105 fundamentem transformacji. GitHub jako '
        '\u201eplatforma, na kt\u00f3rej oprogramowanie jest tworzone\u201d, analogicznie do roli '
        'AWS w infrastrukturze chmurowej. Cytat: \u201eSoftware development itself is being eaten '
        'by software.\u201d')
    add_bullet(doc,
        '\u201eWhy There Will Never Be Another Red Hat: The Economics of Open Source\u201d \u2013 '
        'esej a16z, 2014 r. Teza: model Red Hat (sprzedawanie supportu do open source) jest '
        'przestarza\u0142y. Nowe modele komercjalizacji (hosting, SaaS, open core) s\u0105 '
        'skuteczniejsze. GitHub jako przyk\u0142ad modelu \u201eplatforma hostuj\u0105ca '
        'spo\u0142eczno\u015b\u0107\u201d \u2013 innego ni\u017c Red Hat, ale r\u00f3wnie skutecznego.')
    add_bullet(doc,
        '\u201eOpen Source: From Community to Commercialization\u201d \u2013 wyk\u0142ad '
        'Stanford/a16z, 2016 r. (YouTube). Rozbudowana analiza pe\u0142nego cyklu komercjalizacji '
        'open source: od stworzenia spo\u0142eczno\u015bci, przez budow\u0119 produktu enterprise, '
        'po exit. GitHub, Docker, Cloudera, Hortonworks jako case studies. Teza o \u201etrzyletnim '
        'oknie\u201d mi\u0119dzy adopcj\u0105 community a komercjalizacj\u0105 enterprise.')

    p3 = doc.add_paragraph()
    run3 = p3.add_run('Filozofia inwestycyjna: ')
    run3.bold = True
    p3.add_run(
        'Levine konsekwentnie k\u0142adzie nacisk na trzy elementy: (1) do\u015bwiadczenie operacyjne '
        'GP jako differentiator a16z \u2013 mo\u017cliwo\u015b\u0107 doradzania w kwestiach, '
        'kt\u00f3re sam przeszed\u0142 (skalowanie, enterprise sales, exit); (2) open source '
        'community jako moat \u2013 spo\u0142eczno\u015b\u0107 jest trudna do skopiowania i tworzy '
        'trwa\u0142\u0105 przewag\u0119; (3) timing komercjalizacji \u2013 za wczesna monetyzacja '
        'niszczy spo\u0142eczno\u015b\u0107, za p\u00f3\u017ana nie generuje zwrot\u00f3w dla VC.'
    )

    # 9.2 Marc Andreessen
    doc.add_heading('9.2. Marc Andreessen \u2013 wsp\u00f3\u0142za\u0142o\u017cyciel i Chairman a16z', level=2)

    p4 = doc.add_paragraph()
    run4 = p4.add_run('Background: ')
    run4.bold = True
    p4.add_run(
        'Wsp\u00f3\u0142za\u0142o\u017cyciel Netscape (1994 r.), Loudcloud/Opsware, a16z (2009 r.). '
        'Autor manifestu \u201eWhy Software Is Eating the World\u201d (Wall Street Journal, '
        '20 sierpnia 2011 r.) \u2013 ramy konceptualnej, w kt\u00f3r\u0105 wpisywa\u0142a si\u0119 '
        'teza inwestycyjna GitHub (oprogramowanie zjada \u015bwiat, wi\u0119c narz\u0119dzia '
        'do jego tworzenia s\u0105 krytyczne).'
    )

    p5 = doc.add_paragraph()
    run5 = p5.add_run('Rola w kontek\u015bcie GitHub: ')
    run5.bold = True
    p5.add_run(
        'Andreessen nie pe\u0142ni\u0142 formalnej roli w radzie dyrektor\u00f3w GitHub, '
        'ale jego manifest z 2011 r. stanowi\u0142 intelektualn\u0105 podstaw\u0119 tezy '
        'inwestycyjnej. Uczestniczy\u0142 w deal review i kluczowych spotkaniach z za\u0142o\u017cycielami. '
        'Jego publiczne pozycjonowanie GitHub jako elementu \u201esoftware eating the world\u201d '
        'wp\u0142yn\u0119\u0142o na percepcj\u0119 sp\u00f3\u0142ki w\u015br\u00f3d p\u00f3\u017aniejszych '
        'inwestor\u00f3w i potencjalnych nabywc\u00f3w strategicznych.'
    )

    add_body(doc, 'Kluczowe materia\u0142y publiczne:')

    add_bullet(doc,
        '\u201eWhy Software Is Eating the World\u201d, Wall Street Journal, 20 sierpnia 2011 r. '
        '\u2013 fundament teoretyczny ca\u0142ej strategii inwestycyjnej a16z w developer tools. '
        'Teza: ka\u017cda bran\u017ca zostanie zdominowana przez firmy software\u2019owe, ergo '
        'infrastruktura do tworzenia oprogramowania ma fundamentaln\u0105 warto\u015b\u0107.')
    add_bullet(doc,
        'Wyst\u0105pienia publiczne i komunikacja prasowa \u2013 Andreessen konsekwentnie '
        'u\u017cywa\u0142 GitHub jako przyk\u0142adu tezy \u201esoftware eating\u201d w rozmowach '
        'z mediami i na konferencjach bran\u017cowych.')

    # 9.3 Ben Horowitz
    doc.add_heading('9.3. Ben Horowitz \u2013 wsp\u00f3\u0142za\u0142o\u017cyciel i General Partner a16z', level=2)

    p6 = doc.add_paragraph()
    run6 = p6.add_run('Background: ')
    run6.bold = True
    p6.add_run(
        'Wsp\u00f3\u0142za\u0142o\u017cyciel a16z (2009 r.), wcze\u015bniej CEO Opsware '
        '(sprzeda\u017c do HP w 2007 r. za 1,6 mld USD), wcze\u015bniej VP w Netscape pod '
        'Marcem Andreessenem. Autor bestseller\u00f3w \u201eThe Hard Thing About Hard Things\u201d '
        '(2014) oraz \u201eWhat You Do Is Who You Are\u201d (2019).'
    )

    p7 = doc.add_paragraph()
    run7 = p7.add_run('Rola w kontek\u015bcie GitHub: ')
    run7.bold = True
    p7.add_run(
        'Horowitz uczestniczy\u0142 w deal review inwestycji w GitHub i wspiera\u0142 sp\u00f3\u0142k\u0119 '
        'w kluczowym momencie kryzysu CEO (kwiecie\u0144 2014 \u2013 rezygnacja Prestona-Wernera). '
        'Jako autor ksi\u0105\u017cki o zarz\u0105dzaniu w kryzysie (\u201eThe Hard Thing About Hard '
        'Things\u201d) pe\u0142ni\u0142 rol\u0119 nieformalnego mentora Chrisa Wanstratha w procesie '
        'przejmowania roli CEO. Do\u015bwiadczenie Horowitza z podobnych tranzycji (Opsware, Netscape) '
        'by\u0142o bezpo\u015brednio relewantne.'
    )

    add_body(doc, 'Kluczowe materia\u0142y publiczne:')

    add_bullet(doc,
        '\u201eThe Hard Thing About Hard Things: Building a Business When There Are No Easy Answers\u201d '
        '\u2013 HarperBusiness, 2014. Ksi\u0105\u017cka o zarz\u0105dzaniu CEO w kryzysie \u2013 '
        'bezpo\u015brednio relewantna dla sytuacji GitHub w 2014 r.')
    add_bullet(doc,
        'Aktywny udzia\u0142 w procesie mentoringu CEO sp\u00f3\u0142ek portfelowych a16z \u2013 '
        'filozofia \u201ebest board member\u201d: partner dyskutuj\u0105cy trudne decyzje, '
        'nie s\u0119dzia rozliczaj\u0105cy z KPI.')

    # 9.4 Table
    doc.add_heading('9.4. Zestawienie \u017ar\u00f3de\u0142 i kluczowe tezy', level=2)

    table = doc.add_table(rows=8, cols=4, style='Table Grid')
    # Header
    headers = ['#', '\u0179r\u00f3d\u0142o / format', 'Przedstawiciel', 'Kluczowa teza']
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ''
        run = cell.paragraphs[0].add_run(h)
        run.bold = True

    rows_data = [
        ('1', 'Blog a16z \u2013 \u201eSoftware Eating Software Development\u201d (09.07.2012)',
         'Peter Levine',
         'Oprogramowanie zjada narz\u0119dzia do tworzenia oprogramowania. GitHub = platforma fundamentalna.'),
        ('2', 'Esej a16z \u2013 \u201eWhy There Will Never Be Another Red Hat\u201d (2014)',
         'Peter Levine',
         'Model Red Hat jest przestarza\u0142y. Nowe modele: hosting, SaaS, open core. GitHub jako przyk\u0142ad.'),
        ('3', 'Wyk\u0142ad Stanford/a16z \u2013 \u201eOpen Source: From Community to Commercialization\u201d (2016)',
         'Peter Levine',
         'Trzyletnie okno mi\u0119dzy adopcj\u0105 community a komercjalizacj\u0105 enterprise.'),
        ('4', 'Manifest WSJ \u2013 \u201eWhy Software Is Eating the World\u201d (20.08.2011)',
         'Marc Andreessen',
         'Ka\u017cda bran\u017ca zostanie zdominowana przez software. Infrastruktura dev tools = kilofy w gor\u0105czce z\u0142ota.'),
        ('5', 'Ksi\u0105\u017cka \u2013 \u201eThe Hard Thing About Hard Things\u201d (2014)',
         'Ben Horowitz',
         'Zarz\u0105dzanie CEO w kryzysie. Tranzycja przyw\u00f3dztwa jako test organizacji.'),
        ('6', 'Blog a16z \u2013 Portfolio/Investment announcements',
         'a16z (instytucjonalnie)',
         'GitHub jako cz\u0119\u015b\u0107 portfela developer infrastructure obok Databricks, Docker, Mesosphere.'),
        ('7', 'Podcast a16z / publiczne wyst\u0105pienia',
         'Peter Levine',
         'Open source community = moat. Enterprise = revenue engine. Timing komercjalizacji = klucz.'),
    ]
    for i, (num, source, person, thesis) in enumerate(rows_data):
        row = table.rows[i + 1]
        row.cells[0].text = num
        row.cells[1].text = source
        row.cells[2].text = person
        row.cells[3].text = thesis

    # 9.5 Conclusions
    doc.add_heading('9.5. Wnioski z analizy materia\u0142\u00f3w', level=2)

    add_body(doc,
        'Analiza wyst\u0105pie\u0144 przedstawicieli a16z prowadzi do kilku wniosk\u00f3w '
        'istotnych dla oceny inwestycji w GitHub:')

    add_bullet(doc,
        'Sp\u00f3jno\u015b\u0107 tezy w czasie \u2013 stanowiska a16z dot. GitHub, developer tools '
        'i komercjalizacji open source s\u0105 niezmiennie powtarzane od 2012 r. (blog inwestycyjny) '
        'przez 2014 (Red Hat essay), a\u017c po 2016 r. (wyk\u0142ad Stanford). Brak retoryki '
        '\u201epivot\u201d mimo kryzysu CEO w 2014 r. wskazuje na realn\u0105 conviction.')
    add_bullet(doc,
        'Personalna relacja Levine \u2013 Wanstrath \u2013 Levine aktywnie wspiera\u0142 '
        'Wanstratha po obj\u0119ciu roli CEO w 2014 r. Ten typ d\u0142ugoterminowej relacji '
        'jest charakterystyczny dla modelu a16z i t\u0142umaczy, dlaczego fundusz preferuje '
        'sp\u00f3\u0142ki, w kt\u00f3rych za\u0142o\u017cyciel/nowy CEO jest otwarty na mentoring.')
    add_bullet(doc,
        'Komunikacja publiczna jako element value-add \u2013 publikacje Levine\u2019a '
        'i Andreessena budowa\u0142y narracyjn\u0105 ram\u0119 uzasadniaj\u0105c\u0105 wydatki '
        'korporacji na GitHub Enterprise. To jeden z najbardziej wymiernych element\u00f3w '
        'wsparcia post-investment a16z \u2013 bezpo\u015bredni wp\u0142yw na pipeline '
        'sprzeda\u017cowy.')
    add_bullet(doc,
        'S\u0142abo\u015b\u0107: asymetria komunikacji \u2013 a16z aktywnie komunikowa\u0142 '
        'tez\u0119 inwestycyjn\u0105 w okresie wzrostu (2012\u20132015), ale milcza\u0142 '
        'w okresie kryzysu CEO (2014). Komunikacja jest jednostronna \u2013 silna w momentach '
        'sukcesu, minimalna w momentach trudno\u015bci.')
    add_bullet(doc,
        'Konsekwentne ramy intelektualne \u2013 wszyscy trzej przedstawiciele (Levine, Andreessen, '
        'Horowitz) u\u017cywaj\u0105 sp\u00f3jnych ram analitycznych: software eating the world, '
        'open source community jako moat, enterprise jako revenue engine. \u015awiadczy to '
        'o silnej kulturze instytucjonalnej a16z i jako\u015bci procesu inwestycyjnego.')

    return doc
