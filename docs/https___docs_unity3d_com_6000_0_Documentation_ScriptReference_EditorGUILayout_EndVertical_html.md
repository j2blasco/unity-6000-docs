* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).EndVertical
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
Additional resources: [EditorGUILayout.BeginVertical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/BeginEndVerticalExample.png)  
_Vertical Compound group._
```
// Create a Vertical Compound Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class EndVerticalCS : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Begin-End Vertical usage")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EndVerticalCS));
        window.Show();
    }  
  
    void OnGUI()
    {
        Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) r = EditorGUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html)("Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)");
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(r, GUIContent.none[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent-none.html)))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Go here");
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("I'm inside the button");
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("So am I");
        EditorGUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html)();
    }
}

```

* * *
