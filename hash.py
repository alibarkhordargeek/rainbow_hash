from hashlib import sha256
import csv

def hash_pass(input_file, output_file):
    names= list()
    hashes = list()
    passes = dict()
    f_passes = list()

    with open(input_file, 'r') as fin:
        r = csv.reader(fin)
        for row in r:
            names.append([row[0], row[1]])
            hashes.append(row[1])
        for num in range(1000, 10000):
            hash = sha256(str(num).encode()).hexdigest()
            for hsh in hashes:
                if hash == hsh:
                    passes[num] = hash

    for ps in list(passes.keys()):
        for nm in names:
            if passes[ps] == nm[1]:
                f_passes.append([nm[0], str(ps)])

    with open(output_file, 'w') as fout:
        w = csv.writer(fout)
        w.writerows(f_passes)

hash_pass('example.csv', 'example.csv')