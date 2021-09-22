import sys

sys.path.append('/home/atharva/Python/drago/Drago/')
import drago
renderd = drago.render('Drago/examples/loops/loops.html',{'animals':['pigs','monkeys','dogs']})
print(renderd)