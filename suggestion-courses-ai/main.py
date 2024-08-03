from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import sys


template = """
Please follow the next rules:


Given that we offer these courses (IMPORTANT: do not include courses that are not on the list):

- Infrastructure Design: AWS SQS as a messaging queue
- Design Patterns: Criteria
- Infrastructure Design: RabbitMQ as a messaging queue
- Next.js: Open Graph Images
- DDD Issues: Error Handling in Domain Events
- Javascript for beginners
- Linting in JS
- Domain Modeling: Domain Events
- Static Code Analysis in JS
- Best Practices with CSS: Colors
- Advanced TypeScript: Improve your Developer Experience
- Grafana
- React
- Create your library in React: Carousel
- Best practices for writing clean, maintainable JavaScript
- 10 JavaScript Bad Practices You Should Avoid


And you have to follow these rules:

- Act as an advanced course recommender.
- Return a list with the 2 recommended courses.
- You cannot add courses that the user has already completed.
- You have to respond just JSON
- You have to respond using the next JSON Schema {valid_schema}


Give me the suggested courses for someone who has completed the following courses. Suggest 2 courses for someone who has completed the following:

{completed_list}

"""

validSchema = """
{"suggestedCourses": ["10 JavaScript Bad Practices You Should Avoid"]}
"""
completedCourses = sys.argv[1:]
completedCoursesString = "\n".join("- " + str(p)  for p in completedCourses)

# http://localhost:11434/api
model = OllamaLLM(model="llama3.1")

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({"completed_list": completedCoursesString, "valid_schema": validSchema})

print(result)

## python main.py "React" "Static Code Analysis in JS" "Javascript for Beginners"

## python main.py "DDD Issues: Error Handling in Domain Events"