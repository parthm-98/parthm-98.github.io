"""
Left Factor Elimination
Input: Single grammar rule
Output: Grammar with left factor eliminated.
"""

from os.path import commonprefix


count = 0
# variables = {}

def left_factoring(s):
    # global count
    v = s.split('=')

    # The list of variables v should have 2 elements.
    if len(v) != 2:
        return None

    # Removing left and right spaces in both lhs and rhs
    lhs = v[0].strip()
    rhs = v[1].strip()

    # LHS should have only one character
    if len(lhs) != 1:
        return None

    # Preprocessing the right hand side to see all the OR options
    rhs = [x.strip() for x in rhs.split('|')]
    foo(lhs, rhs)

def foo(lhs, rhs):
    variables = {}
    for i in range(len(rhs)):
        for j in range(len(rhs)):
            if i != j:
                prefix = commonprefix([rhs[i], rhs[j]])
                if prefix:
                    if prefix in variables.keys():
                        variables[prefix].add(i)
                        variables[prefix].add(j)
                    else:
                        variables[prefix] = set([i, j])

    final_order = [k for k in sorted(variables, key=lambda k: len(variables[k]), reverse=True)]

    visited = [False for i in range(len(rhs))]

    global count
    for key in final_order:
        temp = []

        for rule_index in variables[key]:
            if visited[rule_index]:
                break
            visited[rule_index] = True
            temp.append(rhs[rule_index][len(key):])

        if len(temp) > 0:
            count += 1
            lhs_new = lhs + '`'*(count - lhs.count('`'))
            print(lhs, '=', key + lhs_new)
            foo(lhs_new, temp)

    for rule_index in range(len(rhs)):
        if not visited[rule_index]:
            print(lhs, '=', rhs[rule_index])

left_factoring('S = aAB | aA | a')
