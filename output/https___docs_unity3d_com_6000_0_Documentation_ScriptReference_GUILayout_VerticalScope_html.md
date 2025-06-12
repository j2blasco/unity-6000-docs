* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.VerticalScope.html

# VerticalScope
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
Disposable helper class for managing [BeginVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html) / [EndVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html).
All controls rendered inside this element will be placed vertically below each other. The group is automatically closed when the scope ends.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutVertical.png)  
_Vertical Layout._
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        // Starts a vertical group
        using (var verticalScope = new VerticalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.VerticalScope.html)("box"))
        {
            GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the top button");
            GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the bottom button");
        }
        // The group is now ended
    }
}

```

### Constructors
Constructor | Description  
---|---  
[GUILayout.VerticalScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.VerticalScope-ctor.html) | Create a new VerticalScope and begin the corresponding vertical group.  
* * *
