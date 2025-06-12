* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapeBounds.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).GetShapeBounds
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
public [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) GetShapeBounds(List<Bounds> bounds, bool useRadii, bool useWorldSpace); 
### Parameters
Parameter | Description  
---|---  
bounds | The list used to store the returned [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).  
useRadii | Whether the radius of each [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) should be used to calculate the [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) or not.  
useWorldSpace | Whether to transform all the returned [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) to world space or leave them in their default local space.  
### Returns
**Bounds** Returns the combined [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) of the retrieved list. 
### Description
Retrieves a list of [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) for all [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) created by this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), and returns the combined [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) of the retrieved list.
Additional resources: [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html), [Collider2D.GetShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapes.html) and [Collider2D.GetShapeHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapeHash.html).
* * *
