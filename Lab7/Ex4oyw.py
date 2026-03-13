def check_purchases_budget(recent_purchases, budget):
    """
    Returns a list of messages, one per purchase, saying whether it is over or within budget.
    """
    results = []
    for purchase in recent_purchases:
        if purchase > budget:
            results.append("over")
        else:
            results.append("within")
    return results