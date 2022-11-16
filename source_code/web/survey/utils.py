from survey.models import Option



def reorder(question):
    existing_options = Option.objects.filter(question=question)
    if not existing_options.exists():
        return
    number_of_option = existing_options.count()
    new_ordering = range(0, number_of_option)

    for order, option in zip(new_ordering, existing_options):
        option.order = order
        option.save()