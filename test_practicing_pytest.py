# just for practicing 'pytest' while reading
# imports functions from practicing.py
# mostly in-text examples

import pytest
from practicing import AnonymousSurvey

@pytest.fixture
def language_survey():
    """Fixture to create an instance of AnonymousSurvey."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored correctly."""
    response = 'English'
    language_survey.store_response(response)
    
    expected_result = "\t\t\t- English\n\n"
    assert language_survey.show_results() == expected_result

def test_store_print_multiple_response(language_survey):
    """Test that a single response is stored correctly."""
    responses = ['Arabic', 'Japanese', 'English', 'Korean', 'Chinese']
    for response in responses:
        language_survey.store_response(response)
    
    expected_result = ''
    for response in responses:
        expected_result += f"\t\t\t- {response}\n"
    expected_result += "\n"
    
    assert language_survey.show_results() == expected_result