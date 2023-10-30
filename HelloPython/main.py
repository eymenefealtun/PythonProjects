import numpy
from eymenModule import exampleFunc
from AnimalPackage import info
from AnimalPackage.CatPackage import meow ## meow.speakImported is also fired in here

# import eymenModule
# eymenModule.exampleFunc()


print(numpy.zeros((3, 6)))

exampleFunc()

info.info()

meow.speakDirect()
meow.speakImported()


