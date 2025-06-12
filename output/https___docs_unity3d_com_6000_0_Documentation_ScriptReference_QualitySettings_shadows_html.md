* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).shadows
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
[ShadowQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.html) shadows; 
### Description
Real-time Shadows type to be used.
This determines which type of shadows should be used. The available options are Hard and Soft Shadows, Hard Shadows Only and Disable Shadows.  
  
Additional resources: [Light.shadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadows.html).
```
using UnityEngine;  
  
// Let the shadow quality be selected  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private int selection = 0;
    private string[] itemName = {"   Disable   ", "   HardOnly   ", "   Hard and Soft   "};  
  
    void Start()
    {
        QualitySettings.shadows[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html) = ShadowQuality.All[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.All.html);
    }  
  
    void OnGUI()
    {
        GUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html)("Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)");
        selection = GUILayout.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.SelectionGrid.html)(selection, itemName, 1, GUILayout.MinWidth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html)(200), GUILayout.MinHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html)(100));
        GUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html)();  
  
        switch (selection)
        {
            case 0: QualitySettings.shadows[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html) = ShadowQuality.Disable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.Disable.html); break;
            case 1: QualitySettings.shadows[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html) = ShadowQuality.HardOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.HardOnly.html); break;
            default: QualitySettings.shadows[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-shadows.html) = ShadowQuality.All[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.All.html); break;
        }
    }
}

```

* * *
