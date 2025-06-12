* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawPolyLine.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawPolyLine
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
public static void DrawPolyLine(params Vector3[] points); 
### Description
Draw a line going through the list of `points`.
**Note:** Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) where you might want to have constant screen-sized handles.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawPolyLine.png)  
_PolyLine that connects all the objects in the Scene View._
```
// Draw lines between selected GameObjects.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(DrawPolyLineExample))]
public class PolyLineDraw : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions;  
  
    void OnSceneGUI()
    {
        DrawPolyLineExample connectedObjects = target as DrawPolyLineExample;
        if (connectedObjects.objs == null)
        {
            return;
        }  
  
        if (connectedObjects.objs.Length > 0)
        {
            positions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[connectedObjects.objs.Length];
        }  
  
        for (var i = 0; i < connectedObjects.objs.Length; i++)
        {
            if (connectedObjects.objs[i])
            {
                positions[i] = connectedObjects.objs[i].transform.position;
            }
            else
            {
                positions[i] = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
            }
        }  
  
        Handles.DrawPolyLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawPolyLine.html)(positions);
    }
}

```

And the script attached to this handle:
```
using UnityEngine;  
  
public class DrawPolyLineExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objs;
}

```

* * *
