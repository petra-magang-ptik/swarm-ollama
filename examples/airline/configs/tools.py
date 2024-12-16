def escalate_to_agent(reason=None, **kwargs):
    return f"Escalating to agent: {reason}" if reason else "Escalating to agent"


def valid_to_change_flight(**kwargs):
    return "Customer is eligible to change flight"


def change_flight(**kwargs):
    return "Flight was successfully changed!"


def initiate_refund(**kwargs):
    status = "Refund initiated"
    return status


def initiate_flight_credits(**kwargs):
    status = "Successfully initiated flight credits"
    return status


def case_resolved(**kwargs):
    return "Case resolved. No further questions."


def initiate_baggage_search(**kwargs):
    return "Baggage was found!"
