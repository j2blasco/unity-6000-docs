* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).Height
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
public static [GUILayoutOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayoutOption.html) Height(float height); 
### Description
Option passed to a control to give it an absolute height.
**Note:** This option will override the Automatic height Layout parameter  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutHeight.png)  
_Fixed Height for a GUI Control._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a  button with a  fixed height
    void OnGUI()
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("A Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) with fixed height", GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(300));
    }
}

```

* * *
