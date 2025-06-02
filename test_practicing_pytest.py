# just for practicing 'pytest' while reading
# imports functions from practicing.py
# mostly in-text examples

from practicing import AnonymousSurvey

def test_store_print_multiple_response():
    """Test that a single response is stored correctly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['Arabic', 'Japanese', 'English', 'Korean', 'Chinese']
    for response in responses:
        language_survey.store_response(response)
    
    expected_result = ''
    for response in responses:
        expected_result += f"\t\t\t- {response}\n"
    expected_result += "\n"
    
    assert language_survey.show_results() == expected_result