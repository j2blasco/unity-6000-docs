* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GeometryType.Outlines.html

#  [CompositeCollider2D.GeometryType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompositeCollider2D.GeometryType.html).Outlines
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
Sets the Composite Collider 2D to generate closed outlines for the merged collider geometry consisting of only edges.
The outline geometry is equivalent to using an [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html) with the chains of edges all connected. While all the edges are closed (the end edge connects to the start edge), nothing will collide in the interior of such geometry as there is no overlap of the edges. A collision or trigger will be registered only if the edges are in contact with a collider.  
  
This is usually the most efficient geometry to use as it produces far less edges. Continuous edges do not cause unwanted collisions because all edges are connected. Unwanted collisions is where two separate Colliders get in contact even though both are aligned perfectly. Use this type of geometry to produce platform surfaces where other Colliders are to move without any interference from unwanted collisions.  
  
Any interior holes caused by the the composite edges surrounding it, does not cause any interior overlap but is another closed off section of the new Composite Collider shape.
* * *
