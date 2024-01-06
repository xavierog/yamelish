# yamelish

yamelish is a non-parsable YAML-ish output format that was designed as a convenience to diff JSON files.

"non-parsable" means that yamelish was not designed to be parsed by computers. It might actually be parsable with some care and caveats (e.g. no way to distinguish boolean/null values from their string counterparts), but this is not the object of this project.

YAML-ish means that it looks like YAML but is not YAML. Specifically, it looks like YAML, without quotes (except for empty strings), indicators like `>` or `|` and advanced features:
```yaml
postId: 1
id: 1
name: id labore ex et quam laborum
email: Eliseo@gardner.biz
body:
  laudantium enim quasi est quidem magnam voluptate ipsam eos
  tempora quo necessitatibus
  dolor quam autem quasi
  reiciendis et nam sapiente accusantium
examples:
  booleans:
    - True
    - False
  null_value: None
  integer: 4
  float: 4.4
  empty_string: ""
  empty_array: []
  empty_object: {}
```

yamelish's main limitation is that it offers no way to distinguish non-string values from their textual representation: the "True" string and the true boolean values will both end up as `True`. Consequently, yamelish remains relevant to spot changing values and structures but not changing types.

## Command-line usage

```console
$ yamelish file1.json file2.json
```

## Git usage

Git configuration (typically `~/.config/git/config`):
```ini
[diff "json_diff"]
    textconv = /path/to/yamelish
; Optional:
[alias]
    showobject = show --ext-diff
```

Repository's `.gitattributes` file:
```gitattributes
*.json diff=json_diff
```

## Python usage

```python
from yamelish.handlers import handle
yamelish = handle(your_data)[0]
print(yamelish)
```

## Why not ... ?

### Why not JSON?

JSON diff is hard to read because of:

- escaped strings:
  - `"this\nis\na\nmultiline\nstring\nand\nthis\nis\npainful"`
  - `"\"wait, what?\""`
- extra commas when appending to an array:

```diff
 {
    "array": [
        "a",
-       "b"
+       "b",
+       "c"
    ]
 }
```

### Why not gron?

Because the gron format reflects array indices, inserting an element into an array makes diff way longer than expected:

```diff
 json = {};
 json.array = [];
-json.array[0] = "a";
-json.array[1] = "b";
+json.array[0] = "z";
+json.array[1] = "a";
+json.array[2] = "b";
```

### Why not YAML?

YAML is better but it still clutters the output with quotes, escaped values and/or little things like `|-`; this is because YAML is a format that is meant to be parsed, so it has to keep this kind of things.


```diff
 array:
 - "# this string is double-quoted because otherwise it would be a YAML comment"
-- "# this string is double-quoted because otherwise it would be a YAML comment"
+- this string is no longer double-quoted
 - "# this string is double-quoted because otherwise it would be a YAML comment"
```

## License

yamelish is licensed under WTFPL.
Copyright (c) 2022-2024 Xavier G.
