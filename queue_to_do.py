def even_start_sol(start, end):
    """
    Returns the value of the XOR `factorial' 
    
                start ^ (start + 1) ^ ... ^ (end -1)
             
    when start is an EVEN number.
    
    It is based on the property of even numbers that n ^ (n + 1) = 1
    """
    length = end - start

    if length % 4 == 0:
        sol = 0
    elif length % 4 == 2:
        sol = 1
    elif length % 4 == 1:
        sol = 1 ^ end
    else:
        sol = end

    return sol
    
    
def solution(start, length):
    """
    Solution loops through the rows of bunny workers. For each row, the checksum is calculated as follows:
    
    If the first worker's ID is an even number, it applies the function even_start_sol() on the row's endpoints.
    
    If it's an odd number, it applies the even_start_sol() on a row that starts at one worker earlier (so, it starts 
    with an even ID number) and then clears out this first number using the self-inverse XOR property: n ^ n = 0.
    
    The final checksum is the XOR product of all the rows' checksums.
    """
    ans = 0
    
    for i in range(length):
 
        st = start + i * length
        en = st + length  - i
        le = en - st
        
        if st % 2 == 0:
            sol = even_start_sol(st, en)
        else:
            sol = (st - 1) ^ even_start_sol(st - 1, en)
                
        ans ^= sol
        
    return ans
