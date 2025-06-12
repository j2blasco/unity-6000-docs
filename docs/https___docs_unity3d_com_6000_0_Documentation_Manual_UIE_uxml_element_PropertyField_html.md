* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-PropertyField.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * PropertyField


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ProgressBar.html)
ProgressBar
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButton.html)
RadioButton
# PropertyField
A PropertyField is a field element specifically designed to be bound to a [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html). Once you bind a property to a PropertyField, a nested [BaseField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html) element is created based on the property type. For example, if you bind an int property to a PropertyField, an [IntegerField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IntegerField.html) is nested inside the PropertyField.
**Note** : It’s recommended to use [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html) for values that are serialized, and [runtime data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html) for other attributes, such as names and style properties.
## Align a PropertyField with other fields in an Inspector window
By default, PropertyFields are created with the `.unity-base-field__aligned` USS class, which is also applied to each nested field that gets created upon binding. However, if you manually add a child BaseField element to a PropertyField, you must add the style class manually to that child field element. When the `.unity-base-field__aligned` class is present in an InspectorElement, the field calculates the label width to align with other fields in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. If there are IMGUI fields present, UI Toolkit fields are aligned with them for consistency and compatibility.
## C# base class and namespace
**C# class** : [`PropertyField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`label` | `string` | Optionally overwrite the label of the generate property field. If no label is provided the string will be taken from the SerializedProperty.  
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
`ussClassName` | `.unity-property-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-property-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-property-field__input` | USS class name of input elements in elements of this type.  
`inspectorElementUssClassName` | `.unity-property-field__inspector-property` | USS class name of property fields in inspector elements  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [Create a custom inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateCustomInspector.html)
  * [TextField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html)
  * [DoubleField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-DoubleField.html)
  * [LongField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LongField.html)
  * [FloatField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-FloatField.html)
  * [IntegerField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-IntegerField.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ProgressBar.html)
ProgressBar
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-RadioButton.html)
RadioButton
