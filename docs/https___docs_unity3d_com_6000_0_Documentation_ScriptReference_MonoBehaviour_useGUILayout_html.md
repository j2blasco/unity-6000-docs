* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour-useGUILayout.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).useGUILayout
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
useGUILayout; 
### Description
Disabling this lets you skip the GUI layout phase.
It can only be used if you do not use [GUI.Window](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) and GUILayout inside of this OnGUI call.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        //Disabling this lets you skip the GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) layout phase.
        useGUILayout = false;
    }
}

```

* * *
