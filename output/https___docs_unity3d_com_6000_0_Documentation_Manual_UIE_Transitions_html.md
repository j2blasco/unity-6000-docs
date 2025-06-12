* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitions.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Style UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [USS properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-properties.html)
  * USS transition


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html)
USS transform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html)
USS properties reference
# USS transition
USS transitions are similar to [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions). A USS transition changes property values over a given duration. You can use a USS transition to create an animation that changes the appearance of a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). For example, you can use a UI transition to make UI elements that change size or color when a user hovers their cursor over them. 
You can use the controls in the [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html), a [USS file](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html), or a C# script to set the transition properties for a visual element.
The following table lists the transition properties and their corresponding C# methods:
**Property** | **C# method** | **Description**  
---|---|---  
`transition-property` | [`IStyle.transitionProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionProperty.html) | Which USS properties the transition applies to.  
`transition-duration` | [`IStyle.transitionDuration`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionDuration.html) | How long the transition takes to complete.  
`transition-timing-function` | [`IStyle.transitionTimingFunction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionTimingFunction.html) | How the property moves between values over time.  
`transition-delay` | [`IStyle.transitionDelay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionDelay.html) | When the transition starts.  
`transition` |  | Shorthand for `transition-property`, `transition-duration`, `transition-timing-function`, and `transition-delay`.  
## Starting of a transition
A transition triggers if you set a transition duration on the style and the style value changes. You can use pseudo-classes, C# methods, or events to trigger the transition. 
**Note** : A transition animation on a frame is triggered when the property’s current state is different from the previous state. The first frame in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) has no previous state. You must start a transition animation after the first frame.
The following transition example changes the color and rotation of the label when you hover over it. The transition has a duration of 2 seconds.
![A transition example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/transition-gif.gif) A transition example
To implement this example, do the following:
  1. Set the transition properties for the visual element.
  2. Set the transition duration.
  3. Set the start and end style values.


The example USS looks like this:
```
/* Set the transition properties, duration, and start style values. */
.labelClass {
    transition-property: color, rotate;
    transition-duration: 2s;
    color: black;
}

/* The Label:hover triggers the transition. Set the end values for the trigger. */
.labelClass:hover {
    rotate: 10deg;
    color: red;
} 

```

**Note** : The example sets the transition on the element rather than the `:hover`. If you set the transition on the `:hover`, the transition doesn’t work if the cursor leaves the element.
To learn how to trigger a transition with C# events, refer to [Create a simple transition with UI Builder and C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-transition-example.html).
### Match the value units
For properties that you set with a value and unit, make sure the units match. Pay special attention to transitions to or from default values. For example, the default value of the `translate` attribute is `0px`. If you try to transition from this value to a percentage value, the transition doesn’t work. 
The following transition example offsets the visual element to the left by `50px` over 2 seconds. The default value of the `left` property is `auto`. You must explicitly set the unit to `0px` for the transition to work.
![An offset to left transition example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/transition-offset-left.gif) An offset to left transition example
The example USS looks like this:
```
.boxClass:hover {
    left: 50px;
}

.boxClass {
    transition-property: left;
    transition-duration: 2s;
    transition-timing-function: ease-in-out-sine;
    left: 0px;
}

```

### Transitions for an inherited property
For visual elements in a hierarchy, USS transitions behave the same as [CSS transitions](https://drafts.csswg.org/css-transitions/#starting). If you set transitions for an inherited property, such as `color`, transitions applied to the parent elements cascade to the child elements. To find out which property is inherited, refer to [USS property reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html).
### Interrupt transitions
When an incomplete transition is `interruptedSame`, USS transitions behave the same as CSS transitions. The reverse transition might be faster. For more information, refer to [Faster reversing of interrupted transitions](https://drafts.csswg.org/css-transitions/#reversing)
### Transition events
[Transition events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transition-Events.html) are generated by transitions. You can use them to detect when a transition starts and ends. For an example, refer to [Create a transition event](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-transition-event-example.html).
### Usage hints
The **Usage Hints** offers a set of [properties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html) for optimizations. You can use it to reduce draw calls and geometry regeneration.
**Note** : Set the usage hints at edit time or before you add the element to a panel. When the transition starts, the system might automatically add missing relevant usage hints to avoid regenerating geometry in every frame. However, this causes a one-frame performance penalty because the rendering data for the VisualElement and its descendants is regenerated.
## Transition controls in the UI Builder
You can use the controls in the **Transition Animations** section of the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** in the UI Builder to set transition rules for a visual element. You can set multiple transitions on a visual element. To add another transition, select **Add Transition**. To remove a transition, select the **Remove (−)** button.
![This transition causes a visual element to adjust its scale over 500 milliseconds in a linear fashion after a delay of 20 milliseconds.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIBuilder/example-transition.png) This transition causes a visual element to adjust its scale over 500 milliseconds in a linear fashion after a delay of 20 milliseconds.
## Transition property
The transition property defines which USS properties the transition applies to. 
### Keywords
The transition property supports the following keywords:
  * `all`: Applies transitions to all properties and overrides any preceding transitions. This is the default value.
  * `initial`: Applies transitions to all properties.
  * `none`: Ignores transitions for all properties.
  * `ignored`: Ignores transitions for the specified duration, delay, and easing function.


### Animatability
You can apply transitions to most USS properties. However, the animatability for certain properties is different. The animatability of USS properties falls into the following categories:
  * **Fully animatable** : Supports transition from the start value to the end value, at a speed that follows the easing function and transition duration.
  * **Discrete** : Supports transition between values in a single step from the start value to the end value.
  * **Non-animatable** : Doesn’t support transition.


To find out the animatability of each property, see [USS property reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html).
**Note** : It’s recommended that you use transitions with the [USS transform properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html). Although you can use transitions on other USS properties, it might result in animations with low frame rates because value changes on these properties might cause layout recalculations. Layout recalculations in each frame can slow down the frame rate of your transition animation. All color properties, such as `color`, `background-color`, tint, and `opacity`, also have a fast pass that prevents the regeneration of the geometry.
### USS examples
You can supply a single USS property, a keyword, or a comma-separated list of them to `transition-property`.
```
transition-property: scale;
transition-property: translate, all, rotate;
transition-property: initial;
transition-property: none;

```

### C# examples
The [`IStyle.transitionProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionProperty.html) property is of type `StyleList<StylePropertyName>`. [`StylePropertyName`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StylePropertyName.html) is a struct that you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StylePropertyName-ctor.html) from a string. [`StyleList`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1.html) is a struct you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1-ctor.html) from a list of `StylePropertyName`.
```
//Create a list that contains the rotate property, and use it to set transitionProperty.
List<StylePropertyName> properties = new List<StylePropertyName>();
properties.Add(new StylePropertyName("rotate"));
//Given a VisualElement named "element"...
element.style.transitionProperty = new StyleList<StylePropertyName>(properties);

```

You can use implicit conversions to simplify the above code as follows:
```
//Given a VisualElement named "element"...
element.style.transitionProperty = new List<StylePropertyName> { "rotate" };

```

## Transition duration
The transition duration sets how long the transition takes to complete.
### Keywords
The transition duration supports the following keywords:
  * `initial`: Sets the duration to `0s`. This is the default value.


### USS examples
You can supply a number with a unit, a keyword, or a comma-separated list of numbers and units to `transition-duration`.
```
transition-duration: 2s;
transition-duration: 800ms;
transition-duration: 3s, 1500ms, 1.75s;
transition-duration: initial;

```

If you supply multiple values, each value applies to the corresponding property specified in `transition-property`. In the following example, the original duration for scale is `1s`, but `all` overrides it to `2s`.
```
transition-property: scale, all, rotate;
transition-duration: 1s, 2s, 3s;

```

### C# examples
The [`IStyle.transitionDuration`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionDuration.html) property is of type `StyleList<TimeValue>`. [`TimeValue`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeValue.html) is a struct that you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeValue-ctor.html) from a number and a [`TimeUnit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeUnit.html) enum. [`StyleList`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1.html) is a struct you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1-ctor.html) from a list of `TimeValue`.
```
//Create a list that contains durations 2s and 500ms and use it to set transitionDuration.
List<TimeValue> durations = new List<TimeValue>();
durations.Add(new TimeValue(2f, TimeUnit.Second));
durations.Add(new TimeValue(500f, TimeUnit.Millisecond));
//Given a VisualElement named "element"...
element.style.transitionDuration = new StyleList<TimeValue>(durations);

```

You can use implicit conversions to simplify the above code as follows:
```
//Given a VisualElement named "element"...
element.style.transitionDuration = new List<TimeValue> { 2, new (500, TimeUnit.Millisecond) };

```

## Transition timing function
The transition timing function sets how the property moves between values over time. 
### Keywords
The transition timing function supports the following keywords. The default value is `initial`, which sets the easing function to `ease`.
  * `initial`
  * `ease`
  * `ease-in`
  * `ease-out`
  * `ease-in-out`
  * `linear`
  * `ease-in-sine`
  * `ease-out-sine`
  * `ease-in-out-sine`
  * `ease-in-cubic`
  * `ease-out-cubic`
  * `ease-in-out-cubic`
  * `ease-in-circ`
  * `ease-out-circ`
  * `ease-in-out-circ`
  * `ease-in-elastic`
  * `ease-out-elastic`
  * `ease-in-out-elastic`
  * `ease-in-back`
  * `ease-out-back`
  * `ease-in-out-back`
  * `ease-in-bounce`
  * `ease-out-bounce`
  * `ease-in-out-bounce`


For detailed information about each function, refer to [MDN’s documentation for the `transition-timing-function` CSS attribute](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function) or [easings.net](https://easings.net/).
### USS examples
You can supply an easing function, a keyword, or a comma-separated list of easing functions to `transition-timing-function`.
```
transition-timing-function: linear;
transition-timing-function: ease-in, ease-out-circ, ease-in-out-cubic;
transition-timing-function: initial;

```

### C# examples
The [`IStyle.transitionTimingFunction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionTimingFunction.html) property is of type `StyleList<EasingFunction>`. [`EasingFunction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EasingFunction.html) is a struct that you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EasingFunction-ctor.html) from an [`EasingMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EasingMode.html) enum.
```
//Create a list that contains the Linear easing function, and use it to set transitionTimingFunction.
List<EasingFunction> easingFunctions = new List<EasingFunction>();
easingFunctions.Add(new EasingFunction(EasingMode.Linear));
//Given a VisualElement named "element"...
element.style.transitionTimingFunction = new StyleList<EasingFunction>(easingFunctions);

```

You can use implicit conversions to simplify the above code as follows:
```
//Given a VisualElement named "element"...
element.style.transitionTimingFunction = new List<EasingFunction> { EasingMode.Linear };

```

## Transition delay
The transition delay sets when the transition starts. 
### Keywords
The transition delay supports the following keywords:
  * `initial`: Sets the delay to `0s`. This is the default value.


### USS examples
You can supply a number with a unit, a keyword, or a comma-separated list of numbers and units to `transition-delay`.
```
transition-delay: 0s;
transition-delay: 300ms;
transition-delay: 2s, 650ms, 2.75s;
transition-delay: initial;

```

### C# examples
The [`IStyle.transitionDelay`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-transitionDelay.html) property is of type `StyleList<TimeValue>`. [`TimeValue`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeValue.html) is a struct that you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeValue-ctor.html) from a number and a [`TimeUnit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeUnit.html) enum. [`StyleList`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1.html) is a struct you can [construct](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1-ctor.html) from a list of `TimeValue`.
```
//Create a list that contains delays 0.5s and 200ms, and use it to set transitionDelay.
List<TimeValue> delays = new List<TimeValue>();
delays.Add(new TimeValue(0.5f, TimeUnit.Second));
delays.Add(new TimeValue(200f, TimeUnit.Millisecond));
//Given a VisualElement named "element"...
element.style.transitionDelay = new StyleList<TimeValue>(delays);

```

You can use implicit conversions to simplify the above code as follows:
```
//Given a VisualElement named "element"...
element.style.transitionDelay = new List<TimeValue> { 0.5f, new(200, TimeUnit.Millisecond) };

```

## USS `transition`
You can supply one transition, a keyword, or a comma-separated list of transitions to `transition`. You separate properties within a transition by a space in the following order:
  1. `transition-property`
  2. `transition-delay`
  3. `transition-duration`
  4. `transition-timing-function`


### Keywords
`transition` only supports the keyword `initial`, which represents the initial value of each transition property:
  * `transition-delay`: `0s`
  * `transition-duration`: `0s`
  * `transition-property`: `all`
  * `transition-timing-function`: `ease`


### USS examples
```
/*One transition*/
transition: width 2s ease-out;

/*Two transitions*/
transition: margin-right 4s, color 1s;

```

## Transition on multiple property examples
This section includes examples that apply transitions on multiple properties. 
### Example 1
This example applies transitions on the `scale` and `transform-origin` properties:
  * The first transition is on the `scale` property. It has a duration of `4s`, a delay of `0s`, and the `ease-in-sine` easing function.
  * The second transition is on the `transform-origin` property. It has a duration of `3s`, a delay of `600ms`, and the `ease-out-elastic` easing function.

```
.classA {
    transition-property: scale, transform-origin;
    transition-duration: 4s, 3s;
    transition-delay: 0s, 600ms;
    transition-timing-function: ease-in-sine, ease-out-elastic;
}

```

### Example 2
In this example, the later transitions override earlier transitions, including transitions with the `all` keyword:
  * The first transition is on all properties. It applies a duration of 500 milliseconds, a delay of zero seconds, and the `linear` easing function.
  * The second transition is on the `translate` property. It overrides the transition with a duration of `1s`, a delay of `1s`, and the `ease-in` easing function. All other properties still have a duration of `500ms`, a delay of `0s`, and the `linear` easing function.

```
.classB {
    transition-property: all, translate;
    transition-duration: 500ms, 1s;
    transition-delay: 0s, 1s;
    transition-timing-function: linear, ease-in;
}

```

### Example 3
This example shows what happens when property value lists are of different lengths. If any property’s list of values is shorter than that for `transition-property`, Unity repeats its values to make them match. Similarly, if any property’s value list is longer than `transition-property`, Unity truncates it. 
```
.classC {
    transition-property: scale, rotate, translate;
    transition-duration: 1s, 2s;
    transition-delay: 1s, 2s, 3s, 4s, 5s, 6s, 7s;
}

```

The following table shows the final results for the example above:
**Property** | **Duration** | **Delay** | **Easing function**  
---|---|---|---  
`scale` | `1s` | `1s` | `ease`  
`rotate` | `2s` | `2s` | `ease`  
`translate` | `1s` | `3s` | `ease`  
**Important** : `transition-property`, `transition-duration`, `transition-delay`, and `transition-timing-function` are separate USS properties. If you leave any of them undefined, it’s possible that they are defined elsewhere, such as in another USS rule or inline on the UXML element. 
## Additional resources
  * [Use usage hints to reduce draw calls and geometry regeneration](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-performance-consideration-runtime.html)
  * [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)(Mozilla developer documentation)
  * [CSS transition](https://developer.mozilla.org/en-US/docs/Web/CSS/transition) (Mozilla developer documentation)
  * [CSS transition-property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property) (Mozilla developer documentation)
  * [CSS transition-duration property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration) (Mozilla developer documentation)
  * [CSS transition-timing-function property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function) (Mozilla developer documentation)
  * [CSS transition-delay property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay) (Mozilla developer documentation)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html)
USS transform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS-Properties-Reference.html)
USS properties reference
