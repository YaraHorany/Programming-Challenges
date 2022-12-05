"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. 
The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, 
except for the first group, which could be shorter than k but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
"""

def licenseKeyFormatting(s, k):
    s = s.upper() # convert string to uppercase
    length = len(s) - s.count('-')
    numGroups = length // k
    mod = length % k

    if mod > 0 and numGroups > 0:
        numGroups += 1

    # remove all '-' from string
    while '-' in s:
        pos = s.index('-')
        s = s[:pos] + s[pos + 1:]

    # all groups have the same length
    if mod == 0:
        for i in range(1, numGroups):
            s = s[:i*k + i - 1] + '-' + s[i*k + i - 1:]
            
    # first group with different length
    else: 
        if numGroups > 0:
            s = s[:mod] + '-' + s[mod:]
        for i in range(1, numGroups - 1):
            s = s[:i*k + mod + i] + '-' + s[i*k + mod + i:]
    return s

print(licenseKeyFormatting("5F3Z-2e-9-w", 4)) # output: "5F3Z-2E9W"
print(licenseKeyFormatting("2-5g-3-J", 2)) # output: "2-5G-3J"
print(licenseKeyFormatting("--------EyRfCyHxyUJzhygiazYpjuDFdHvrnDwoQKQEsccLDiwhpmjueADIzqIvExbDDFnEGovAxYeszbzuTekRuWUPXRPbVKJuDQzIzzTj", 16)) # output: "EYRF-CYHXYUJZHYGIAZYP-JUDFDHVRNDWOQKQE-SCCLDIWHPMJUEADI-ZQIVEXBDDFNEGOVA-XYESZBZUTEKRUWUP-XRPBVKJUDQZIZZTJ"
print(licenseKeyFormatting("a-a-a-a-", 1)) # output: "A-A-A-A"