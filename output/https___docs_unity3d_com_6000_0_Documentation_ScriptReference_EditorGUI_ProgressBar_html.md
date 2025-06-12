* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).ProgressBar
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
public static void ProgressBar([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, float value, string text); 
### Parameters
Parameter | Description  
---|---  
totalPosition | Rectangle on the screen to use in total for both the control.  
value | Value that is shown.  
### Description
Makes a progress bar.
Value goes from 0 to 1, where 0 means 0% of the bar filled and 1 means the bar is at 100% fully filled  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIProgressBar.png)  
_Progress bar in an Editor Window._
```
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Draw the armor and damage with bars in an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window  
  
public class EditorGUIProgressBar : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float armor = 20;
    float damage  = 80;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) Info")]  
  
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EditorGUIProgressBar), false, "DisplayInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DisplayInfo.html)");
        window.Show();
    }  
  
    void OnGUI()
    {
        armor = EditorGUI.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 15), "Armor", Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(armor), 0, 100);
        damage = EditorGUI.IntSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 6, 15), "Damage", Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(damage), 0, 100);  
  
        EditorGUI.ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 45, position.width - 6, 20), armor / 100, "Armor");
        EditorGUI.ProgressBar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 70, position.width - 6, 20), damage / 100, "Damage");
    }
}

```

* * *
