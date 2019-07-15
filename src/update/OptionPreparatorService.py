from springboot.Service import Service

@Service
class OptionPreparatorService:

    def prepareOptionsToOffer(self, rowNumber, data, categories):
        answers = self.getResultsForRow(rowNumber, data)
        options = self.prepareProbableAnswers(categories, answers)
        return options
    
    def getResultsForRow(self,i, data):
        results = []
        for j in range(data.output_neurons):
            results.append((data.problemValues[i][j], j))        
        results = sorted(results, key=lambda rec:rec[0], reverse=True)
        return results

    def prepareProbableAnswers(self, categories, answers):
        index = 1
        options = {}
        for c in answers:
            if c[1] in categories and c[0] > config.MIN_PROBABILITY:
                print("\t", index, ":", c[0], c[1], categories[c[1]])
                options[index] = c[1], categories[c[1]]
                index += 1
        return options

