* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-bounds.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).bounds
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
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds; 
### Description
The bounding box of the renderer in world space.
This is the axis-aligned bounding box fully enclosing the object in world space.  
  
Using `bounds` is convenient to make rough approximations about the object's location and its extents. For example, the `center` property is often a more precise approximation to the center of the object than [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html), especially if the object is not symmetrical.  
  
[Mesh.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html) and [localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localBounds.html) are similar but they return the bounds in local space.  
  
You can override the default bounding box by setting your own world space bounding box. This is mostly useful when the renderer uses a shader that does custom vertex deformations, and the default bounding box is not accurate.  
  
When you set custom world bounds, the renderer bounding volume no longer automatically tracks Transform component changes. If there is a local space bounding volume override ([localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localBounds.html)) active at the same time, it is ignored and the custom world space bounds are used. Use [ResetBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.ResetBounds.html) to remove the custom bounds override. Note that the custom world bounds value is not saved into scenes or prefabs and has to be set from a script at runtime.
```
using UnityEngine;  
  
public class DrawRendererBounds : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a wireframe box around the selected object,
    // indicating world space bounding volume.
    public void OnDrawGizmosSelected()
    {
        var r = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        if (r == null)
            return;
        var bounds = r.bounds;
        Gizmos.matrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) = Matrix4x4.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html);
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        Gizmos.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html)(bounds.center, bounds.extents * 2);
    }
}

```

Additional resources: [ResetBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.ResetBounds.html), [localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localBounds.html), [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html), [Mesh.bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bounds.html).
* * *
