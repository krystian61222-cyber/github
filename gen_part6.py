"""Part 6: Section 10, Bibliography, and Uwaga metodologiczna."""


def build_section_10_and_bibliography(doc):
    from gen_part1 import add_body, add_bullet, add_italic_para

    # Section 10
    doc.add_heading('10. Podsumowanie i synteza wniosk\u00f3w', level=1)

    add_body(doc,
        'Inwestycja a16z w GitHub (Series A, lipiec 2012, 100 mln USD przy wycenie 750 mln USD) '
        'jest modelowym przyk\u0142adem wczesno-wzrostowej strategii funduszu w segmencie developer '
        'infrastructure: wej\u015bcie w sp\u00f3\u0142k\u0119 z udowodnionym product-market fit '
        '(3,5 mln u\u017cytkownik\u00f3w, dominuj\u0105ca pozycja w hostingu Git, silne efekty '
        'sieciowe), ale przed pe\u0142n\u0105 komercjalizacj\u0105 enterprise. Peter Levine '
        'prowadzi\u0142 transakcj\u0119 i pe\u0142ni\u0142 rol\u0119 cz\u0142onka rady dyrektor\u00f3w, '
        'dostarczaj\u0105c do\u015bwiadczenie operacyjne z budowy i sprzeda\u017cy XenSource '
        '\u2013 bezpo\u015brednio analogicznego biznesu (open source -> enterprise).')

    add_body(doc,
        'Z perspektywy ksi\u0119gowej inwestycja przynios\u0142a a16z solidny zwrot: '
        'ok. 10\u00d7 na 100 mln USD kapita\u0142u (absolutny zwrot ok. 1 mld USD) w ci\u0105gu '
        '6 lat (2012\u20132018). Exit nast\u0105pi\u0142 poprzez przej\u0119cie strategiczne '
        'przez Microsoft za 7,5 mld USD w akcjach MSFT \u2013 form\u0119 zapewniaj\u0105c\u0105 '
        'pewno\u015b\u0107 i p\u0142ynno\u015b\u0107 zwrotu. GitHub by\u0142 jednym z g\u0142\u00f3wnych '
        'driver\u00f3w wynik\u00f3w Fund III a16z (Net TVPI ok. 11,3\u00d7 wg danych z 2025 r.), '
        'obok Lyft, Coinbase, Pinterest i Databricks.')

    add_body(doc,
        'Por\u00f3wnanie z innymi kluczowymi inwestycjami a16z ujawnia pozycj\u0119 GitHub '
        'w portfelu:')

    add_bullet(doc,
        'Instagram (2010) \u2013 najwy\u017cszy mno\u017cnik (312\u00d7), ale na minimalnym czeku '
        '(250 tys. USD). Absolutny zwrot ok. 78 mln USD. Le\u015bne \u201eznalezisko\u201d, '
        'nie strategiczna pozycja portfelowa.')
    add_bullet(doc,
        'Lyft (2013) \u2013 spektakularny mno\u017cnik papierowy (88\u00d7 na IPO), ale '
        'ograniczony realny IRR po spadkach kursu. Demonstracja si\u0142y i s\u0142abo\u015bci '
        'modelu marketplace.')
    add_bullet(doc,
        'Coinbase (wielokrotne rundy) \u2013 najwy\u017cszy absolutny zwrot w historii a16z '
        '(ok. 10 mld USD na direct listingu). Konsekwentny follow-on jako kluczowa lekcja.')
    add_bullet(doc,
        'Roblox (2020) \u2013 wysoki mno\u017cnik (11\u00d7) w kr\u00f3tkim czasie (13 miesi\u0119cy), '
        'ale na p\u00f3\u017anym etapie (late-stage). Inna kategoria ryzyka.')
    add_bullet(doc,
        'GitHub (2012) \u2013 umiarkowany mno\u017cnik (10\u00d7), ale na du\u017cym czeku '
        '(100 mln USD) z pewnym exitem (przej\u0119cie strategiczne). Optymalny profil '
        'risk-adjusted return dla funduszu wczesno-wzrostowego.')

    add_body(doc,
        'Case GitHub pokazuje zar\u00f3wno si\u0142\u0119, jak i strukturalne ograniczenia modelu '
        'a16z w segmencie developer tools:')

    add_bullet(doc,
        'Si\u0142a \u2013 operacyjne wsparcie (rekrutacja, enterprise GTM, mentoring) mia\u0142o '
        'bezpo\u015bredni wp\u0142yw na wzrost przychod\u00f3w i wycen\u0119. Publikacje Levine\u2019a '
        'budowa\u0142y narracyjn\u0105 ram\u0119 uzasadniaj\u0105c\u0105 wycen\u0119 enterprise. '
        'Wsparcie w kryzysie CEO (2014) zapobieg\u0142o destabilizacji sp\u00f3\u0142ki.')
    add_bullet(doc,
        'Ograniczenie \u2013 exit przy 7,5 mld USD (2018) by\u0142 racjonalny, ale ograniczy\u0142 '
        'upside. Pod parasolem Microsoftu GitHub uruchomi\u0142 Copilot (AI), Actions, Security '
        'i osi\u0105gn\u0105\u0142 >100 mln u\u017cytkownik\u00f3w (2023). Hipotetyczna wycena '
        'niezale\u017cnego GitHub w 2023 r. mog\u0142aby przekroczy\u0107 30\u201350 mld USD. '
        'Jednak utrzymanie prywatnej sp\u00f3\u0142ki przez kolejne 5 lat nios\u0142o istotne ryzyka.')

    add_body(doc,
        'Wniosek dla strategii a16z: model wczesno-wzrostowy z silnym wsparciem operacyjnym '
        'i strategicznym (platform model) sprawdza si\u0119 w generowaniu solidnych, pewnych '
        'zwrot\u00f3w w segmencie developer infrastructure. Forma exitu (przej\u0119cie '
        'strategiczne vs. IPO) jest kluczow\u0105 zmienn\u0105 determinuj\u0105c\u0105 realny '
        'IRR \u2013 w przypadku GitHub pewny exit przy 10\u00d7 okaza\u0142 si\u0119 lepsz\u0105 '
        'decyzj\u0105 risk-adjusted ni\u017c hipotetyczne IPO z wy\u017cszym mno\u017cnikiem, '
        'ale niepewnym timingiem i ryzykiem lock-upu (por. Lyft). Inwestycja w GitHub pozostaje '
        'jednym z najbardziej konsekwentnych przyk\u0142ad\u00f3w realizacji tezy \u201esoftware '
        'eating the world\u201d \u2013 od manifestu Andreessena (2011), przez blog Levine\u2019a '
        '(2012), po exit do Microsoftu (2018) \u2013 firmy, kt\u00f3ra sama przesz\u0142a '
        'transformacj\u0119 z wroga open source w jego najwi\u0119kszego korporacyjnego sponsora.')

    # Bibliography
    doc.add_heading('Bibliografia', level=1)

    # Category 1
    doc.add_heading('Materia\u0142y \u017ar\u00f3d\u0142owe Andreessen Horowitz (a16z)', level=2)

    add_bullet(doc,
        'Levine P., \u201eSoftware Eating Software Development\u201d, blog a16z, 9 lipca 2012 r., '
        'https://a16z.com/2012/07/09/software-eating-software-development/ (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Levine P., \u201eWhy There Will Never Be Another Red Hat: The Economics of Open Source\u201d, '
        'blog a16z, 2014, '
        'https://a16z.com/why-there-will-never-be-another-redhat-the-economics-of-open-source/ '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Levine P., \u201eOpen Source: From Community to Commercialization\u201d, wyk\u0142ad '
        'Stanford/a16z, 2016, https://www.youtube.com/watch?v=c9Tn2nEPp7A (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Andreessen Horowitz, Portfolio \u2013 GitHub, https://a16z.com/portfolio/ '
        '(dost\u0119p: maj 2026).')

    # Category 2
    doc.add_heading('Publikacje bran\u017cowe i prasowe', level=2)

    add_bullet(doc,
        'Ha A., \u201eAndreessen Horowitz Puts $100 Million Into GitHub\u201d, TechCrunch, '
        '9 lipca 2012 r., '
        'https://techcrunch.com/2012/07/09/andreessen-horowitz-puts-100-million-in-github/ '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Tsotsis A., \u201eGitHub Raises $250M Series B Round To Boost Enterprise Offering\u201d, '
        'TechCrunch, 29 lipca 2015 r., '
        'https://techcrunch.com/2015/07/29/github-raises-250m-series-b-round-to-boost-enterprise-offering/ '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Gelles D., \u201eGitHub, Long a Favorite of Programmers, Raises $250 Million\u201d, '
        'The New York Times, 29 lipca 2015 r., '
        'https://www.nytimes.com/2015/07/29/technology/github-raises-250-million-in-new-funding-round.html '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'McMillan R., \u201eThe GitHub Investigation\u201d, Wired, kwiecie\u0144 2014 r., '
        'https://www.wired.com/2014/04/the-github-investigation/ (dost\u0119p: maj 2026).')

    # Category 3
    doc.add_heading('Materia\u0142y dotycz\u0105ce exitu (przej\u0119cie przez Microsoft)', level=2)

    add_bullet(doc,
        'Bass D., \u201eMicrosoft Agrees to Acquire GitHub for $7.5 Billion\u201d, Bloomberg, '
        '4 czerwca 2018 r., '
        'https://www.bloomberg.com/news/articles/2018-06-04/microsoft-is-said-to-have-agreed-to-acquire-coding-site-github '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Microsoft Official Blog, \u201eMicrosoft to acquire GitHub for $7.5 billion\u201d, '
        '4 czerwca 2018 r., '
        'https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/ '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Friedman N., \u201eGitHub is now free for teams\u201d, The GitHub Blog, '
        '14 kwietnia 2020 r., '
        'https://github.blog/2020-04-14-github-is-now-free-for-teams/ (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Warren T., \u201eWhy Microsoft is willing to pay so much for GitHub\u201d, Fortune, '
        '4 czerwca 2018 r., '
        'https://fortune.com/2018/06/04/microsoft-github-acquisition/ (dost\u0119p: maj 2026).')

    # Category 4
    doc.add_heading('Analizy inwestorskie i raporty rynkowe', level=2)

    add_bullet(doc,
        'McCormick P., \u201ea16z: The Power Brokers\u201d, Not Boring, '
        'https://www.notboring.co/p/a16z-the-power-brokers (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Crunchbase, GitHub \u2013 Funding, Financials, Valuation & Investors, '
        'https://www.crunchbase.com/organization/github (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'PitchBook, GitHub Inc. \u2013 Company Profile, '
        'https://pitchbook.com/profiles/github-inc (dost\u0119p: maj 2026).')

    # Category 5
    doc.add_heading('Materia\u0142y kontekstowe', level=2)

    add_bullet(doc,
        'Andreessen M., \u201eWhy Software Is Eating the World\u201d, The Wall Street Journal, '
        '20 sierpnia 2011 r., '
        'https://www.wsj.com/articles/SB10001424053111903480904576512250915629460 '
        '(dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Horowitz B., \u201eThe Hard Thing About Hard Things: Building a Business When There Are '
        'No Easy Answers\u201d, HarperBusiness, Nowy Jork 2014.')
    add_bullet(doc,
        'Microsoft 8-K SEC Filing, '
        'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789019&type=8-K '
        '(dost\u0119p: maj 2026).')

    # Category 6
    doc.add_heading('\u0179r\u00f3d\u0142a encyklopedyczne', level=2)

    add_bullet(doc,
        'GitHub, Wikipedia \u2013 The Free Encyclopedia, '
        'https://en.wikipedia.org/wiki/GitHub (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Andreessen Horowitz, Wikipedia \u2013 The Free Encyclopedia, '
        'https://en.wikipedia.org/wiki/Andreessen_Horowitz (dost\u0119p: maj 2026).')
    add_bullet(doc,
        'Peter Levine (venture capitalist), Wikipedia, '
        'https://en.wikipedia.org/wiki/Peter_Levine_(venture_capitalist) (dost\u0119p: maj 2026).')

    # Uwaga metodologiczna
    doc.add_heading('Uwaga metodologiczna', level=1)

    add_italic_para(doc,
        'Dane finansowe rund (warto\u015b\u0107, wycena, lead investor) by\u0142y weryfikowane '
        'krzy\u017cowo w co najmniej dw\u00f3ch niezale\u017cnych \u017ar\u00f3d\u0142ach '
        '(komunikat a16z + relacja prasowa lub a16z + Crunchbase/PitchBook). Dane o wycenie '
        'GitHub na moment exitu pochodz\u0105 z komunikatu Microsoft (8-K SEC Filing) oraz '
        'raport\u00f3w Bloomberg i TechCrunch. Dane o udziale a16z w GitHub zosta\u0142y '
        'oszacowane na podstawie wielko\u015bci rundy i wyceny post-money (Series A: 100 mln / '
        '750 mln = 13,3%), z uwzgl\u0119dnieniem rozwodnienia w Series B. Cytaty Petera Levine\u2019a '
        'pochodz\u0105 z oryginalnych wpis\u00f3w blogowych a16z oraz wyk\u0142adu Stanford (2016). '
        'Cytaty Marca Andreessena pochodz\u0105 z manifestu WSJ (2011). Informacje o kryzysie CEO '
        '(2014) pochodz\u0105 z reporta\u017cu investigative Wired. A16z nie ujawnia publicznie '
        'st\u00f3p zwrotu na poziomie poszczeg\u00f3lnych inwestycji ani tempa up\u0142ynniania '
        'pozycji w sp\u00f3\u0142kach portfelowych, dlatego oceny realnego zwrotu sformu\u0142owano '
        'z zaznaczeniem tej niepewno\u015bci.')

    return doc
