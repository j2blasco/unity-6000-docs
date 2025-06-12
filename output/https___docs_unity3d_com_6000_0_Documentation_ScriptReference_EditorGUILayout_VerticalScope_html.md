* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.VerticalScope.html

# VerticalScope
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
Disposable helper class for managing [BeginVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html) / [EndVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html).
This is an extension to [GUILayout.VerticalScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.VerticalScope.html). It can be used for making compound controls  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BeginEndVerticalExample.png)  
_Vertical Compound group._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Create a Vertical Compound Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
class VerticalScopeExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Vertical scope usage")]
    static void Init()
    {
        var window = GetWindow<VerticalScopeExample>();
        window.Show();
    }  
  
    void OnGUI()
    {
        using (var v = new EditorGUILayout.VerticalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.VerticalScope.html)("Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)"))
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(v.rect, GUIContent.none[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html)))
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
[rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.VerticalScope-rect.html) | The rect of the vertical group.  
### Constructors
Constructor | Description  
---|---  
[EditorGUILayout.VerticalScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.VerticalScope-ctor.html) | Create a new VerticalScope and begin the corresponding vertical group.  
* * *
