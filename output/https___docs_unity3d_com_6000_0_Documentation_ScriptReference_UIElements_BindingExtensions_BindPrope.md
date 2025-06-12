* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html

#  [BindingExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.html).BindProperty
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public static [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) BindProperty([UIElements.IBindable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable.html) field, [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) obj); 
### Parameters
Parameter | Description  
---|---  
field | VisualElement field editing a property.  
obj | Root SerializedObject containing the bindable property.  
### Returns
**SerializedProperty** The serialized object that owns the bound property. 
### Description
Binds a property to a field and synchronizes their values. This method finds the property using the field's binding path. 
* * *
## Declaration
public static void BindProperty([UIElements.IBindable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindable.html) field, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
field | VisualElement field editing a property.  
property | The SerializedProperty to bind.  
### Description
Binds a property to a field and synchronizes their values. 
* * *
