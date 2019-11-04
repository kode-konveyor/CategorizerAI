from winterboot.Service import Service

PROMPT = "choice: "

@Service
class ChoiceAskService:
    
    def call(self) -> str:
        answer = input(PROMPT)
        return answer
