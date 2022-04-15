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

tree('sample_dir', indent=5, thick=True)
```

```
sample_dir
  ┣━━.hidden
  ┃    ┗━━.hidden
  ┣━━app
  ┃    ┣━━app
  ┃    ┃    ┗━━views
  ┃    ┗━━static
  ┃         ┗━━img
  ┗━━library
       ┣━━.pytest_cache
       ┣━━src
       ┃    ┣━━core
       ┃    ┗━━utils
       ┗━━tests
```

Setting wider indentation and an additional space before the dir name:

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

Not including the root directory in the listing:

```python
from beech import tree

tree('sample_dir', show_root=False)
```

```
.hidden
 └─.hidden
app
 ├─app
 │  └─views
 └─static
    └─img
library
 ├─.pytest_cache
 ├─src
 │  ├─core
 │  └─utils
 └─tests
```
