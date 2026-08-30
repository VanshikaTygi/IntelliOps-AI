import os
from dotenv import load_dotenv
from groq import Groq

from agents.maintenance import run_maintenance_agent
from agents.safety import run_safety_agent
from agents.compliance import run_compliance_agent
from utils.rag_chain import get_answer

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

ROUTING_PROMPT = """
You are a routing classifier for an industrial AI system. Given a
user's question, decide which of the following specialist agents are
relevant to answering it:

- maintenance: equipment failures, breakdowns, repair history, root causes
- safety: hazards, risks, incidents, unsafe conditions
- compliance: regulatory requirements, missing inspections, audit gaps

Respond with ONLY the relevant agent names, comma-separated, in
lowercase (e.g. "maintenance,safety"). If none clearly apply, respond
with exactly: none
"""


def route_question(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": ROUTING_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    raw_decision = response.choices[0].message.content.strip().lower()

    if raw_decision == "none":
        return []

    return [name.strip() for name in raw_decision.split(",")]


def get_supervised_answer(question):
    agent_names = route_question(question)

    if not agent_names:
        result = get_answer(question)
        return {
            "agents_used": ["general"],
            "responses": [{"agent": "general", "answer": result["answer"], "sources": result["sources"]}]
        }

    responses = []

    for name in agent_names:
        if name == "maintenance":
            result = run_maintenance_agent(question)
        elif name == "safety":
            result = run_safety_agent(question)
        elif name == "compliance":
            result = run_compliance_agent(question)
        else:
            continue

        responses.append({"agent": name, "answer": result["answer"], "sources": result["sources"]})

    return {
        "agents_used": agent_names,
        "responses": responses
    }


if __name__ == "__main__":
    result = get_supervised_answer("What compliance responsibilities does this document outline for employers?")
    print("AGENTS USED:", result["agents_used"])
    for r in result["responses"]:
        print(f"\n--- {r['agent'].upper()} ---")
        print(r["answer"])
        print("Sources:", r["sources"])