while True:
    inches = float(input("Anna luku tuumissa (negatiivinen luku pysäyttää ohjelman): "))

    if inches < 0:
        print("Lopetetaan")
        break

    print(f"{inches} tuumaa senttimetreinä on {inches * 2.54}cm.")