* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.SetRotationOffset.html

#  [ParentConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.html).SetRotationOffset
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
public void SetRotationOffset(int index, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) value); 
### Parameters
Parameter | Description  
---|---  
index | The index of the constraint source.  
value | The new rotation offset.  
### Description
Sets the rotation offset associated with a source by index.
Throws InvalidOperationException, if the list of sources is empty. Throws ArgumentOutOfRangeException, if the index is invalid.
* * *
