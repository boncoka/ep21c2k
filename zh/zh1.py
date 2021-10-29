def feladatsort_pontoz(right, m):
    points = 0
    for index in range(len(right)):
        if right[index] == m[index]:
            if 0 <= index <= 4:
                points += 3
            elif 5 <= index <= 9:
                points += 4
            elif 10 <= index <= 12:
                points += 5
            elif index == 13:
                points += 6
    return points


# 1. feladat
answer = []

source = open('valaszok.txt')
for sor in source:
    answer.append(sor.strip().split())
source.close()

correct = answer[0][0]
answer = answer[1:]

print('2. feladat: A versenyen', len(answer), 'versenyző indult.')

id = input('3. Kérem adja meg a versenyző azonosítóját: ')
for bejegyzes in answer:
    if bejegyzes[0] == id:
        comp_answ = bejegyzes[1]
        print(comp_answ, ' (a versenyző válasza)')
        break

print('4. feladat')
print(correct, ' (a helyes megoldás: )')
for index in range(len(comp_answ)):
    if comp_answ[index] == correct[index]:
        print('+', end='')
    else:
        print(' ', end='')
print(' (a versenyző helyes válaszai)')

sorszam = int(input('5. feladat: A feladat sorszáma = '))
feladat_indexe = sorszam - 1

counter = 0
for bejegyzes in answer:
    if bejegyzes[1][feladat_indexe] == correct[feladat_indexe]:
        counter += 1
print('A feladatra', counter, 'fő, a versenyzők', round(counter / len(answer) * 100, 2),
      '%-a adott helyes választ.')

# 6. feladat
pontok = []
for bejegyzes in answer:
    pontok.append([bejegyzes[0], feladatsort_pontoz(correct, bejegyzes[1])])
fileobject = open('pontok.txt', 'w')
for sor in pontok:
    print(sor[0], sor[1], file=fileobject)
fileobject.close()

print('7. feladat: A verseny legjobbjai:')
ponthalmaz = set()
for bejegyzes in pontok:
    ponthalmaz.add(bejegyzes[1])
pontlista = sorted(list(ponthalmaz), reverse=True)[0:3]

for points in pontlista:
    for bejegyzes in pontok:
        if bejegyzes[1] == points:
            print(pontlista.index(points) + 1, '. (', points, ' pont): ', bejegyzes[0], sep='')