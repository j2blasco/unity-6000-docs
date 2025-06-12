* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).color
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color; 
### Description
Sets the color of handles. Color is a persistent state and affects any handles drawn after it is set. Use [DrawingScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope.html) to set the color for a block of handles without affecting the color of other handles.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SliderHandle.png)   
_White cone that points to 0,0,0._
```
// Name this script "SliderHandleEditor"
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(SliderHandle))]
public class SliderHandleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    // Simple script that creates a Slide Handle that
    // allows you to drag a 'look at' point along the X axis  
  
    void OnSceneGUI()
    {
        SliderHandle t = (target as SliderHandle);  
  
        // Set the colour of the next handle to be drawn:
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.magenta[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-magenta.html);  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lookTarget = Handles.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Slider.html)(t.lookTarget, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 0, 0), 2, Handles.ConeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html), 0.1f);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(target, "Changed Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) Look Target[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html)");
            t.lookTarget = lookTarget;
            t.Update();
        }
    }
}

```

And the script attached to this GameObject:
```
// Name this script "SliderHandle"
using UnityEngine;
using System.Collections;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class SliderHandle : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lookTarget = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.LookAt(lookTarget);
    }
}

```

* * *
