#!/usr/bin/env python3
"""
Create a modern business-style Fintech presentation in Polish.
Uses python-pptx to generate a 16:9 widescreen PowerPoint file.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import copy

# ============================================================
# CONSTANTS
# ============================================================

PRIMARY_DARK = RGBColor(0x1B, 0x28, 0x38)
TEAL_ACCENT = RGBColor(0x00, 0xB4, 0xD8)
ORANGE_ACCENT = RGBColor(0xF4, 0xA2, 0x61)
LIGHT_BG = RGBColor(0xF8, 0xF9, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_TEXT = RGBColor(0x1B, 0x2B, 0x3C)
GRAY_TEXT = RGBColor(0x6C, 0x75, 0x7D)

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


def add_shape_with_transparency(slide, shape_type, left, top, width, height, color, transparency=0.85):
    """Add a semi-transparent shape (decorative circle)."""
    shape = slide.shapes.add_shape(shape_type, left, top, width, height)
    shape.line.fill.background()
    fill = shape.fill
    fill.solid()
    fill.fore_color.rgb = color
    # Set transparency via XML on the spPr/solidFill/srgbClr element
    spPr = shape._element.spPr
    solidFill = spPr.find(qn('a:solidFill'))
    srgbClr = solidFill.find(qn('a:srgbClr'))
    alpha = srgbClr.makeelement(qn('a:alpha'), {})
    alpha.set('val', str(int((1 - transparency) * 100000)))
    srgbClr.append(alpha)
    return shape


def add_decorative_circles(slide, dark_bg=False):
    """Add semi-transparent decorative circles in corners."""
    color = TEAL_ACCENT if dark_bg else PRIMARY_DARK
    # Top-right circle
    add_shape_with_transparency(
        slide, MSO_SHAPE.OVAL,
        Inches(11.0), Inches(-0.8), Inches(3.0), Inches(3.0),
        color, 0.88
    )
    # Bottom-left circle
    add_shape_with_transparency(
        slide, MSO_SHAPE.OVAL,
        Inches(-1.0), Inches(5.5), Inches(2.5), Inches(2.5),
        ORANGE_ACCENT, 0.90
    )


def add_sidebar(slide, color=TEAL_ACCENT):
    """Add a colored sidebar on the left."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.15), SLIDE_HEIGHT
    )
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = color


def add_bottom_bar(slide, color=TEAL_ACCENT):
    """Add a colored accent bar at the bottom."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.2), SLIDE_WIDTH, Inches(0.3)
    )
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = color


def add_rounded_card(slide, left, top, width, height, border_color=None, fill_color=WHITE):
    """Add a rounded rectangle card with optional colored top border."""
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    card.fill.solid()
    card.fill.fore_color.rgb = fill_color
    card.line.color.rgb = RGBColor(0xE0, 0xE0, 0xE0)
    card.line.width = Pt(0.5)
    # Add shadow effect via adjusting the shape
    card.shadow.inherit = False

    if border_color:
        # Add a thin rectangle on top as color border
        border = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, Inches(0.12)
        )
        border.fill.solid()
        border.fill.fore_color.rgb = border_color
        border.line.fill.background()

    return card


def add_text_box(slide, left, top, width, height, text, font_size=12,
                 bold=False, color=DARK_TEXT, alignment=PP_ALIGN.LEFT,
                 font_name='Segoe UI'):
    """Add a text box with specified formatting."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_multiline_text_box(slide, left, top, width, height, lines, font_size=11,
                           color=DARK_TEXT, line_spacing=1.3, bullet=False,
                           font_name='Segoe UI'):
    """Add a text box with multiple lines/paragraphs."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        if bullet:
            p.text = f"\u2022 {line}"
        else:
            p.text = line
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = font_name
        p.space_after = Pt(4)
    return txBox


def add_numbered_badge(slide, left, top, number, color=TEAL_ACCENT, size=Inches(0.4)):
    """Add a colored circle with a number inside."""
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    tf = circle.text_frame
    tf.word_wrap = False
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    run = tf.paragraphs[0].add_run()
    run.text = str(number)
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = WHITE
    run.font.name = 'Segoe UI'
    return circle


def add_slide_title(slide, text, dark_bg=False, font_size=28):
    """Add a slide title."""
    color = WHITE if dark_bg else PRIMARY_DARK
    add_text_box(slide, Inches(0.6), Inches(0.3), Inches(10), Inches(0.8),
                 text, font_size=font_size, bold=True, color=color)


# ============================================================
# SLIDE CREATION FUNCTIONS
# ============================================================

def create_slide1(prs):
    """Title slide - dark background."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    set_slide_bg(slide, PRIMARY_DARK)
    add_decorative_circles(slide, dark_bg=True)
    add_bottom_bar(slide, TEAL_ACCENT)

    # Title
    add_text_box(
        slide, Inches(1.0), Inches(2.0), Inches(11.0), Inches(1.2),
        "Edukacja czy automatyzacja?",
        font_size=40, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER
    )

    # Subtitle
    subtitle = (
        "Wp\u0142yw korzystania z aplikacji fintechowych i robo-doradc\u00f3w "
        "na poziom wiedzy finansowej oraz \u015bwiadomo\u015b\u0107 ryzyka "
        "inwestor\u00f3w indywidualnych."
    )
    add_text_box(
        slide, Inches(1.5), Inches(3.3), Inches(10.0), Inches(1.5),
        subtitle,
        font_size=18, bold=False, color=RGBColor(0xCC, 0xCC, 0xCC),
        alignment=PP_ALIGN.CENTER
    )

    # Bottom text
    bottom_text = "Projekt Badania Jako\u015bciowego: Fintech a \u015bwiadomo\u015b\u0107 inwestycyjna"
    add_text_box(
        slide, Inches(1.0), Inches(6.2), Inches(11.0), Inches(0.6),
        bottom_text,
        font_size=13, bold=False, color=TEAL_ACCENT, alignment=PP_ALIGN.CENTER
    )


def create_slide2(prs):
    """3-column cards - Uzasadnienie wyboru tematu."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_BG)
    add_sidebar(slide, TEAL_ACCENT)
    add_bottom_bar(slide, ORANGE_ACCENT)
    add_decorative_circles(slide, dark_bg=False)

    add_slide_title(slide, "Uzasadnienie wyboru tematu")

    # Card 1
    card_top = Inches(1.4)
    card_height = Inches(5.0)
    card_width = Inches(3.8)

    add_rounded_card(slide, Inches(0.6), card_top, card_width, card_height, TEAL_ACCENT)
    add_text_box(slide, Inches(0.9), Inches(1.8), Inches(3.3), Inches(0.5),
                 "Dlaczego aktualny?", font_size=14, bold=True, color=TEAL_ACCENT)
    lines1 = [
        "Boom na aplikacje (Revolut, eToro, XTB) + robo-doradztwo (Finax, Portu)",
        "Niskie bariery wej\u015bcia, gamifikacja",
        "Pytania o \u015bwiadomo\u015b\u0107 ryzyka"
    ]
    add_multiline_text_box(slide, Inches(0.9), Inches(2.4), Inches(3.3), Inches(3.5),
                           lines1, font_size=11, bullet=True)

    # Card 2
    add_rounded_card(slide, Inches(4.7), card_top, card_width, card_height, ORANGE_ACCENT)
    add_text_box(slide, Inches(5.0), Inches(1.8), Inches(3.3), Inches(0.5),
                 "Kogo dotyczy?", font_size=14, bold=True, color=ORANGE_ACCENT)
    lines2 = [
        "Pocz\u0105tkuj\u0105cych inwestor\u00f3w detalicznych",
        "Szukaj\u0105 alternatywy dla lokat",
        "Pierwszy kontakt z rynkiem przez smartfon"
    ]
    add_multiline_text_box(slide, Inches(5.0), Inches(2.4), Inches(3.3), Inches(3.5),
                           lines2, font_size=11, bullet=True)

    # Card 3
    add_rounded_card(slide, Inches(8.8), card_top, card_width, card_height, PRIMARY_DARK)
    add_text_box(slide, Inches(9.1), Inches(1.8), Inches(3.3), Inches(0.5),
                 "Jakie ma znaczenie?", font_size=14, bold=True, color=PRIMARY_DARK)
    lines3 = [
        "Dla KNF \u2013 ochrona konsumenta",
        "Dla rynku \u2013 ryzyko paniki t\u0142umu",
        "Dla tw\u00f3rc\u00f3w \u2013 odpowiedzialne projektowanie"
    ]
    add_multiline_text_box(slide, Inches(9.1), Inches(2.4), Inches(3.3), Inches(3.5),
                           lines3, font_size=11, bullet=True)


def create_slide3(prs):
    """Two-column - Cel badania i pytania badawcze."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, WHITE)
    add_sidebar(slide, ORANGE_ACCENT)
    add_bottom_bar(slide, TEAL_ACCENT)
    add_decorative_circles(slide, dark_bg=False)

    add_slide_title(slide, "Cel badania i pytania badawcze")

    # Left column - teal card
    add_rounded_card(slide, Inches(0.6), Inches(1.5), Inches(5.5), Inches(5.2), TEAL_ACCENT)
    add_text_box(slide, Inches(1.0), Inches(1.9), Inches(4.8), Inches(0.5),
                 "Cel", font_size=16, bold=True, color=TEAL_ACCENT)
    cel_lines = [
        "Zrozumienie czy interakcja z platformami kszta\u0142tuje wiedz\u0119",
        "",
        "Czy aplikacje edukuj\u0105 czy usypiaj\u0105 czujno\u015b\u0107"
    ]
    add_multiline_text_box(slide, Inches(1.0), Inches(2.5), Inches(4.8), Inches(3.5),
                           cel_lines, font_size=13, bullet=True)

    # Right column - numbered questions
    add_text_box(slide, Inches(6.5), Inches(1.9), Inches(5.5), Inches(0.5),
                 "Pytania badawcze", font_size=16, bold=True, color=PRIMARY_DARK)

    questions = [
        "Jak interfejs wp\u0142ywa na poczucie zrozumienia rynku?",
        "Dlaczego u\u017cytkownicy podejmuj\u0105 decyzje \u2013 w\u0142asna wiedza vs algorytmy?",
        "Jak pocz\u0105tkuj\u0105cy interpretuj\u0105 ryzyko w \u015brodowisku przypominaj\u0105cym gry?"
    ]

    for i, q in enumerate(questions):
        y_pos = Inches(2.6 + i * 1.5)
        add_numbered_badge(slide, Inches(6.5), y_pos, i + 1, TEAL_ACCENT)
        add_text_box(slide, Inches(7.1), y_pos, Inches(5.5), Inches(1.2),
                     q, font_size=12, color=DARK_TEXT)


def create_slide4(prs):
    """4-card grid - Charakterystyka badanych."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_BG)
    add_sidebar(slide, TEAL_ACCENT)
    add_bottom_bar(slide, ORANGE_ACCENT)
    add_decorative_circles(slide, dark_bg=False)

    add_slide_title(slide, "Charakterystyka badanych")

    cards_data = [
        ("Kto", "Osoby 25\u201340 lat, bez wykszta\u0142cenia finansowego", TEAL_ACCENT),
        ("Kryteria", "Inwestowanie przez smartfon 12\u201324 mies., min. 5 transakcji", ORANGE_ACCENT),
        ("Wielko\u015b\u0107 pr\u00f3by", "12\u201315 os\u00f3b; \u015awie\u017cy inwestorzy najbardziej nara\u017ceni", PRIMARY_DARK),
        ("Dob\u00f3r", "Celowy + metoda kuli \u015bnieznej", TEAL_ACCENT),
    ]

    positions = [
        (Inches(0.6), Inches(1.5)),
        (Inches(6.8), Inches(1.5)),
        (Inches(0.6), Inches(4.2)),
        (Inches(6.8), Inches(4.2)),
    ]

    for (title, desc, color), (left, top) in zip(cards_data, positions):
        add_rounded_card(slide, left, top, Inches(5.8), Inches(2.3), color)
        add_text_box(slide, left + Inches(0.4), top + Inches(0.4), Inches(5.0), Inches(0.5),
                     title, font_size=14, bold=True, color=color)
        add_text_box(slide, left + Inches(0.4), top + Inches(1.1), Inches(5.0), Inches(1.0),
                     desc, font_size=12, color=DARK_TEXT)


def create_slide5(prs):
    """Dark bg with cards - Dlaczego wywiad pog\u0142\u0119biony (IDI)?"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, PRIMARY_DARK)
    add_decorative_circles(slide, dark_bg=True)
    add_bottom_bar(slide, ORANGE_ACCENT)

    add_slide_title(slide, "Dlaczego wywiad pog\u0142\u0119biony (IDI)?", dark_bg=True)

    reasons = [
        "Finanse osobiste to tematy wra\u017cliwe \u2013 presja spo\u0142eczna w grupie",
        "Dok\u0142adne prze\u015bledzenie zachowania i interakcji z aplikacj\u0105",
        "Odtworzenie procesu decyzji krok po kroku",
        "Swoboda reagowania, dopytywania i pog\u0142\u0119biania w\u0105tk\u00f3w"
    ]

    colors = [TEAL_ACCENT, ORANGE_ACCENT, TEAL_ACCENT, ORANGE_ACCENT]

    for i, (reason, badge_color) in enumerate(zip(reasons, colors)):
        y_pos = Inches(1.8 + i * 1.35)
        # Card background
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), y_pos, Inches(10.8), Inches(1.1)
        )
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(0x25, 0x35, 0x48)
        card.line.fill.background()

        add_numbered_badge(slide, Inches(1.5), y_pos + Inches(0.3), i + 1, badge_color, Inches(0.45))
        add_text_box(slide, Inches(2.2), y_pos + Inches(0.3), Inches(9.5), Inches(0.7),
                     reason, font_size=13, color=WHITE)


def create_slide6(prs):
    """Scenariusz wywiadu - A. Wprowadzenie."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, WHITE)
    add_sidebar(slide, TEAL_ACCENT)
    add_bottom_bar(slide, TEAL_ACCENT)
    add_decorative_circles(slide, dark_bg=False)

    add_slide_title(slide, "Scenariusz wywiadu \u2013 A. Wprowadzenie")

    questions = [
        "Jakie by\u0142y motywacje by lokowa\u0107 oszcz\u0119dno\u015bci poza kontem bankowym?",
        "Z jakich aplikacji Pan(i) korzysta i dlaczego?"
    ]

    for i, q in enumerate(questions):
        y_pos = Inches(2.0 + i * 2.2)
        add_rounded_card(slide, Inches(0.8), y_pos, Inches(11.5), Inches(1.8), TEAL_ACCENT)
        add_numbered_badge(slide, Inches(1.2), y_pos + Inches(0.6), i + 1, TEAL_ACCENT, Inches(0.5))
        add_text_box(slide, Inches(2.0), y_pos + Inches(0.6), Inches(9.8), Inches(0.8),
                     q, font_size=14, color=DARK_TEXT)


def create_slide7(prs):
    """Scenariusz wywiadu - B. Cz\u0119\u015b\u0107 g\u0142\u00f3wna."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, LIGHT_BG)
    add_sidebar(slide, ORANGE_ACCENT)
    add_bottom_bar(slide, ORANGE_ACCENT)
    add_decorative_circles(slide, dark_bg=False)

    add_slide_title(slide, "Scenariusz wywiadu \u2013 B. Cz\u0119\u015b\u0107 g\u0142\u00f3wna")

    questions = [
        "Opowie\u015b\u0107 o pierwszej transakcji krok po kroku",
        "Jak aplikacja pomaga zrozumie\u0107 w co inwestowane s\u0105 pieni\u0105dze?",
        "Decyzja pod wp\u0142ywem impulsu z ekranu g\u0142\u00f3wnego?",
        "Wyja\u015bnienie swoimi s\u0142owami czym jest ETF/akcja",
        "Reakcja na komunikaty o ryzyku utraty kapita\u0142u",
        "Co robi gdy portfel jest na czerwono?",
        "Czy wiedza o finansach wzros\u0142a od u\u017cycia aplikacji?"
    ]

    for i, q in enumerate(questions):
        y_pos = Inches(1.4 + i * 0.82)
        add_numbered_badge(slide, Inches(0.8), y_pos, i + 3, ORANGE_ACCENT, Inches(0.38))
        add_text_box(slide, Inches(1.4), y_pos, Inches(11.0), Inches(0.7),
                     q, font_size=12, color=DARK_TEXT)


def create_slide8(prs):
    """Scenariusz wywiadu - C. Zako\u0144czenie."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, WHITE)
    add_sidebar(slide, PRIMARY_DARK)
    add_bottom_bar(slide, PRIMARY_DARK)
    add_decorative_circles(slide, dark_bg=False)

    add_slide_title(slide, "Scenariusz wywiadu \u2013 C. Zako\u0144czenie")

    questions = [
        "Czy aplikacje powinny sprawdza\u0107 wiedz\u0119 przed zakupem?",
        "Na co ostrzec znajomego bez wiedzy finansowej?",
        "Czy jest jeszcze co\u015b wa\u017cnego o czym nie zapyta\u0142em?"
    ]

    for i, q in enumerate(questions):
        y_pos = Inches(2.0 + i * 1.6)
        add_rounded_card(slide, Inches(0.8), y_pos, Inches(11.5), Inches(1.3), PRIMARY_DARK)
        add_numbered_badge(slide, Inches(1.2), y_pos + Inches(0.4), i + 10, PRIMARY_DARK, Inches(0.5))
        add_text_box(slide, Inches(2.0), y_pos + Inches(0.4), Inches(9.8), Inches(0.7),
                     q, font_size=14, color=DARK_TEXT)


def create_slide9(prs):
    """Dark bg, 3 cards - Ograniczenia badania."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, PRIMARY_DARK)
    add_decorative_circles(slide, dark_bg=True)
    add_bottom_bar(slide, TEAL_ACCENT)

    add_slide_title(slide, "Ograniczenia badania", dark_bg=True)

    # Card 1 - Teal
    add_rounded_card(slide, Inches(0.5), Inches(1.6), Inches(3.9), Inches(5.0), TEAL_ACCENT)
    add_text_box(slide, Inches(0.9), Inches(2.0), Inches(3.2), Inches(0.5),
                 "Efekt Dunninga-Krugera", font_size=13, bold=True, color=TEAL_ACCENT)
    lines1 = [
        "Przecenianie wiedzy w hossie",
        "Z\u0142udzenie kontroli"
    ]
    add_multiline_text_box(slide, Inches(0.9), Inches(2.6), Inches(3.2), Inches(3.0),
                           lines1, font_size=11, bullet=True)

    # Card 2 - Orange
    add_rounded_card(slide, Inches(4.7), Inches(1.6), Inches(3.9), Inches(5.0), ORANGE_ACCENT)
    add_text_box(slide, Inches(5.1), Inches(2.0), Inches(3.2), Inches(0.5),
                 "Trudno\u015b\u0107 ewaluacji wiedzy", font_size=13, bold=True, color=ORANGE_ACCENT)
    lines2 = [
        "Wywiad nie jest testem",
        "Badany nie mo\u017ce czu\u0107 si\u0119 jak na egzaminie"
    ]
    add_multiline_text_box(slide, Inches(5.1), Inches(2.6), Inches(3.2), Inches(3.0),
                           lines2, font_size=11, bullet=True)

    # Card 3 - White/Light
    add_rounded_card(slide, Inches(8.9), Inches(1.6), Inches(3.9), Inches(5.0), WHITE)
    add_text_box(slide, Inches(9.3), Inches(2.0), Inches(3.2), Inches(0.5),
                 "Bariera technologiczna", font_size=13, bold=True, color=PRIMARY_DARK)
    lines3 = [
        "R\u00f3\u017cne interfejsy",
        "Odpowiedzi zale\u017c\u0105 od rozwi\u0105zania",
        "Trudno\u015b\u0107 wsp\u00f3lnych mianownik\u00f3w"
    ]
    add_multiline_text_box(slide, Inches(9.3), Inches(2.6), Inches(3.2), Inches(3.0),
                           lines3, font_size=11, bullet=True)


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
