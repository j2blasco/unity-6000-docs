* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.GetTranslationOffset.html

#  [ParentConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ParentConstraint.html).GetTranslationOffset
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetTranslationOffset(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the constraint source.  
### Returns
**Vector3** The translation offset. 
### Description
Gets the rotation offset associated with a source by index.
Throws InvalidOperationException, if the list of sources is empty. Throws ArgumentOutOfRangeException, if the index is invalid.
* * *
