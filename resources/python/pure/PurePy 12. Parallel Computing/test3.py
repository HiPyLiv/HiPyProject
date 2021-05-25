import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self, id):
        super(MyProcess, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        print("I'm the process with id: {}".format(self.id))

# processes = MyProcess(0), MyProcess(1), MyProcess(2)
# [p.start() for p in processes]
# print("Executed after?")

def isprime(n):
    if n == 2  or n == 3:
        return True
    if n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def prime_batch(batch):
    return [isprime(x) for x in batch]

def create_batches(seq, batchsize):
    tasks = len(seq) // batchsize
    batches = [seq[batchsize*x: batchsize*(x+1)] for x in range(tasks)]
    batches.append(seq[tasks*batchsize:])
    return batches

if __name__ == '__main__':
    import itertools
    flatten = lambda l: list(itertools.chain.from_iterable(l))

    pool = multiprocessing.Pool()
    data_range = 1000000
    process_together = 20
    inputs = create_batches(range(data_range), process_together)
    outputs = pool.map(prime_batch, inputs)
    outputs = flatten(outputs)
    outputs = [x for x in range(data_range) if outputs[x]]
