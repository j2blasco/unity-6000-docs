* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RenderingLayerMaskField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * RenderingLayerMaskField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RepeatButton.html)
RepeatButton
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)
ScrollView
# RenderingLayerMaskField
A RenderingLayerMaskField is an [Editor-only](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-interface-overview.html#enable-editor-extension-authoring-for-ui-documents-uxml) control that lets users select one or more rendering layers from a list of available [HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Rendering-Layers.html) or [URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html) rendering layers defined in [Tags and Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).
## Create a RenderingLayerMaskField
You can create a RenderingLayerMaskField with UXML and C#. The following C# example creates a RenderingLayerMaskField with the default value:
```
using UnityEditor.UIElements;
...
RenderingLayerMaskField myElement = new RenderingLayerMaskField("Label text");
// Sets the default value.
myElement.value = UnityEngine.RenderingLayerMask.defaultRenderingLayerMask;

```

## C# base class and namespace
**C# class** : [`RenderingLayerMaskField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RenderingLayerMaskField.html)  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : [`BaseMaskField_1`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseMaskField_1.html)
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `RenderingLayerMask` | The value associated with the field.  
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
`ussClassName` | `.unity-rendering-layer-mask-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-rendering-layer-mask-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-rendering-layer-mask-field__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-popup-field` | USS class name of elements of this type.  
`textUssClassName` | `.unity-base-popup-field__text` | USS class name of text elements in elements of this type.  
`arrowUssClassName` | `.unity-base-popup-field__arrow` | USS class name of arrow indicators in elements of this type.  
`labelUssClassName` | `.unity-base-popup-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-popup-field__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-field__input` | USS class name of input elements in elements of this type.  
`noLabelVariantUssClassName` | `.unity-base-field--no-label` | USS class name of elements of this type, when there is no label.  
`labelDraggerVariantUssClassName` | `.unity-base-field__label--with-dragger` | USS class name of labels in elements of this type, when there is a dragger attached on them.  
`mixedValueLabelUssClassName` | `.unity-base-field__label--mixed-value` | USS class name of elements that show mixed values  
`alignedFieldUssClassName` | `.unity-base-field__aligned` | USS class name of elements that are aligned in a **inspector** element  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [LayerMaskField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LayerMaskField.html)
  * [RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html)
  * [Rendering layers in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Rendering-Layers.html)
  * [Rendering layers in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RepeatButton.html)
RepeatButton
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)
ScrollView
