* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.OverridePhysicsShape.html

#  [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html).OverridePhysicsShape
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
public void OverridePhysicsShape(IList<Vector2[]> physicsShapes); 
### Parameters
Parameter | Description  
---|---  
physicsShapes | A multidimensional list of points in [Sprite.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html) space denoting the physics shape outlines.  
### Description
Sets up a new Sprite physics shape.
The positions are in [Sprite.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html) space and this space is from [Rect.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-zero.html) to [Rect.size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-size.html). Pivot offset and transformation to unit space are done automatically. Values outside of the Rect bounds are valid and are transformed based on [Sprite.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html) space.  
  
Each internal array of physics shape outlines must have more than 2 positions to be able to describe a shape.  
  
Additional resources: [Sprite.rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html). 
* * *
