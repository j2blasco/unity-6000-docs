* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenToWorldPoint.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).ScreenToWorldPoint
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
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ScreenToWorldPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
## Declaration
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ScreenToWorldPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Camera.MonoOrStereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
position | A 2D screen space point in pixels, plus a z coordinate for the distance from the camera in world units. The lower left pixel of the screen is (0,0). The upper right pixel of the screen is (screen width in pixels - 1, screen height in pixels - 1).  
eye | By default, [Camera.MonoOrStereoscopicEye.Mono](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Mono.html). Can be set to [Camera.MonoOrStereoscopicEye.Left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Left.html) or [Camera.MonoOrStereoscopicEye.Right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Right.html) for use in stereoscopic rendering (e.g., for VR).  
### Returns
**Vector3** The world space point created by converting the screen space point at the provided distance z from the camera plane. 
### Description
Transforms a point from screen space into world space, where world space is defined as the coordinate system at the very top of your game's hierarchy.
World space coordinates can still be calculated even when provided as an off-screen coordinate, for example for instantiating an off-screen object near a specific corner of the screen.  
  
To make sure the world space point is part of the camera's view volume, the z coordinate you provide must be between the camera's `nearClipPlane` and `farClipPlane`. 
```
// Convert the 2D position of the mouse into a
// 3D position.  Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) these on the game window.  
  
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        cam = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
    }  
  
    void OnGUI()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)();
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html)   currentEvent = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePos = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)();  
  
        // Get the mouse position from Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html).
        // Note that the y position from Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) is inverted.
        mousePos.x = currentEvent.mousePosition.x;
        mousePos.y = cam.pixelHeight - currentEvent.mousePosition.y;  
  
        point = cam.ScreenToWorldPoint(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(mousePos.x, mousePos.y, cam.nearClipPlane));  
  
        GUILayout.BeginArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 250, 120));
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) pixels: " + cam.pixelWidth + ":" + cam.pixelHeight);
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Mouse position: " + mousePos);
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("World position: " + point.ToString("F3"));
        GUILayout.EndArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html)();
    }
}

```

* * *
