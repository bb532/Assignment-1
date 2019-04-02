# lab03.py
# Beverly Balasu bb532
# 2/28/217
# Skeleton by Walker M. White (wmw2), Lillian Lee (LJL2), Feb 2017


"""Lab 03 module:
        
        * potentially initially erroneous function for students to test 

        * skeleton of function needed for Assignment 1
"""

def replace_first(word,target,rep):
    ####
    #### THIS FUNCTION MAY HAVE BUGS 
    ####
    """Returns: a copy of word with the FIRST instance of target replaced by rep

    Example: replace_first('crane','a','o') returns 'crone'
    Example: replace_first('poll','ll','p') returns 'pop'

    Parameter word: The string to copy and replace
    Precondition: word is a string

    Parameter target: The substring to find in word
    Precondition: target is a nonempty valid substring of word

    Parameter rep: The substring to use in place of target
    Precondition: rep is a string
    """
    pos = word.index(target)                   # <pos> should be where the first target starts
    #print "DEBUG: pos is: " + str(pos)
    
    before = word[:pos]                        # <before> should be the part of word up to but not including
    #print "DEBUG: before is: " + str(before)  # the first occurrence of target
                        
    after  = word[pos+len(target):]            # <after> should be the part of word after the first
    #print "DEBUG: after is: " + str(after)    # occurrence of target
                          
    result = before + rep + after              # <result> should be the desired output.
    #print "DEBUG: result is: " + str(result)
    
    return result



def first_in_double_quotes(s):
    """Returns: The first substring of s between two double-quote characters

    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'Aaa "B C" D "E F" G', this function still returns 'B C'
       because it only picks the first such substring.
    Example: If s is 'A "   B C" D', this function returns '   B C'

    Parameter s: a string to search
    Precondition: s contains at least two double-quote characters
    """
    ""  # PLACEHOLDER - REPLACE WITH YOUR REAL CODE
    position_of_first_double_quote = s.index('"')
    string_from_first_quote = s[position_of_first_double_quote+1:]
    position_of_second_double_quote = string_from_first_quote.index('"')
    return string_from_first_quote[:position_of_second_double_quote]
