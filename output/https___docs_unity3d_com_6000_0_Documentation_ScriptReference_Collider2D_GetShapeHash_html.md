* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetShapeHash.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).GetShapeHash
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
public uint GetShapeHash(); 
### Returns
**uint** A hash value that uniquely identifies the configured geometry of the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html). 
### Description
Generates a simple hash value based upon the geometry of the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
The geometry of a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) can be configured by various properties on all of the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) types such as the radius of a [CircleCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CircleCollider2D.html) or the size of a [BoxCollider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider2D.html). The geometry created as opposed to the properties used to generate them are what is is hashed here. Two different [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are configured to produce the same geometry produce the same hash.  
  
This hash can be used to determine if the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) geometry is the same as another [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) geometry or if the geometry has changed by comparing against previous hash values.  
  
A common use-case is when using [Collider2D.CreateMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CreateMesh.html) where it is useful to determine if the resulting [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) would change due to the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) geometry changing.  
  
Additional resources: [Collider2D.CreateMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.CreateMesh.html).
* * *
