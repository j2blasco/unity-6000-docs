* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-data-binding.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
  * Introduction to SerializedObject data binding


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
SerializedObject data binding
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
Bindable elements reference
# Introduction to SerializedObject data binding
You can use the SerializedObject data binding system to bind to [serialized properties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html). This means you can bind **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) to the following objects that are compatible with the [Serialization system](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html):
  * User-defined [`ScriptableObject`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) classes
  * User-defined [`MonoBehaviour`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) classes
  * Native Unity component types
  * Native Unity asset types
  * Primitive C# types such as `int`, `bool`, or `float`.
  * Native Unity types such as `Vector3`, `Color`, or `Object`.


## Value binding
You can only bind the `value` property of visual elements that implement the [`INotifyValueChanged`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyValueChanged_1.html) interface. For example, you can bind [`TextField.value`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField-value.html) to a `string`, but you can’t bind [`TextField.name`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-name.html) to a `string`. 
You can bind between an object and any visual element that either derives from [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html) or implements the [`IBindable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable.html) interface.
## Create a binding
To create a binding, either [call `Bind()`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html#call-bind) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html#call-bindproperty).
### Call `Bind()`
You can call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) to bind an element to a [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html). Before you bind an element, you must [set the binding path](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html#set-binding-path) and create a SerializedObject. 
Use this method if you don’t have easy access to the `SerializedProperty` for the binding. Refer to [Create a binding with a C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-csharp.html) for an example.
The [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) extension method sets up an entire hierarchy of visual elements with specified [`bindingPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable-bindingPath.html) properties. You can call the [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) method on a single element or the parent of the hierarchy that you want to bind. For example, you can call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) on the `rootVisualElement` of an Editor window. This binds all child elements with specified [`bindingPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable-bindingPath.html) properties.
Don’t call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) from the `Editor.CreateInspectorGUI()` or `PropertyDrawer.CreatePropertyGUI()` override. These overrides are called automatically on the visual elements that these methods return.
### Call `Unbind()`
The [`Unbind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Unbind.html) method stops the value tracking for the element and all its direct and indirect child elements. In general, you don’t need to call [`Unbind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Unbind.html) because tracking stops when a user closes the Inspector or Editor window. Call [`Unbind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Unbind.html) if you must bind elements to different targets in their lifetimes. 
If you construct an [`InspectorElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) in C# by calling its constructor, binding occurs during the constructor call. If you want to rebind an [`InspectorElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) after it has been constructed, you must call [`Unbind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Unbind.html) and then either call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) explicitly or let a bind operation from a parent create a binding.
### Set binding path
If you call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) to create the binding, you must set the visual element’s binding path to the property name of the object that you want to bind to. 
For example:
  * If you have the following component script:
```
using UnityEngine;

public class MyComp : MonoBehaviour
{
    [SerializeField]
    int m_Count;
}

```

To bind your visual element to `m_Count`, set the binding path to `m_Count`.
  * If you want to bind a visual element to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)’s name property, which is `m_Name`, set the binding path to `m_Name`. 


You can set the binding path in UI Builder, UXML, or with a C# script:
  * In UI Builder, enter the binding path in the **Binding Path** field for a visual element in the [Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-interface-overview.html#uibuilder-inspector)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
  * In UXML, set the `binding-path` attribute for a visual element. Refer to [Define the binding path in UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-bind.html#binding-path-uxml) for an example.
  * In C#, set [`bindingPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable-bindingPath.html) from the [`IBindable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable.html) interface. Refer to [Bind with the binding path](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-csharp.html#binding-path-csharp) for an example.


### Call `BindProperty()`
You can call [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) to bind an element to a [`SerializedProperty`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) directly. 
Use this method if you already have a `SerializedProperty` object, and especially if you traverse the properties of a [`SerializedObject`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) to build a UI dynamically. Refer to [Bind without the binding path](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-without-bindpath.html) for an example.
### Bind elements to nested properties
You can bind a visual element to nested properties in the source object. To do so, combine the binding path of an element with the binding path of the first ancestor. Use this method with the following elements:
  * [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html)
  * [`TemplateContainer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TemplateContainer.html) (corresponds to the `<Instance>` tag in UXML)
  * [`GroupBox`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GroupBox.html)


Refer to [Bind to nested properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-nested-properties.html) for an example.
### Receive callbacks when values change
You can create a binding to receive a callback when a bound serialized property changes. To do so, leverage the [`TrackPropertyValue()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.TrackPropertyValue.html) extension method, which is available to any `VisualElement`. This registers a callback that executes when the provided `SerializedProperty` changes. Refer to [Receive callbacks when a serialized property changes](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback.html) for an example.
You can also create a binding to receive a callback when any properties of the bound serialized object change. To do so, leverage the [`TrackSerializedObjectValue()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.TrackSerializedObjectValue.html) extension method, which is available to any `VisualElement`. This registers a callback that executes when the provided `SerializedProperty` changes. Refer to [Receive callbacks when any properties change](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback-any-properties.html) for an example.
### Bind custom elements
You can create custom elements and bind them to serialized properties through the [value binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html#value-binding) system.
To create bindable custom elements:
  1. [Declare a custom element](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html).
  2. Inherit the element from `BindableElement` or implement the `IBinding` interface.
  3. Implement the `INotifyValueChanged` interface.
  4. Implement the `SetValueWithoutNotify()` method to the `INotifyValueChanged` interface.
  5. Implement the `value` property accessors to the `INotifyValueChanged` interface.


Refer to [Create and style a custom control](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list-without-listview.html#custom-control) for an example.
**Note** : You can’t bind custom data types directly to custom elements because the binding system only allows you to bind an element to a type supported by SerializedPropertyType of `enum`. This means you can’t define a class or structure, for example, a struct called `MyStruct`, and bind it to an element that implements `INotifyValueChanged<MyStruct>`. However, you can bind to serializable nested properties of custom data types. This includes polymorphic serialization (when a field uses the [`[SerializeReference]` attribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)). Refer to [Bind a custom control to custom data type](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-custom-data-type.html) for an example.
## Bind time
Based on the type of UI you create, binding occurs at various times. This is called bind time.
The following table describes the bind time of a control:
**Condition** | **Automatic bind time (assuming binding path was set)**  
---|---  
**An`InspectorElement` constructed in C#** | During the [constructor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement-ctor.html) call  
**A child element that is under the return value of[`CreateInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) or [`CreatePropertyGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.CreatePropertyGUI.html) when those methods return** | After [`CreateInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) or [`CreatePropertyGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.CreatePropertyGUI.html) returns  
**A child element that is under an element when[`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) is called on the parent element** | During the [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) call  
**Other** | No automatic binding; you must bind the element or one of its parents manually  
The following are best practices when creating a binding regarding bind time:
  * If you create a custom [`Editor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) or custom [`PropertyDrawer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html), set the elements’ binding paths instead of calling [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) on any visual elements that are in the [visual tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree) by the end of the body of [`CreateInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) or `CreatePropertyGUI()`. These elements are bound automatically after [`CreateInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) or [`CreatePropertyGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.CreatePropertyGUI.html) returns. However, if you add any elements to the visual tree after that point, call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) to bind them.
  * If you create any other type of UI, call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) regardless of the time at which the elements get added to the visual tree. If you call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) or [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html) and bind multiple controls at the same time, set the binding path of each control and then call [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) on the lowest-level parent element that encompasses all the controls. [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) binds the element on which it’s called if it has a binding path and recursively binds all its child elements if they have binding paths. To prevent a negative performance impact, don’t bind a visual element with the [`Bind()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html) method more than once.


## Bind to a serialized property backing field
When you use an auto-property, the compiler automatically generates a backing field with a name as `<PropertyName>k__BackingField`. This field is not explicitly visible in your code but can be referenced if necessary, as in binding scenarios.
For example, the following example defines an auto-property `SomeProp` and serializes it:
```
[field: SerializeField] 
public float SomeProp 
{ 
    get; 
    private set; 
}

```

The compiler generates the following backing field:
```
[SerializedField]
private float <SomeProp>k__BackingField;

public float SomeProp
{
    get => <SomeProp>k__BackingField;
    set => <SomeProp>k__BackingField = value;
}

```

To bind to `<SomeProp>k__BackingField` in UXML, you must escape `<` and `>` because they’re reserved for tags. For example, set the `binding-path` as follows:
```
<editor:PropertyField name="some-prop" binding-path="&lt;SomeProp&gt;k__BackingField"/>

```

## Binding examples
Try the following examples to learn how to code with data binding:
  * [Bind with binding path in C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-csharp.html)
  * [Bind without the binding path](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-without-bindpath.html)
  * [Bind with UXML and C#](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-bind.html)
  * [Create a binding with the Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-uxml-inspector.html)
  * [Bind to nested properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-nested-properties.html)
  * [Bind to a UXML template](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-uxml-template.html)
  * [Receive callbacks when a bound property changes](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback.html)
  * [Receive callbacks when any bound properties change](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-a-binding-callback-any-properties.html)
  * [Bind to a list with ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html)
  * [Bind to a list without ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list-without-listview.html)
  * [Bind a custom control](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-custom-control.html)
  * [Bind a custom control to custom data type](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-custom-data-type.html)


## Additional resources
  * [Binding data type conversion](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-data-type-conversion.html)
  * [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-implementation-details.html)
  * [Binding examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-binding-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-editor-binding.html)
SerializedObject data binding
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bindable-elements.html)
Bindable elements reference
