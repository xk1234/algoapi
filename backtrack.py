def permns(arr):
    present = [False] * len(arr)
    perm = []
    def p_help():
        if len(perm) == len(arr):
            print(perm)
        else:
            for i in range(len(arr)):
                if present[i]:
                    continue
                present[i] = True
                perm.append(arr[i])
                p_help()
                perm.pop()
                present[i] = False
    p_help()

def subs(arr):
    ss = []
    def s_help(i):
        if i == len(arr) - 1:
            print(ss)
            return
        ss.append(arr[i])
        s_help(i+1)
        ss.pop()
        s_help(i+1)
    s_help(0)



permns([1,2,3,4])
subs([1,2,3,4])