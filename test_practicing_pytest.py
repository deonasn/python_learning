# just for practicing 'pytest' while reading
# imports functions from practicing.py
# mostly in-text examples

from practicing import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored correctly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    
    language_survey.store_response('Arabic')
    language_survey.store_response('Japanese')
    language_survey.store_response('English')
    language_survey.store_response('Korean')
    language_survey.store_response('Chinese')
    
    # assert 'English' in language_survey.responses
    assert language_survey.show_results() == ("\t\tSurvey results:\n"
                                              "\t\t\t- Arabic\n"
                                              "\t\t\t- Japanese\n"
                                              "\t\t\t- English\n"
                                              "\t\t\t- Korean\n"
                                              "\t\t\t- Chinese\n\n")