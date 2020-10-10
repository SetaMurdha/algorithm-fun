"""
Question:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link    : https://projecteuler.net/problem=1

"""

def nilai(nilai,sum):
    tampungNilai =[]
    nilai = nilai
    while nilai < 1000:
        tampungNilai.append(nilai)
        nilai += sum
    return tampungNilai


hasil1 = sum(nilai(3,3))
hasil2 = sum(nilai(5,5))

print(hasil1+hasil2)

