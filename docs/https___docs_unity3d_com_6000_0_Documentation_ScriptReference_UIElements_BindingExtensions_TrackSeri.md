* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.TrackSerializedObjectValue.html

#  [BindingExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.html).TrackSerializedObjectValue
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
public static void TrackSerializedObjectValue([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) element, [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) obj, Action<SerializedObject> callback); 
### Parameters
Parameter | Description  
---|---  
element | VisualElement tracking an object.  
obj | The SerializedObject to track.  
callback | Invoked when one of the tracked SerializedObject's value changes.  
### Description
Executes the callback when the property value changes. Unity checks properties for changes at regular intervals during the update loop. If no callback is specified, a SerializedPropertyChangeEvent is sent to the target element. 
* * *
