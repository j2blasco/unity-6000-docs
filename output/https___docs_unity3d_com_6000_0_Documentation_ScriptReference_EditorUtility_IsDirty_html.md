* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsDirty.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).IsDirty
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
public static bool IsDirty(int instanceID); 
## Declaration
public static bool IsDirty([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target); 
### Parameters
Parameter | Description  
---|---  
instanceID | The object's instance ID.  
target | The object.  
### Returns
**bool** True if the object has changed; otherwise false. 
### Description
Gets a boolean value that indicates whether the specified object has changed since the last time it was saved.
Additional resources: [GetDirtyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.GetDirtyCount.html), [SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html).
* * *
