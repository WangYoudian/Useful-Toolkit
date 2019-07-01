def greet(name):
    print (u"Hello, {0}!".format(name))
print u"What's your name?"
name = eval(raw_input())
greet(name)