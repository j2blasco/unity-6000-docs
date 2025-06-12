* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).FlexibleSpace
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
public static void FlexibleSpace(); 
### Description
Insert a flexible space element.
Flexible spaces use up any leftover space in a layout.  
  
**Note:** This will override the [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html) and [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html)  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutFlexibleSpace.png)  
_Flexible Space in a GUILayout Area._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float sliderValue = 1.0f;  
  
    void OnGUI()
    {
        // Wrap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Wrap.html) everything in the designated GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Area
        GUILayout.BeginArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 200, 60));
        // Begin the singular Horizontal Group[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Group.html)
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
        // Place a Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) normally
        GUILayout.RepeatButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.RepeatButton.html)("A button with\ntwo lines");
        // Place a space between the button and the vertical area
        // so it fits the whole area
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        // Arrange two more Controls vertically beside the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
        GUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html)();
        GUILayout.Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Box.html)("Value:" + Mathf.Round[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Round.html)(sliderValue));
        sliderValue = GUILayout.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalSlider.html)(sliderValue, 0.0f, 10f);  
  
        // End the Groups and Area
        GUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html)();
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
        GUILayout.EndArea[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html)();
    }
}

```

* * *
