"""
Exercise 5.4.
What is the output of the following program? Draw a stack diagram that shows the
state of the program when it prints the result.
    def recurse(n, s):
        if n == 0:
            print(s)
        else:
            recurse(n-1, n+s)
    recurse(3, 0)
1.  What would happen if you called this function like this:
    recurse(-1, 0) ?
2.  Write a docstring that explains everything someone would need to know in
    order to use this function (and nothing else).
"""



def recurse(n, s):
    '''Recursive function for getting and printing the value of s;
    n - positive integer;
    s - integer.
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(2,1)

