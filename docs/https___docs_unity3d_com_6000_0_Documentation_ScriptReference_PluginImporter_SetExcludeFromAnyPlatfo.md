* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetExcludeFromAnyPlatform.html

#  [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).SetExcludeFromAnyPlatform
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
public void SetExcludeFromAnyPlatform(string platformName, bool excludedFromAny); 
## Declaration
public void SetExcludeFromAnyPlatform([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform, bool excludedFromAny); 
### Parameters
Parameter | Description  
---|---  
platformName | Target platform.  
### Description
Exclude platform from compatible platforms when **Any Platform** is set to true.
Useful when you want to apply logic - "plugin is compatible with any platform except this platform".  
  
Note: [PluginImporter.SetCompatibleWithPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetCompatibleWithPlatform.html) or [PluginImporter.SetCompatibleWithEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetCompatibleWithEditor.html) will override this setting.  
  
You can also use [PluginImporter.GetImporters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetImporters.html) to check whether or not your plugin is compatible with specific platforms.
* * *
