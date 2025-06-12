* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Show.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).Show
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
public void Show(); 
## Declaration
public void Show(bool immediateDisplay); 
### Parameters
Parameter | Description  
---|---  
immediateDisplay | Immediately display [Show](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Show.html).  
### Description
Show the EditorWindow window.
[EditorWindow.Show](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Show.html) displays any window that has been created. In the script example below the window is created with no addition functionality. Many of the script examples in [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) are more complex. 
```
// Create an empty Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window and show it

using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

public class ShowWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ShowWindow")]
    public static void ShowExample()
    {
        ShowWindow wnd = GetWindow<ShowWindow>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("ShowWindow");
        wnd.Show();
    }
}

```

* * *
