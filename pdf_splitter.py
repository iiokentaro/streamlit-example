import streamlit as st
from io import BytesIO, StringIO
from pypdf import PdfReader, PdfWriter
from datetime import datetime


# ページの設定 (これはimportの直後に書く必要あり)
st.set_page_config(
    page_title='PDF Splitter',
    page_icon="favicon/favicon.ico"
)


def get_utc_time_in_string(use_colon=False):
    utc_now = datetime.utcnow()
    if use_colon:
        return utc_now.strftime("%Y-%m-%d %H:%M:%S UTC")
    else:
        return utc_now.strftime("%Y-%m-%d-%H-%M-%S UTC")
    

def write_pdf_and_create_button(writer, file_name: str):
    """Generate a download button for the PDF file."""

    # PDFをBytesIOオブジェクトに書き込む
    pdf_bytes = BytesIO()
    writer.write(pdf_bytes)
    pdf_bytes.seek(0)  # Reset the pointer to the beginning of the BytesIO object

    # ダウンロードボタンを表示
    st.download_button(
        label=f"Download {file_name}",
        data=pdf_bytes,
        file_name=file_name,
        mime="application/pdf",
    )


def split_pdf(pdf_object_):
    """Split the PDF into odd and even pages."""

    # ファイル名を取得
    uploaded_file_name = pdf_object_.name if pdf_object_ is not None else "generated_pdf"

    # ファイル名が".pdf"で終わっている場合にファイル名の文字列から".pdf"を削除
    uploaded_file_name = uploaded_file_name.replace(".pdf", "").replace(".PDF", "")
    # TODO: The above line is not perfect because it repolaces all ".pdf" and ".PDF" in the file name.

    reader = PdfReader(pdf_object_)

    number_of_pages = len(reader.pages)

    if number_of_pages == 1:
        st.error("This PDF has only one page.")
        return

    # 書き込み用のオブジェクトを作成
    odd_writer = PdfWriter(); even_writer = PdfWriter()

    progress_text = "Splitting..."
    my_bar = st.progress(0, text=progress_text)

    # 分割処理
    for i, page in enumerate(reader.pages):
        if i % 2 != 0:  # This is because the number start at 0 in Python
            even_writer.add_page(page)
        else:
            odd_writer.add_page(page)
        my_bar.progress((i+1)/number_of_pages, text=progress_text)

    my_bar.empty()
    utc_str = get_utc_time_in_string()
    st.write(f"✅ PDF split completed at {get_utc_time_in_string(use_colon=True)}.")

    # ダウンロードボタンを生成
    write_pdf_and_create_button(odd_writer, f"{uploaded_file_name}_{utc_str} (odd).pdf")
    write_pdf_and_create_button(even_writer, f"{uploaded_file_name}_{utc_str} (even).pdf")