"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

"""
#my solution - completely different approach than proposed on the page, but looks quite smart, as all of them were comparing elements

def same_structure_as(original, other):
    special = ["\'[\'", "\']\'", "\"]\"", "\"[\""]
    original_str = str(original)
    other_str = str(other)
    for i in special:
        if i in original_str:
            original_str = original_str.replace(i,"")
    
    for i in special:
        if i in other_str:
            other_str = other_str.replace(i,"")

    if "".join([i for i in original_str if i in ["[","]",","]]) == "".join([i for i in other_str if i in ["[","]",","]]):
        return True
    else:
        return False


#another solutions
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)

def same_structure_as(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)



