* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LinkButton.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).LinkButton
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
public static bool LinkButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label); 
## Declaration
public static bool LinkButton([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the control. The underline is done with the bottom border so set the size accordingly.  
label | Label of the link.  
### Returns
**bool** `true` when the user clicks the link. 
### Description
Make a clickable link label.
The label has an hyperlink style and returns true when clicked.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  

class EditorGUILinkButton : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/EditorGUILinkButton")]
    static void Init()
    {
        var window = GetWindow<EditorGUILinkButton>();
        window.Show();
    }  
  
    void OnGUI()
    {
        var label = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Link Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)");
        var size = EditorStyles.linkLabel.CalcSize(label);
        if (EditorGUI.LinkButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LinkButton.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(50, 50, size.x, size.y), label))
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Clicked");
    }
}

```

* * *
