#!/usr/bin/env python3
"""
Premium business-style Fintech presentation in Polish.
Clean unified layout with single content blocks per slide.
McKinsey/BCG inspired: dark top banner, unified cards, minimal decoration.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ============================================================
# COLOR SCHEME
# ============================================================

DARK_NAVY = RGBColor(0x0D, 0x1B, 0x2A)
TEAL_ACCENT = RGBColor(0x00, 0xB4, 0xD8)
WARM_GOLD = RGBColor(0xE8, 0xA8, 0x38)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xF4, 0xF5, 0xF7)
TEXT_DARK = RGBColor(0x1A, 0x1A, 0x2E)
TEXT_MEDIUM = RGBColor(0x4A, 0x4A, 0x5A)

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def set_slide_bg(slide, color):
    """Set solid background color for a slide."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_top_banner(slide, title_text):
    """Add dark navy top banner (1.2 inches) with white title and teal underline."""
    # Dark banner rectangle
    banner = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), SLIDE_WIDTH, Inches(1.2)
    )
    banner.fill.solid()
    banner.fill.fore_color.rgb = DARK_NAVY
    banner.line.fill.background()

    # Title text in banner
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.25), Inches(11), Inches(0.7))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = 'Segoe UI'

    # Teal underline beneath banner
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.05), Inches(4.0), Inches(0.04)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = TEAL_ACCENT
    line.line.fill.background()


def add_unified_card(slide, left, top, width, height):
    """Add a single unified content card with subtle shadow effect."""
    # Shadow rectangle (slightly offset)
    shadow = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.04), top + Inches(0.04), width, height
    )
    shadow.fill.solid()
    shadow.fill.fore_color.rgb = RGBColor(0xE0, 0xE1, 0xE3)
    shadow.line.fill.background()

    # Main card
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = RGBColor(0xE8, 0xE9, 0xEB)
    card.line.width = Pt(0.75)
    return card


def add_vertical_divider(slide, x, top, height):
    """Add a thin vertical divider line."""
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, x, top, Inches(0.02), height
    )
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(0xE0, 0xE1, 0xE3)
    line.line.fill.background()


def add_horizontal_divider(slide, left, y, width):
    """Add a thin horizontal divider line."""
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, y, width, Inches(0.02)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(0xE0, 0xE1, 0xE3)
    line.line.fill.background()


def add_text(slide, left, top, width, height, text, font_size=12,
             bold=False, color=TEXT_DARK, alignment=PP_ALIGN.LEFT):
    """Add a simple text box."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = 'Segoe UI'
    p.alignment = alignment
    return txBox


def add_bullet_text(slide, left, top, width, height, lines, font_size=11,
                    color=TEXT_DARK, bullet_color=TEAL_ACCENT, spacing=6):
    """Add bulleted text with teal square markers."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, line_text in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        # Use a small square marker
        run_marker = p.add_run()
        run_marker.text = "\u25A0  "
        run_marker.font.size = Pt(8)
        run_marker.font.color.rgb = bullet_color
        run_marker.font.name = 'Segoe UI'

        run_text = p.add_run()
        run_text.text = line_text
        run_text.font.size = Pt(font_size)
        run_text.font.color.rgb = color
        run_text.font.name = 'Segoe UI'
        p.space_after = Pt(spacing)
    return txBox


def add_numbered_text(slide, left, top, width, height, items, start_num=1,
                      font_size=12, color=TEXT_DARK, num_color=TEAL_ACCENT, spacing=10):
    """Add numbered items with colored number prefix."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item_text in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        # Number
        run_num = p.add_run()
        run_num.text = f"{start_num + i}.  "
        run_num.font.size = Pt(font_size)
        run_num.font.bold = True
        run_num.font.color.rgb = num_color
        run_num.font.name = 'Segoe UI'

        # Text
        run_text = p.add_run()
        run_text.text = item_text
        run_text.font.size = Pt(font_size)
        run_text.font.color.rgb = color
        run_text.font.name = 'Segoe UI'
        p.space_after = Pt(spacing)
    return txBox


# ============================================================
# SLIDE CREATION
# ============================================================

def create_slide1(prs):
    """Title slide - full dark background, centered, minimal."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, DARK_NAVY)

    # Gold line above title
    line_top = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(4.0), Inches(2.4), Inches(5.333), Inches(0.03)
    )
    line_top.fill.solid()
    line_top.fill.fore_color.rgb = WARM_GOLD
    line_top.line.fill.background()

    # Main title
    add_text(slide, Inches(1.5), Inches(2.7), Inches(10.333), Inches(1.0),
             "Edukacja czy automatyzacja?",
             font_size=38, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)

    # Gold line below title
    line_bottom = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(4.0), Inches(3.85), Inches(5.333), Inches(0.03)
    )
    line_bottom.fill.solid()
    line_bottom.fill.fore_color.rgb = WARM_GOLD
    line_bottom.line.fill.background()

    # Subtitle
    subtitle = (
        "Wp\u0142yw korzystania z aplikacji fintechowych i robo-doradc\u00f3w\n"
        "na poziom wiedzy finansowej oraz \u015bwiadomo\u015b\u0107 ryzyka\n"
        "inwestor\u00f3w indywidualnych"
    )
    txBox = slide.shapes.add_textbox(Inches(2.0), Inches(4.2), Inches(9.333), Inches(1.5))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, line in enumerate(subtitle.split('\n')):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(0xB0, 0xB8, 0xC4)
        p.font.name = 'Segoe UI'
        p.alignment = PP_ALIGN.CENTER
        p.space_after = Pt(4)

    # Bottom project name
    add_text(slide, Inches(1.5), Inches(6.4), Inches(10.333), Inches(0.5),
             "Projekt Badania Jako\u015bciowego  |  Fintech a \u015bwiadomo\u015b\u0107 inwestycyjna",
             font_size=11, color=RGBColor(0x6B, 0x7B, 0x8D), alignment=PP_ALIGN.CENTER)


def create_slide2(prs):
    """Uzasadnienie wyboru tematu - single card with 3 internal columns."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Uzasadnienie wyboru tematu")

    # Single unified card
    card_left = Inches(0.6)
    card_top = Inches(1.5)
    card_width = Inches(12.1)
    card_height = Inches(5.5)
    add_unified_card(slide, card_left, card_top, card_width, card_height)

    # Internal vertical dividers
    col_width = Inches(3.9)
    add_vertical_divider(slide, Inches(4.6), Inches(1.9), Inches(4.7))
    add_vertical_divider(slide, Inches(8.7), Inches(1.9), Inches(4.7))

    # Column 1: Dlaczego aktualny?
    add_text(slide, Inches(1.0), Inches(1.8), Inches(3.4), Inches(0.5),
             "Dlaczego aktualny?", font_size=14, bold=True, color=TEAL_ACCENT)
    add_bullet_text(slide, Inches(1.0), Inches(2.5), Inches(3.3), Inches(4.0), [
        "Boom na aplikacje inwestycyjne\n   (Revolut, eToro, XTB)",
        "Rozwoj robo-doradztwa\n   (Finax, Portu)",
        "Niskie bariery wejscia\n   i gamifikacja inwestowania",
        "Rosna pytania o swiadomosc\n   ryzyka wsrod nowych uzytkownikow"
    ], font_size=11, spacing=10)

    # Column 2: Kogo dotyczy?
    add_text(slide, Inches(5.0), Inches(1.8), Inches(3.4), Inches(0.5),
             "Kogo dotyczy?", font_size=14, bold=True, color=TEAL_ACCENT)
    add_bullet_text(slide, Inches(5.0), Inches(2.5), Inches(3.3), Inches(4.0), [
        "Poczatkujacych inwestorow\n   detalicznych",
        "Osoby szukajace alternatywy\n   dla lokat bankowych",
        "Uzytkownikow, ktorych pierwszy\n   kontakt z rynkiem jest przez\n   smartfon"
    ], font_size=11, spacing=10)

    # Column 3: Jakie ma znaczenie?
    add_text(slide, Inches(9.1), Inches(1.8), Inches(3.4), Inches(0.5),
             "Jakie ma znaczenie?", font_size=14, bold=True, color=TEAL_ACCENT)
    add_bullet_text(slide, Inches(9.1), Inches(2.5), Inches(3.3), Inches(4.0), [
        "Dla KNF: ochrona konsumenta\n   i regulacje rynku",
        "Dla rynku: ryzyko paniki tlumu\n   i niestabilnosci",
        "Dla tworcow aplikacji:\n   odpowiedzialne projektowanie\n   interfejsow"
    ], font_size=11, spacing=10)


def create_slide3(prs):
    """Cel badania i pytania badawcze - single card, top/bottom split."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Cel badania i pytania badawcze")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    # Top section: Cel
    add_text(slide, Inches(1.0), Inches(1.8), Inches(3.0), Inches(0.4),
             "CEL BADANIA", font_size=13, bold=True, color=DARK_NAVY)

    cel_text = (
        "Zrozumienie, w jaki sposob interakcja z platformami fintechowymi "
        "i robo-doradcami ksztaltuje (lub nie) wiedze finansowa oraz "
        "swiadomosc ryzyka wsrod poczatkujacych inwestorow indywidualnych. "
        "Zbadanie, czy aplikacje pelnia role edukacyjna, czy raczej usypiaja "
        "czujnosc uzytkownikow."
    )
    add_text(slide, Inches(1.0), Inches(2.3), Inches(11.0), Inches(1.2),
             cel_text, font_size=12, color=TEXT_MEDIUM)

    # Horizontal divider
    add_horizontal_divider(slide, Inches(1.0), Inches(3.5), Inches(11.0))

    # Bottom section: Pytania badawcze
    add_text(slide, Inches(1.0), Inches(3.7), Inches(4.0), Inches(0.4),
             "PYTANIA BADAWCZE", font_size=13, bold=True, color=DARK_NAVY)

    questions = [
        "W jaki sposob interfejs aplikacji inwestycyjnych wplywa na "
        "subiektywne poczucie zrozumienia mechanizmow rynkowych?",
        "Dlaczego uzytkownicy podejmuja decyzje inwestycyjne - na podstawie "
        "wlasnej wiedzy czy w oparciu o algorytmy i rekomendacje aplikacji?",
        "Jak poczatkujacy inwestorzy interpretuja i oceniaja ryzyko "
        "w srodowisku cyfrowym przypominajacym gry?"
    ]
    add_numbered_text(slide, Inches(1.0), Inches(4.2), Inches(11.0), Inches(3.0),
                      questions, start_num=1, font_size=12, spacing=12)


def create_slide4(prs):
    """Charakterystyka badanych - single card with structured labels."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Charakterystyka badanych")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    items = [
        ("Kto?", "Osoby w wieku 25-40 lat, bez formalnego wyksztalcenia finansowego, "
         "aktywnie korzystajace z aplikacji inwestycyjnych"),
        ("Kryteria doboru:", "Inwestowanie za posrednictwem smartfona przez 12-24 miesiace, "
         "minimum 5 zrealizowanych transakcji"),
        ("Wielkosc proby:", "12-15 osob - swiezi inwestorzy, najbardziej narazeni "
         "na ryzyko nieswiadomych decyzji"),
        ("Dlaczego ta grupa?", "Najbardziej podatna na wplyw interfejsu aplikacji, "
         "brak doswiadczenia z tradycyjnym doradztwem finansowym"),
        ("Dobor proby:", "Celowy + metoda kuli snieznej (rekrutacja przez "
         "spolecznosci inwestorow online)")
    ]

    y_start = Inches(1.9)
    for i, (label, desc) in enumerate(items):
        y = y_start + Inches(i * 1.0)

        # Label (bold, teal)
        txBox = slide.shapes.add_textbox(Inches(1.0), y, Inches(11.0), Inches(0.8))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]

        run_label = p.add_run()
        run_label.text = f"{label}  "
        run_label.font.size = Pt(12)
        run_label.font.bold = True
        run_label.font.color.rgb = TEAL_ACCENT
        run_label.font.name = 'Segoe UI'

        run_desc = p.add_run()
        run_desc.text = desc
        run_desc.font.size = Pt(12)
        run_desc.font.color.rgb = TEXT_DARK
        run_desc.font.name = 'Segoe UI'

        # Thin separator line (except after last item)
        if i < len(items) - 1:
            add_horizontal_divider(slide, Inches(1.0), y + Inches(0.7), Inches(11.0))


def create_slide5(prs):
    """Dlaczego wywiad poglebiony (IDI)? - single card with 4 numbered points."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Dlaczego wywiad pog\u0142\u0119biony (IDI)?")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    reasons = [
        "Finanse osobiste to tematy wrazliwe - w grupie wystepuje "
        "presja spoleczna, ktora znieksztalca odpowiedzi",
        "Umozliwia dokladne prosledzenie zachowania respondenta "
        "i jego interakcji z aplikacja krok po kroku",
        "Pozwala na odtworzenie calego procesu podejmowania decyzji "
        "inwestycyjnej w naturalny sposob",
        "Daje swobode reagowania, dopytywania i poglebiania "
        "interesujacych watkow w czasie rzeczywistym"
    ]

    add_numbered_text(slide, Inches(1.2), Inches(2.0), Inches(10.8), Inches(4.5),
                      reasons, start_num=1, font_size=13, spacing=18,
                      num_color=TEAL_ACCENT)


def create_slide6(prs):
    """Scenariusz wywiadu - A. Wprowadzenie - single card with 2 questions."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Scenariusz wywiadu \u2013 A. Wprowadzenie")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    # Section label
    add_text(slide, Inches(1.0), Inches(1.8), Inches(6.0), Inches(0.4),
             "PYTANIA OTWIERAJACE", font_size=11, bold=True, color=TEXT_MEDIUM)

    questions = [
        "Jakie byly Pana/Pani motywacje, zeby zaczac lokowac "
        "oszczednosci poza kontem bankowym lub lokata?",
        "Z jakich aplikacji inwestycyjnych Pan(i) korzysta "
        "i co zadecydowalo o ich wyborze?"
    ]

    add_numbered_text(slide, Inches(1.2), Inches(2.5), Inches(10.8), Inches(4.0),
                      questions, start_num=1, font_size=14, spacing=24,
                      num_color=TEAL_ACCENT)


def create_slide7(prs):
    """Scenariusz wywiadu - B. Czesc glowna - single card with questions 3-9."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Scenariusz wywiadu \u2013 B. Cz\u0119\u015b\u0107 g\u0142\u00f3wna")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    # Section label
    add_text(slide, Inches(1.0), Inches(1.8), Inches(6.0), Inches(0.4),
             "PYTANIA GLOWNE", font_size=11, bold=True, color=TEXT_MEDIUM)

    questions = [
        "Prosze opowiedziec o pierwszej transakcji krok po kroku",
        "Jak aplikacja pomaga zrozumiec, w co inwestowane sa pieniadze?",
        "Czy zdarzyla sie decyzja pod wplywem impulsu z ekranu glownego?",
        "Prosze wyjasnic swoimi slowami czym jest ETF lub akcja",
        "Jak reaguje Pan(i) na komunikaty o ryzyku utraty kapitalu?",
        "Co robi Pan(i) gdy portfel jest na czerwono (strata)?",
        "Czy wiedza o finansach wzrosla od momentu uzycia aplikacji?"
    ]

    add_numbered_text(slide, Inches(1.2), Inches(2.4), Inches(10.8), Inches(4.5),
                      questions, start_num=3, font_size=12, spacing=10,
                      num_color=TEAL_ACCENT)


def create_slide8(prs):
    """Scenariusz wywiadu - C. Zakonczenie - single card with questions 10-12."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Scenariusz wywiadu \u2013 C. Zako\u0144czenie")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    # Section label
    add_text(slide, Inches(1.0), Inches(1.8), Inches(6.0), Inches(0.4),
             "PYTANIA ZAMYKAJACE", font_size=11, bold=True, color=TEXT_MEDIUM)

    questions = [
        "Czy uwaza Pan(i), ze aplikacje powinny sprawdzac "
        "poziom wiedzy uzytkownika przed umozliwieniem zakupu "
        "instrumentow finansowych?",
        "Na co ostrzeglby/ostrzeglaby Pan(i) znajomego, ktory "
        "nie ma wiedzy finansowej, a chce zaczac inwestowac "
        "przez aplikacje?",
        "Czy jest jeszcze cos waznego zwiazanego z tym tematem, "
        "o czym nie zapytalem, a chcialby/chcialaby Pan(i) powiedziec?"
    ]

    add_numbered_text(slide, Inches(1.2), Inches(2.5), Inches(10.8), Inches(4.0),
                      questions, start_num=10, font_size=13, spacing=20,
                      num_color=TEAL_ACCENT)


def create_slide9(prs):
    """Ograniczenia badania - single card with 3 sections."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_GRAY)
    add_top_banner(slide, "Ograniczenia badania")

    # Single unified card
    add_unified_card(slide, Inches(0.6), Inches(1.5), Inches(12.1), Inches(5.5))

    # Section 1
    add_text(slide, Inches(1.0), Inches(1.8), Inches(10.0), Inches(0.4),
             "1.  Efekt Dunninga-Krugera", font_size=13, bold=True, color=DARK_NAVY)
    add_bullet_text(slide, Inches(1.4), Inches(2.3), Inches(10.0), Inches(1.2), [
        "Respondenci moga przeceniac swoja wiedze, szczegolnie w okresie hossy",
        "Zludzenie kontroli wynikajace z prostoty interfejsu aplikacji"
    ], font_size=11, color=TEXT_MEDIUM, spacing=6)

    # Divider
    add_horizontal_divider(slide, Inches(1.0), Inches(3.4), Inches(11.0))

    # Section 2
    add_text(slide, Inches(1.0), Inches(3.6), Inches(10.0), Inches(0.4),
             "2.  Trudnosc ewaluacji wiedzy", font_size=13, bold=True, color=DARK_NAVY)
    add_bullet_text(slide, Inches(1.4), Inches(4.1), Inches(10.0), Inches(1.2), [
        "Wywiad poglebiony nie jest testem wiedzy - nie mozna stosowac punktacji",
        "Respondent nie moze czuc sie jak na egzaminie, co ogranicza weryfikacje"
    ], font_size=11, color=TEXT_MEDIUM, spacing=6)

    # Divider
    add_horizontal_divider(slide, Inches(1.0), Inches(5.2), Inches(11.0))

    # Section 3
    add_text(slide, Inches(1.0), Inches(5.4), Inches(10.0), Inches(0.4),
             "3.  Bariera technologiczna", font_size=13, bold=True, color=DARK_NAVY)
    add_bullet_text(slide, Inches(1.4), Inches(5.9), Inches(10.0), Inches(1.2), [
        "Rozne interfejsy aplikacji - odpowiedzi zaleza od konkretnego rozwiazania",
        "Trudnosc znalezienia wspolnych mianownikow miedzy platformami"
    ], font_size=11, color=TEXT_MEDIUM, spacing=6)


# ============================================================
# MAIN
# ============================================================

def main():
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT

    create_slide1(prs)
    create_slide2(prs)
    create_slide3(prs)
    create_slide4(prs)
    create_slide5(prs)
    create_slide6(prs)
    create_slide7(prs)
    create_slide8(prs)
    create_slide9(prs)

    output_path = "/projects/sandbox/github/Prezentacja_Fintech.pptx"
    prs.save(output_path)
    print(f"Presentation saved to: {output_path}")
    print(f"Total slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()
