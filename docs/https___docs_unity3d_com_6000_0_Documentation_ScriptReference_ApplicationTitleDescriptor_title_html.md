* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-title.html

#  [ApplicationTitleDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor.html).title
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
title; 
### Description
Setting this field will set the complete editor title without using any of the other fields of [ApplicationTitleDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

public class WindowTitleExample
{
    private static void CustomTitleBar(ApplicationTitleDescriptor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor.html) desc)
    {
        desc.title = $"My Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Custom Title version: {Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html)}";
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/Setup custom title bar")]
    static void Setup()
    {
        EditorApplication.updateMainWindowTitle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-updateMainWindowTitle.html) -= CustomTitleBar;
        // This callback will be triggered when a new scene is loaded or when Unity starts.
        EditorApplication.updateMainWindowTitle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-updateMainWindowTitle.html) += CustomTitleBar;
        EditorApplication.UpdateMainWindowTitle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.UpdateMainWindowTitle.html)();
    }
}

```

* * *
