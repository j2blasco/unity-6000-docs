* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Focus.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).Focus
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
public void Focus(); 
### Description
Moves keyboard focus to another EditorWindow.
The [Focus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Focus.html) public method controls which window is active for use of the keyboard. In the examples below the active EditorWindow keyboard is changed to a different EditorWindow keyboard. Additional resources: [focusedWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-focusedWindow.html).  
  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Window1.png)  
_Focus one window by pressing the button on other window._
```
// A window that changes state to the second window when
// the button is pressed.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class FocusExample1 : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public static FocusExample1 Instance = null;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Focus Example 1")]
    static void Init()
    {
        Instance = GetWindow<FocusExample1>("Focus1");
    }

    void CreateGUI()
    {
        var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)(() => {
            if (FocusExample2.Instance)
                FocusExample2.Instance.Focus();
        });
        button.text = "Focus Window2";
        rootVisualElement.Add(button);    
    }
}

```

```
// Second window.

using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class FocusExample2 : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    public static FocusExample2 Instance = null;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Focus Example 2")]
    static void Init()
    {
        Instance = GetWindow<FocusExample2>("Focus2");
    }
    void CreateGUI()
    {
        var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)(() => {
            if (FocusExample1.Instance)
                FocusExample1.Instance.Focus();
        });
        button.text = "Focus Window1";
        rootVisualElement.Add(button);
    }
}

```

* * *
