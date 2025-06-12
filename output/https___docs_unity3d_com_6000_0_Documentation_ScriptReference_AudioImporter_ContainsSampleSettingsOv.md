* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.ContainsSampleSettingsOverride.html

#  [AudioImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html).ContainsSampleSettingsOverride
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
public bool ContainsSampleSettingsOverride([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) platformGroup); 
## Declaration
public bool ContainsSampleSettingsOverride(string platform); 
### Parameters
Parameter | Description  
---|---  
platformGroup | The platform for which to query if this AudioImporter has an override.  
  
See [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the complete list of options.  
platform | The platform for which to query if this AudioImporter has an override.  
  
See [BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) for the complete list of options and type the desired platform enum name in the form of a string.  
### Returns
**bool** Returns true if the platform is currently overriden in this AudioImporter. 
### Description
Returns whether the sample settings for a specified build target are currently overridden.
* * *
