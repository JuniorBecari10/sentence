# Sentence

A simple program that transforms a given sentence into another, based on a map. <br />
For example, it transforms `5percent and sum` into `5% & ∑`.

It's useful where you want to reduce a sentence in size, but want to keep its meaning. <br />
**Sentence** is very flexible, you can read either from _stdin_ or from a file, and create your own map!

Here is the table of options:

Argument|Description|Default value
---|---|---
`-i`|The input file.|_stdin_
`-m`|The map file.|The default map built inside the program.

## Examples

Reading from _stdin_ using the default map:
```
./sentence
```

Reading from `file.txt`, using the default map:
```
./sentence -i file.txt
```

Reading from `file.txt`, using a custom map:
```
./sentence -i file.txt -m map.txt
```

## Using a custom map

Creating a map is very simple, just create a new file using these rules:
```
text replace
```

Where `text` is the text to be found in the given sentence, and `replace` is the one that will replace it.

So, a map like this:
```
one 1
and &
two 2
```

With an input like this:
```
one and two
```

Will result in:
```
1 & 2
```

