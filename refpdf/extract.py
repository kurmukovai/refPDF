import pdftotext
import re

class GetReferenceList():

    def __init__(self,):
        '''
        Extract Reference list from PDF document (scientific paper).
        -------

        text - str,
         whole PDF document

        reference_text - str,
         References
        '''
        self.text = None
        self.reference_text = None

    def get_reference_list(self, path=None, header=None,
                                 enumeration_format=None):
        '''
        path - str,
         path to PDF document

        header - str,
         header of the Reference list in the document
         (e.g. "References", "List of References" etc)

        enumeration_format - str,
         enumeration format used in PDF References list
         (e.g. "\n[0-9]+\.", "\n\[[0-9]\]")
        '''
        if header is None:
            header = 'References'
        if enumeration_format is None:
            enumeration_format = '\n[0-9]+\.'

        self.text = self._load_pdf(path)
        start_index = self._find_start_index(header)
        self.reference_text = self.text[start_index:]
        reference_list = self._split_reference_text(enumeration_format)

        return reference_list[1:]

    def _load_pdf(cls, path):
        '''
        Loads pdf from file to python string, using pdftotext package.
        --------
        '''
        with open(path, 'rb') as f:
            text = ' '.join(pdftotext.PDF(f))
        return text

    def _find_start_index(cls, header=None):
        '''
        Finds first occurence of the header (Reference header) in the text.
        --------
        '''
        start_index = cls.text.find(header)
        return start_index

    def _split_reference_text(cls, enumeration_format=None):
        '''
        Splits text into single citations using enumeration format.
        --------

        enumeration_format - str,
         string pattern used by regex.split()
        '''
        ref_text = '\n'.join([line.strip() for line in cls.reference_text.split('\n')])
        return re.split(enumeration_format, ref_text)
