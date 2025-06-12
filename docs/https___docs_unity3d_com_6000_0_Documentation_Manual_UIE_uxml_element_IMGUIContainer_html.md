* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IMGUIContainer.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * IMGUIContainer


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-HelpBox.html)
HelpBox
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html)
Image
# IMGUIContainer
The IMGUIContainer element renders [IMGUI](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html) code in a UI. You can use it to render complex UIs that aren’t possible with the existing UI Toolkit elements.
## Create an IMGUIContainer
You can create an IMGUIContainer with UXML or C#. 
Assume you have an IMGUI code snippet like the following:
```
void IMGUICode()
{
    GUILayout.BeginArea(new Rect(0, 0, 100, 100));
    GUILayout.Button("Hello World");
    GUILayout.EndArea();
}

```

You can create an IMGUIContainer with the following:
**UXML**
```
<IMGUIContainer onGUIHandler="IMGUICode" />

```

**C#**
```
var imguiContainer = new IMGUIContainer(IMGUICode);

```

## C# base class and namespace
**C# class** : [`IMGUIContainer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMGUIContainer.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
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
`ussClassName` | `.unity-imgui-container` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [VisualElement](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-VisualElement.html)
  * [Immediate Mode GUI (IMGUI)](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-HelpBox.html)
HelpBox
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Image.html)
Image
