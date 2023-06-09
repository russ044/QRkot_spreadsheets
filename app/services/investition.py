from datetime import datetime


def investing_object(
    target,
    sources,
):
    modified_sources = []
    target.invested_amount = int(target.invested_amount or 0)
    for source in sources:
        investing_volume = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount,
        )
        for object in (source, target):
            object.invested_amount += investing_volume
            if object.invested_amount == object.full_amount:
                object.fully_invested = True
                object.close_date = datetime.now()
        if target.fully_invested:
            break
        modified_sources.append(source)
    return modified_sources
