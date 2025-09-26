import time
def loading():
    for i in range(100):

        
        time.sleep(0.05)
        print(f'\r loading...{i+1}%', end='', flush=True)


            
    print("\n     over")
if __name__ == "__main__":
    loading()