* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddControl.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).AddControl
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
public static void AddControl(int controlId, float distance); 
### Parameters
Parameter | Description  
---|---  
controlId | The ID that is recorded as the nearest control if the mouse cursor is near the handle.  
distance | The distance from the mouse cursor to the handle.  
### Description
Record a distance measurement from a handle.
All handles call this with their controlID during layout, then use nearestControl to check if they got the mouseDown.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);

public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float value = 1.0f;
}

// A tiny custom editor for ExampleScript component.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ExampleScript))]
public class ExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    // Custom in-scene UI for when ExampleScript component is selected.
    public void OnSceneGUI()
    {
        var controlID = GUIUtility.GetControlID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html)(FocusType.Passive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.Passive.html));
        var evt = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);

        var t = target as ExampleScript;
        var tr = t.transform;
        var pos = tr.position;

        switch (evt.GetTypeForControl(controlID))
        {
            case EventType.Layout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Layout.html):
            case EventType.MouseMove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseMove.html):
                // Set the nearest control ID to "controlID" if the mouse cursor is
                // near or directly above the solid disc handle.
                var distanceToHandle = HandleUtility.DistanceToCircle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCircle.html)(pos, t.value);
                HandleUtility.AddControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddControl.html)(controlID, distanceToHandle);
                break;
            case EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html):
                // Log the nearest control ID if the click is near or directly above
                // the solid disc handle.
                if (controlID == HandleUtility.nearestControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-nearestControl.html) && evt.button == 0)
                {
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"The nearest control is {controlID}.");

                    GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) = controlID;
                    evt.Use();
                }
                break;
            case EventType.MouseUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html):
                if (GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) == controlID && evt.button == 0)
                {
                    GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) = 0;
                    evt.Use();
                }
                break;
            case EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html):
                // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) an orange solid disc where the object is.
                Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 0.8f, 0.4f, 1);
                Handles.DrawSolidDisc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidDisc.html)(pos, tr.up, t.value);
                break;
        }
    }
}

```

* * *
