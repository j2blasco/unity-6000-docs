* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.OverlapPoint.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).OverlapPoint
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
public bool OverlapPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point); 
### Parameters
Parameter | Description  
---|---  
point | A point in world space.  
### Returns
**bool** Does `point` overlap the collider? 
### Description
Check if a collider overlaps a point in space.
This will always return false when used on an [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html).
* * *
