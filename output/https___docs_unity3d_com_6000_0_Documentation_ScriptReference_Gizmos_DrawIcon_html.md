* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawIcon
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
public static void DrawIcon([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, string name, bool allowScaling = true); 
## Declaration
public static void DrawIcon([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, string name, bool allowScaling = true, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) tint = Color(255,255,255,255)); 
### Parameters
Parameter | Description  
---|---  
center | The location of the icon in world space.  
name | The file name of the image relative to the **Assets/Gizmos** folder.  
allowScaling | Whether the icon is permitted to be scaled.  
tint | A tint applied to the icon. (Optional).  
### Description
Draw an icon at a position in the Scene view.
Place the image file in the **Assets/Gizmos** folder.  
  
DrawIcon can be used to allow important objects in your game to be selected quickly.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnDrawGizmos()
    {
        // Draws the Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) bulb icon at position of the object.
        // Because we draw it inside OnDrawGizmos the icon is also pickable
        // in the scene view.  
  
        Gizmos.DrawIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawIcon.html)(transform.position, "Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) Gizmo.tiff", true, Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
    }
}

```

* * *
