class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr: str, open_count: int, close_count: int):
            # If the string is complete
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # Add "(" if we still have some left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ")" if it doesn’t exceed the number of "("
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res