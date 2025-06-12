* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).Label
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
public static void Label([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, string text); 
## Declaration
public static void Label([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) image); 
## Declaration
public static void Label([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content); 
## Declaration
public static void Label([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, string text, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
## Declaration
public static void Label([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) content, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style); 
### Parameters
Parameter | Description  
---|---  
position | The position in 3D space as seen from the current handle camera.  
text | The text to display on the label.  
image | The texture to display on the label.  
content | The text, image, and tooltip for this label.  
style | The style to use for this label. If left out, the `label` style from the current GUISkin is used.  
### Description
Creates a text label for a handle that is positioned in 3D space.
Labels have no user interaction and canot be clicked on. Labels are always rendered in normal style.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HandlesLabel.png)  
_Label in the Scene view._
```
//This script is not an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) script
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)  
  
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class HandleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float shieldArea = 5.0f;  
  
    // Use this for initialization
    void Start()
    {
    }  
  
    // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) is called once per frame
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
    }
}

```

```
//Create a folder named "Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)" in your project directory, if the directroy does not already have one. Place this script in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) folder.  
  
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
// lets you visualize some info of the transform  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(HandleExample))]
class LabelHandle : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    void OnSceneGUI()
    {
        HandleExample handleExample = (HandleExample)target;
        if (handleExample == null)
        {
            return;
        }  
  
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        Handles.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html)(handleExample.transform.position + Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * 2,
            handleExample.transform.position.ToString() + "\nShieldArea: " +
            handleExample.shieldArea.ToString());  
  
        Handles.BeginGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Reset Area", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(100)))
        {
            handleExample.shieldArea = 5;
        }
        Handles.EndGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html)();  
  

        Handles.DrawWireArc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html)(handleExample.transform.position,
            handleExample.transform.up,
            -handleExample.transform.right,
            180,
            handleExample.shieldArea);
        handleExample.shieldArea =
            Handles.ScaleValueHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html)(handleExample.shieldArea,
                handleExample.transform.position + handleExample.transform.forward * handleExample.shieldArea,
                handleExample.transform.rotation,
                1,
                Handles.ConeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ConeHandleCap.html),
                1);
    }
}

```

* * *
