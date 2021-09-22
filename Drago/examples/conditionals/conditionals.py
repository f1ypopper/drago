import sys

sys.path.append('/home/atharva/Python/drago/Drago/')
import drago
renderd = drago.render('/home/atharva/Python/drago/Drago/examples/conditionals/conditionals.html',{'foo':False,'a':6,'b':2})
print(renderd)