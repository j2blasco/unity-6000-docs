* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetPhysicsShape.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).GetPhysicsShape
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
public int GetPhysicsShape(int shapeIdx, List<Vector2> physicsShape); 
### Parameters
Parameter | Description  
---|---  
shapeIdx | The index of the physics shape to retrieve.  
physicsShape | An ordered list of the points in the selected physics shape to store points in.  
### Returns
**int** The number of points stored in the given list. 
### Description
Gets a physics shape from the Sprite by its index.
A _physics shape_ is a cyclic sequence of line segments between points that define the outline of the Sprite used for physics. Since the Sprite can have holes and discontinuous parts, its outline is not necessarily defined by a single physics shape.
* * *
