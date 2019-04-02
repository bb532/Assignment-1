# lab03_test.py
# Beverly Balasu bb532
# PUT THE DATE YOU LAST CHANGED THIS FILE HERE
# Skeleton by Walker M. White (wmw2), Lillian Lee (LJL2), Feb 2017


"""(Skeleton of) tests for lab03.py"""

import cornelltest      # For assert_equals and assert_true
import lab03   # This is what we are testing


def test_replace_first():
    """Test procedure for repeat_first"""
    print 'Testing the function replace_first'
    
    print "\tTesting crane, a-> o"    
    result = lab03.replace_first('crane','a','o')
    cornelltest.assert_equals('crone', result)
    result2 = lab03.replace_first('POLL','L','o')
    cornelltest.assert_equals('POoL', result2)
    result3 = lab03.replace_first('a bird','bird','plane')
    cornelltest.assert_equals('a plane', result3)
    result4 = lab03.replace_first('Geoffry','eoffr','u')
    cornelltest.assert_equals('Guy', result4)
    result5 = lab03.replace_first('Sup','u','ou')
    cornelltest.assert_equals('Soup', result5)

    # YOU NEED TO ADD MORE TEST CASES
    
###########
### SCRIPT CODE (Call test procedures here)
###########

def test_first_in_double_quotes():
    """Test procedure for first_in_double_quotes"""
    print 'Testing the function first_in_double_quotes'
    
    print '\tTesting \'A \"B C\" D\''
    result = lab03.first_in_double_quotes('A "B C" D')
    cornelltest.assert_equals('B C', result)
    
    # YOU NEED TO ADD MORE TEST CASES
    


test_replace_first()
# test_first_in_double_quotes()
print 'Module lab03: all tests passed'