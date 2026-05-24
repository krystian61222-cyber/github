"""Part 3: Section 6 - Follow-on and full investment path."""


def build_section_6(doc):
    from gen_part1 import add_body, add_bullet

    doc.add_heading('6. Follow-on i pe\u0142na \u015bcie\u017cka inwestycyjna', level=1)

    add_body(doc,
        'Po Series A a16z uczestniczy\u0142 w kolejnej rundzie jako follow-on investor, '
        'utrzymuj\u0105c sw\u00f3j udzia\u0142 w sp\u00f3\u0142ce mimo dynamicznego wzrostu wyceny '
        'i napływu nowych inwestor\u00f3w. W rundzie Series B (lipiec 2015, 250 mln USD przy wycenie '
        'ok. 2 mld USD) a16z do\u0142o\u017cy\u0142 kapita\u0142 obok Sequoia Capital (lead), '
        'Thrive Capital i IVP.')

    add_body(doc, '\u015acie\u017cka sp\u00f3\u0142ki po inwestycji a16z:')

    add_bullet(doc,
        '2008 \u2013 za\u0142o\u017cenie GitHub przez Toma Prestona-Wernera, Chrisa Wanstratha '
        'i PJ Hyetta. Sp\u00f3\u0142ka bootstrapowana, brak finansowania VC.')
    add_bullet(doc,
        'Lipiec 2012 \u2013 Series A prowadzona przez a16z (jedyny inwestor), 100 mln USD, '
        'wycena post-money ok. 750 mln USD. Peter Levine do\u0142\u0105cza do rady dyrektor\u00f3w.')
    add_bullet(doc,
        '2012\u20132014 \u2013 dynamiczny wzrost: z 3,5 mln do ponad 10 mln u\u017cytkownik\u00f3w. '
        'Rozw\u00f3j GitHub Enterprise, ekspansja zespo\u0142u sprzeda\u017cy. Firma staje si\u0119 '
        'standardem bran\u017cowym.')
    add_bullet(doc,
        'Kwiecie\u0144 2014 \u2013 rezygnacja Toma Prestona-Wernera z funkcji CEO w wyniku '
        'wewn\u0119trznego dochodzenia dot. mobbingu w miejscu pracy (opisanego przez Wired). '
        'Chris Wanstrath obejmuje stanowisko CEO.')
    add_bullet(doc,
        'Lipiec 2015 \u2013 Series B: 250 mln USD, lead Sequoia Capital, follow-on a16z, '
        'Thrive Capital, IVP jako wsp\u00f3\u0142inwestorzy. Wycena ok. 2 mld USD (+167% vs. Series A).')
    add_bullet(doc,
        '2015\u20132017 \u2013 kontynuacja wzrostu: z 10 mln do ponad 20 mln u\u017cytkownik\u00f3w. '
        'Masowa adopcja enterprise \u2013 Google, Microsoft, Facebook, Amazon i setki firm Fortune 500 '
        'korzystaj\u0105 z GitHub Enterprise. Przychody przekraczaj\u0105 200 mln USD ARR.')
    add_bullet(doc,
        '4 czerwca 2018 \u2013 og\u0142oszenie przej\u0119cia GitHub przez Microsoft za 7,5 mld USD '
        'w akcjach MSFT. Najwi\u0119ksza akwizycja Microsoftu od czasu LinkedIn (2016, 26,2 mld USD).')
    add_bullet(doc,
        'Lato 2018 \u2013 uzyskanie zgody regulacyjnej Komisji Europejskiej.')
    add_bullet(doc,
        'Pa\u017adziernik 2018 \u2013 zamkni\u0119cie transakcji przej\u0119cia. Pe\u0142ne wyj\u015bcie '
        'a16z ze sp\u00f3\u0142ki. Nat Friedman zostaje CEO GitHub pod parasolem Microsoftu.')

    add_body(doc,
        'A16z utrzymywa\u0142 udzia\u0142 na poziomie ok. 10\u201312% od Series A do exitu, '
        'uczestnicz\u0105c w Series B w celu ograniczenia rozwodnienia. Pocz\u0105tkowy udzia\u0142 '
        '13,3% (100 mln / 750 mln) zosta\u0142 cz\u0119\u015bciowo rozwodniony w Series B, '
        'ale follow-on pozwoli\u0142 zachowa\u0107 istotny pakiet na moment exitu.')

    # Subsection 6.1
    doc.add_heading('6.1. Koszt alternatywny', level=2)

    add_body(doc,
        'Strategia a16z w GitHubie pokazuje racjonaln\u0105 alokacj\u0119 kapita\u0142u: fundusz '
        'wszed\u0142 agresywnie w Series A (100 mln USD \u2013 ca\u0142a runda), a nast\u0119pnie '
        'utrzyma\u0142 pozycj\u0119 poprzez follow-on w Series B. Dla oceny efektywno\u015bci '
        'tej strategii warto por\u00f3wna\u0107 zwrot z GitHub z innymi inwestycjami a16z:')

    add_bullet(doc,
        'Coinbase \u2013 a16z dok\u0142ada\u0142 kapita\u0142 w kolejnych kilkunastu rundach, '
        'gromadz\u0105c ostatecznie ok. 15% udzia\u0142. W momencie direct listingu (2021) pakiet '
        'by\u0142 wart ok. 10 mld USD \u2013 ok. 60\u00d7 zwrot na zagregowanym kapitale. '
        'Konsekwentny follow-on okaza\u0142 si\u0119 kluczowym differentiatorem.')
    add_bullet(doc,
        'Lyft \u2013 a16z utrzyma\u0142 6,3% akcji a\u017c do IPO (marzec 2019), ucze\u015btnic\u0105c '
        'w rundach D, E i F. Warto\u015b\u0107 pakietu na IPO: ok. 1,2 mld USD \u2013 ok. 88\u00d7 '
        'mno\u017cnik papierowy w nieca\u0142e 6 lat od Series C (60 mln USD przy wycenie 275 mln USD).')
    add_bullet(doc,
        'Instagram \u2013 a16z zainwestowa\u0142 250 tys. USD w rundzie seed (2010). Zwrot 312\u00d7 '
        'przy przej\u0119ciu przez Facebook za 1 mld USD (2012). Jednak ze wzgl\u0119du na '
        'rezygnacj\u0119 z dalszych rund absolutny zarobek wyni\u00f3s\u0142 ok. 78 mln USD \u2013 '
        'wielokrotnie mniej ni\u017c w przypadku konsekwentnego follow-on (por. Baseline Ventures, '
        'kt\u00f3ry uzyska\u0142 120\u2013150 mln USD z 12% udzia\u0142u).')
    add_bullet(doc,
        'Roblox \u2013 a16z zainwestowa\u0142 150 mln USD w Series G (luty 2020) przy wycenie 4 mld USD. '
        'Zwrot ok. 11\u00d7 w 13 miesi\u0119cy do direct listingu (45,3 mld USD). Wysoki mno\u017cnik, '
        'ale na p\u00f3\u017anym etapie \u2013 mniejsze ryzyko, kr\u00f3tszy hold period.')

    add_body(doc,
        'GitHub z mno\u017cnikiem ok. 10\u00d7 na 100 mln USD kapita\u0142u (absolutny zwrot ok. 1 mld USD) '
        'plasuje si\u0119 pomi\u0119dzy tymi inwestycjami: ni\u017cszy mno\u017cnik ni\u017c Lyft '
        'czy Coinbase, ale na ogromnym czeku, co przek\u0142ada si\u0119 na istotny wk\u0142ad w wyniki '
        'Fund III. Decyzja o pe\u0142nym exicie przy 7,5 mld USD (zamiast trzymania dalej) by\u0142a '
        'racjonalna \u2013 sp\u00f3\u0142ka by\u0142a prywatna, p\u0142ynno\u015b\u0107 ograniczona, '
        'a oferta Microsoftu gwarantowa\u0142a pewny zwrot.')

    return doc
