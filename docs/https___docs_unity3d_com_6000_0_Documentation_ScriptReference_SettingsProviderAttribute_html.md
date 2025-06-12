* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProviderAttribute.html

# SettingsProviderAttribute
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
Attribute used to register a new [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html). Use this attribute to decorate a function that returns an instance of a [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html). If the function returns null, no SettingsProvider appears in the Settings window.
```
using System.IO;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyCustomSettingsProvider : SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)
{
    const string k_MyCustomSettingsPath = "Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html)/MyCustomSettings.asset";
    public MyCustomSettingsProvider(string path, SettingsScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) scope)
        : base(path, scope) {}  
  
    public static bool IsSettingsAvailable()
    {
        return File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(k_MyCustomSettingsPath);
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateMyCustomSettingsProvider()
    {
        if (IsSettingsAvailable())
        {
            return new MyCustomSettingsProvider("MyCustomSettings", SettingsScope.Project[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.Project.html));
        }  
  
        // Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) doesn't exist yet. No need to display anything in the Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) window.
        return null;
    }
}

```

### Constructors
Constructor | Description  
---|---  
[SettingsProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProviderAttribute-ctor.html) | Creates a new SettingsProviderAttribute used to register new SettingsProvider.   
* * *
