* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.html

# LightingWindowTab
class in UnityEditor
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
### Description
Base class to add custom tabs to the Lighting window.
See also [LightingWindowEnvironmentSection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Rendering;
using UnityEngine;
using UnityEngine.Rendering;  
  
class CustomLightingTab : LightingWindowTab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.html)
{
    public override void OnEnable()
    {
        titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Custom");
        priority = 1; // This tab will be the second option in the toolbar
    }  
  
    public override void OnGUI()
    {
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("My Custom Lighting Tab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Tab.html) !!");
    }
}

```

In this example, a new section is added in the Lighting window with the name Custom.
### Properties
Property | Description  
---|---  
[priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab-priority.html) | The priority of the tab in the header toolbar.  
[titleContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab-titleContent.html) | The title of the tab.  
### Public Methods
Method | Description  
---|---  
[FocusTab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.FocusTab.html) | FocusTab will open the lighting window with this tab selected.  
[HasHelpGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.HasHelpGUI.html) | Returns true if window has a doc button in the header.  
[OnBakeButtonGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnBakeButtonGUI.html) | OnBakeButtonGUI is called to draw a button at the bottom of the tab.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnDisable.html) | OnDisable is called when this Inspector override is not used anymore.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnEnable.html) | OnEnable is called when this Inspector override is used.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnGUI.html) | A callback that is called when drawing the main section of the tab.  
[OnHeaderSettingsGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnHeaderSettingsGUI.html) | A callback that is called when drawing the header icons in the top right of the tab.  
[OnSelectionChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnSelectionChange.html) | Called when the selection changes.  
[OnSummaryGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.OnSummaryGUI.html) | A callback that is called when drawing the bottom section of the tab.  
* * *
