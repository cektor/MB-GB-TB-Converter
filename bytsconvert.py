import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QPushButton, QGroupBox, QProgressBar, QMessageBox, QComboBox
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QTimer, QTimeLine
from PyQt6.QtGui import QColor, QPainter, QBrush, QPixmap, QFont, QClipboard
import pyttsx3
import matplotlib.pyplot as plt

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MB-GB-TB Çevirici")
        self.setFixedSize(500, 700)
        self.setStyleSheet("background-color: #2e3b4e; border-radius: 10px;")

        # Başlık Etiketi
        self.title_label = QLabel("MB-GB-TB Çevirici")
        self.title_label.setStyleSheet("font: bold 24px; color: #8eba00; padding: 10px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Değer Girişi
        self.entry_label = QLabel("Bir Değer Girin:")
        self.entry_label.setStyleSheet("font: 14px; color: white;")
        
        self.entry = QLineEdit()
        self.entry.setStyleSheet("font: 14px; padding: 5px; border-radius: 5px; border: 2px solid #8eba00;")

        # Dönüşüm tipi için Radyo Butonları
        self.conversion_type = "MB"  # Varsayılan değer
        self.mb_radio = QRadioButton("MB")
        self.mb_radio.setStyleSheet("font: 14px; color: white;")
        self.mb_radio.setChecked(True)  # Varsayılan MB seçili
        self.mb_radio.toggled.connect(self.set_conversion_type)
        
        self.gb_radio = QRadioButton("GB")
        self.gb_radio.setStyleSheet("font: 14px; color: white;")
        self.gb_radio.toggled.connect(self.set_conversion_type)

        self.tb_radio = QRadioButton("TB")
        self.tb_radio.setStyleSheet("font: 14px; color: white;")
        self.tb_radio.toggled.connect(self.set_conversion_type)

        # Radyo butonları grubunu düzenleyin
        self.radio_group = QGroupBox()
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.mb_radio)
        radio_layout.addWidget(self.gb_radio)
        radio_layout.addWidget(self.tb_radio)
        self.radio_group.setLayout(radio_layout)
        self.radio_group.setStyleSheet("background-color: #2e3b4e;")

        # Dönüştür Butonu
        self.convert_button = QPushButton("Dönüştür")
        self.convert_button.setStyleSheet("font: 14px; background-color: #8eba00; color: white; padding: 10px; border-radius: 5px;")
        self.convert_button.clicked.connect(self.convert)

        # Sonuç etiketi - Geliştirilmiş tasarım
        self.result_label = QLabel("Sonuç: ")
        self.result_label.setStyleSheet("""
            font: bold 16px;
            color: white;
            padding: 20px;
            background-color: #8eba00;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        """)

        # Dönüşüm Geçmişi
        self.history_label = QLabel("Dönüşüm Geçmişi:")
        self.history_label.setStyleSheet("font: 14px; color: white; margin-top: 20px;")
        self.history_list = QLabel("Geçmişteki dönüşümler burada görünecek.")
        self.history_list.setStyleSheet("font: 12px; color: white; margin-top: 10px;")

        # İlerleme Çubuğu
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(50, 370, 300, 20)
        self.progress_bar.setStyleSheet("QProgressBar {border: 2px solid #8eba00; border-radius: 5px; text-align: center;}")        
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)

        # Dil Seçimi
        self.language_combo = QComboBox(self)
        self.language_combo.addItem("Türkçe")
        self.language_combo.addItem("English")
        self.language_combo.currentTextChanged.connect(self.change_language)

        # Sesli Dönüşüm
        self.engine = pyttsx3.init()
        self.check_available_voices()

        # Sesli dönüşüm için radyo butonları
        self.voice_checkbox = QRadioButton("Seslendir")
        self.voice_checkbox.setStyleSheet("font: 14px; color: white;")
        self.voice_checkbox.setChecked(True)  # Varsayılan olarak sesli dönüşüm açık
        self.voice_checkbox.toggled.connect(self.toggle_voice)

        # Seslendir Butonu
        self.speak_button = QPushButton("Seslendir")
        self.speak_button.setStyleSheet("font: 14px; background-color: #8eba00; color: white; padding: 10px; border-radius: 5px;")
        self.speak_button.clicked.connect(self.speak_result)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.entry_label)
        layout.addWidget(self.entry)
        layout.addWidget(self.radio_group)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.result_label)
        layout.addWidget(self.history_label)
        layout.addWidget(self.history_list)
        layout.addWidget(self.language_combo)
        layout.addWidget(self.voice_checkbox)  # Sesli dönüşüm radyo butonu
        layout.addWidget(self.speak_button)  # Seslendir butonu

        self.setLayout(layout)

    def check_available_voices(self):
        """Sistemimizdeki sesleri listele."""
        voices = self.engine.getProperty('voices')
        print("Mevcut Sesler:")
        for voice in voices:
            print(f"Ses adı: {voice.name}, Ses ID: {voice.id}")

    def set_voice(self, language):
        """Dil ayarlarını yap."""
        voices = self.engine.getProperty('voices')
        
        # Türkçe ses
        if language == "tr":
            for voice in voices:
                if 'turkish' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
            else:
                print("Türkçe ses bulunamadı, varsayılan ses kullanılıyor.")
        
        # İngilizce ses
        elif language == "en":
            for voice in voices:
                if 'english' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
            else:
                print("İngilizce ses bulunamadı, varsayılan ses kullanılıyor.")

    def toggle_voice(self):
        """Sesli dönüşümün açık mı kapalı mı olduğunu kontrol et."""
        if self.voice_checkbox.isChecked():
            self.engine.runAndWait()  # Sesli dönüşümü başlat
        else:
            self.engine.stop()  # Sesli dönüşümü durdur

    def set_conversion_type(self):
        """Hangi radyo butonunun seçildiğini kontrol et."""
        if self.mb_radio.isChecked():
            self.conversion_type = "MB"
        elif self.gb_radio.isChecked():
            self.conversion_type = "GB"
        elif self.tb_radio.isChecked():
            self.conversion_type = "TB"

    def convert(self):
        """Dönüşüm işlemi ve animasyonlu ilerleme çubuğu."""
        try:
            value = float(self.entry.text())
            if value < 0:
                raise ValueError("Pozitif bir değer giriniz!")
            self.progress_bar.setValue(20)
            QTimer.singleShot(500, lambda: self.calculate_conversion(value))
        except ValueError as e:
            self.show_error_message(f"Hata: {str(e)}")
            self.result_label.setText("Lütfen geçerli bir sayı giriniz!")
            self.progress_bar.setValue(0)

    def calculate_conversion(self, value):
        """Dönüşümü hesapla ve ilerleme çubuğunun ilerlemesini sağla."""
        try:
            if self.conversion_type == "MB":
                gb_result = value / 1024
                tb_result = value / (1024 * 1024)
                result = f"Sonuç:\n{value} MB = {gb_result:.1f} GB\n{value} MB = {tb_result:.0f} TB"
            elif self.conversion_type == "GB":
                mb_result = value * 1024
                tb_result = value / 1024
                result = f"Sonuç:\n{value} GB = {mb_result:.0f} MB\n{value} GB = {tb_result:.0f} TB"
            elif self.conversion_type == "TB":
                mb_result = value * (1024 * 1024)
                gb_result = value * 1024
                result = f"Sonuç:\n{value} TB = {mb_result:.0f} MB\n{value} TB = {gb_result:.0f} GB"

            self.progress_bar.setValue(100)
            self.result_label.setText(result)

            # Sonucu seslendir
            if self.voice_checkbox.isChecked():
                self.speak_result()

            # Geçmişi güncelle
            self.history_list.setText(f"{self.history_list.text()}\n{result}")
        except Exception as e:
            self.show_error_message(f"Hata: {str(e)}")
            self.progress_bar.setValue(0)

    def show_error_message(self, message):
        """Hata mesajı göster."""
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Hata")
        msg_box.exec()

    def speak_result(self):
        """Sonucu sesli olarak okur."""
        result_text = self.result_label.text().replace("Sonuç: ", "")  # "Sonuç:" kısmını kaldır
        self.engine.say(result_text)
        self.engine.runAndWait()

    def change_language(self):
        """Dil değiştiğinde yapılacak işlemler."""
        language = "tr" if self.language_combo.currentText() == "Türkçe" else "en"
        self.set_voice(language)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())
