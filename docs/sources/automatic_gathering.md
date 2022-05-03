<span style="float:right;">[[source]](https://github.com/JustinGoheenAI/material-sphinx/blob/main/material_sphinx/gathering_members.py#L30)</span>

### get_functions


```python
material_sphinx.get_functions(module, exclude=None, return_strings=True)
```


Get all the functions of a module.

__Arguments__

- __module__: The module to fetch the functions from. If it's a
    string, it should be in the dotted format. `'keras.backend'` for example.
- __exclude__ `Optional[List[str]]`: The names which will be excluded from the returned list. For
    example, `get_functions('keras.backend', exclude=['max'])`.
- __return_strings__ `bool`: If False, the actual functions will be returned. Note that
    if you use aliases when building your docs, you should use strings.
    This is because the computed signature uses
    `__name__` and `__module__` if you don't provide a string as input.

__Returns__

A list of strings or a list of functions.


----

<span style="float:right;">[[source]](https://github.com/JustinGoheenAI/material-sphinx/blob/main/material_sphinx/gathering_members.py#L7)</span>

### get_classes


```python
material_sphinx.get_classes(module, exclude=None, return_strings=True)
```


Get all the classes of a module.

__Arguments__

- __module__: The module to fetch the classes from. If it's a
    string, it should be in the dotted format. `'keras.layers'` for example.
- __exclude__ `Optional[List[str]]`: The names which will be excluded from the returned list. For
    example, `get_classes('keras.layers', exclude=['Dense', 'Conv2D'])`.
- __return_strings__ `bool`: If False, the actual classes will be returned. Note that
    if you use aliases when building your docs, you should use strings.
    This is because the computed signature uses
    `__name__` and `__module__` if you don't provide a string as input.

__Returns__

A list of strings or a list of classes.


----

<span style="float:right;">[[source]](https://github.com/JustinGoheenAI/material-sphinx/blob/main/material_sphinx/gathering_members.py#L53)</span>

### get_methods


```python
material_sphinx.get_methods(cls, exclude=None, return_strings=True)
```


Get all the method of a class.

__Arguments__

- __cls__: The class to fetch the methods from. If it's a
    string, it should be in the dotted format. `'keras.layers.Dense'`
    for example.
- __exclude__: The names which will be excluded from the returned list. For
    example, `get_methods('keras.Model', exclude=['save'])`.
- __return_strings__: If False, the actual methods will be returned. Note that
    if you use aliases when building your docs, you should use strings.
    This is because the computed signature uses
    `__name__` and `__module__` if you don't provide a string as input.

__Returns__

A list of strings or a list of methods.


----

