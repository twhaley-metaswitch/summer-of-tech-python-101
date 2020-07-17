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
# We write this function to work recursively.
def clean_config(config):
    # The first thing we want to do is check for the key in the dict that we've been passed.
    if "present" in config:
        # The "present" key is present in this config dict. If the corresponding value is false,
        # then we shouldn't include this particular dict, and return None instead.
        # We purposefully return None, because an empty dict is valid config that we could want.
        if not config["present"]:
            return None

    # We can now proceed.
    # We loop through the given config dict and construct a corresponding output dict.
    # We either recursively run over nested dicts, or write corresponding key/value pairs
    # in the output dict.
    updated_config = {}
    for key, value in config.items():
        if isinstance(value, dict):
            # If value is a dict, then we want to remove any "present: false" elements.
            value = clean_config(value)
            # If the returned value is None, then the original dict contained the "present: false"
            # flag, and so shouldn't be included in the output.
            if value is not None:
                updated_config[key] = value

        else:
            # The value isn't a dict, so we put into the output dict unaltered.
            updated_config[key] = value

    # Finally, we can return the updated config that we have constructed.
    return updated_config


# Let's test this function.
cleaned_config = clean_config(config_example)

# Use the json module to produce strings that we can compare.
# This is a "trick" to compare two dictionaries, which can be a difficult thing to do in Python.
import json
cleaned_config_str = json.dumps(cleaned_config, indent=4, sort_keys=True)
expected_config_str = json.dumps(expected_config, indent=4, sort_keys=True)

if cleaned_config_str == expected_config_str:
    print("The two dicts are equal")
else:
    print("The two dicts are different")
