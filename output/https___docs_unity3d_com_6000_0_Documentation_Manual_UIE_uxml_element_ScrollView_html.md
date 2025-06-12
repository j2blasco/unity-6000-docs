* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * ScrollView


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RenderingLayerMaskField.html)
RenderingLayerMaskField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Scroller.html)
Scroller
# ScrollView
ScrollView displays its content inside a scrollable area. When you add content to a **ScrollView** , the content is added to the content container (`#unity-content-container`) of the ScrollView.
## Create a ScrollView
You can create a ScrollView with UI Builder, UXML, or C#. The following C# example creates a ScrollView with both horizontal and vertical scroll capabilities, that contains a title Label, and a number of Toggle elements:
```
var scrollView = new ScrollView(ScrollViewMode.VerticalAndHorizontal);
scrollView.style.width = 250;
scrollView.style.height = 400;

scrollView.Add(new Label("List of checkboxes:"));

for (int i = 0; i < 100; ++i)
{
    var toggle = new UnityEngine.UIElements.Toggle()
    { text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." };
    scrollView.Add(toggle);
}

```

## Manage the scroll bar visibility
You can specify the scroll mode of the scroll bar movement, whether the horizontal or vertical scroll bars are visible, and control the speed of the scroll bars.
To set the scroll mode of the scroll bar movement in UI Builder, in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window of the ScrollView, select one of the following options for **Mode** :
  * Vertical (default)
  * Horizontal
  * Vertical and Horizontal


To set the visibility of the scroll bar in UI Builder, in the Inspector window of the ScrollView, select one of the following options for **Horizontal Scroller Visibility** or **Vertical Scroller Visibility** :
  * Auto (default)
  * Always Visible
  * Hidden


## Control the scroll speed
To control the scroll speed, adjust the values of the following properties in UI Builder, UXML, or C# code. The higher the value, the faster the scrolling speed.
  * `horizontal-page-size` controls the speed of horizontal scrolling when using a keyboard or the on-screen scrollbar buttons (arrows and handle). The speed is calculated by multiplying the page size by the specified value. For example, a value of `2` means that each scroll movement covers a distance equal to twice the width of the page.
  * `vertical-page-size` controls the speed of vertical scrolling when using a keyboard or the on-screen scrollbar buttons (arrows and handle). The speed is calculated by multiplying the page size by the specified value. For example, a value of `2` means that each scroll movement covers a distance equal to twice the length of the page.
  * `mouse-wheel-scroll-size` controls the speed of scrolling when using the mouse wheel. The speed is calculated by dividing the specified value by `18`, which corresponds to the default line height of `18px`. For example, if you set the value to `36`, each scroll movement covers a distance equivalent to two lines of content.


**Note** : You can also override the [USS built-in variable](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uss-built-in-variable-reference.html) `–unity-metrics-single_line-height` to control the speed of scrolling when using the mouse wheel. The `mouse-wheel-scroll-size` attribute takes precedence over the `–unity-metrics-single_line-height` USS variable.
## Wrap elements inside ScrollView
You can wrap **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) inside a ScrollView so that the elements display in a row. If the row is full, the elements continue to display on the next line.
To wrap visual elements inside a ScrollView, set the ScrollView’s content container `flex-direction` to `row` and `flex-wrap` to `wrap`.
**In USS** :
```
.unity-scroll-view__content-container {
    flex-direction: row;
    flex-wrap: wrap;
}

```

**In C#** :
```
scrollview.contentContainer.style.flexDirection = FlexDirection.Row;
scrollview.contentContainer.style.flexWrap = Wrap.Wrap;

```

## Wrap text of elements inside ScrollView
To wrap the text of an element inside a ScrollView, for example, the text of a Label element, do the following:
  1. Style the Label element with any of the following methods: 
     * In UI Builder, in the Inspector window of the Label, select **Text** > **Wrap** > **normal**.
     * Apply style `white-space: normal;` to the Label element in USS, UXML, or C#.
  2. Create a VisualElement as a container inside the ScrollView. The original container element inside the ScrollView does not have bounds set (is infinite in size), so text won’t properly wrap. This container VisualElement provides the finite size for text to wrap within.
  3. Add the Label to the VisualElement container.


## Examples
  * [Wrap content inside a ScrollView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-wrap-content-inside-scrollview.html): This example demonstrates how to use styles to wrap content inside a scroll view.


## C# class and namespace
**C# class** : [`ScrollView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`elastic-animation-interval-ms` | `long` | The minimum amount of time, in milliseconds, between executions of elastic spring animation.  
`elasticity` | `float` | The amount of elasticity to use when a user tries to scroll past the boundaries of the scroll view.  
  
Elasticity is only used when `touchScrollBehavior` is set to Elastic.  
`horizontal-page-size` | `float` | This property controls the speed of the horizontal scrolling when using a keyboard or the on-screen scrollbar buttons (arrows and handle), based on the size of the page.  
  
When scrolling the page size will be applied to the offset for each scroll step, so the final offset will be the page size multiplied by the number of steps. SA: BaseSlider_1::ref::pageSize.  
`horizontal-scroller-visibility` | [`UIElements.ScrollerVisibility`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.html) | Specifies whether the horizontal scroll bar is visible.  
`mode` | [`UIElements.ScrollViewMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollViewMode.html) | Controls how the ScrollView allows the user to scroll the contents. `ScrollViewMode` The default is `ScrollViewMode.Vertical`. Writing to this property modifies the class list of the ScrollView according to the specified value of `ScrollViewMode`. When the value changes, the class list matching the old value is removed and the class list matching the new value is added.  
`mouse-wheel-scroll-size` | `float` | This property controls the scrolling speed only when using a mouse scroll wheel, based on the size of the page. It takes precedence over the –unity-metrics-single_line-height USS variable.  
`nested-interaction-kind` | [`UIElements.ScrollView+NestedInteractionKind`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView+NestedInteractionKind.html) | The behavior to use when scrolling reaches limits of a nested `ScrollView`.  
`scroll-deceleration-rate` | `float` | Controls the rate at which the scrolling movement slows after a user scrolls using a touch interaction.  
  
The deceleration rate is the speed reduction per second. A value of 0.5 halves the speed each second. A value of 0 stops the scrolling immediately.  
`vertical-page-size` | `float` | This property controls the speed of the vertical scrolling when using a keyboard or the on-screen scrollbar buttons (arrows and handle), based on the size of the page.  
  
The speed is calculated by multiplying the page size by the specified value. For example, a value of `2` means that each scroll movement covers a distance equal to twice the width of the page.  
`vertical-scroller-visibility` | [`UIElements.ScrollerVisibility`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.html) | Specifies whether the vertical scroll bar is visible.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
This element also inherits the following attributes from [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-VisualElement.html):
**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`data-source` | `Object` | Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.  
`data-source-path` | `string` | Path from the data source to the value.  
`data-source-type` | `System.Type` | The possible type of data source assignable to this VisualElement.  
  
This information is only used by the UI Builder as a hint to provide some completion to the data source path field when the effective data source cannot be specified at design time.  
`language-direction` | [`UIElements.LanguageDirection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LanguageDirection.html) | Indicates the directionality of the element’s text. The value will propagate to the element’s children.  
  
Setting the languageDirection to RTL adds basic support for right-to-left (RTL) by reversing the text and handling linebreaking and word wrapping appropriately. However, it does not provide comprehensive RTL support, as this would require text shaping, which includes the reordering of characters, and OpenType font feature support. Comprehensive RTL support is planned for future updates, which will involve additional APIs to handle language, script, and font feature specifications.  
  
To enhance the RTL functionality of this property, users can explore available third-party plugins in the Unity Asset Store and make use of `ITextElementExperimentalFeatures.renderedText`  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | [`UIElements.PickingMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.html) | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Sets the `VisualElement` style values.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | [`UIElements.UsageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html) | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence, such as tree expanded states, scroll position, or zoom level.  
  
This key is used to save and load the view data from the view data store. If you don’t set this key, the persistence is disabled for the associated `VisualElement`. For more information, refer to [View data persistence](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ViewData.html).  
## USS classes
The following table lists all the C# public property names and their related USS selector.
**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-scroll-view` | USS class name of elements of this type.  
`viewportUssClassName` | `.unity-scroll-view__content-viewport` | USS class name of **viewport** elements in elements of this type.  
`horizontalVariantViewportUssClassName` | `.unity-scroll-view__content-viewport--horizontal` | USS class name that’s added when the Viewport is in horizontal mode. `ScrollViewMode.Horizontal`  
`verticalVariantViewportUssClassName` | `.unity-scroll-view__content-viewport--vertical` | USS class name that’s added when the Viewport is in vertical mode. `ScrollViewMode.Vertical`  
`verticalHorizontalVariantViewportUssClassName` | `.unity-scroll-view__content-viewport--vertical-horizontal` | USS class name that’s added when the Viewport is in both horizontal and vertical mode. `ScrollViewMode.VerticalAndHorizontal`  
`contentAndVerticalScrollUssClassName` | `.unity-scroll-view__content-and-vertical-scroll-container` | USS class name of content elements in elements of this type.  
`contentUssClassName` | `.unity-scroll-view__content-container` | USS class name of content elements in elements of this type.  
`horizontalVariantContentUssClassName` | `.unity-scroll-view__content-container--horizontal` | USS class name that’s added when the ContentContainer is in horizontal mode. `ScrollViewMode.Horizontal`  
`verticalVariantContentUssClassName` | `.unity-scroll-view__content-container--vertical` | USS class name that’s added when the ContentContainer is in vertical mode. `ScrollViewMode.Vertical`  
`verticalHorizontalVariantContentUssClassName` | `.unity-scroll-view__content-container--vertical-horizontal` | USS class name that’s added when the ContentContainer is in both horizontal and vertical mode. `ScrollViewMode.VerticalAndHorizontal`  
`hScrollerUssClassName` | `.unity-scroll-view__horizontal-scroller` | USS class name of horizontal scrollers in elements of this type.  
`vScrollerUssClassName` | `.unity-scroll-view__vertical-scroller` | USS class name of vertical scrollers in elements of this type.  
`horizontalVariantUssClassName` | `.unity-scroll-view--horizontal` | USS class name that’s added when the ScrollView is in horizontal mode. `ScrollViewMode.Horizontal`  
`verticalVariantUssClassName` | `.unity-scroll-view--vertical` | USS class name that’s added when the ScrollView is in vertical mode. `ScrollViewMode.Vertical`  
`verticalHorizontalVariantUssClassName` | `.unity-scroll-view--vertical-horizontal` | USS class name that’s added when the ScrollView is in both horizontal and vertical mode. `ScrollViewMode.VerticalAndHorizontal`  
`scrollVariantUssClassName` | `.unity-scroll-view--scroll` | USS class name that’s added when the ScrollView is in scroll mode.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html)
  * [Scroller](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Scroller.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RenderingLayerMaskField.html)
RenderingLayerMaskField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Scroller.html)
Scroller
