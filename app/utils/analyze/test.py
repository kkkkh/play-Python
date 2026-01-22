from chain import language_analysis_chain

text = """
I was really able to figure out what he meant after thinking about it for a while.
"""

result = language_analysis_chain.invoke({"text": text})

print(result)
print(result.dict())
