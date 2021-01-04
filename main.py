from models import autopict
from models import converter
from models import merger


if __name__ == '__main__':
    """Take screenshot"""
    screenCapture = autopict.ScreenCapture()
    screenCapture.size_check()
    screenCapture.display_set()
    screenCapture.screen_shot()

    """Convert PGN to PDF"""
    converter = converter.Converter('target', '.png')
    converter.png_to_pdf()

    """Combine PDFs into one"""
    merger = merger.Merger()
    merger.join()