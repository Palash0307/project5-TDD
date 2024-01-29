import unittest
from ner_client import NamedEntityClient
from test_double import NerModelTestDouble
class TestNerClient(unittest.TestCase):
    def test_get_ents_returns_dictionary_given_empty_string_causes_return_empty(self):  
        model = NerModelTestDouble(model='eng')  
        model.returns_doc_ents([]) 
        ner = NamedEntityClient(model)
        ents = ner.get_ents(" ")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_strings(self):
        model = NerModelTestDouble(model='eng')  
        model.returns_doc_ents([]) 
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    def test_get_ents_spacy_Person_returned_serializes_to_person(self):
        model = NerModelTestDouble('eng') 
        doc_ents = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}] 
        model.returns_doc_ents(doc_ents) #using our test model
        ner = NamedEntityClient(model)  # behaving like spacy
        result = ner.get_ents('...') 
        expected_result = {'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': ""} #expected result
        self.assertListEqual(result['ents'], expected_result['ents']) #testing our double environment whether giving us the expected result

    def test_get_ents_spacy_NORP_returned_serializes_to_group(self):
        model = NerModelTestDouble('eng') 
        doc_ents = [{'text': 'Lithuanian', 'label_': 'NORP'}] 
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)  # behaving like spacy
        result = ner.get_ents('...') #will change NORP to Group
        expected_result = {'ents': [{'ent': 'Lithuanian', 'label': 'Group'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])  

    def test_get_ents_spacy_LOC_returned_serializes_to_location(self):
        model = NerModelTestDouble('eng') 
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}] 
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)  # behaving like spacy
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_spacy_LANGUAGE_returned_serializes_to_language(self):
        model = NerModelTestDouble('eng') 
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}] 
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)  # behaving like spacy
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_spacy_GPE_returned_serializes_to_GPE(self):
        model = NerModelTestDouble('eng') 
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}] 
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)  # behaving like spacy
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Australia', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents(self):
        model = NerModelTestDouble('eng') 
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}, {'text': 'Paris', 'label_': 'GPE'}] 
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)  # behaving like spacy
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Australia', 'label': 'Location'}, {'ent': 'Paris', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])


    










