* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-depth.html

#  [GUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html).depth
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
depth; 
### Description
The sorting depth of the currently executing GUI behaviour.
Set this to determine ordering when you have different scripts running simultaneously. GUI elements drawn with lower depth values will appear on top of elements with higher values (ie, you can think of the depth as "distance" from the camera).  
  
**Note:** To see this example working, you will need to create 2 scripts. Remember to name the scripts with the same name as the class names, else it will not work.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUIDepth.png)  
_One Button behind the other._
```
using UnityEngine;
using System.Collections;  
  
// Makes this button go back in depth  
  
public class Example1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int guiDepth = 0;
    public Example2 example2;  
  
    private float buttonX, buttonY;  
  
    void Start()
    {
        buttonX = (Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2) - 100;
        buttonY = (Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2) - 100;
    }  
  
    void OnGUI()
    {
        GUI.depth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-depth.html) = guiDepth;
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) size = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)("button");
        size.fontSize = 16;  
  
        if (GUI.RepeatButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(buttonX, buttonY, 200, 100), "Go Backwards", size))
        {
            guiDepth = 1;
            example2.guiDepth = 0;
        }
    }
}

```

And copy this other example to another script:
```
using UnityEngine;
using System.Collections;  
  
// Makes this button go back in depth  
  
public class Example2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int guiDepth = 1;
    public Example1 example1;  
  
    private float buttonX, buttonY;  
  
    void Start()
    {
        buttonX = (Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2)  - 50;
        buttonY = (Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2) - 50;
    }  
  
    void OnGUI()
    {
        GUI.depth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-depth.html) = guiDepth;
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);  
  
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) size = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)("button");
        size.fontSize = 16;  
  
        if (GUI.RepeatButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(buttonX, buttonY, 200, 100), "Go Backwards", size))
        {
            guiDepth = 1;
            example1.guiDepth = 0;
        }
    }
}

```

* * *
