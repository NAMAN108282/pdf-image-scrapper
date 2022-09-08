import os,subprocess,glob

#Move to the project directory
os.chdir('/usr/src/mypdftoolbox')

#Sample PDF file
input_file_name  = 'Sample1.pdf'
input_path  = './static'
output_path = '/usercode/output'

#Extracting images from the input file
subprocess.call(['python3'
                 , 'script.py'
                 , '-i'
                 ,  os.path.join(input_path,input_file_name)
                 , '-o'
                 , output_path
                  ])
                  
#Downloading the input file.
subprocess.call(['cp'
                 , os.path.join(input_path,input_file_name)
                 , os.path.join(output_path,input_file_name)
                ]) 
