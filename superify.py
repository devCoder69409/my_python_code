def superify(name):
    return "super" + name

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
#prints "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
#prints "Look, it's supersupersupercat!"