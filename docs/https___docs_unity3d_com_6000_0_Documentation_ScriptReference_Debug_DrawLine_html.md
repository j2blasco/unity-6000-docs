* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).DrawLine
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
public static void DrawLine([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) end, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = Color.white, float duration = 0.0f, bool depthTest = true); 
### Parameters
Parameter | Description  
---|---  
start | Point in world space where the line should start.  
end | Point in world space where the line should end.  
color | Color of the line.  
duration | How long the line should be visible for.  
depthTest | Determines whether objects closer to the camera obscure the line.  
### Description
Draws a line between specified start and end points.
The line will be drawn in the Game view of the editor when the game is running and the gizmo drawing is enabled. The line will also be drawn in the Scene when it is visible in the Game view. Leave the game running and showing the line. Switch to the Scene view and the line will be visible.  
  
The `duration` is the time (in seconds) for which the line will be visible after it is first displayed. A duration of zero shows the line for just one frame.  
  
If `depthTest` is set to true then the line will be obscured by other objects in the Scene that are nearer to the camera.  
  
**Note:** This is for debugging playmode only. Editor gizmos should be drawn with Gizmos.Drawline or [Handles.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html) instead.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // draw a 5-unit white line from the origin for 2.5 seconds
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5, 0, 0), Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html), 2.5f);
    }  
  
    private float q = 0.0f;  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        // always draw a 5-unit colored line from the origin
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(q, q, 1.0f);
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 5, 0), color);
        q = q + 0.01f;  
  
        if (q > 1.0f)
        {
            q = 0.0f;
        }
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
        foreach (ContactPoint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint.html) contact in collision.contacts)
        {
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(contact.point, contact.point + contact.normal, Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 2, false);
        }
    }
}

```

* * *
