import csv
from typing import List, Dict
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class CSVValidationService:
    def __init__(self, csv_path: str, openai_api_key: str):
        self.csv_data = self.load_csv(csv_path)
        self.llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
        self.prompt = PromptTemplate(
            input_variables=["question", "answer", "csv_content"],
            template="""
            Validate the given answer for the question based on the CSV content:
            Question: {question}
            Given Answer: {answer}
            CSV Content: {csv_content}
            
            Is the given answer correct and supported by the CSV data? 
            If yes, explain why. If no, provide the correct answer based on the CSV data.
            
            Validation:
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def load_csv(self, file_path: str) -> List[Dict]:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def validate_answer(self, question: str, answer: str) -> str:
        csv_content = "\n".join([str(row) for row in self.csv_data])
        response = self.chain.run(question=question, answer=answer, csv_content=csv_content)
        return response

# Usage example
if __name__ == "__main__":
    csv_path = "/Users/abdel/Documents/projects/fact-check-hub/backend/sample-political-facts.txt"
    openai_api_key = ""
    
    service = CSVValidationService(csv_path, openai_api_key)
    
    # Example usage
    question2 = "Al Assad as killed in 2016"
    answer2 = "True"
    
    validation_result2 = service.validate_answer(question2, answer2)
    print(validation_result2)