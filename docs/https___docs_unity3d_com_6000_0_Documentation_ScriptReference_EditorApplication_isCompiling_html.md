* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isCompiling.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).isCompiling
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
isCompiling; 
### Description
Is editor currently compiling scripts? (Read Only)
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/FinishCompiling.png)   
_Editor Window that tells you if Unity is compiling scripts._
```
// Small example that shows when scripts are being compiled.  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class isCompilingExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Is compiling?")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindowWithRect(typeof(isCompilingExample), new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 200, 200));
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Compiling:", EditorApplication.isCompiling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isCompiling.html) ? "Yes" : "No");  
  
        this.Repaint();
    }
}

```

* * *
