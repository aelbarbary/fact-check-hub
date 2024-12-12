import csv
from typing import List, Dict
from io import StringIO
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class FactCheckService:
    def __init__(self, csv_content: str, openai_api_key: str):
        self.csv_data = self.load_csv_from_content(csv_content)
        self.llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, openai_api_key=openai_api_key)
        self.prompt = PromptTemplate(
            input_variables=["statement", "csv_content"],
            template="""
            Validate the following political statement based on the CSV data provided below:
            
            Statement: {statement}
            CSV Content: {csv_content}
            
            Rules:
            - Do **not** make assumptions or add information that is not explicitly stated in the CSV content.
            - Only refer to the data in the CSV content to validate the statement.
            - If the statement is correct, explain why it aligns with the CSV data.
            - If the statement is incorrect, provide the correct information **based only on the CSV data**.
            
            Please ensure the response does not contain any information that is not in the CSV content.
            
            Validation:
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def load_csv_from_content(self, csv_content: str) -> List[Dict]:
        csv_file = StringIO(csv_content)
        reader = csv.DictReader(csv_file)
        return [row for row in reader]

    def validate_answer(self, statement: str) -> str:
        csv_content = "\n".join([str(row) for row in self.csv_data])
        response = self.chain.run(statement=statement, csv_content=csv_content)
        return response

# Usage example
if __name__ == "__main__":
    csv_content = """State,Count\nUSA,50\nCanada,10\n"""
    openai_api_key = ""

    service = FactCheckService(csv_content, openai_api_key)

    # Example usage
    statement = "USA has 60 states"

    validation_result = service.validate_answer(statement)
    print(validation_result)