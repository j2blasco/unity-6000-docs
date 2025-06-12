* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.html

# RenderMode
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
RenderMode for the Canvas.
```
//Attach this script to your Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    enum RenderModeStates { camera, overlay, world };
    RenderModeStates m_RenderModeStates;  
  
    Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) m_Canvas;  
  
    // Use this for initialization
    void Start()
    {
        m_Canvas = GetComponent<Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html)>();
    }  
  
    // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) is called once per frame
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space key to switch between render mode states
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            ChangeState();
        }
    }  
  
    void ChangeState()
    {
        switch (m_RenderModeStates)
        {
            case RenderModeStates.camera:
                m_Canvas.renderMode = RenderMode.ScreenSpaceCamera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.ScreenSpaceCamera.html);
                m_RenderModeStates = RenderModeStates.overlay;
                break;  
  
            case RenderModeStates.overlay:
                m_Canvas.renderMode = RenderMode.ScreenSpaceOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.ScreenSpaceOverlay.html);
                m_RenderModeStates = RenderModeStates.world;
                break;
            case RenderModeStates.world:
                m_Canvas.renderMode = RenderMode.WorldSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.WorldSpace.html);
                m_RenderModeStates = RenderModeStates.camera;  
  
                break;
        }
    }
}

```

### Properties
Property | Description  
---|---  
[ScreenSpaceOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.ScreenSpaceOverlay.html) | Render at the end of the Scene using a 2D Canvas.  
[ScreenSpaceCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.ScreenSpaceCamera.html) | Render using the Camera configured on the Canvas.  
[WorldSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderMode.WorldSpace.html) | Render using any Camera in the Scene that can render the layer.  
* * *
