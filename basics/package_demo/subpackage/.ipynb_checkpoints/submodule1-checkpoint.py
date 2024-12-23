def submodule_demo():
    print("inside submodule 1")

from .. import module1
module1.mod1_demo()