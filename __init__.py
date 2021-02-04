from mycroft import MycroftSkill, intent_file_handler


class Quiz(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('quiz.intent')
    def handle_quiz(self, message):
        self.speak_dialog('quiz')


def create_skill():
    return Quiz()

