#!/usr/bin/python3
def matrix_mul(m_a, m_b):

    """
    Returns the product of two matrices

    Args:
    m_a -- The 1st matrix
    m_b -- The 2nd matrix

    Returns:
    The product of m_a * m_b
    """

    # if not list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # if not list of lists
    if False in {isinstance(m_a[i], list) for i in range(len(m_a))}:
        raise ValueError("m_a must be a list of lists")
    elif False in {isinstance(m_b[i], list) for i in range(len(m_b))}:
        raise ValueError("m_b must be a list of lists")

    # Auxiliary set for checks
    set_a = {len(m_a[i]) for i in range(len(m_a))}
    set_b = {len(m_b[i]) for i in range(len(m_b))}

    # if list is empty
    if 0 in set_a:
        raise ValueError("m_a can't be empty")
    elif 0 in set_b:
        raise ValueError("m_b can't be empty")

    # Check for rectangularity
    if len(set_a) > 1:
        raise TypeError("each row of m_a must be of the same size")
    elif len(set_b) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check for size matching
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
