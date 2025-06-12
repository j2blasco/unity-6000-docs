* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TwoPaneSplitView.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * TwoPaneSplitView


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TreeView.html)
TreeView
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-UnsignedLongField.html)
UnsignedLongField
# TwoPaneSplitView
The `TwoPaneSplitView` element is a container that arranges its children in two panes, either horizontally or vertically. The user can resize the panes by dragging the divider between them. A `TwoPaneSplitView` must have exactly two children.
![TwoPaneSplitView example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uxml/TwoPaneSpitView.gif) TwoPaneSplitView example
## Create a TwoPaneSplitView
You can create a TwoPaneSplitView with UXML and C#.
To create a TwoPaneSplitView with C#, create a new instance of a [TwoPaneSplitView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TwoPaneSplitView.html) object. For example:
```
TwoPaneSplitView myElement = new TwoPaneSplitView();

// Add two child elements to the TwoPaneSplitView
VisualElement child1 = new VisualElement();
VisualElement child2 = new VisualElement();
myElement.Add(child1);
myElement.Add(child2);

```

By default, the orientation is horizontal. You can change the orientation with the [orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TwoPaneSplitView-orientation.html) property.
## Examples
The best way to learn how to use TwoPaneSplitView is to try examples:
  * [Create a custom Editor window with C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateEditorWindow.html)
  * [Create a drag-and-drop list and tree views between windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html)


## C# base class and namespace
**C# class** : [`TwoPaneSplitView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TwoPaneSplitView.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`fixed-pane-index` | `int` | 0 for setting first child as the fixed pane, 1 for the second child element.  
`fixed-pane-initial-dimension` | `float` | The initial width or height for the fixed pane.  
`orientation` | [`UIElements.TwoPaneSplitViewOrientation`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TwoPaneSplitViewOrientation.html) | Orientation of the split view.  
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
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TreeView.html)
TreeView
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-UnsignedLongField.html)
UnsignedLongField
