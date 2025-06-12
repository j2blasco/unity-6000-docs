* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineStrip.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawLineStrip
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
public static void DrawLineStrip(ReadOnlySpan<Vector3> points, bool looped); 
### Parameters
Parameter | Description  
---|---  
points | The points that define the sequence of lines to draw. The function draws a line between each point and the one that follows it.  
looped | Whether to draw an additional line between the last point and the first. When this is `true`, Unity draws an additional line between `points[points.Length - 1]` and `points[0]`. When this is `false`, the lines terminate at the last point.  
### Description
Draws a line between each point in the supplied span.
This function provides a more efficient way to draw multiple lines than repeatedly calling the [Gizmos.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html) function for each one.  
  
Unity draws the first line from `points[0]` to `points[1]`, the next from `points[1]` to `points[2]`, and so on.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] points;  
  
    void Start()
    {
        points = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[4]
        {
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-100, 0, 0),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(100, 0, 0),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(100, 100, 0),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-100, 100, 0)
        };
    }  
  
    void OnDrawGizmosSelected()
    {
        // Draws four lines making a square
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        Gizmos.DrawLineStrip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineStrip.html)(points, true);
    }
}

```

Additional resources: [Gizmos.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html), [Gizmos.DrawLineList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineList.html).
* * *
