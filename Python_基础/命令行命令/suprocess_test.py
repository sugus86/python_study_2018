
import subprocess
p = subprocess.Popen('dir', shell=True)

print(p.returncode)

p.wait()

p.returncode


import subprocess
child1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
child2 = subprocess.Popen(['wc', '-l'], stdin=child1.stdout, stdout=subprocess.PIPE)
out = child2.communicate()
child1.wait()
child2.wait()
print(out)


p=subprocess.Popen("df -h",shell=True,stdout=subprocess.PIPE)
out=p.stdout.readlines()

p=Popen(['ls','-l'],stdout=PIPE).communicate()[0]

p1=Popen(['dmesg'],stdout=PIPE)
p2=Popen(['grep','cpu'],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]
