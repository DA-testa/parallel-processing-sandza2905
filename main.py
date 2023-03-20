# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i,0) for i in range(n)]

    for j in range(m):
          thread = 0
          for i in range(0, n):
              if threads[i][1] < threads[thread][1]:
                  thread = i

          index, time = threads[thread]
          output.append(threads[thread])
          threads[thread] = (index, time + data[j])

          return output
    
def main():

    first_line = input().split()
    n = int(first_line[0])
    m = int(first_line[1])
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)

    for a,b in result:
        print(str(a)+' '+str(b))
        
        
if __name__ == "__main__":
      main()
    
