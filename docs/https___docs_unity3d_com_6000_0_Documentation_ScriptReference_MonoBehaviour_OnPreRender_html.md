* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreRender.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnPreRender()
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
[Event function](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) that Unity calls before a [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) renders the scene.
In the Built-in Render Pipeline, Unity calls `OnPreRender` on MonoBehaviours that are attached to the same GameObject as an enabled [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) component, just before that Camera renders the scene. Use `OnPreRender` to execute your own code at this point in the render loop; for example, you could change visual settings to affect the scene while a given Camera is rendering. `OnPreRender` can be a coroutine.  
  
For similar functionality that does not require the script to be on the same GameObject as a Camera component, see [Camera.onPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreRender.html). For similar functionality in the Scriptable Render Pipeline, see [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html).  
  
Unity calls `OnPreRender` after the Camera performs its culling operation. This means that if you make a change that affects what the Camera sees, the change will take effect from the next frame. To make a change to what the Camera sees in the current frame, use [MonoBehaviour.OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html).  
  
When Unity calls `OnPreRender`, the Camera's render target and depth textures are not yet set up. If you need to access these, you can execute code later in the render loop using a [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).
```
// This script lets you enable/disable fog per camera.
// by enabling or disabling the script in the title of the Inspector
// you can turn fog on or off per camera.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private bool revertFogState = false;  
  
    void OnPreRender()
    {
        revertFogState = RenderSettings.fog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fog.html);
        RenderSettings.fog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fog.html) = enabled;
    }  
  
    void OnPostRender()
    {
        RenderSettings.fog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-fog.html) = revertFogState;
    }
}

```

Additional resources: [Camera.onPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreRender.html), [MonoBehaviour.OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html), [MonoBehaviour.OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPostRender.html), [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [Extending the Built-in Render Pipeline using CommandBuffers](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html).
* * *
