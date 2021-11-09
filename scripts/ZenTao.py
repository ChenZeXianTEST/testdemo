import os


# os.popen(R'cd \application\apache-jmeter-5.0\bin')
cmd = R'cd \application\apache-jmeter-5.0\bin & jmeter -n -t d:\test\test.jmx'
os.system(cmd)
# with os.popen(cmd, 'r') as f:
#     print(f.read())
