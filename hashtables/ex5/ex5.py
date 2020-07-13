# Your code here
# create cache
# cache = {}



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    endpoints = dict()
    answer = []
    for query in queries:
        if query not in endpoints:
            endpoints[query] = 1
    for path in files:
        splitpath = path.split('/')
        decon_path = splitpath[-1]
        if decon_path in endpoints:
            answer.append(path)
    return answer



if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
