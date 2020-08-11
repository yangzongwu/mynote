from urllib.request import urlopen
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import open
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup
import csv

class txt():
    def read(self):
        textPage = urlopen(
        "http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
        print(textPage.read())
    def read2(self):
        # 其他语言可能乱码，需要转化为utf-8
        textPage = urlopen(
        "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
        print(str(textPage.read(), 'utf-8'))


class cvs():
    """
    Python 的csv 库主要是面向本地文件。而进行网络数据采集的时候，很多文件都是在线的。
    不过有一些方法可以解决这个问题：
    • 手动把CSV 文件下载到本机，然后用Python 定位文件位置；
    • 写Python 程序下载文件，读取之后再把源文件删除；
    • 从网上直接把文件读成一个字符串，然后转换成一个StringIO 对象，使它具有文件的属性。
    """
    def read(self):
        data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv") \
        .read().decode('ascii', 'ignore')
        dataFile = StringIO(data)
        csvReader = csv.reader(dataFile)
        for row in csvReader:
            print(row)
            print("The album \"" + row[0] + "\" was released in " + str(row[1]))
        # ["Monty Python's Flying Circus", '1970']
        # The album "Monty Python's Flying Circus" was released in 1970

    def read2(self):
        data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv") \
            .read().decode('ascii', 'ignore')
        dataFile = StringIO(data)
        dictReader = csv.DictReader(dataFile)
        print(dictReader.fieldnames)  # 打印标题
        for row in dictReader:
            print(row)  # 只打印内容

class pdf():
    def read(self):
        def readPDF(pdfFile):
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            process_pdf(rsrcmgr, device, pdfFile)
            device.close()

            content = retstr.getvalue()
            retstr.close()
            return content

        pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
        outputString = readPDF(pdfFile)
        print(outputString)
        pdfFile.close()

class docx():
    def read(self):
        wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
        wordFile = BytesIO(wordFile)
        document = ZipFile(wordFile)
        xml_content = document.read('word/document.xml')

        wordObj = BeautifulSoup(xml_content.decode('utf-8'))
        textStrings = wordObj.findAll("w:t")
        for textElem in textStrings:
            print(textElem.text)