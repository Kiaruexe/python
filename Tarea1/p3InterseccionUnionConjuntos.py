import re
from typing import Set

def parseSet(input_str: str) -> Set[int]:
    nums = re.findall(r"-?\d+", input_str)
    return set(int(n) for n in nums)

def main() -> None:
    print("Introduce los elementos del primer conjunto (ejemplo: 1 2 3 o 1,2,3):")
    s1Input = input().strip()
    print("Introduce los elementos del segundo conjunto (ejemplo: 3 4 5 o 3,4,5):")
    s2Input = input().strip()

    set1 = parseSet(s1Input)
    set2 = parseSet(s2Input)

    intersection = set1 & set2               
    union = set1 | set2                        
    symmetricDifference = set1 ^ set2         

    print("\nConjunto 1 (ordenado):", sorted(set1))
    print("Conjunto 2 (ordenado):", sorted(set2))
    print("\nIntersección (elementos comunes):", sorted(intersection))
    print("Unión (todos los elementos, sin duplicados):", sorted(union))
    print("Diferencia simétrica (en uno u otro, pero no en ambos):", sorted(symmetricDifference))

if __name__ == "__main__":
    main()
