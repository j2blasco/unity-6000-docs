* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-adjacentStartPoint.html

#  [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html).adjacentStartPoint
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) adjacentStartPoint; 
### Description
Defines the position of a virtual point adjacent to the start point of the EdgeCollider2D.
An EdgeCollider2D is made up of contiguous edges defined by a set of points adjacent to each other. When a collision occurs with a point along the Collider, Unity uses the two edges the point makes with its adjacent points to form a collision normal, and calculate the collision response. This produces a continuous edge chain and an uninterrupted collision surface.  
  
However, when a collision occurs with the start or end point of the Edge Collider, Unity is unable to form a collision normal with a single edge and so the collision normal becomes the direction of motion of the collision.  
  
This property defines a virtual point that is adjacent to the end point to create a "virtual edge" from which Unity calculates and forms a collision normal. This point is only used when [useAdjacentStartPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-useAdjacentStartPoint.html) it set to true. The "virtual edge" formed cannot be collided with and only a collision normal is used.  
  
An important and useful use case for this feature is to allow multiple [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html)s to connect together by specifying [adjacentStartPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-adjacentStartPoint.html) and [adjacentEndPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D-adjacentEndPoint.html) that overlap the points of other [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html)s. This produces a seamless transition for collisions when moving across multiple [EdgeCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EdgeCollider2D.html)s.
* * *
