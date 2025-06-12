* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-CustomProperties.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS custom properties (variables)](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-variables.html)
  * Create USS variables


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-variables.html)
USS custom properties (variables)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-UnityVariables.html)
Introduction to USS built-in variables
# Create USS variables
You can create a USS variable and use it in other USS properties. When you update a USS variable, all of the USS properties that use that variable update. You can also specify default values for USS variables.
## Create and use USS variables
To create a USS variable, prefix its name with a double-hyphen (`--`).
```
--color-1: red;

```

To use a USS variable value in another USS rule, use the `var()` function to call it.
```
var(--color-1);

```

When you update a variable, it updates all the USS properties that use it.
For example, the following USS snippet defines one style rule that declares two color variables, and two style rules that use those variables.
```
:root {
  --color-1: blue;
  --color-2: yellow;
}

.paragraph-regular {
  color: var(--color-1);
  background: var(--color-2);
  padding: 2px;
  }

.paragraph-reverse {
  color: var(--color-2);
  background: var(--color-1);
  padding: 2px;
  }

```

To update the color scheme, you can change the two variable values instead of the four color values.
Variables make it easier to manage styles for complex UI, where multiple rules, sometimes in different style sheets, use the same values.
## Specify default values for USS variables
The `var()` function accepts an optional default value. The UI system uses the default value when it cannot resolve the variable. For example, if you remove a variable from a style sheet but forget to remove a reference to it.
To specify a default value for a variable, add it after the variable value, separated by a comma `,`. 
The following USS snippet calls the `--color-1` variable. If the UI system can’t resolve the variable, it uses the hex value for red (`#FF0000`).
```
var(--color-1, #FF0000);

```

## Differences from CSS variables
Variables work mostly the same way in USS as they do in CSS. For detailed information about CSS variables, see the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties). However, USS doesn’t support some of the functionalites of CSS:
  * USS doesn’t support the `var()` function inside of other functions, such as shown below:

```
  background-color: rgb(var(--red), 0, 0);

```

  * USS doesn’t support mathematical operations on variables.


## Additional resources
  * [Introduction to USS built-in variables](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-UnityVariables.html)
  * [USS built-in variable reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-built-in-variable-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-variables.html)
USS custom properties (variables)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-UnityVariables.html)
Introduction to USS built-in variables
