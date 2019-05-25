import pdftotext
import re

class GetReferenceList():
    
    def __init__(self,):
        self.text = None
        self.reference_text = None
        
    def get_reference_list(self,
                           path=None,
                           header=None,
                           enumeration_format=None):

        self.text = self._load_pdf(path)
        start_index = self._find_start_index(header)
        self.reference_text = self.text[start_index:]
        reference_list = self._split_reference_text()
        
        return reference_list[1:]
    
    def _load_pdf(cls, path):
        with open(path, 'rb') as f:
            text = ' '.join(pdftotext.PDF(f))
        return text
    
    def _find_start_index(cls, header=None):
        start_index = cls.text.find(header)
        return start_index
    
    def _split_reference_text(cls, enumeration_format=None):
        enumeration_format = '\n[0-9]+\.'
        ref_text = '\n'.join([line.strip() for line in cls.reference_text.split('\n')])
        return re.split(enumeration_format, ref_text)
