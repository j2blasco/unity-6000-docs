* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireCube.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawWireCube
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
public static void DrawWireCube([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size); 
### Description
Draw a wireframe box with `center` and `size`.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
//this class should exist somewhere in your project
public class WireCubeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size;  
  
    // ...other code...
}

```

```
// Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) script. This would go into an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) directory.
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(WireCubeExample))]
public class WireBoxExample : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    void OnSceneGUI()
    {
        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        WireCubeExample myObj = (WireCubeExample)target;
        Handles.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireCube.html)(myObj.transform.position, myObj.size);
    }
}

```

* * *
