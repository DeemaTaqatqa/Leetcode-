def search_matrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    # Binary search to find the correct row
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:  # Target is larger than the largest element in the row
            top = row + 1
        elif target < matrix[row][0]:  # Target is smaller than the smallest element in the row
            bot = row - 1
        else:  # Target is within the range of this row
            break

    if not (top <= bot):  # No valid row found
        return False

    # Perform binary search in the identified row
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:  # Target is larger than the current element
            l = m + 1
        elif target < matrix[row][m]:  # Target is smaller than the current element
            r = m - 1
        else:  # Target found
            return True

    return False  # Target not found in the row
