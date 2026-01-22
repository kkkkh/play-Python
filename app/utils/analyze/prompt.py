from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an English learning assistant.
        You analyze short English transcripts from audio lessons.
        {format_instructions}"""
    ),
    (
        "human",
        """Analyze the following transcript:
        {text}
        """
    )
])
