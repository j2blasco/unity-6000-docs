* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).Space
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
public static void Space(float pixels); 
### Description
Insert a space in the current layout group.
The direction of the space is dependent on the layout group you're currently in when issuing the command. If in a vertical group, the space will be vertical. **Note:** This will override the [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html) and [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutSpace.png)  
_Space of 20px between two buttons._
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the first button");  
  
        // Insert 20 pixels of space between the 2 buttons.
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(20);  
  
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm a bit further down");
    }
}

```

In horizontal groups, the `pixels` are measured horizontally:
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the first button");  
  
        // Insert 20 pixels of space between the 2 buttons.
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(20);  
  
        GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("I'm the second button");
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
    }
}

```

An example that is based on [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html):
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Example of using GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html) inside an EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).
// Clicking on the buttons changes the size of the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html).  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)")]
    static void CreateWindow()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow<ExampleClass>();
        window.Show();
    }  
  
    private float spaceSize = 20.0f;  
  
    void OnGUI()
    {
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Button1: Move Button2 down by 2 pixels"))
        {
            spaceSize = spaceSize + 2.0f;
        }  
  
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(spaceSize);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Button2: Move up by 1 pixel"))
        {
            spaceSize = spaceSize - 1.0f;
        }
    }
}

```

* * *
