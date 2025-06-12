* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.AreaScope.html

# AreaScope
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
Disposable helper class for managing [BeginArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html) / [EndArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html).
[BeginArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html) is called at construction, and [EndArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html) is called when the instance is disposed. By default, any GUI controls made using GUILayout are placed in the top-left corner of the screen. If you want to place a series of automatically laid out controls in an arbitrary area, use [GUILayout.BeginArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html) to define a new area for the automatic layouting system to use.  
  
Additional resources: [BeginArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html), [EndArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutArea.png)  
_Explained Area of the example._
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        using (var areaScope = new GUILayout.AreaScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.AreaScope.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 100)))
        {
            GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Click me");
            GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Or me");
        }
    }
}

```

### Constructors
Constructor | Description  
---|---  
[GUILayout.AreaScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.AreaScope-ctor.html) | Create a new AreaScope and begin the corresponding Area.  
* * *
