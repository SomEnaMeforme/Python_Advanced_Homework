import sys

def get_mean_size(data) -> str:
    summary_size = 0
    count = 1
    if len(data) > 0:
        files = list(filter(lambda line: len(line.split()[-1].split('.')) > 1 or not(line.split()[4].isnumeric()), data))
        summary_size = sum([float(line.split()[4]) for line in files])
        count = len(files) if len(files) > 0 else 1
    return str(summary_size / count)


if __name__ == '__main__':
    print(get_mean_size(sys.stdin.readlines()[1:]))
