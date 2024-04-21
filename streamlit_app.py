import streamlit as st
from io import BytesIO, StringIO
from pypdf import PdfReader, PdfWriter
from datetime import datetime

"""
# 🖨 PDF Splitter 💔

[🇯🇵 PDF分割] 両面印刷オプションが無いプリンターでも簡単に手動裏表印刷ができるよう、PDFを奇数ページと偶数ページに分割します (パスワード付きのPDFには対応していません)。

[🇬🇧 PDF Splitter] Split a PDF into odd and even pages so that you can manually print both sides on printers without a duplex option (for example, my Canon PIXMA G3470...).

[🇨🇳 PDF分割器] 将 PDF 拆分为奇数页和偶数页，以便您可以在没有双面选项的打印机上手动打印两面（例如，我的 Canon PIXMA G3470...）。

[🇪🇸 Separador de PDF] Divida un PDF en páginas pares e impares para poder imprimir manualmente ambas caras en impresoras sin opción dúplex (por ejemplo, mi Canon PIXMA G3470...).

قم بتقسيم ملف PDF إلى صفحات فردية وزوجية بحيث يمكنك طباعة الوجهين يدويًا على الطابعات دون خيار الطباعة على الوجهين (على سبيل المثال، Canon PIXMA G3470...). [فاصل PDF 🇪🇬]

[🇷🇺 Разделитель PDF-файлов] Разделите PDF-файл на нечетные и четные страницы, чтобы вручную распечатать обе стороны на принтерах без функции двусторонней печати (например, на моем Canon PIXMA G3470...).

[🇭🇷 PDF Razdjelnik] Podijelite PDF na neparne i parne stranice tako da možete ručno ispisivati obje strane na pisačima bez opcije obostranog ispisa (na primjer, moj Canon PIXMA G3470...).

[🇬🇪 PDF სპლიტერი] დაყავით PDF კენტ და ლუწ გვერდებად, რათა ხელით შეძლოთ ორივე მხარის დაბეჭდვა პრინტერებზე დუპლექსის გარეშე (მაგალითად, ჩემი Canon PIXMA G3470...).

:coffee: [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-blue)](https://buymeacoffee.com/iiokentaro)

"""

def write_pdf_and_create_button(writer, file_name):
    # Write the PDF to a BytesIO object
    pdf_bytes = BytesIO()
    writer.write(pdf_bytes)
    pdf_bytes.seek(0)  # Reset the pointer to the beginning of the BytesIO object

    # Create a download button for the PDF
    st.download_button(
        label=f"Download {file_name}",
        data=pdf_bytes,
        file_name=file_name,
        mime="application/pdf",
    )


def split_pdf(pdf_object):
    # Get the uploaded file name as a string
    uploaded_file_name = uploaded_file.name if uploaded_file is not None else "generated_pdf"
    # If uploaded_file_name ends with ".pdf" or ".PDF", remove it
    uploaded_file_name = uploaded_file_name.replace(".pdf", "").replace(".PDF", "")
    # TODO: The above line is not perfect because it repolaces all ".pdf" and ".PDF" in the file name.

    reader = PdfReader(pdf_object)

    # ページ数を取得
    number_of_pages = len(reader.pages)

    if number_of_pages == 1:
        st.error("This PDF has only one page.")
        return

    # 書き込み用のオブジェクトを作成
    odd_writer = PdfWriter(); even_writer = PdfWriter()

    progress_text = "Splitting..."
    my_bar = st.progress(0, text=progress_text)

    # Split the PDF into two groups: odd and even pages
    for i, page in enumerate(reader.pages):
        if i % 2 != 0:  # This is because the number start at 0 in Python
            even_writer.add_page(page)
        else:
            odd_writer.add_page(page)
        my_bar.progress((i+1)/number_of_pages, text=progress_text)

    my_bar.empty()
    utc_str = get_utc_time_in_string()
    st.write(f"✅ PDF split completed at {get_utc_time_in_string(use_colon=True)}.")

    # Write PDFs and create download buttons
    write_pdf_and_create_button(odd_writer, f"{uploaded_file_name}_{utc_str} (odd).pdf")
    write_pdf_and_create_button(even_writer, f"{uploaded_file_name}_{utc_str} (even).pdf")


def get_utc_time_in_string(use_colon=False):
    utc_now = datetime.utcnow()
    if use_colon:
        return utc_now.strftime("%Y-%m-%d %H:%M:%S UTC")
    else:
        return utc_now.strftime("%Y-%m-%d-%H-%M-%S UTC")


if __name__ == '__main__':

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "PDF"], accept_multiple_files=False)

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            split_pdf(uploaded_file)
        else:
            st.error("Please choose a PDF file.")







