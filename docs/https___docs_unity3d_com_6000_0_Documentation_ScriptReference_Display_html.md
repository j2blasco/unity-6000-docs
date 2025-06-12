* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html

# Display
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Provides access to a display / screen for rendering operations.
Unity supports multi-display rendering on: 
  * Desktop platforms (Windows, macOS X, and Linux)
  * Android (OpenGL ES and Vulkan)
  * iOS


Some features in the Display class only work on some of the supported platforms. See the properties and methods for more information about platform compatibility.  
  
Use the Display class to operate on the displays themselves, and [Camera.targetDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetDisplay.html) to set up cameras for rendering to individual displays.  
  
Additional resources: [Camera.targetDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetDisplay.html), [Canvas.targetDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-targetDisplay.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) extCam;
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        // GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) is rendered with last camera.
        // As we want it to end up in the main screen, make sure main camera is the last one drawn.
        extCam.depth = cam.depth - 1;  
  
        cam.SetTargetBuffers(Display.main.colorBuffer, Display.main.depthBuffer);
        extCam.enabled = false;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Display.displays.Length > 1 && !extCam.enabled)
        {
            Display.displays[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-displays.html)[1].SetRenderingResolution(256, 256);
            extCam.SetTargetBuffers(Display.displays[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-displays.html)[1].colorBuffer, Display.displays[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-displays.html)[1].depthBuffer);
        }
        extCam.enabled = Display.displays.Length > 1;
    }
}

```

### Static Properties
Property | Description  
---|---  
[activeEditorGameViewTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-activeEditorGameViewTarget.html) | Get the Editors active GameView display target.  
[displays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-displays.html) | The list of connected displays.  
[main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-main.html) | Main Display.  
### Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-active.html) | Gets the state of the display and returns true if the display is active and false if otherwise.  
[colorBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-colorBuffer.html) | Color RenderBuffer.  
[depthBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-depthBuffer.html) | Depth RenderBuffer.  
[renderingHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-renderingHeight.html) | Vertical resolution that the display is rendering at.  
[renderingWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-renderingWidth.html) | Horizontal resolution that the display is rendering at in the viewport.  
[requiresBlitToBackbuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-requiresBlitToBackbuffer.html) | True when the back buffer requires an intermediate texture to render.  
[requiresSrgbBlitToBackbuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-requiresSrgbBlitToBackbuffer.html) | True when doing a blit to the back buffer requires manual color space conversion.  
[systemHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-systemHeight.html) | Vertical native display resolution.  
[systemWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-systemWidth.html) | Horizontal native display resolution.  
### Public Methods
Method | Description  
---|---  
[Activate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.Activate.html) | Activates an external display. For example, a secondary monitor connected to the system.  
[SetParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.SetParams.html) | Windows platforms only. Sets rendering size and position on screen.  
[SetRenderingResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.SetRenderingResolution.html) | Sets rendering resolution for the display.  
### Static Methods
Method | Description  
---|---  
[RelativeMouseAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.RelativeMouseAt.html) | Query relative mouse coordinates.  
* * *
