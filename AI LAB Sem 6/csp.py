#csp
import random

def backtrackSearch(assignment, variables, domain, constraints):
  if len(assignment) == len(variables):
    return assignment
  var = select(assignment, variables)
  if var is None:
    return None
  random.shuffle(domain)
  for value in domain:
    assignment[var] = value
    if isConsistent(var, value, domain, constraints):
      result = backtrackSearch(assignment, variables, domain, constraints)
      if result is not None:
        return result
    assignment[var] = None
  return None

def select(assignment, variables):
  for var in variables:
    if var not in assignment:
      return var
  return None

def isConsistent(var, value, domain, constraints):
  for constraint in constraints:
    if var in constraint[0]:
      relatedVar = constraint[0][0] if constraint[0][1] == var else constraint[0][1]
      if relatedVar in assignment and assignment[relatedVar] == var:
        return False
    return True

assignment = {}
variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
domain = ['Monday', 'Tuesday', 'Wednesday']
constraints = [
    (('A', 'B'),),
    (('A', 'C'),),
    (('B', 'C'),),
    (('B', 'D'),),
    (('B', 'E'),),
    (('D', 'E'),),
    (('C', 'E'),),
    (('C', 'F'),),
    (('E', 'F'),),
    (('E', 'G'),),
    (('F', 'G'),)
]
solution = backtrackSearch(assignment, variables, domain, constraints)
print(solution)