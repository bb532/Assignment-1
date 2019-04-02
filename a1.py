# a1.py
# Beverly Balasu bb532
# 2/28/17
# Skeleton by Walker M. White (wmw2), Lillian Lee (LJL2), Feb 2017
"""Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service.  The primary
function in this module is exchange_amount()."""

from lab03 import*
from urllib2 import*


# PART A
def pre_space(s):
    """Returns: Substring of s up to, but not including, the first space
    
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    #condensed = s.strip()
    space = s.index(' ')
    return s[:space]


def post_space(string):
    """Returns: Substring of string after the first space

    Parameter string: the string to slice
    Precondition: string has at least one space in it"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    #cond = string.strip()
    s_pace = string.index(' ')
    #number_of_spaces = string.count(' ')
    return string[s_pace+1:]


# PART B
def get_source(json):
    """Returns: The source value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside double quotes (") immediately following the keyword "source". For
    example, if the JSON is

    '{"success":true,"error":"","source"   :"2 United States Dollars","target":"1.878102 Euros"}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    It returns the empty string if the JSON is the result of on invalid query.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    position_of_source = json.index('source')
    return first_in_double_quotes(json[position_of_source+7:])


def get_target(json):
    """Returns: The target value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside double quotes (") immediately following the keyword target. For
    example, if the JSON is

        '{"success":true,"error":"","source" :"2 United States Dollars","target":  "1.878102 Euros"}'

    then this function returns '1.878102 Euros' (not '"1.878102 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    position_of_target = json.index('target')
    return first_in_double_quotes(json[position_of_target+7:])

def has_error(json):
    """Returns: True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the opposite of (the
    intended bool version of) the value following the keyword success. For
    example, if the JSON is

        '{"success":false,"error":"Source currency code is invalid.", "source":"","target":""}'

    then this function returns True (it does NOT return the message
    'Source currency code is invalid', nor the string "True").

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    sucess = json[json.index('success'):]
    first_error = sucess.index(',')
    return 'false' in sucess[:first_error]


# PART C
def currency_response(currency_from, currency_to, amount_from):
    """Returns: A JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency
    currency_from to the currency currency_to. The response
    should be a string of the form

    '{ "success" : true, "error" : "", "source" : "<old-amount>", "target" : "<new-amount>" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty.

    Preconditions:
        currency_from is a string
        currency_to is a string
        amount_from is a positive float"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    from_string = str(currency_from).strip()
    to_string = str(currency_to).strip()
    amount_string = str(amount_from).strip()
    json_url = urlopen('http://cs1110.cs.cornell.edu/2017sp/a1server.php?source='+from_string+'&target='+to_string+'&amt='+amount_string+'')
    return json_url.read()
    

# PART D
def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency.
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition currency is a string"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    json = currency_response(currency.strip(), currency.strip(), 1.0)
    return not has_error(json)


def exchange_amount(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange, as a float.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    Preconditions:
        currency_from is a string for a valid currency code
        currency_to is a string for a valid currency code
        amount_from is a positive float"""
    # PLACEHOLDER. FIRST PUT TEST CASES IN a1test.py, THEN WRITE THE BODY
    json = currency_response(currency_from, currency_to, amount_from)
    target_value = get_target(json)
    first_space = target_value.index(' ')
    exchange_amount_substring = target_value[:first_space]
    return float(exchange_amount_substring)
