* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.SetOverrideSampleSettings.html

#  [AudioImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html).SetOverrideSampleSettings
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
public bool SetOverrideSampleSettings([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) platformGroup, [AudioImporterSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) settings); 
## Declaration
public bool SetOverrideSampleSettings(string platform, [AudioImporterSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) settings); 
### Parameters
Parameter | Description  
---|---  
platformGroup | The platform which will have the sample settings overridden.  
  
See [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the complete list of options.  
platform | The platform which will have the sample settings overridden.  
  
See [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the complete list of options and type the desired platform enum name in the form of a string.  
settings | The override settings for the given platform.  
### Returns
**bool** Returns true if the settings were successfully overriden. Some setting overrides are not possible for the given platform, in which case false is returned and the settings are not registered. 
### Description
Sets the override sample settings for the given platform.
For certain target platforms, overriding the audio importer settings may be beneficial for performance or other reasons. This function enables the registration of override settings specific to a given platform.
* * *
