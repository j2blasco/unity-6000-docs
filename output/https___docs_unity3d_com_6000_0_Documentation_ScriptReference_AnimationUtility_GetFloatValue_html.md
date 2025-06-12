* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.GetFloatValue.html

#  [AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html).GetFloatValue
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
public static bool GetFloatValue([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) root, [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding, out float data); 
### Parameters
Parameter | Description  
---|---  
root | The root GameObject of the animated hierarchy.  
binding | The binding that defines the path and the properties of the value.  
data | The resulting float value, if a value exists.  
### Returns
**bool** Returns True if the value exists. False otherwise. 
### Description
Retrieves the float value that the binding points to.
Use this method when recording keyframes.
* * *
**Obsolete** This overload is deprecated. Use the one with EditorCurveBinding instead.
## Declaration
public static bool GetFloatValue([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) root, string relativePath, Type type, string propertyName, out float data); 
### Description
Samples a curve on the GameObject you pass in and retrieves the current float value.
Use this method when recording keyframes.
* * *
