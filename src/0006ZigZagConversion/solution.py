class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        cycle = 2 * numRows - 2
        ls = []

        for i in range(numRows):

            for j in range(len(s) // cycle + 1):
                sub = s[j * cycle: (j + 1) * cycle]
                # 1行目と最後の行
                try:
                    ls.append(sub[i])
                except IndexError:
                    pass

                if 0 < i < numRows - 1:
                    # 真ん中の行
                    try:
                        ls.append(sub[cycle - i])
                    except IndexError:
                        pass

        return "".join(ls)
