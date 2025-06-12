* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLines.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawDottedLines
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
public static void DrawDottedLines(Vector3[] lineSegments, float screenSpaceSize); 
### Parameters
Parameter | Description  
---|---  
lineSegments | A list of pairs of points that represent the start and end of line segments.  
screenSpaceSize | The size in pixels for the lengths of the line segments and the gaps between them.  
### Description
Draw a list of dotted line segments.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawDottedLines.png) "Draw multiple dotted lines in sceneview.".
```
// Draw lines to the connected game objects that a script has.
// if the target object doesn't have any game objects attached
// then it draws a line from the object to 0,0,0.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections.Generic;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ConnectedLineObjects))]
class ConnectDottedLineHandle : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    float dashSize = 4.0f;
    void OnSceneGUI()
    {
        ConnectedLineObjects connectedObjects = target as ConnectedLineObjects;
        if (connectedObjects.objs == null ||
            connectedObjects.objs.Length == 0)
            return;
        // we store the start and end points of the line segments in this array
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] lineSegments = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[connectedObjects.objs.Length * 2];  
  
        int lastObject = connectedObjects.objs.Length - 1;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) prevPoint;
        if (connectedObjects.objs[lastObject])
        {
            prevPoint = connectedObjects.objs[lastObject].transform.position;
        }
        else
        {
            prevPoint = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        }
        int pointIndex = 0;
        for (int currObjectIndex = 0; currObjectIndex < connectedObjects.objs.Length; currObjectIndex++)
        {
            // find the position of our connected object and store it
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) currPoint;
            if (connectedObjects.objs[currObjectIndex])
            {
                currPoint = connectedObjects.objs[currObjectIndex].transform.position;
            }
            else
            {
                currPoint = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
            }  
  
            // store the starting point of the line segment
            lineSegments[pointIndex] = prevPoint;
            pointIndex++;  
  
            // store the ending point of the line segment
            lineSegments[pointIndex] = currPoint;
            pointIndex++;  
  
            prevPoint = currPoint;
        }
        Handles.DrawDottedLines[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLines.html)(lineSegments, dashSize);
    }
}

```

And the script attached to this Handle:
```
using UnityEngine;
using System.Collections;  
  
public class ConnectedLineObjects : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objs = null;
}

```

* * *
## Declaration
public static void DrawDottedLines(Vector3[] points, int[] segmentIndices, float screenSpaceSize); 
### Parameters
Parameter | Description  
---|---  
points | A list of points.  
segmentIndices | A list of pairs of indices to the start and end points of the line segments.  
screenSpaceSize | The size in pixels for the lengths of the line segments and the gaps between them.  
### Description
Draw a list of indexed dotted line segments.
```
// Draw lines to the connected game objects that a script has.
// If the target object doesn't have any game objects attached
// then it draws a line from the object to (0, 0, 0).  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections.Generic;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ConnectedLinesObjects))]
class ConnectDottedLinesHandle : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    float dashSize = 4.0f;
    void OnSceneGUI()
    {
        ConnectedLinesObjects connectedObjects = target as ConnectedLinesObjects;
        if (connectedObjects.objs == null ||
            connectedObjects.objs.Length == 0)
            return;  
  
        // we store the points of the line segments in this array
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] points = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[connectedObjects.objs.Length];  
  
        // for each line segment we need two indices into the points array:
        // the index to the start and the end point
        int[] segmentIndices = new int[connectedObjects.objs.Length * 2];  
  
        // create the points and line segments indices
        int prevIndex = connectedObjects.objs.Length - 1;
        int pointIndex = 0;
        int segmentIndex = 0;
        for (int currIndex = 0; currIndex < connectedObjects.objs.Length; currIndex++)
        {
            // find the position of our connected object and store it
            if (connectedObjects.objs[pointIndex])
            {
                points[pointIndex] = connectedObjects.objs[currIndex].transform.position;
            }
            else
            {
                points[pointIndex] = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
            }  
  
            // the index to the start of the line segment
            segmentIndices[segmentIndex] = prevIndex;
            segmentIndex++;  
  
            // the index to the end of the line segment
            segmentIndices[segmentIndex] = pointIndex;
            segmentIndex++;  
  
            pointIndex++;
            prevIndex = currIndex;
        }
        Handles.DrawDottedLines[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLines.html)(points, segmentIndices, dashSize);
    }
}

```

And the script attached to this Handle:
```
using UnityEngine;
using System.Collections;  
  
public class ConnectedLinesObjects : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objs = null;
}

```

* * *
