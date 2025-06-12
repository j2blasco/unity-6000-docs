* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-WritingStyleSheets.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * Best practices for USS


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html)
Apply styles in C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-tss.html)
Theme Style Sheet (TSS)
# Best practices for USS
Follow these best practices when you write USS to style **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement).
## Avoid inline styles
Use USS files instead of inline styles when you can for more efficient memory usage.
Inline styles are per element and can cause memory overhead. When you use inline styles in a C# script or a UXML file on many elements, the memory usage becomes high quickly.
## Selector architecture consideration
All USS selectors are applied at runtime so the architecture affects initialization performance. USS selectors are applied when an element first appears or when its classes change:
  * The `:hover` selector is the main culprit for selectors to cause interactivity issues and a re-styling.
  * The performance impact appears under the **Update Styling** in the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler).


Usually, it’s not a problem if you have a lot of selectors because each USS file is turned into a lookup table. However, the performance decreases linearly as you add classes to an element. Each class in the list is used to query the lookup table. The complexity is `N1 x N2`, where:
  * `N1` is the number of class on the element
  * `N2` is the current number of applicable USS files


The number of elements in the hierarchy is the main fact that affects performance. **Update Styling** might be negligible for simple UIs but is significant for large UIs that have several thousands of elements. If an element matches a lot of selectors, it causes overhead to merge the styles coming from each rule.
## Complex selectors hierarchy guidelines
In general, complex selectors have more impact on performance than simple selectors. Complex selectors depend on the ancestors of an element to match it. When possible, consider the following:
  * If you want to have partial match, use the [child selector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-child.html) (`selector1 > selector2 > selector3`) instead of the [descendant selector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors-descendant.html) (`selector1 selector2 selector3`).
  * Avoid using universal selector at the end of complex selectors (`selector1 > selector2 > *`) or the combination of descendant selector with the universal selector (`selector1 * selector2`). The universal selector tests every potential element against the selector which can impact performance.
  * Avoid using `:hover` pseudo-class in selectors on elements with many descendants, such as `.yellow:hover > * > Button`. Mouse movements invalidate the entire hierarchy of elements targeted by an `:hover` selector.


## Use BEM to improve performance
You can use the [Block Element Modifier](https://getbem.com/)(BEM) convention to reduce hierarchical selectors. With BEM, each element receives a class that combines its specific existence inside another element.
### About BEM
BEM stands for Block Element Modifier. BEM is a simple system that helps you write structured, non-ambiguous, easy to maintain selectors. With BEM, you assign classes to elements and then use these classes as the selectors in style sheets.
BEM classes have up to three components:
  * Block name: a block is a meaningful, standalone entity or control. For example, `menu`, `button`, `list-view`
  * Element name: a part of a block that has no standalone meaning and is semantically tied to its block. Element names are appended to the block name using two underscores. For example, `menu__item`, `button__icon`, or `list-view__item`
  * Modifier: a flag that changes the appearance or behavior of a block or element. Append a modifier to a block or element name with two dashes. For example, `menu--disabled`, `menu__item--disabled`, `button--small`, or `list-view__item--selected`.


Each name part may consist of Latin letters, digits, and dashes. Each name part is joined together with either a double underscore `__` or a double dash `--`.
The following example shows UXML code for a menu:
```
<VisualElement class="menu">
    <Label class="menu__item" text="Banana" />
    <Label class="menu__item" text="Apple" />
    <Label class="menu__item menu__item--disabled" text="Orange" />
</VisualElement>

```

Each element is equipped with classes that describe its role and appearance, you can write most of your selectors with only one class name:
```
.menu {
}

.menu__item {
}

.menu__item--disabled {
}

```

You can style elements with a single class name. Sometimes, you might need to use complex selectors. For example, you can use a complex selector when the style of an element depends on the modifier of its block:
```
.button {
}

.button__icon {
}

.button--small {
}

.button--small .button__icon {
}

```

**Note** :
  * Avoid specifying long selectors. A long selector could indicate inconsistencies in the graphic design of your UI.
  * Avoid using type names (`Button`, `Label`) or element names (`#my-button`) in your BEM selectors.


### Make visual elements BEM-friendly
UI Toolkit adheres to BEM. Each visual element has the necessary class names attached. For example, all `TextElement` have the `unity-text-element` class. Each instance of `Button`, which derives from `TextElement`, has its class list populated with the `unity-button` and `unity-text-element` classes.
If you derive a new element from `VisualElement` or one of its descendants, following these guidelines to ensure that your element is easy to style using the BEM methodology:
  * Use `AddToClassList()` in the constructor to add the relevant USS classes to your element instances.
  * If your new element instantiates child elements in its constructor, assign the relevant classes to the children. For example, `my-block__first-child`, `my-block__other-child`.
  * If your element supports multiple states or variants, such as small and large, add and remove relevant classes when the element state changes or when the element variant is selected.
  * If you use the element in other projects, consider prefixing your classes to avoid conflicts with existing user class names.


## Additional resources
  * [Introduction to USS](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-about-uss.html)
  * [USS selectors](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Selectors.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-apply-styles-with-csharp.html)
Apply styles in C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-tss.html)
Theme Style Sheet (TSS)
