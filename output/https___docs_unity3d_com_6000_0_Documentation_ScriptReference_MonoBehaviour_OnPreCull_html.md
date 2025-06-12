* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnPreCull()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
[Event function](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) that Unity calls before a [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) culls the scene.
In the Built-in Render Pipeline, Unity calls `OnPreCull` on MonoBehaviours that are attached to the same GameObject as an enabled [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) component, just before that Camera performs the culling operation that determines what it can see. Use `OnPreCull` to execute your own code at this point in the render loop; for example, you can change the Camera's settings before performing the culling operation, to affect what the Camera sees. `OnPreCull` can be a coroutine.  
  
For similar functionality that does not require the script to be on the same GameObject as a Camera component, see [Camera.onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html). For similar functionality in the Scriptable Render Pipeline, see [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html).
```
// Attach this to the same GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) as a Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) component.
// This script inverts the view of the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html), so that everything rendered by it is flipped  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
    }  
  
    void OnPreCull()
    {
        cam.ResetWorldToCameraMatrix();
        cam.ResetProjectionMatrix();
        cam.projectionMatrix = cam.projectionMatrix * Matrix4x4.Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Scale.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, -1, 1));
    }  
  
    void OnPreRender()
    {
        GL.invertCulling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-invertCulling.html) = true;
    }  
  
    void OnPostRender()
    {
        GL.invertCulling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-invertCulling.html) = false;
    }
}

```

Additional resources: [Camera.onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html), [MonoBehaviour.OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreRender.html), [MonoBehaviour.OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPostRender.html), [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [Extending the Built-in Render Pipeline using CommandBuffers](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html).
* * *
