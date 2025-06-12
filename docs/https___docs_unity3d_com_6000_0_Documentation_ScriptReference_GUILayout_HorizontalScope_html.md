* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScope.html

# HorizontalScope
class in UnityEngine
/
Implemented in:[UnityEngine.IMGUIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.IMGUIModule.html)
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
### Description
Disposable helper class for managing [BeginHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html) / [EndHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html).
All controls rendered inside this element will be placed horizontally next to each other. The `using` statement means [BeginHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html) and [EndHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html) are not needed.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutHorizontal.png)  
_Horizontal Layout._
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Starts a horizontal group
        using (var horizontalScope = new GUILayout.HorizontalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScope.html)("box"))
        {
            GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the first button");
            GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm to the right");
        }
        // Now the group is ended.
    }
}

```

### Constructors
Constructor | Description  
---|---  
[GUILayout.HorizontalScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScope-ctor.html) | Create a new HorizontalScope and begin the corresponding horizontal group.  
* * *
