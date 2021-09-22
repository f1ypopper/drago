import sys

sys.path.append('/drago/Drago/')
import drago
renderd = drago.render('/drago/Drago/examples/conditionals/conditionals.html',{'foo':False,'a':6,'b':2})
print(renderd)