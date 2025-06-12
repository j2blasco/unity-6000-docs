* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.html

# TransformAccess
struct in UnityEngine.Jobs
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Represents the position, rotation and scale of an object.
### Properties
Property | Description  
---|---  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-isValid.html) | Determines whether this instance refers to a valid Transform.  
[localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-localPosition.html) | The position of the transform relative to the parent.  
[localRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-localRotation.html) | The rotation of the transform relative to the parent transform's rotation.  
[localScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-localScale.html) | The scale of the transform relative to the parent.  
[localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-localToWorldMatrix.html) | Matrix that transforms a point from local space into world space (Read Only).  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-position.html) | The position of the transform in world space.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-rotation.html) | The rotation of the transform in world space stored as a Quaternion.  
[worldToLocalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess-worldToLocalMatrix.html) | Matrix that transforms a point from world space into local space (Read Only).  
### Public Methods
Method | Description  
---|---  
[GetLocalPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.GetLocalPositionAndRotation.html) | Gets the position and rotation of the transform in local space relative to its parent transform.  
[GetPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.GetPositionAndRotation.html) | Gets the position and rotation of the transform in world space.  
[SetLocalPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.SetLocalPositionAndRotation.html) | Sets the position and rotation of the transform in local space relative to its parent transform.  
[SetPositionAndRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.SetPositionAndRotation.html) | Sets the world space position and rotation of the transform.  
* * *
