# This is an attempt to capture an example of some work that I did recently.
# We had some config stored in a nested dictionary structure, and had to remove any
# sub-dicts that contained the key-value pair "present": False.

# Let's have a look at what this nested dict structure could look like.
config_example = {
    "name1": "value1",
    "name2": {
        "nested_name": "nested_value"
    },
    "name3": {
        "nested_name": "nested_value",
        "present": False
    },
    "name4": {
        "nested_name1": {
            "name": "value"
        },
        "nested_name2": {
            "name": "value",
            "present": False
        },
        "nested_name3": {
            "name": "value",
            "present": True
        }
    }
}

expected_config = {
    "name1": "value1",
    "name2": {
        "nested_name": "nested_value"
    },
    "name4": {
        "nested_name1": {
            "name": "value"
        },
        "nested_name3": {
            "name": "value",
            "present": True
        }
    }
}


# Write a method to remove the elements that we don't want.
