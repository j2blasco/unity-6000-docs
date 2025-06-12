* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.html

# RTClearFlags
enumeration
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
Flags that determine which render targets Unity clears when you use [CommandBuffer.ClearRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.ClearRenderTarget.html).
You can combine flags by using the bitwise OR operator.
```
using UnityEngine;
using UnityEngine.Rendering;  
  
// Attach this script to a Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and select a Clear Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html).
// When you enter Play mode, a command buffer clears the screen with different clear parameters.
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)))]
public class MyClearScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public enum ClearMode
    {
        All,
        ColorStencil
    }  
  
    public ClearMode m_ClearMode;  
  
    void Start()
    {
        var camera = GetComponent<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>();
        var buffer = new CommandBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html)();  
  
        switch (m_ClearMode)
        {
            case ClearMode.All:
                // Clear color, depth and stencil render targets. Stencil is cleared with value 0xF0.
                buffer.ClearRenderTarget(RTClearFlags.All[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.All.html), Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f, 0xF0);
                break;
            case ClearMode.ColorStencil:
                // Clear only color and stencil render targets. Stencil is cleared with value 0xF0.
                buffer.ClearRenderTarget((RTClearFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.html))((int)RTClearFlags.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.Color.html) | (int)RTClearFlags.Stencil[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.Stencil.html)), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 1.0f, 0xF0);
                break;
        }  
  
        camera.AddCommandBuffer(CameraEvent.AfterSkybox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterSkybox.html), buffer);
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.None.html) | Do not clear any render target.  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.Color.html) | Clear all color render targets.  
[Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.Depth.html) | Clear the depth buffer.  
[Stencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.Stencil.html) | Clear the stencil buffer.  
[All](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.All.html) | Clear all color render targets, the depth buffer, and the stencil buffer. This is equivalent to combining RTClearFlags.Color, RTClearFlags.Depth and RTClearFlags.Stencil.  
[DepthStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.DepthStencil.html) | Clear both the depth and the stencil buffer. This is equivalent to combining RTClearFlags.Depth and RTClearFlags.Stencil.  
[ColorDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.ColorDepth.html) | Clear both the color and the depth buffer. This is equivalent to combining RTClearFlags.Color and RTClearFlags.Depth.  
[ColorStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.ColorStencil.html) | Clear both the color and the stencil buffer. This is equivalent to combining RTClearFlags.Color and RTClearFlags.Stencil.  
* * *
