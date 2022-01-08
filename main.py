from collections import OrderedDict
my_dict = OrderedDict({
    "Sakti":"9901",
    "Akash":"9902"
})
my_dict.update({"Atish":"9900"})
my_dict.move_to_end("Atish", last = False)
print(my_dict)