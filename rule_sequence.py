
def zero(s):
    if s[0] == "0":
        return s[1:]

def one(s):
    if s[0] == "1":
        return s[1:]


############### IMPERATIVE-STYLE CODE ###############

# def rule_sequence(s, rules):
#     for rule in rules:
#         s = rule(s)
#         if s == None:
#             break

#     return s

#####################################################


def print_state(string, rules):
    print({ 'string' : string, 'rules' : rules})

def rule_sequence(string, rules):

    # print_state(string,rules)

    if string != None and len(rules)>= 1:
        return rule_sequence(rules[0](string),rules[1:])
    else:
        return string

print(rule_sequence('0101', [zero, one, zero]))
# => 1

print(rule_sequence('0101', [zero, zero]))
# => None