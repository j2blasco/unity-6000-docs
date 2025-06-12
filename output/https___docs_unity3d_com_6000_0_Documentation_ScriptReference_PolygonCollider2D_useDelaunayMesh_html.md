* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D-useDelaunayMesh.html

#  [PolygonCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PolygonCollider2D.html).useDelaunayMesh
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
useDelaunayMesh; 
### Description
When the value is true, the Collider uses an additional Delaunay triangulation step to produce the Collider mesh. When the value is false, this additional step does not occur.
Using Delaunay triangulation can reduce the number of shapes created in the Collider mesh and reduce the number of small triangle fans produced, both of which can improve overall physics performance.
* * *
