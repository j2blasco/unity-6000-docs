* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Lerp
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
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Lerp([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b, float t); 
### Parameters
Parameter | Description  
---|---  
a | Start value, returned when t = 0.  
b | End value, returned when t = 1.  
t | Value used to interpolate between a and b.  
### Returns
**Vector3** Interpolated value, equals to a + (b - a) * t. 
### Description
Linearly interpolates between two points.
Interpolates between the points `a` and `b` by the interpolant `t`. The parameter `t` is clamped to the range [0, 1]. This is most commonly used to find a point some fraction of the way along a line between two endpoints (e.g. to move an object gradually between those points).  
  
The value returned equals **a + (b - a) * t** (which can also be written **a * (1-t) + b*t**).  
When `t` = 0, **Vector3.Lerp(a, b, t)** returns `a`.  
When `t` = 1, **Vector3.Lerp(a, b, t)** returns `b`.  
When `t` = 0.5, **Vector3.Lerp(a, b, t)** returns the point midway between `a` and `b`.  

```
// A short example of Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html) usage.
// Add it to an object in your scene, and at Play time it will draw in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View a small yellow line between the scene origin, and a position interpolated between two other positions (one on the up axis, one on the forward axis).  
  
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int interpolationFramesCount = 45; // Number of frames to completely interpolate between the 2 positions
    int elapsedFrames = 0;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float interpolationRatio = (float)elapsedFrames / interpolationFramesCount;  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) interpolatedPosition = Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), interpolationRatio);  
  
        elapsedFrames = (elapsedFrames + 1) % (interpolationFramesCount + 1);  // reset elapsedFrames to zero after it reached (interpolationFramesCount + 1)  
  
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html));
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), interpolatedPosition, Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html));
    }
}

```

```
// A longer example of Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html) usage.
// Drop this script under an object in your scene, and specify 2 other objects in the "startMarker"/"endMarker" variables in the script inspector window.
// At play time, the script will move the object along a path between the position of those two markers.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Transforms to act as start and end markers for the journey.
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) startMarker;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) endMarker;  
  
    // Movement speed in units per second.
    public float speed = 1.0F;  
  
    // Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) when the movement started.
    private float startTime;  
  
    // Total distance between the markers.
    private float journeyLength;  
  
    void Start()
    {
        // Keep a note of the time the movement started.
        startTime = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);  
  
        // Calculate the journey length.
        journeyLength = Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(startMarker.position, endMarker.position);
    }  
  
    // Move to the target end position.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Distance moved equals elapsed time times speed..
        float distCovered = (Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) - startTime) * speed;  
  
        // Fraction of journey completed equals current distance divided by total distance.
        float fractionOfJourney = distCovered / journeyLength;  
  
        // Set our position as a fraction of the distance between the markers.
        transform.position = Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html)(startMarker.position, endMarker.position, fractionOfJourney);
    }
}

```

Additional resources: [Slerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Slerp.html), [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.LerpUnclamped.html).
* * *
