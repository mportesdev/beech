Directory tree listing, without files.

With default settings:

```python
from beech import tree

tree('sample_dir')
```

```
sample_dir
 ├─.hidden
 │  └─.hidden
 ├─app
 │  ├─app
 │  │  └─views
 │  └─static
 │     └─img
 └─library
    ├─.pytest_cache
    ├─src
    │  ├─core
    │  └─utils
    └─tests
```

Setting wider indentation and thick branches:

```python
from beech import tree

tree('sample_dir', indent=4, thick=True)
```

```
sample_dir
  ┣━.hidden
  ┃   ┗━.hidden
  ┣━app
  ┃   ┣━app
  ┃   ┃   ┗━views
  ┃   ┗━static
  ┃       ┗━img
  ┗━library
      ┣━.pytest_cache
      ┣━src
      ┃   ┣━core
      ┃   ┗━utils
      ┗━tests
```

Setting even wider indentation, plus an additional space before the dir name:

```python
from beech import tree

tree('sample_dir', indent=5, add_space=True)
```

```
sample_dir
  ├── .hidden
  │    └── .hidden
  ├── app
  │    ├── app
  │    │    └── views
  │    └── static
  │         └── img
  └── library
       ├── .pytest_cache
       ├── src
       │    ├── core
       │    └── utils
       └── tests
```

Not including the root directory and omitting hidden subdirectories:

```python
from beech import tree

tree('sample_dir', show_root=False, skip_hidden=True)
```

```
app
 ├─app
 │  └─views
 └─static
    └─img
library
 ├─src
 │  ├─core
 │  └─utils
 └─tests
```
