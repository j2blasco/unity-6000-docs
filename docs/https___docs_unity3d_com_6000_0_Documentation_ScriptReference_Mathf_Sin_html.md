* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Sin
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static float Sin(float f); 
### Parameters
Parameter | Description  
---|---  
f | The input angle, in radians.  
### Returns
**float** The return value between -1 and +1. 
### Description
Returns the sine of angle `f`.
**Note:** If using very large numbers with this function, there is an acceptable range for input angle values for this method, beyond which the calculation will fail. On windows, the acceptable range is approximately between -9223372036854775295 to 9223372036854775295. This range may differ on other platforms. For values outside of the acceptable range, the Sin method returns the input value, rather than throwing an exception.  
  
Additional resources: [Cos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html), [Tan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Tan.html)
```
using UnityEngine;
using System.Collections;  
  
public class PolyDrawExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int numberOfSides;
    public float polygonRadius;
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) polygonCenter;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        DebugDrawPolygon(polygonCenter, polygonRadius, numberOfSides);
    }  
  
    // Draw a polygon in the XY plane with a specfied position, number of sides
    // and radius.
    void DebugDrawPolygon(Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) center, float radius, int numSides)
    {
        // The corner that is used to start the polygon (parallel to the X axis).
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) startCorner = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(radius, 0) + center;  
  
        // The "previous" corner point, initialised to the starting corner.
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) previousCorner = startCorner;  
  
        // For each corner after the starting corner...
        for (int i = 1; i < numSides; i++)
        {
            // Calculate the angle of the corner in radians.
            float cornerAngle = 2f * Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) / (float)numSides * i;  
  
            // Get the X and Y coordinates of the corner point.
            Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) currentCorner = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(cornerAngle) * radius, Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(cornerAngle) * radius) + center;  
  
            // Draw a side of the polygon by connecting the current corner to the previous one.
            Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(currentCorner, previousCorner);  
  
            // Having used the current corner, it now becomes the previous corner.
            previousCorner = currentCorner;
        }  
  
        // Draw the final side by connecting the last corner to the starting corner.
        Debug.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.DrawLine.html)(startCorner, previousCorner);
    }
}

```

* * *
