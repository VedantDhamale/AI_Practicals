import math


def fun(d, node, maxP, v, A, B, td):
    # d=current depth of the tree.,maxP: A boolean flag indicating max or min,td:: The target depth
    if d == td:
        # v[node] is used to access the value associated with a specific node in a binary tree.
        return v[node]
    if maxP:
        for i in range(2):
            value = fun(d + 1, node * 2 + i, False, v, A, B, td)
            A = max(A, value)
            if B <= A:
                break
        return A
    else:
        for i in range(2):
            value = fun(d + 1, node * 2 + i, True, v, A, B, td)
            B = min(B, value)
            if B <= A:
                break
        return B


n = int(input("Enter the number of  teminalnodes: "))
m = []
for i in range(n):
    entry = int(input(f"Enter the value for node[{i}]: "))
    m.append(entry)

td = int(math.log2(len(m)))
d = 0
node = 0
ans = fun(d, node, True, m, -999, 999, td)
print("Ans = ", ans)
