* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).OnInspectorGUI
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
public void OnInspectorGUI(); 
### Description
Implement this function to make a custom inspector.
Inside this function you can add your own custom IMGUI based GUI for the inspector of a specific object class.  
  
**Note:** This function has to be overridden in order to work.  
  
Additional resources: [Editor.DrawDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawDefaultInspector.html).  
  
The example below shows how a custom label can be created by using `override`:
```
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Creates a custom Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) on the inspector for all the scripts named ScriptName
// Make sure you have a ScriptName script in your
// project, else this will not work.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ScriptName))]
public class TestOnInspector : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public override void OnInspectorGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html) ("This is a Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) in a Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)");
    }
}

```

* * *
