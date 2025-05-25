import ollama
def getFinalAnalysis(data):
    response = ollama.chat(
        model="deepseek-r1:8b",
        messages=[
            {"role": "user", "content": """
    You are a financial analyst.

    Based only on the data provided below, do the following:
    1. Output your investment recommendation as exactly one of: Strong Buy, Buy, Hold, Sell, Strong Sell.
    2. Place your recommendation between the tags: <<RECOMMENDATION>> and <<END>> on a single line by itself.
    3. After the recommendation, write an explanation of around 200 words justifying your decision, referencing specific numbers from the data.

    If any important data is missing, mention that as a limitation.

    Here is the data:
    ---
    Company fundamentals:
    """ + data+""""


    Format your answer exactly as follows:

    <<RECOMMENDATION>>
    [Strong Buy/Buy/Hold/Sell/Strong Sell]
    <<END>>

    [Your 200-word explanation here.]


    """}
        ],
    )
    return(response["message"]["content"])
