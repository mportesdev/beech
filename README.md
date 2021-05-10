Directory tree listing, without files.

With default settings:

```python
from beech import tree

tree('sample_dir')
```

```
sample_dir
 ├─library
 │  ├─dist
 │  ├─src
 │  │  ├─core
 │  │  └─utils
 │  └─tests
 └─web
    ├─app
    │  ├─templates
    │  └─views
    └─static
       └─img
```

Setting wider indentation and thick branches:

```python
from beech import tree

tree('sample_dir', indent=5, thick=True)
```

```
sample_dir
  ┣━━library
  ┃    ┣━━dist
  ┃    ┣━━src
  ┃    ┃    ┣━━core
  ┃    ┃    ┗━━utils
  ┃    ┗━━tests
  ┗━━web
       ┣━━app
       ┃    ┣━━templates
       ┃    ┗━━views
       ┗━━static
            ┗━━img
```

Setting wider indentation and an additional space before the dir name:

```python
from beech import tree

tree('sample_dir', indent=5, add_space=True)
```

```
sample_dir
  ├── library
  │    ├── dist
  │    ├── src
  │    │    ├── core
  │    │    └── utils
  │    └── tests
  └── web
       ├── app
       │    ├── templates
       │    └── views
       └── static
            └── img
```

Not including the root directory in the listing:

```python
from beech import tree

tree('sample_dir', show_root=False)
```

```
library
 ├─dist
 ├─src
 │  ├─core
 │  └─utils
 └─tests
web
 ├─app
 │  ├─templates
 │  └─views
 └─static
    └─img
```
