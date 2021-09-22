def concat_modules(modules):
    separator = '%2C'
    joined = separator.join(modules)
    return joined


def concat_events(events):
    separator = '%7C'
    joined = separator.join(events)
    return joined


def concat_parameters(parameters):
    separator = '&'
    joined = separator.join(parameters)
    return joined
