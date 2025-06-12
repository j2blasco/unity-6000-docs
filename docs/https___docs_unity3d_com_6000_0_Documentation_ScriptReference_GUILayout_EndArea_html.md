* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).EndArea
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
public static void EndArea(); 
### Description
Close a GUILayout block started with BeginArea.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutArea.png)   
_Explained Area of the example._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUILayout.BeginArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100));
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Click me");
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Or me");
        // Ends the area started above
        GUILayout.EndArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html)();
    }
}

```

* * *
