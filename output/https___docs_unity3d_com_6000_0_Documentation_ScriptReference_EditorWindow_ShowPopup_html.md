* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowPopup.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).ShowPopup
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
public void ShowPopup(); 
### Description
Shows an Editor window using popup-style framing.
This means the window has no frame, and is not draggable. It is intended for showing something like a popup menu within an existing window.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ShowPopupEx.png)  
  
Opening a window using this method will not give it the functionality of a popup window, only the styling. For full popup functionality (eg, auto closing when the window loses focus), use [PopupWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindow.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class ShowPopupExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ShowPopup Example")]
    static void Init()
    {
        ShowPopupExample window = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<ShowPopupExample>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2, 250, 150);
        window.ShowPopup();
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("This is an example of EditorWindow.ShowPopup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowPopup.html)");
        rootVisualElement.Add(label);

        var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        button.text = "Agree!";
        button.clicked += () => this.Close();
        rootVisualElement.Add(button);
    }
}

```

* * *
