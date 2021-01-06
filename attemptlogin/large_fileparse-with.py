#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

# ^same, but with successes
loginsuccess = 0 # counter for success

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            print(line.split(" ")[-1])
            loginfail += 1 # this is the same as loginfail = loginfail + 1

        elif "-] Authorization failed" in line:
            loginsuccess += 1
print("The number of failed log in attempts is", loginfail)
print("The number of successful log in attempts is", loginsuccess)

