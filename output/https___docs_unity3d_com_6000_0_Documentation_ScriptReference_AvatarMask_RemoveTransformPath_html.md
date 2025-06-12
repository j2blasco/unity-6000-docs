* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.RemoveTransformPath.html

#  [AvatarMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarMask.html).RemoveTransformPath
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AvatarMask.html "Go to AvatarMask Component in the Manual")
## Declaration
public void RemoveTransformPath([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform, bool recursive = true); 
### Parameters
Parameter | Description  
---|---  
transform | The Transform that should be removed from the AvatarMask.  
recursive | Whether to also remove all children of the specified transform.  
### Description
Removes a transform path from the AvatarMask.
If there is no transform path matching **transform** nothing will be removed.
* * *
