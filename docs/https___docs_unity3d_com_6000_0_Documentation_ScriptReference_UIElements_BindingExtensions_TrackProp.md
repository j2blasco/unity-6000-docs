* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.TrackPropertyValue.html

#  [BindingExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.html).TrackPropertyValue
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
public static void TrackPropertyValue([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) element, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, Action<SerializedProperty> callback); 
### Parameters
Parameter | Description  
---|---  
element | VisualElement tracking a property.  
property | The SerializedProperty to track.  
callback | Invoked when the tracked SerializedProperty value changes.  
### Description
Executes the callback when the property value changes. Unity checks properties for changes at regular intervals during the update loop. If no callback is specified, a SerializedPropertyChangeEvent is sent to the target element. 
* * *
