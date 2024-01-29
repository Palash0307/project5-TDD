class NerModelTestDouble:
    def __init__(self, model):
        self.model = model
        self.ents = []

    def returns_doc_ents(self, ents):
        self.ents = ents

    # to call in doc type
    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)


class DocTestDouble:
    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]  ##to be stored in NER model

    def patch_method(self, attr, return_value):
        def patched():
            return return_value

        setattr(self, attr, patched)
        return self


class SpanTestDouble:
    def __init__(self, text, label):
        self.text = text #retreived from doctest double
        self.label_ = label 
