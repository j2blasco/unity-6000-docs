* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.Bind.html

#  [BindingExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.html).Bind
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
public static void Bind([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) element, [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) obj); 
### Parameters
Parameter | Description  
---|---  
element | Root VisualElement containing IBindable fields.  
obj | Data object.  
### Description
Binds a SerializedObject to fields in the element hierarchy. 
Don’t call `Bind()` from the @@Editor.CreateInspectorGUI()@2 or `PropertyDrawer.CreatePropertyGUI()` override. It is called automatically on the hierarchy that these methods return. 
* * *
