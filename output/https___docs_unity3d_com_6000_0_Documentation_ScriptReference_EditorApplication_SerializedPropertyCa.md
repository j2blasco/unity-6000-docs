* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SerializedPropertyCallbackFunction.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).SerializedPropertyCallbackFunction
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
public delegate void SerializedPropertyCallbackFunction([GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property); 
### Parameters
Parameter | Description  
---|---  
menu | The contextual menu which is about to be shown to the user.  
property | The property for which the contextual menu is shown.  
### Description
Delegate to be called from [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html) contextual inspector callbacks.
SerializedPropertyCallbackFunction is used by [EditorApplication.contextualPropertyMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-contextualPropertyMenu.html).
* * *
