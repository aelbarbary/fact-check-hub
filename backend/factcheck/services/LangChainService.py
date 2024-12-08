import csv
from typing import List, Dict
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class FactCheckService:
    def __init__(self, csv_path: str, openai_api_key: str):
        self.csv_data = self.load_csv(csv_path)
        self.llm = OpenAI( model= "gpt-3.5-turbo-instruct",temperature=0, openai_api_key=openai_api_key)
        self.prompt = PromptTemplate(
            input_variables=["statement", "csv_content"],
            template="""
            Validate the given political statement based on the CSV content:
            Statement: {statement}
            CSV Content: {csv_content}
            
            Is the given statement correct and supported by the CSV data? 
            If yes, explain why. If no, provide the correct answer based on the CSV data.
            
            Validation:
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def load_csv(self, file_path: str) -> List[Dict]:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def validate_answer(self, statement: str) -> str:
        csv_content = "\n".join([str(row) for row in self.csv_data])
        response = self.chain.run(statement=statement, csv_content=csv_content)
        return response

# Usage example
if __name__ == "__main__":
    csv_path = "/Users/abdel/Documents/projects/fact-check-hub/backend/sample-political-facts.txt"
    openai_api_key = ""
    
    service = FactCheckService(csv_path, openai_api_key)
    
    # Example usage
    statement = "USA has 60 states"

    
    validation_result2 = service.validate_answer(statement)
    print(validation_result2)