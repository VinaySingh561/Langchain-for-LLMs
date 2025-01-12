
import getpass
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass()


if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain



def resturant_recommender(cuisine):
    model1= ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
    prompt_template_name_food = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine}. Suggest me single name ,only name"
    )

    name_chain = LLMChain(llm=model1,prompt=prompt_template_name_food, 
                                output_key= "restaurant_name")

    model2= ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
    prompt_template_name = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggestions for menu items for {restaurant_name}."
    )
    food_items_chain = LLMChain(llm=model2,prompt=prompt_template_name,
                                output_key= "food_items")
    chain = SequentialChain(chains = [name_chain, food_items_chain],
                        input_variables=["cuisine"],
                        output_variables=["restaurant_name","food_items"])

    response = chain({"cuisine":cuisine})
    return response



if __name__ == "__main__":
    print(resturant_recommender("Italian"))