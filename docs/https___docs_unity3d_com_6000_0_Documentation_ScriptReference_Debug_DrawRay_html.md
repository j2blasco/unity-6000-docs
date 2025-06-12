* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).DrawRay
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
## Declaration
public static void DrawRay([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) dir, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = Color.white, float duration = 0.0f, bool depthTest = true); 
### Parameters
Parameter | Description  
---|---  
start | Point in world space where the ray should start.  
dir | Direction and length of the ray.  
color | Color of the drawn line.  
duration | How long the line will be visible for (in seconds).  
depthTest | Determines whether objects closer to the camera obscure the line.  
### Description
Draws a line from `start` to `start` + `dir` in world coordinates.
The `duration` parameter determines how long the line will be visible after the frame it is drawn. If duration is 0 (the default) then the line is rendered 1 frame.  
  
If `depthTest` is set to true then the line will be obscured by other objects in the Scene that are nearer to the camera.  
  
The line will be drawn in the Scene view of the editor. If gizmo drawing is enabled in the game view, the line will also be drawn there.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Frame update example: Draws a 10 meter long green line from the position for 1 frame.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) forward = transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)) * 10;
        Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(transform.position, forward, Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
    }
}

```

```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) callback example: Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html)-draw all contact points and normals for 2 seconds.
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        Debug.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawRay.html)(collision.contacts[0].point, collision.contacts[0].normal, Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 2, false);
    }
}

```

* * *
