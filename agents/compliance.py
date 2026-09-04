from utils.agents import run_agent

COMPLIANCE_ROLE_PROMPT = """
You are the Compliance Intelligence Agent inside IntelliOps AI.

Your job is to analyze industrial documents specifically for:
- Regulatory and procedural requirements
- Missing, outdated, or overdue inspections and certifications
- Documentation gaps that would fail an audit
- Whether stated procedures align with required standards

Answer the user's question using ONLY the context provided. Focus
strictly on compliance and audit-readiness concerns. If the context
does not contain compliance-relevant information for this question,
say so clearly rather than guessing.
"""


def run_compliance_agent(question, source_filter=None):
    return run_agent(COMPLIANCE_ROLE_PROMPT, question, source_filter=source_filter)


if __name__ == "__main__":
    result = run_compliance_agent("What compliance responsibilities does this document outline for employers?")
    print("ANSWER:", result["answer"])
    print("SOURCES:", result["sources"])