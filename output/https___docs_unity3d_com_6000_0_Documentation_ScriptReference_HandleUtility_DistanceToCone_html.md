* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCone.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).DistanceToCone
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
public static float DistanceToCone([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, float size); 
### Parameters
Parameter | Description  
---|---  
position | Position of the cone.  
rotation | Rotation of the cone.  
size | Size of the cone.  
### Returns
**float** Distance from mouse to cone in pixels. 
### Description
Returns the distance in pixels from the mouse pointer to a cone.
Calculates the screen space distance from the mouse pointer to a cone at given world space `position` with the given `rotation` and `size`.  
  
Returns zero when mouse pointer is directly over the cone.  
  
Uses the current camera to determine the distance.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
}  
  
// Displays cone in scene view, and distance from mouse
// to the cone.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ExampleScript))]
public class ExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public void OnSceneGUI()
    {
        var t = target as ExampleScript;
        var tr = t.transform;
        var position = tr.position;
        var rotation = tr.rotation;
        var size = 1.0f;
        // draw a cone in scene
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        Handles.ConeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html)(0, position, rotation, size, Event.current.type);
        // calculate distance from mouse to cone, and display it
        var distance = HandleUtility.DistanceToCone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCone.html)(position, rotation, size);
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html);
        Handles.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html)(position, distance.ToString("F0"));
        // make scene view repaint on mouse move
        if (Event.current.type == EventType.MouseMove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseMove.html))
            Event.current.Use();
    }
}

```

![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HandleUtilityDistanceToCone.png).  
  
Additional resources: [DistanceToCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCircle.html), [DistanceToCube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCube.html), [DistanceToLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToLine.html).
* * *
