"""Several methods to help with the tests."""

# Python3 support
from __future__ import print_function
from __future__ import unicode_literals


def test_model(model, data):
    """Return if the dictionary `data` complies with the `model`."""
    same_keys = set(model.keys()) == set(data.keys())

    if not same_keys:
        print("model_keys: {}\ndata_keys: {}".format(sorted(model.keys()), sorted(data.keys())))

    correct_class = True
    for key, instance_class in model.items():
        same_class = isinstance(data[key], instance_class)
        correct_class = correct_class and same_class
        if not same_class:
            print("key: {}\nmodel_class: {}\ndata_class: {}".format(
                                                    key, instance_class, data[key].__class__))

    return correct_class and same_keys
