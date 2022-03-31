import random


# The four BOTS defined as functions with four different responses each:
def mj(a, b=None):
    responses = ["I think {} sounds great!".format(a + "ing"),
                 "2 {}".format(a + "ing"),
                 "3 {}".format(a + "ing"),
                 "4 {}".format(a + "ing")]
    return random.choice(responses)


def lebron(a, b=None):
    responses = ["{}, my favorite!".format(a + "ing"),
                 "2 {}, my favorite!".format(a + "ing"),
                 "3 {}, my favorite!".format(a + "ing"),
                 "4 {}, my favorite!".format(a + "ing")]
    return random.choice(responses)


def lavine(a, b=None):
    responses = ["I am down for {}!".format(a + "ing"),
                 "I am down for {} 2!".format(a + "ing"),
                 "I am down for {} 3!".format(a + "ing"),
                 "I am down for {} 4!".format(a + "ing")]
    return random.choice(responses)


def kobe(a, b=None):
    responses = ["Hell na, {} is so 2000".format(a + "ing"),
                 "2 Hell na, {} is so 2000".format(a + "ing"),
                 "3 Hell na, {} is so 2000".format(a + "ing"),
                 "4 Hell na, {} is so 2000".format(a + "ing")]
    return random.choice(responses)


# Returns a response from the specified bot
def bot_response(bot_name, action):
    if bot_name == "mj":
        response = mj(action)
        return response

    if bot_name == "lebron":
        response = lebron(action)
        return response

    if bot_name == "lavine":
        response = lebron(action)
        return response

    if bot_name == "kobe":
        response = kobe(action)
        return response
