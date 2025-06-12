* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-orthographicSize.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).orthographicSize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
orthographicSize; 
### Description
Camera's half-size when in orthographic mode.
The `orthographicSize` property defines the viewing volume of an [orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-orthographic.html) Camera. To edit `orthographicSize`, you must set the Camera projection to orthographic.  
  
The height of the viewing volume is (`orthographicSize` * 2). Unity calculates the width of the viewing volume using `orthographicSize` and the camera's [aspect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-aspect.html).  
  
Unity ignores `orthographicSize` if the camera is not orthographic. Use [fieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-fieldOfView.html) instead.  
  
Additional resources: [camera component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Assign this Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) in the Inspector
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) m_OrthographicCamera;
    //These are the positions and dimensions of the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) view in the Game view
    float m_ViewPositionX, m_ViewPositionY, m_ViewWidth, m_ViewHeight;  
  
    void Start()
    {
        // This sets the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) view rectangle to be in the bottom corner of the screen
        m_ViewPositionX = 0;
        m_ViewPositionY = 0;  
  
        // This sets the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) view rectangle to be smaller so you can compare the orthographic view of this Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) with the perspective view of the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
        m_ViewWidth = 0.4f;
        m_ViewHeight = 0.4f;  
  
        // This enables the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) (the one that is orthographic)
        m_OrthographicCamera.enabled = true;  
  
        // If the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) exists in the inspector, enable orthographic mode and change the size
        if (m_OrthographicCamera)
        {
            // This enables the orthographic mode
            m_OrthographicCamera.orthographic = true;  
  
            // Set the size of the viewing volume you'd like the orthographic Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) to pick up
            m_OrthographicCamera.orthographicSize = 5.0f;  
  
            // Set the orthographic Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) Viewport size and position
            m_OrthographicCamera.rect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(m_ViewPositionX, m_ViewPositionY, m_ViewWidth, m_ViewHeight);
        }
    }
}

```

* * *
