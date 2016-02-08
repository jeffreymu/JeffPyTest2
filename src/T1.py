# T1.py
import sys

def Fuc():
     print("hello T1")

if __name__ == '__main__':
     if len(sys.argv) != 3:
         print("Usage: python input_name output_name")
         exit(1)
     f_input = sys.argv[1]
     print(f_input)


     f_output = sys.argv[2]
     print(f_output)
     Fuc()






