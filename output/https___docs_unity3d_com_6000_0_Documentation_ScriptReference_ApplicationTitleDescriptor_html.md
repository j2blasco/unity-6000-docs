* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor.html

# ApplicationTitleDescriptor
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
Utility class containing all the information necessary to format Unity Editor main window title. All the various fields are concatenated to create a fully formed title. If only [ApplicationTitleDescriptor.title](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-title.html) is provided, this will become the complete title.
See also: [EditorApplication.updateMainWindowTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-updateMainWindowTitle.html).
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
### Properties
Property | Description  
---|---  
[activeSceneName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-activeSceneName.html) | Unity active scene.  
[codeCoverageEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-codeCoverageEnabled.html) | Is code coverage enabled.  
[projectName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-projectName.html) | Current project name.  
[targetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-targetName.html) | What is the runtime target for a Unity build.  
[title](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-title.html) | Setting this field will set the complete editor title without using any of the other fields of ApplicationTitleDescriptor.  
[unityProductName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-unityProductName.html) | Unity version name in the form of: Unity <number> <release stream (optional)>.  
[unityVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor-unityVersion.html) | Unity version number.  
* * *
