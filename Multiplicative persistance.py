max = int(input("Max number: "))

def per(n, calls=0):
    if len(str(n)) == 1:
        return calls

    digits = [int(i) for i in str(n)]
    result = 1
    for j in digits:
        result *= j
    return per(result, calls + 1)


for i in range(1, max):
    if '0' not in str(i):
        if '5' in str(i):
            if '2' not in str(i):
                if '4' not in str(i):
                    if '6' not in str(i):
                        if '8' not in str(i):
                            calls = per(i)
        else:
            calls = per(i)
    if calls > 9:
        print(i, ":", calls)
print("Finished")

# calls = per(277777788888899)
# print(calls)
