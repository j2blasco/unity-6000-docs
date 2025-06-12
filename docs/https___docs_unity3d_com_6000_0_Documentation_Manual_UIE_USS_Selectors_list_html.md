* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-list.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS selectors](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors.html)
  * Selector lists


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-multiple.html)
Multiple selectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-Pseudo-Classes.html)
Pseudo-classes
# Selector lists
A selector list is a comma-separated list of selectors that share the same style rule.
## Syntax
A selector list consists of multiple selectors separated by commas:
```
selector1, selector2 {...}

```

## Example
The following two USS snippets have the same effect.
```
#container2 {
  background-color: pink;
  border-radius: 10px;
}

Button {
  background-color: pink;
  border-radius: 10px;
}

```
```
#container2, Button {
   background-color: pink;
     border-radius: 10px;
 }

```

## Additional resources
  * [Best practices for USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-WritingStyleSheets.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-multiple.html)
Multiple selectors
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-Pseudo-Classes.html)
Pseudo-classes
