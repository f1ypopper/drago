import sys

sys.path.append('/home/atharva/Python/drago/Drago/')
import drago
renderd = drago.render('Drago/examples/variables/variable.html',{'foo':'bar'})
print(renderd)