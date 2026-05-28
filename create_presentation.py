#!/usr/bin/env python3
"""Generate Fintech presentation PPTX file."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import copy

# Colors
NAVY = RGBColor(0x1F, 0x38, 0x64)
BLUE_ACCENT = RGBColor(0x2E, 0x75, 0xB6)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xF2, 0xF2, 0xF2)
DARK_TEXT = RGBColor(0x33, 0x33, 0x33)

# Create presentation with 16:9 widescreen
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)


def add_background(slide, color):
    """Set slide background color."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_accent_bar(slide):
    """Add a thin accent bar at the top of the slide."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
        prs.slide_width, Inches(0.15)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = BLUE_ACCENT
    shape.line.fill.background()


def add_title_shape(slide, title_text, top=Inches(0.4)):
    """Add a styled title text box."""
    txBox = slide.shapes.add_textbox(Inches(0.8), top, Inches(11.5), Inches(0.9))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = NAVY
    return txBox


def add_content_frame(slide, top=Inches(1.5), left=Inches(0.8), width=Inches(11.5), height=Inches(5.5)):
    """Add a content text box and return its text frame."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    return tf


def add_bullet(tf, text, level=0, bold=False, font_size=Pt(18), space_before=Pt(6), space_after=Pt(4), color=DARK_TEXT):
    """Add a bullet point paragraph."""
    p = tf.add_paragraph()
    p.text = text
    p.level = level
    p.font.size = font_size
    p.font.bold = bold
    p.font.color.rgb = color
    p.space_before = space_before
    p.space_after = space_after
    return p


# ============================================================
# SLIDE 1: Title Slide
# ============================================================
slide1 = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
add_background(slide1, NAVY)

# Main title
txBox = slide1.shapes.add_textbox(Inches(1.5), Inches(1.8), Inches(10.3), Inches(1.5))
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = u'\u201eEdukacja czy automatyzacja?\u201d'
p.font.size = Pt(38)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Subtitle
txBox2 = slide1.shapes.add_textbox(Inches(1.5), Inches(3.3), Inches(10.3), Inches(1.8))
tf2 = txBox2.text_frame
tf2.word_wrap = True
p2 = tf2.paragraphs[0]
p2.text = (
    u'Wp\u0142yw korzystania z aplikacji fintechowych i robo-doradc\u00f3w '
    u'na poziom wiedzy finansowej oraz \u015bwiadomo\u015b\u0107 ryzyka '
    u'inwestor\u00f3w indywidualnych.'
)
p2.font.size = Pt(20)
p2.font.color.rgb = RGBColor(0xBD, 0xD7, 0xEE)
p2.alignment = PP_ALIGN.CENTER

# Bottom text
txBox3 = slide1.shapes.add_textbox(Inches(1.5), Inches(5.8), Inches(10.3), Inches(0.8))
tf3 = txBox3.text_frame
tf3.word_wrap = True
p3 = tf3.paragraphs[0]
p3.text = u'Projekt Badania Jako\u015bciowego: Fintech a \u015bwiadomo\u015b\u0107 inwestycyjna'
p3.font.size = Pt(14)
p3.font.color.rgb = RGBColor(0x9D, 0xC3, 0xE6)
p3.alignment = PP_ALIGN.CENTER

# Accent line
shape = slide1.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(4.5), Inches(5.5),
    Inches(4.3), Inches(0.04)
)
shape.fill.solid()
shape.fill.fore_color.rgb = BLUE_ACCENT
shape.line.fill.background()



# ============================================================
# SLIDE 2: Uzasadnienie wyboru tematu
# ============================================================
slide2 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide2, WHITE)
add_accent_bar(slide2)
add_title_shape(slide2, u'Uzasadnienie wyboru tematu')

tf = add_content_frame(slide2)

# Section 1
add_bullet(tf, u'Dlaczego ten problem jest aktualny?', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(0))
add_bullet(tf, u'Rynek prze\u017cywa boom na aplikacje inwestycyjne (Revolut, eToro, XTB) oraz us\u0142ugi robo-doradztwa (Finax, Portu)', level=1, font_size=Pt(16))
add_bullet(tf, u'Niskie bariery wej\u015bcia, brak minimalnych kwot oraz \u201egamifikacja\u201d interfejs\u00f3w sprawiaj\u0105, \u017ce inwestowanie sta\u0142o si\u0119 dost\u0119pne na jedno klikni\u0119cie', level=1, font_size=Pt(16))
add_bullet(tf, u'Rodzi to pytania o rzeczywist\u0105 \u015bwiadomo\u015b\u0107 ryzyka', level=1, font_size=Pt(16))

# Section 2
add_bullet(tf, u'Kogo dotyczy?', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(16))
add_bullet(tf, u'Pocz\u0105tkuj\u0105cych inwestor\u00f3w detalicznych oraz gospodarstw domowych', level=1, font_size=Pt(16))
add_bullet(tf, u'Szukaj\u0105 alternatywy dla nisko oprocentowanych lokat bankowych', level=1, font_size=Pt(16))
add_bullet(tf, u'Po raz pierwszy stykaj\u0105 si\u0119 z rynkiem kapita\u0142owym za po\u015brednictwem smartfona', level=1, font_size=Pt(16))

# Section 3
add_bullet(tf, u'Jakie ma znaczenie?', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(16))
add_bullet(tf, u'Dla regulator\u00f3w (KNF) \u2013 wiedza o skuteczno\u015bci ostrze\u017ce\u0144 o ryzyku i potrzebie ochrony konsumenta', level=1, font_size=Pt(16))
add_bullet(tf, u'Dla rynku finansowego \u2013 ocena ryzyka \u201epaniki t\u0142umu\u201d', level=1, font_size=Pt(16))
add_bullet(tf, u'Dla tw\u00f3rc\u00f3w aplikacji \u2013 wskaz\u00f3wki z zakresu odpowiedzialnego projektowania', level=1, font_size=Pt(16))



# ============================================================
# SLIDE 3: Cel badania i pytania badawcze
# ============================================================
slide3 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide3, WHITE)
add_accent_bar(slide3)
add_title_shape(slide3, u'Cel badania i pytania badawcze')

tf = add_content_frame(slide3, top=Inches(1.4), height=Inches(5.8))

add_bullet(tf, u'Cel:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(0))
add_bullet(tf, (
    u'Zrozumienie, czy i w jaki spos\u00f3b interakcja z nowoczesnymi platformami inwestycyjnymi '
    u'kszta\u0142tuje rzeczywist\u0105 wiedz\u0119 finansow\u0105 u\u017cytkownik\u00f3w. Zbadanie, czy aplikacje te pe\u0142ni\u0105 '
    u'funkcj\u0119 edukacyjn\u0105, buduj\u0105c \u015bwiadomo\u015b\u0107 rynkow\u0105, czy raczej zwalniaj\u0105 u\u017cytkownika '
    u'z my\u015blenia, usypiaj\u0105c czujno\u015b\u0107.'
), level=1, font_size=Pt(15))

add_bullet(tf, u'Pytania badawcze:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(16))
add_bullet(tf, (
    u'1. W jaki spos\u00f3b interfejs i funkcjonalno\u015bci aplikacji finansowych wp\u0142ywaj\u0105 na poczucie '
    u'zrozumienia rynku i pewno\u015b\u0107 siebie inwestor\u00f3w indywidualnych?'
), level=1, font_size=Pt(15))
add_bullet(tf, (
    u'2. Dlaczego u\u017cytkownicy podejmuj\u0105 decyzje o zakupie konkretnych instrument\u00f3w \u2013 '
    u'w jakim stopniu opieraj\u0105 si\u0119 na w\u0142asnej wiedzy i analizie, a w jakim na sugestiach '
    u'algorytm\u00f3w i \u0142atwo\u015bci \u201eklikni\u0119cia\u201d?'
), level=1, font_size=Pt(15))
add_bullet(tf, (
    u'3. Jak pocz\u0105tkuj\u0105cy inwestorzy rozumiej\u0105 i interpretuj\u0105 ryzyko utraty kapita\u0142u '
    u'w \u015brodowisku aplikacji, kt\u00f3re przypominaj\u0105 gry mobilne lub platformy spo\u0142eczno\u015bciowe?'
), level=1, font_size=Pt(15))



# ============================================================
# SLIDE 4: Charakterystyka badanych
# ============================================================
slide4 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide4, WHITE)
add_accent_bar(slide4)
add_title_shape(slide4, u'Charakterystyka badanych')

tf = add_content_frame(slide4)

add_bullet(tf, u'Kto b\u0119dzie rozm\u00f3wc\u0105:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(0))
add_bullet(tf, u'Osoby doros\u0142e (25\u201340 lat), zarz\u0105dzaj\u0105ce w\u0142asnym bud\u017cetem domowym', level=1, font_size=Pt(16))
add_bullet(tf, u'Bez wykszta\u0142cenia kierunkowego (finansowego/ekonomicznego)', level=1, font_size=Pt(16))

add_bullet(tf, u'Kryteria w\u0142\u0105czaj\u0105ce:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(14))
add_bullet(tf, u'Rozpocz\u0119cie samodzielnego inwestowania za po\u015brednictwem smartfona w ci\u0105gu ostatnich 12\u201324 miesi\u0119cy', level=1, font_size=Pt(16))
add_bullet(tf, u'Minimum 5 zrealizowanych transakcji', level=1, font_size=Pt(16))

add_bullet(tf, u'Wielko\u015b\u0107 pr\u00f3by:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(14))
add_bullet(tf, u'12\u201315 os\u00f3b (nasycenie informacyjne)', level=1, font_size=Pt(16))

add_bullet(tf, u'Dlaczego ta grupa:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(14))
add_bullet(tf, u'\u201e\u015awie\u017cy\u201d inwestorzy detaliczni s\u0105 najbardziej nara\u017ceni na skutki braku edukacji, a ich nawyki dopiero si\u0119 kszta\u0142tuj\u0105', level=1, font_size=Pt(16))

add_bullet(tf, u'Dob\u00f3r pr\u00f3by:', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(14))
add_bullet(tf, u'Celowy (selekcja wed\u0142ug kryteri\u00f3w sta\u017cu i u\u017cywanych aplikacji) po\u0142\u0105czony z metod\u0105 kuli \u015bnie\u017cnej', level=1, font_size=Pt(16))



# ============================================================
# SLIDE 5: Uzasadnienie wyboru metody (IDI)
# ============================================================
slide5 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide5, WHITE)
add_accent_bar(slide5)
add_title_shape(slide5, u'Dlaczego wywiad pog\u0142\u0119biony (IDI)?')

tf = add_content_frame(slide5)

add_bullet(tf, (
    u'Finanse osobiste (straty, b\u0142\u0119dy, brak wiedzy) to tematy mocno wra\u017cliwe \u2013 '
    u'w grupie uczestnicy ulegaliby presji spo\u0142ecznej'
), level=0, font_size=Pt(18), space_before=Pt(0))

add_bullet(tf, (
    u'Zale\u017cy nam na bardzo dok\u0142adnym prze\u015bledzeniu zachowania u\u017cytkownika '
    u'i jego interakcji z aplikacj\u0105'
), level=0, font_size=Pt(18), space_before=Pt(12))

add_bullet(tf, (
    u'Chcemy, \u017ceby rozm\u00f3wca odtworzy\u0142 proces podejmowania konkretnej decyzji '
    u'inwestycyjnej krok po kroku'
), level=0, font_size=Pt(18), space_before=Pt(12))

add_bullet(tf, (
    u'Tylko w IDI mamy swobod\u0119, \u017ceby na bie\u017c\u0105co reagowa\u0107, dopytywa\u0107 '
    u'o detale i pog\u0142\u0119bia\u0107 w\u0105tki'
), level=0, font_size=Pt(18), space_before=Pt(12))



# ============================================================
# SLIDE 6: Scenariusz wywiadu - Wprowadzenie
# ============================================================
slide6 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide6, WHITE)
add_accent_bar(slide6)
add_title_shape(slide6, u'Scenariusz wywiadu \u2013 A. Wprowadzenie')

tf = add_content_frame(slide6)

add_bullet(tf, (
    u'1. Jakie by\u0142y Pana/Pani g\u0142\u00f3wne motywacje, \u017ceby w og\u00f3le zacz\u0105\u0107 '
    u'lokowa\u0107 swoje oszcz\u0119dno\u015bci poza standardowym kontem w banku?'
), level=0, font_size=Pt(18), space_before=Pt(0))

add_bullet(tf, (
    u'2. Z jakich aplikacji lub platform inwestycyjnych Pan(i) obecnie korzysta '
    u'i dlaczego pad\u0142 wyb\u00f3r akurat na nie?'
), level=0, font_size=Pt(18), space_before=Pt(20))



# ============================================================
# SLIDE 7: Scenariusz wywiadu - Czesc glowna
# ============================================================
slide7 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide7, WHITE)
add_accent_bar(slide7)
add_title_shape(slide7, u'Scenariusz wywiadu \u2013 B. Cz\u0119\u015b\u0107 g\u0142\u00f3wna')

tf = add_content_frame(slide7, top=Inches(1.3), height=Inches(6.0))

add_bullet(tf, (
    u'3. Prosz\u0119 opowiedzie\u0107 mi o swojej pierwszej transakcji lub za\u0142o\u017ceniu portfela '
    u'w aplikacji. Jak to wygl\u0105da\u0142o krok po kroku i jak si\u0119 Pan(i) wtedy czu\u0142(a)?'
), level=0, font_size=Pt(15), space_before=Pt(0))

add_bullet(tf, (
    u'4. W jaki spos\u00f3b aplikacja, z kt\u00f3rej Pan(i) korzysta, pomaga (lub nie) zrozumie\u0107, '
    u'w co dok\u0142adnie inwestowane s\u0105 pieni\u0105dze?'
), level=0, font_size=Pt(15), space_before=Pt(10))

add_bullet(tf, (
    u'5. Zdarzy\u0142o si\u0119 Panu(i) podj\u0105\u0107 decyzj\u0119 o zainwestowaniu w co\u015b pod wp\u0142ywem impulsu, '
    u'bo zobaczy\u0142(a) Pan(i) to na ekranie g\u0142\u00f3wnym aplikacji?'
), level=0, font_size=Pt(15), space_before=Pt(10))

add_bullet(tf, (
    u'6. Gdyby mia\u0142(a) Pan(i) swoimi s\u0142owami wyja\u015bni\u0107, czym jest instrument, w kt\u00f3ry '
    u'Pan(i) inwestuje (np. ETF, akcja) \u2013 jak by to Pan(i) opisa\u0142(a)?'
), level=0, font_size=Pt(15), space_before=Pt(10))

add_bullet(tf, (
    u'7. Aplikacje cz\u0119sto pokazuj\u0105 komunikaty o ryzyku utraty kapita\u0142u. Jak Pan(i) reaguje '
    u'na te komunikaty w momencie podejmowania decyzji o zakupie?'
), level=0, font_size=Pt(15), space_before=Pt(10))

add_bullet(tf, (
    u'8. Co si\u0119 dzieje, gdy wchodzi Pan(i) do aplikacji i widzi, \u017ce ca\u0142y wykres portfela jest '
    u'\u201ena czerwono\u201d? Co Pan(i) wtedy robi i dlaczego?'
), level=0, font_size=Pt(15), space_before=Pt(10))

add_bullet(tf, (
    u'9. Czy uwa\u017ca Pan(i), \u017ce od kiedy u\u017cywa Pan(i) tej aplikacji, Pana/Pani wiedza '
    u'o finansach i ekonomii wzros\u0142a? Sk\u0105d to przekonanie?'
), level=0, font_size=Pt(15), space_before=Pt(10))



# ============================================================
# SLIDE 8: Scenariusz wywiadu - Zakonczenie
# ============================================================
slide8 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide8, WHITE)
add_accent_bar(slide8)
add_title_shape(slide8, u'Scenariusz wywiadu \u2013 C. Zako\u0144czenie')

tf = add_content_frame(slide8)

add_bullet(tf, (
    u'10. Czy uwa\u017ca Pan(i), \u017ce takie aplikacje powinny przed pozwoleniem na zakup '
    u'sprawdza\u0107 wiedz\u0119 u\u017cytkownika (np. kr\u00f3tkim quizem), czy inwestowanie powinno '
    u'by\u0107 dost\u0119pne dla ka\u017cdego bez ogranicze\u0144? Dlaczego?'
), level=0, font_size=Pt(17), space_before=Pt(0))

add_bullet(tf, (
    u'11. Gdyby znajomy bez \u017cadnej wiedzy o finansach zapyta\u0142 Pana(i\u0105), czy warto '
    u'zacz\u0105\u0107 korzysta\u0107 z tej samej aplikacji \u2013 na co uwa\u017ca\u0142by/aby Pan(i) '
    u'za konieczne, by go ostrzec?'
), level=0, font_size=Pt(17), space_before=Pt(16))

add_bullet(tf, (
    u'12. Zbli\u017camy si\u0119 do ko\u0144ca naszej rozmowy. Czy jest jeszcze co\u015b wa\u017cnego '
    u'w kwestii Pana/Pani do\u015bwiadcze\u0144 z tymi aplikacjami, o co nie zapyta\u0142em?'
), level=0, font_size=Pt(17), space_before=Pt(16))



# ============================================================
# SLIDE 9: Ograniczenia badania
# ============================================================
slide9 = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide9, WHITE)
add_accent_bar(slide9)
add_title_shape(slide9, u'Ograniczenia badania')

tf = add_content_frame(slide9)

add_bullet(tf, u'Efekt Dunninga-Krugera', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(0))
add_bullet(tf, u'Badani mog\u0105 znacz\u0105co przecenia\u0107 swoj\u0105 wiedz\u0119 finansow\u0105, szczeg\u00f3lnie w okresach hossy', level=1, font_size=Pt(16))
add_bullet(tf, u'Deklaratywny wzrost wiedzy mo\u017ce by\u0107 w rzeczywisto\u015bci tylko z\u0142udzeniem kontroli', level=1, font_size=Pt(16))

add_bullet(tf, u'Trudno\u015b\u0107 w ewaluacji \u201eobiektywnej\u201d wiedzy', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(14))
add_bullet(tf, u'Wywiad jako\u015bciowy nie jest testem wiedzy', level=1, font_size=Pt(16))
add_bullet(tf, u'Trudno wywa\u017cy\u0107 dopytywanie o definicje, tak aby badany nie poczu\u0142 si\u0119 jak na egzaminie', level=1, font_size=Pt(16))

add_bullet(tf, u'Bariera technologiczna', level=0, bold=True, font_size=Pt(20), color=BLUE_ACCENT, space_before=Pt(14))
add_bullet(tf, u'Aplikacje r\u00f3\u017cni\u0105 si\u0119 interfejsem', level=1, font_size=Pt(16))
add_bullet(tf, u'Odpowiedzi badanych mog\u0105 by\u0107 mocno uzale\u017cnione od konkretnego rozwi\u0105zania (robo-doradca vs aktywny broker)', level=1, font_size=Pt(16))
add_bullet(tf, u'Utrudni to znalezienie wsp\u00f3lnych mianownik\u00f3w na etapie analizy', level=1, font_size=Pt(16))


# ============================================================
# Save the presentation
# ============================================================
output_path = '/projects/sandbox/github/Prezentacja_Fintech.pptx'
prs.save(output_path)
print(f'Presentation saved to: {output_path}')
print(f'Total slides: {len(prs.slides)}')

