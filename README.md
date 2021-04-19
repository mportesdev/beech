Directory tree listing, no files.

Default settings:

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
 │  │  │  └─__pycache__
 │  │  └─utils
 │  │     └─__pycache__
 │  └─tests
 ├─parsers
 │  ├─engine
 │  │  ├─json
 │  │  └─yaml
 │  └─syntax
 │     ├─json
 │     └─yaml
 └─web
    ├─app
    │  ├─templates
    │  └─views
    └─static
       └─img
```

Wider indentation, thick branches:

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
  ┃    ┃    ┃    ┗━━__pycache__
  ┃    ┃    ┗━━utils
  ┃    ┃         ┗━━__pycache__
  ┃    ┗━━tests
  ┣━━parsers
  ┃    ┣━━engine
  ┃    ┃    ┣━━json
  ┃    ┃    ┗━━yaml
  ┃    ┗━━syntax
  ┃         ┣━━json
  ┃         ┗━━yaml
  ┗━━web
       ┣━━app
       ┃    ┣━━templates
       ┃    ┗━━views
       ┗━━static
            ┗━━img
```
