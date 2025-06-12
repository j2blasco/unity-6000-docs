* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).EndGUI
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
public static void EndGUI(); 
### Description
End a 2D GUI block and get back to the 3D handle GUI.
Additional resources: [Handles.BeginGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BeginEndGUI2.png)  
_GUI in the Scene View._
```
// Change the transform values for the selected object.
// When selected this script starts and the handleExample is managed.
// The HandlesGUI.BeginGUI() and EndGUI() functions allow the shieldArea
// to be changed back to five, which is the starting value.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(HandleExample))]
class HandleExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    protected virtual void OnSceneGUI()
    {
        HandleExample handleExample = (HandleExample)target;  
  
        if (handleExample == null)
        {
            return;
        }  
  
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();
        style.normal.textColor = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = handleExample.transform.position + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 2f;
        string posString = position.ToString();  
  
        Handles.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html)(position,
            posString + "\nShieldArea: " +
            handleExample.shieldArea.ToString(),
            style
        );  
  
        Handles.BeginGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Reset Area", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100)))
        {
            handleExample.shieldArea = 5;
        }
        Handles.EndGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html)();  
  
        Handles.DrawWireArc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html)(
            handleExample.transform.position,
            handleExample.transform.up,
            -handleExample.transform.right,
            180,
            handleExample.shieldArea);  
  
        handleExample.shieldArea =
            Handles.ScaleValueHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html)(handleExample.shieldArea,
                handleExample.transform.position + handleExample.transform.forward * handleExample.shieldArea,
                handleExample.transform.rotation,
                1, Handles.ConeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html), 1);
    }
}

```

Add a script that specifies the object that can be animated in the SceneView.
```
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class HandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float shieldArea = 5.0f;
}

```

* * *
