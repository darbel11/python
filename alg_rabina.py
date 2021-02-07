d = 256

def search(pat, txt, q):
    s = []
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1


    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(N - M + 1):

        if p == t:

            for j in range(M):

                if txt[i + j] != pat[j]:
                    break

            j += 1

            if j == M:
                s.append(i)

        if i < N - M:

            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            if t < 0:
                t = t + q
    print(s)
if __name__ == '__main__':
    search("cat", "my cat loves playing with other cats", 101)