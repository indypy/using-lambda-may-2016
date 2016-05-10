import this


def lambda_handler(event, context):
    return "".join([this.d.get(c, c) for c in this.s])
