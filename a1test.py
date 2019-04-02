# a1test.py
# Beverly Balasu bb532 (With help from Loius Liu, ll677, more specifically in part D)
# 2/28/17
# skeleton by Walker M. White (wmw2), Lillian Lee (LJL2), Feb 2017
"""Unit test for module currency

When run as an application, this module invokes several procedures that
test the various functions in the module currency."""
from cornelltest import *
import lab03
from a1 import *
from cornelltest import *
from lab03 import *


def test_A():
    """Test functions from Part A"""
    print "\t" + "Running test_A"
    # PLACEHOLDER - REPLACE WITH YOUR CODE
    assert_equals('123',pre_space('123 base'))
    assert_equals('123',pre_space('123             base'))
    assert_equals('',pre_space('           123  base'))
    assert_equals('123',pre_space('123  base          '))
    
    assert_equals('base',post_space('123 base'))
    assert_equals('            base',post_space('123             base'))
    assert_equals('          123  base',post_space('           123  base'))
    assert_equals(' base          ',post_space('123  base          '))
    
    assert_equals('U.S. dollar',post_space('1 U.S. dollar'))
    assert_equals('',pre_space(' 1 USD'))
    assert_equals('1 USD',post_space(' 1 USD'))


def test_B():
    """Test functions from Part B"""
    print "\t" + "Running test_B"
    # PLACEHOLDER - REPLACE WITH YOUR CODE
    assert_equals('2 United States Dollars',get_source('{"success":true,"error":"","source":"2 United States Dollars","target":"1.878102 Euros"}'))
    assert_equals('',get_source('{ "success" : false, "error" : "Source currency code is invalid.", "source" : "", "target" : "" }'))
    assert_equals('2 United States Dollars',get_source('{"success":   true,"error":"","source"   :    "2 United States Dollars","target":  "1.878102 Euros"}'))
    
    assert_equals('1.878102 Euros',get_target('{"success":true,"error":"","source":"2 United States Dollars","target":"1.878102 Euros"}'))
    assert_equals('',get_target('{ "success" : false, "error" : "Source currency code is invalid.", "source" : "", "target" : "" }'))
    assert_equals('1.878102 Euros',get_target('{"success":   true,"error":"","source"   :    "2 United States Dollars","target":  "1.878102 Euros"}'))
    
    assert_equals(False,has_error('{"success":true,"error":"","source":"2 United States Dollars","target":"1.878102 Euros"}'))
    assert_equals(True,has_error('{ "success" :            false, "error" : "Source currency code is invalid.", "source" : "", "target" : "" }'))
    assert_equals(False,has_error('{"success"  :   true,"error":"","source"   :    "2 United States Dollars","target":  "1.878102 Euros"}'))
    
    assert_equals('2.5 United States Dollars',get_source('{"source" : "2.5 United States Dollars","target" : "2.3 Euros","success" : true, "error" : "","target": "" }'))
    assert_equals('2.3 Euros',get_target('{"source" : "2.5 United States Dollars","target" : "2.3 Euros","success" : true, "error" : "","target": "" }'))
    

def test_C():
    """Test functions from Part C"""
    print "\t" + "Running test_C"
    # PLACEHOLDER - REPLACE WITH YOUR CODE
    assert_equals('{ "success" : true, "error" : "", "source" : "1 United States Dollar", "target" : "0.001028329131 Bitcoins" }',
                  currency_response('USD', 'BTC', 1))
    assert_equals('{ "success" : true, "error" : "", "source" : "7.8 United States Dollars", "target" : "7.3245978 Euros" }',
                  currency_response('USD', 'EUR', 7.8))
    assert_equals('{ "success" : true, "error" : "", "source" : "5 Japanese Yen", "target" : "0.044156309804202 United States Dollars" }',
                  currency_response('JPY', 'USD', 5.0))
    assert_equals('{ "success" : true, "error" : "", "source" : "3.141592 Namibian Dollars", "target" : "0.23425049864852 United States Dollars" }',
                  currency_response('NAD', 'USD', 3.141592))
    assert_equals('{ "success" : false, "error" : "Exchange currency code is invalid.", "source" : "", "target" : "" }',
                  currency_response('USD', 'aaa', 3))
    assert_equals('{ "success" : false, "error" : "Source currency code is invalid.", "source" : "", "target" : "" }',
                  currency_response('UD', 'PEN', 2.3))
    assert_equals('{ "success" : false, "error" : "Currency amount is invalid.", "source" : "", "target" : "" }',
                  currency_response('USD', 'SEK', False))
    assert_equals('{ "success" : false, "error" : "Currency amount is invalid.", "source" : "", "target" : "" }',
                  currency_response('USD', 'SEK', False))
    assert_equals('{ "success" : false, "error" : "Source currency code is invalid.", "source" : "", "target" : "" }',
                  currency_response('UD', 'SK', False))
    assert_equals('{ "success" : true, "error" : "", "source" : "1 United States Dollar", "target" : "1 United States Dollar" }',
                  currency_response('USD', 'USD', 1.0))
    

def test_D():
    """Test functions from Part D"""
    print "\t" + "Running test_D"
    # PLACEHOLDER - REPLACE WITH YOUR CODE
    assert_equals(True,iscurrency('NOK'))
    assert_equals(True,iscurrency('USD'))
    assert_equals(False,iscurrency('NK'))
    assert_equals(False,iscurrency('usd'))
    assert_equals(False,iscurrency('27'))
    assert_equals(True,iscurrency('        NOK'))
    assert_equals(False,iscurrency('N           OK'))
    
    assert_floats_equal(0.001028329131,exchange_amount('USD', 'BTC', 1))
    assert_floats_equal(0.044156309804202,exchange_amount('       JPY', 'USD      ', 5.0))
    assert_floats_equal(0.23425049864852,exchange_amount('NAD  ', 'USD', 3.141592))
    
    
#def test_E():
#    """Test functions from Part E, the optional test code for the first_in_double_quotes() function"""
#    print "\t" + "Running test_E"
#    # PLACEHOLDER - REPLACE WITH YOUR CODE
#    assert_equals('23',first_in_double_quotes('1"23" base'))
#    assert_equals('12',first_in_double_quotes('"12"3 base'))
#    assert_equals('12',first_in_double_quotes('          "12"3 base'))
#    assert_equals('3 b',first_in_double_quotes('12          "3 b"          ase'))
#    assert_equals('',first_in_double_quotes('1""23"" base'))
#    assert_equals('23',first_in_double_quotes('1"23"" base'))
#    assert_equals('',first_in_double_quotes('1"" base'))
#    assert_equals('',first_in_double_quotes('1 base""'))
    


# Script code
test_A()
test_B()
test_C()
test_D()
#test_E()
print "Ya did it!"