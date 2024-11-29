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

def E1(K, U):
    try:
        E = int(K.split('-')[-1])
        C = (E - len(U)) % 10000
    except ValueError:
        C = 0
    return C

def V1(U, K):
    C = E1(K, U)
    EK = K1(U)
    return K == EK, C

def login():
    U = input("Enter username: ")
    K = input("Enter license key: ")
    V, C = V1(U, K)
    if V:
        print(f"Login Success: Welcome!")
    else:
        print(f"Login Failed: Invalid license key.")

if __name__ == "__main__":
    login()
