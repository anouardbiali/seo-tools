from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QThread, pyqtSignal,QUrl
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtGui import QDesktopServices,QPixmap
from ArticleTranslator import start_translation
import os 
import sys


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class TranslatorWorker(QThread):
    progress_update = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, source_path, save_path, source_lang, target_lang):
        super().__init__()
        self.source_path = source_path
        self.save_path = save_path
        self.source_lang = source_lang
        self.target_lang = target_lang

    def run(self):
        def print_override(message):
            self.progress_update.emit(str(message))

        original_print = print
        globals()['print'] = print_override

        try:
            start_translation(self.source_path, self.save_path, self.source_lang, self.target_lang)
        finally:
            globals()['print'] = original_print

        self.finished.emit()

class ClickableImageLabel(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(586, 240)
        Dialog.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
        self.btn_import = QtWidgets.QPushButton(parent=Dialog)
        self.btn_import.setGeometry(QtCore.QRect(430, 20, 131, 31))
        self.btn_import.setObjectName("btn_import")
        self.importfile = QtWidgets.QTextEdit(parent=Dialog)
        self.importfile.setGeometry(QtCore.QRect(230, 20, 181, 31))
        self.importfile.setObjectName("importfile")
        self.generate = QtWidgets.QPushButton(parent=Dialog)
        self.generate.setGeometry(QtCore.QRect(320, 120, 231, 31))
        self.generate.setObjectName("generate")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 81, 31))
        self.label.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.label_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.combolang = QtWidgets.QComboBox(parent=Dialog)
        self.combolang.setGeometry(QtCore.QRect(220, 110, 71, 22))
        self.combolang.setObjectName("combolang")
        self.exportfile = QtWidgets.QTextEdit(parent=Dialog)
        self.exportfile.setGeometry(QtCore.QRect(230, 60, 181, 31))
        self.exportfile.setObjectName("exportfile")
        self.btn_export = QtWidgets.QPushButton(parent=Dialog)
        self.btn_export.setGeometry(QtCore.QRect(430, 60, 131, 31))
        self.btn_export.setObjectName("btn_export")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 201, 20))
        self.label_3.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 61, 31))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.progress = QtWidgets.QLabel(parent=Dialog)
        self.progress.setGeometry(QtCore.QRect(90, 190, 321, 31))
        self.progress.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.progress.setObjectName("progress")
        self.combolang_2 = QtWidgets.QComboBox(parent=Dialog)
        self.combolang_2.setGeometry(QtCore.QRect(220, 140, 71, 22))
        self.combolang_2.setObjectName("combolang_2")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 191, 20))
        self.label_5.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 101, 81))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("src/softgrid.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = ClickableImageLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(510, 180, 51, 41))
        self.label_7.setObjectName("label_7")
        self.label_7.setCursor(QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_8 = ClickableImageLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 180, 51, 51))
        self.label_8.setObjectName("label_8")
        self.label_8.setCursor(QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
       

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_import.clicked.connect(self.import_folder)
        self.btn_export.clicked.connect(self.export_folder)
        self.generate.clicked.connect(self.translate_articles)
        self.label_7.clicked.connect(self.openLink7)
        self.label_8.clicked.connect(self.openLink8)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        languages = [
    "en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ko",
    "ar", "hi", "bn", "ur", "tr", "nl", "pl", "sv", "fi", "da",
    "no", "el", "he", "th", "vi", "id", "ms", "fa", "uk", "cs",
    "ro", "hu", "sk", "bg", "hr", "sr", "sl", "et", "lv", "lt",
    "sw", "af", "am", "hy", "az", "eu", "be", "ka", "is", "km",
    "lo", "mk", "mn", "ne", "si", "tl", "ta", "te", "uz"
]
        Dialog.setWindowTitle(_translate("Dialog", "Bulk Article Translator"))
        self.btn_import.setText(_translate("Dialog", "Import"))
        self.generate.setText(_translate("Dialog", "Translate Bulk Articles "))
        self.label.setText(_translate("Dialog", "Select Folder : "))
        self.label_2.setText(_translate("Dialog", "Select Folder : "))
        self.btn_export.setText(_translate("Dialog", "Export "))
        self.label_3.setText(_translate("Dialog", "Source language code (e.g. \'EN\'):"))
        self.label_4.setText(_translate("Dialog", "Statue :"))
        self.progress.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "Target language code (e.g. \'FR\'\'):"))
        self.label_7.setPixmap(QPixmap("./src/website.png").scaled(51, 41, Qt.AspectRatioMode.KeepAspectRatio))
        self.label_8.setPixmap(QPixmap("./src/youtube.jpg").scaled(51, 51, Qt.AspectRatioMode.KeepAspectRatio))

        for lang in languages:
            self.combolang.addItem(_translate("Dialog", lang))
            self.combolang_2.addItem(_translate("Dialog", lang))

    def openLink7(self):
        QDesktopServices.openUrl(QUrl("https://softgrid.me"))

    def openLink8(self):
        QDesktopServices.openUrl(QUrl("https://www.youtube.com/@ultrabyteagency5921"))

    def import_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Input Folder")
        self.importfile.setText(folder_path)

    def export_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        self.exportfile.setText(folder_path)

    def translate_articles(self):
        input_folder = self.importfile.toPlainText()
        output_folder = self.exportfile.toPlainText()
        source_language = self.combolang.currentText()
        target_language = self.combolang_2.currentText()

        if not input_folder or not output_folder:
            QMessageBox.warning(None, "Missing Information", "Please select both input and output folders.")
            return
        
        self.start_translation(input_folder, output_folder, source_language, target_language)

        QMessageBox.information(None, "Translation Started", "You can't click anything until the translation is completed.")

    def start_translation(self, input_folder, output_folder, source_language, target_language):
        self.worker = TranslatorWorker(input_folder, output_folder, source_language, target_language)
        self.worker.progress_update.connect(self.update_progress)
        self.worker.finished.connect(self.translation_finished)
    
        self.disable_inputs()
        
        self.progress.setText("Translation in progress...(check the output folder)")
        
        self.worker.start()

    def update_progress(self, message):
        if "is translated successfully" in message:
            self.progress.setText(message)
            QtCore.QCoreApplication.processEvents()  

    def translation_finished(self):
        # Re-enable all inputs
        self.enable_inputs()
        
        self.progress.setText("Translation completed!")
        QMessageBox.information(None, "Translation Complete", "All files have been translated successfully!")

    def disable_inputs(self):
        self.btn_import.setEnabled(False)
        self.btn_export.setEnabled(False)
        self.generate.setEnabled(False)
        self.importfile.setReadOnly(True)
        self.exportfile.setReadOnly(True)
        self.combolang.setEnabled(False)
        self.combolang_2.setEnabled(False)
        #self.Dialog.setEnabled(False)

    def enable_inputs(self):
        self.btn_import.setEnabled(True)
        self.btn_export.setEnabled(True)
        self.generate.setEnabled(True)
        self.importfile.setReadOnly(False)
        self.exportfile.setReadOnly(False)
        self.combolang.setEnabled(True)
        self.combolang_2.setEnabled(True)
        #self.Dialog.setEnabled(True)

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
