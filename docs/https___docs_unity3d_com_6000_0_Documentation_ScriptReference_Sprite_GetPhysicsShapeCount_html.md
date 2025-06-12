* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetPhysicsShapeCount.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).GetPhysicsShapeCount
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
public int GetPhysicsShapeCount(); 
### Returns
**int** The number of physics shapes for the Sprite. 
### Description
The number of physics shapes for the Sprite.
A _physics shape_ is a cyclic sequence of line segments between points that define the outline of the Sprite used for physics. Since the Sprite can have holes and discontinuous parts, its outline is not necessarily defined by a single physics shape.
* * *
