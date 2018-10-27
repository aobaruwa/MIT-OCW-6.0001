# Problem Set 4A
# Name: Ahmed Baruwa
# Collaborators:None
# Time Spent: 4:20

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    partial = []
    # if there's only one element; return that element
    if len(sequence) <= 1:

        return sequence
    # elif there's only two elements; swap them
    elif len(sequence) == 2: 
        return ([sequence] +[sequence[1] + sequence[0]])

    else:
        # bring out the element in question   
        # and permute the remaining elements around it
        
        for i in range(len(sequence)):
            excluded = sequence[0: i] + sequence[i + 1: ]

            for j in get_permutations(excluded):

                partial.append(sequence[i] + j)

    return (partial)

    
#    print(partial)
    


if __name__ == '__main__':
    #EXAMPLE
    example_input1 = 'abc'
    example_input2 = 'abcd'
    example_input3 = '0123456'
    example_input4 = 'aeiou'
    
    print('Input1:', example_input1)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input1))
    print('Actual Output:', get_permutations(example_input1))
#    print('Actual Output:', get_permutations(example_input3))
##    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


    print('Input4:', example_input4)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input1))
    print('Actual Output:', get_permutations(example_input4))




