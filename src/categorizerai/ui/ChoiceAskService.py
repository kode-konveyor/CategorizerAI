from winterboot.Service import Service

PROMPT = "choice: "

@Service
class ChoiceAskService:
    
    def call(self):
        answer = input(PROMPT)
        return answer
