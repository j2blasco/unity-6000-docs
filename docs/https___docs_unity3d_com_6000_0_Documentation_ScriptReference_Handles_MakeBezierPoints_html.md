* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.MakeBezierPoints.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).MakeBezierPoints
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
public static Vector3[] MakeBezierPoints([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startPosition, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endPosition, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startTangent, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endTangent, int division); 
### Description
Retuns an array of points to representing the bezier curve.
The `division` argument provides the number of lines used to make the bezier curve.  
  
Additional resources: [Handles.DrawBezier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawBezier.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Generates 20 points that define the bezier curve  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(DrawBezier))]
public class DrawBezierExample : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] points;  
  
    private void OnSceneGUI()
    {
        points = Handles.MakeBezierPoints[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.MakeBezierPoints.html)(
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f,  0.0f,   0.0f),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1.0f,  0.0f,   0.0f),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1.0f,  0.75f,  0.75f),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, -0.75f, -0.75f),
            20);  
  
        Handles.DrawAAPolyLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawAAPolyLine.html)(points);
    }
}

```

This is the second script:
```
using UnityEngine;  
  
// The class called by the DrawBezierExample  
  
public class DrawBezier : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // no script needed, just the class
}

```

* * *
