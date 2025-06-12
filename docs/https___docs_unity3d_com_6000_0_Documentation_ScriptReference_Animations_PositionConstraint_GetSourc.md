* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PositionConstraint.GetSource.html

#  [PositionConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PositionConstraint.html).GetSource
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
public [Animations.ConstraintSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ConstraintSource.html) GetSource(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the source.  
### Returns
**ConstraintSource** The source object and its weight. 
### Description
Gets a constraint source by index.
Throws ArgumentOutOfRangeException, if the index is invalid.
* * *
