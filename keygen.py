import hashlib as H

def H1(S, I=1):
    for _ in range(I):
        S = H.sha256(S.encode()).hexdigest()
        S = H.md5(S.encode()).hexdigest()
        S = H.blake2b(S.encode()).hexdigest()
    return S

def K1(U):
    C = 256000
    S = U + str(C)
    S = H1(S, I=C)
    L = []
    for i in range(0, 25, 5):
        P = S[i:i+5].upper()
        L.append(P)
    F = '-'.join(L)
    F = H1(F, I=C)
    L = [F[i:i+5].upper() for i in range(0, 25, 5)]
    F = '-'.join(L)
    E = (C + len(U)) % 10000
    F += f"-{E:04d}"
    return F

def main():
    U = input("Enter username: ")
    K = K1(U)
    print(f"Generated License Key: {K}")

if __name__ == "__main__":
    main()
