* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-localBounds.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).localBounds
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
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) localBounds; 
### Description
The bounding box of the renderer in local space.
This is the axis-aligned bounding box fully enclosing the object in local space.  
  
For a [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html), default local bounds are precomputed based on animations associated with that model, which means that the bounding box might be much bigger than the mesh itself. When [SkinnedMeshRenderer.updateWhenOffscreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-updateWhenOffscreen.html) is enabled, Unity recomputes the local bounds every frame.  
  
You can override the default bounding box by setting your own local space bounding box. This is mostly useful when the renderer uses a shader that does custom vertex deformations, and the default bounding box is not accurate. Use [ResetLocalBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.ResetLocalBounds.html) to remove custom bounds override. Note that the custom local bounds value is not saved into scenes or prefabs and has to be set from a script at runtime.
```
using UnityEngine;  
  
public class DrawRendererBounds : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a wireframe box around the selected object,
    // indicating local space bounding volume.
    public void OnDrawGizmosSelected()
    {
        var r = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        if (r == null)
            return;
        var bounds = r.localBounds;
        Gizmos.matrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-matrix.html) = transform.localToWorldMatrix;
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        Gizmos.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html)(bounds.center, bounds.extents * 2);
    }
}

```

Additional resources: [ResetLocalBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.ResetLocalBounds.html), [bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-bounds.html), [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).
* * *
