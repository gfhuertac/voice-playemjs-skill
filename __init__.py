from mycroft import MycroftSkill, intent_file_handler


class VoicePlayemjs(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('playemjs.voice.intent')
    def handle_playemjs_voice(self, message):
        self.speak_dialog('playemjs.voice')


def create_skill():
    return VoicePlayemjs()

