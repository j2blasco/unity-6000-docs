* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Button.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).Button
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
public static bool Button([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) direction, float size, float pickSize, [Handles.CapFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CapFunction.html) capFunction); 
### Parameters
Parameter | Description  
---|---  
position | The position to draw the button in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
direction | The rotation of the button in the space of [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).  
size | The visual size of the handle. Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
pickSize | The size of the button for the purpose of detecting a click. Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
capFunction | The draw style of the button.  
### Returns
**bool** True when the user clicks the button. 
### Description
Make a 3D Button.
This button works like one drawn with [GUI.Button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html), but it has a 3D position and is drawn by a handle function.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ButtonHandle.png)  
_Button Handle as a rectangle in the Scene View._  
  
Add the following script to your Assets folder as ButtonExample.cs and add the ButtonExample component to an object in a Scene.
```
using UnityEngine;  
  
public class ButtonExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {}

```

Add the following script to Assets/Editor as ButtonExampleEditor.cs and select the object with the ButtonExample component.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ButtonExample)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
class ButtonExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    protected virtual void OnSceneGUI()
    {
        ButtonExample buttonExample = (ButtonExample)target;  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position = buttonExample.transform.position + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 2f;
        float size = 2f;
        float pickSize = size * 2f;  
  
        if (Handles.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Button.html)(position, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), size, pickSize, Handles.RectangleHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.RectangleHandleCap.html)))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The button was pressed!");
    }
}

```

* * *
