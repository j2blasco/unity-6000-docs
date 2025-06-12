* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-custom-control-to-data.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-custom-controls.html)
  * Bind custom controls to data


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-attributes.html)
Customize UXML attributes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-define-a-namespace-prefix.html)
Define a namespace prefix
# Bind custom controls to data
You bind custom controls to serialized properties to synchronize values between the control and the property. You can create a bindable custom control derived from the [`BaseField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html) generic base class instead of [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html). This provides the following advantages:
  * Implements the `INotifyValueChanged` interface for the generic parameter type that you specify.
  * Makes the control focusable by default.
  * Provides a horizontal layout with a label element on the left and input on the right.

![FloatField is a built-in UI Toolkit control which inherits from BaseField.<br/>A. The label element.<br/>B. The input element.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/base-field-example.png) FloatField is a built-in UI Toolkit control which inherits from `BaseField`.  
A. The label element.  
B. The input element.
**Note** : It’s possible to create custom controls derived from built-in UI controls if you understand their internal hierarchy and existing USS classes. Unity discourages this practice because your custom controls might be dependent on their internal structure, which is subject to change in the future.
To [bind](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html) custom controls to data:
  * Implement the [`INotifyValueChanged`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyValueChanged_1.html) interface and listen for [`ChangeEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ChangeEvent_1.html)s as needed.
  * Inherit from the [`BindableElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html) class or implement the [`IBindable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable.html) interface.


Refer to [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html) for more details.
For a bindable custom control example, refer to [Create a bindable custom control](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-bindable-custom-control.html).
## Additional resources
  * [Create custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html)
  * [SerializedObject data binding](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)
  * [Create a bindable custom control](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-bindable-custom-control.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-attributes.html)
Customize UXML attributes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-define-a-namespace-prefix.html)
Define a namespace prefix
