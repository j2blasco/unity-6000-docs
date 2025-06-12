* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PerlinNoise1D.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).PerlinNoise1D
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
public static float PerlinNoise1D(float x); 
### Parameters
Parameter | Description  
---|---  
x | The X-coordinate of the given sample point.  
### Returns
**float** A value in the range of 0.0 and 1.0. The value might be slightly higher or lower than this range. 
### Description
Generates a 1D pseudo-random pattern of float values across a 2D plane.
Although the noise plane is two-dimensional, you can use a single one-dimensional line through the pattern to good effect, for example for animation effects. The result of PerlinNoise1D(x) is equivalent to PerlinNoise(x, 0), but the former is faster.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // "Bobbing" animation from 1D Perlin noise.  
  
    // Range over which height varies.
    float heightScale = 1.0f;  
  
    // Distance covered per second along X axis of Perlin plane.
    float xScale = 1.0f;  
  

    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float height = heightScale * Mathf.PerlinNoise1D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PerlinNoise1D.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * xScale);
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = transform.position;
        pos.y = height;
        transform.position = pos;
    }
}

```

**Note:** It is possible for the return value to be slightly less than 0.0f or slightly exceed 1.0f. You may need to clamp the return value if the 0.0 to 1.0 range is important to you.
* * *
