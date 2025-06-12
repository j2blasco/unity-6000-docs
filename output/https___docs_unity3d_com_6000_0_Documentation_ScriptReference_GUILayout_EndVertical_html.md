* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).EndVertical
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
public static void EndVertical(); 
### Description
Close a group started with BeginVertical.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutVertical.png)   
_Vertical Layout._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html)("box");  
  
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the top button");
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the bottom button");  
  
        // End the vertical group we started above
        GUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html)();
    }
}

```

* * *
