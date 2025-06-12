* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineList.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawLineList
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
public static void DrawLineList(ReadOnlySpan<Vector3> points); 
### Parameters
Parameter | Description  
---|---  
points | Pairs of points to use as the beginning and end of each line to draw. Unity throws an exception if `points` contains an odd number of elements.  
### Description
Draws multiple lines between pairs of points.
This function provides a more efficient way to draw multiple lines than repeatedly calling the [Gizmos.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html) function for each one.  
  
Each pair of points from the `points` span represents the start and end of each line, so Unity draws the first line from `points[0]` to `points[1]`, the next from `points[2]` to `points[3]`, and so on.
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
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-100, 100, 0),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(100, 100, 0)
        };
    }  
  
    void OnDrawGizmosSelected()
    {
        // Draws two parallel blue lines
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        Gizmos.DrawLineList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineList.html)(points);
    }
}

```

Additional resources: [Gizmos.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html), [Gizmos.DrawLineStrip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineStrip.html).
* * *
