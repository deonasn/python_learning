# just for practicing while reading
# mostly in-text examples
# chapter 11: survey example

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        new_response = new_response.title()
        if new_response in self.responses:
            print("\t->This response has already been recorded.")
        else:
            self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("\t\tSurvey results:")
        for response in self.responses:
            print(f"\t\t\t- {response}")
        print("\n")


question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)
language_survey.show_question()
while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    language_survey.store_response(response)
language_survey.show_results()