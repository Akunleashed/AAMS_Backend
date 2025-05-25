import ollama
def getFinalAnalysis(data):
    response = ollama.chat(
        model="deepseek-r1:8b",
        messages=[
            {"role": "user", "content": """You are a financial analyst.

Based strictly on the data provided below, do the following:

1. Output your investment recommendation as exactly one of the following: Strong Buy, Buy, Hold, Sell, Strong Sell.
2. Place your recommendation between the tags: <RECOMMENDATION> and </RECOMMENDATION> on a single line by itself.
3. After the recommendation, write a concise, professional explanation (around 200 words) justifying your decision between the tags <Explanation> and </Explanation> 

In your explanation:
- Use specific data points (like valuation ratios, profit margins, or revenue trends) where they clearly support your reasoning.
- Do not use vague or generic language — your justification should be grounded in the actual numbers or facts provided.
- If any important data appears to be missing or insufficient to make a confident decision, mention it as a limitation.

Here is the data:
---
Company fundamentals:
""" + data + """
---

While making extra sure that the phrase between the <RECOMMENDATION> and </RECOMMENDATION> are one of the following -Strong Buy/Buy/Hold/Sell/Strong Sell
Format your answer exactly as follows:

<RECOMMENDATION>[Strong Buy/Buy/Hold/Sell/Strong Sell]</RECOMMENDATION>
<Explanation>[Explanation here, referring to specific data when relevant.]</Explanation>
"""}
        ],
    )
    return(response["message"]["content"])
