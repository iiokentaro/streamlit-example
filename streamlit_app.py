import streamlit as st
from pdf_splitter import get_utc_time_in_string, write_pdf_and_create_button, split_pdf


if __name__ == '__main__':
    tabs = st.tabs(["🇯🇵", "🇬🇧", "🇨🇳", "🇮🇳", "🇪🇸", "🇪🇬", "🇷🇺", "🇭🇷", "🇬🇪"])
    headers = ["🖨 PDF分割 💔", "🖨 PDF Splitter 💔", "🖨 PDF分割器 💔", "🖨 PDF विभाजक 💔", "🖨 Separador de PDF 💔", "💔 فاصل PDF 🖨", "🖨 Разделитель PDF-файлов💔 ", "🖨 PDF Razdjelnik 💔", "🖨 PDF სპლიტერი 💔"]
    texts = [
        "両面印刷オプションが無いプリンターでも簡単に手動裏表印刷ができるよう、PDFを奇数ページと偶数ページに分割します (パスワード付きのPDFには対応していません)。",
        "Split a PDF into odd and even pages so that you can manually print both sides on printers without a duplex option (for example, my Canon PIXMA G3470...).",
        "将 PDF 拆分为奇数页和偶数页，以便您可以在没有双面选项的打印机上手动打印两面（例如，我的 Canon PIXMA G3470...）。",
        "PDF को विषम और सम पृष्ठों में विभाजित करें ताकि आप डुप्लेक्स विकल्प के बिना प्रिंटर पर दोनों ओर मुद्रण कर सकें (उदाहरण के लिए, मेरा Canon PIXMA G3470...).",
        "Divida un PDF en páginas pares e impares para poder imprimir manualmente ambas caras en impresoras sin opción dúplex (por ejemplo, mi Canon PIXMA G3470...).",
        "قم بتقسيم ملف PDF إلى صفحات فردية وزوجية بحيث يمكنك طباعة الوجهين يدويًا على الطابعات دون خيار الطباعة على الوجهين (على سبيل المثال، Canon PIXMA G3470...).",
        "Разделите PDF-файл на нечетные и четные страницы, чтобы вручную распечатать обе стороны на принтерах без функции двусторонней печати (например, на моем Canon PIXMA G3470...).",
        "Podijelite PDF na neparne i parne stranice tako da možete ručno ispisivati obje strane na pisačima bez opcije obostranog ispisa (na primjer, moj Canon PIXMA G3470...).",
        "დაყავით PDF კენტ და ლუწ გვერდებად, რათა ხელით შეძლოთ ორივე მხარის დაბეჭდვა პრინტერებზე დუპლექსის გარეშე (მაგალითად, ჩემი Canon PIXMA G3470...)."
    ]

    for tab, header, text in zip(tabs, headers, texts):
        with tab:
            st.header(header)
            st.write(text)

    """
    :coffee: [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-blue)](https://buymeacoffee.com/iiokentaro)
    """
   
    uploaded_file = st.file_uploader("Choose a file", type=["pdf"], accept_multiple_files=False)

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            split_pdf(uploaded_file)
        else:
            st.error("Please choose a PDF file.")







