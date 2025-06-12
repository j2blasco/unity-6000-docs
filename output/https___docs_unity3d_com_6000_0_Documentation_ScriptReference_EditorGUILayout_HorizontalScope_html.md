* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HorizontalScope.html

# HorizontalScope
class in UnityEditor
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
Disposable helper class for managing [BeginHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html) / [EndHorizontal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html).
This is an extension to [GUILayout.HorizontalScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScope.html). It can be used for making compound controls  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BeginEndHorizontalExample.png)  
_Horizontal Compound group._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Create a Horizontal Compound Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
class HorizontalScopeExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Horizontal scope usage")]
    static void Init()
    {
        var window = GetWindow<HorizontalScopeExample>();
        window.Show();
    }  
  
    void OnGUI()
    {
        using (var h = new EditorGUILayout.HorizontalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HorizontalScope.html)("Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)"))
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(h.rect, GUIContent.none[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html)))
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Go here");
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("I'm inside the button");
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("So am I");
        }
    }
}

```

### Properties
Property | Description  
---|---  
[rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HorizontalScope-rect.html) | The rect of the horizontal group.  
### Constructors
Constructor | Description  
---|---  
[EditorGUILayout.HorizontalScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HorizontalScope-ctor.html) | Create a new HorizontalScope and begin the corresponding horizontal group.  
* * *
