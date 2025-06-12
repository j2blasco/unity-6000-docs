* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GeometryType.Polygons.html

#  [CompositeCollider2D.GeometryType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GeometryType.html).Polygons
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
Sets the Composite Collider 2D to generate closed outlines for the merged collider geometry consisting of convex polygon shapes.
The polygon geometry is equivalent to using an [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html) with the polygon outlines from other colliders being merged then decomposed into multiple convex polygon shapes forming a closed outline composite. The interior of this closed outline registers collisions or triggers.  
  
This is usually the least efficient geometry to use as it produces multiple shapes or edges. These multiple shapes cause unwanted collisions when two separate colliders come in contact with each other even when they are aligned perfectly. Only use this geometry type when you need to detect the interior of the composite outline, such as when you use triggers.  
  
Any interior holes caused by forming the Composite Collider 2D does not register any collision or trigger.
* * *
