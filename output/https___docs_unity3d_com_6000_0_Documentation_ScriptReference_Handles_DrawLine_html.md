* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawLine
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
public static void DrawLine([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p1, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p2, float thickness = 0.0f); 
### Parameters
Parameter | Description  
---|---  
p1 | The position of the first line's end point in world space.  
p2 | The position of the second line's end point in world space.  
thickness | Line thickness in UI points (zero thickness draws single-pixel line).  
### Description
Draws a line from `p1` to `p2`.
The [Handles.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) and [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html) properties colorize and additionally transform the line position. Unity ignores `DrawLine` (that is, nothing happens) when the current GUI event type is not [Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawLine.png)  
_Draw Line in the Scene View._  
  
Below is an example of an Editor script that draws lines in SceneView to GameObjects listed in a script.
```
// Draw lines to the connected game objects that a script has.
// If the target object doesnt have any game objects attached
// then it draws a line from the object to (0, 0, 0).  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ConnectedObjectsExampleScript))]
class ConnectLineHandleExampleScript : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    void OnSceneGUI()
    {
        ConnectedObjectsExampleScript connectedObjects = target as ConnectedObjectsExampleScript;
        if (connectedObjects.objs == null)
            return;  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center = connectedObjects.transform.position;
        for (int i = 0; i < connectedObjects.objs.Length; i++)
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) connectedObject = connectedObjects.objs[i];
            if (connectedObject)
            {
                Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(center, connectedObject.transform.position);
            }
            else
            {
                Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(center, Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html));
            }
        }
    }
}

```

Example script to attach to a GameObject that will act as a handle:
```
using UnityEngine;  
  
public class ConnectedObjectsExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objs = null;
}

```

Line `thickness` can be optionally set. Zero thickness draws a one-pixel line. Larger thickness values express line thickness in UI points. For example, a thickness of 1.0 could be two pixels wide on screen if the display zoom is 200% (see [EditorGUIUtility.pixelsPerPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-pixelsPerPoint.html)).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HandlesDrawLineThickness.png)  
_Lines of varying thickness._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}  
  
// Displays lines of various thickness in the scene view
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ExampleScript))]
public class ExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        var t = target as ExampleScript;
        var tr = t.transform;
        var position = tr.position;
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        for (int i = 0; i < 10; ++i)
        {
            var linePos = position + Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * (i * 0.5f);
            Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(linePos, linePos + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), i);
        }
    }
}

```

Additional resources: [Handles.lineThickness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-lineThickness.html), [Handles.DrawLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLines.html), [Handles.DrawPolyLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawPolyLine.html), [Handles.DrawWireDisc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireDisc.html).
* * *
