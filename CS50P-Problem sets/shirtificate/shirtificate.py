from fpdf import FPDF

class PDF:
    def __init__(self, name):
        # Initialize FPDF object and add a page
        # The format of the PDF should be A4
        # P-Portrait : The orientation of the PDF should be Portrait.
        self._pdf = FPDF("P", "mm", "A4")
        self._pdf.add_page()

        # 셔츠 증명서 제목 The title 'CS50 Shirtificate' should be centered at the top of the file
        self._pdf.set_font("helvetica", "B", 50) #B = Bold, font size = 50

        # 제목 출력: 페이지 너비(0), 높은 셀(60), 중앙 정렬
        # new_y="NEXT"는 자동으로 다음 줄로 이동시켜 줍니다.
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

        # shirt image : x="C"로 설정하여 이미지를 페이지 중앙에 위치시키고, y 좌표 지정 (예: 70mm)
        self._pdf.image("shirtificate.png", x="C", y=70, w=self._pdf.epw)

        # user name printed on the shirt
        # white text
        self._pdf.set_text_color(255, 255, 255)

        # 글꼴 설정: 셔츠에 들어갈 텍스트 (예: 30)
        self._pdf.set_font("helvetica", style="", size=30)

        # 출력할 텍스트 정의
        txt = f"{name} took CS50"
        # 1단계: 텍스트의 너비 측정
        text_width = self._pdf.get_string_width(txt)
        # 2단계: 중앙 정렬 X 좌표 계산 (A4 너비 210mm 가정)
        # Y 좌표 140은 셔츠 이미지 중앙에 맞추기 위한 최적의 값이라고 가정
        start_x = (210 - text_width) / 2
        self._pdf.text(x=start_x, y=140, txt=txt)

        # PDF 저장 :Your program should create a file, shirtificate.pdf
        self._pdf.output("shirtificate.pdf")

name = input("NAME: ")
pdf = PDF(name)
