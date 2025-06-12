* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.GetTargetSettings.html

#  [VideoClipImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html).GetTargetSettings
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
public [VideoImporterTargetSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoImporterTargetSettings.html) GetTargetSettings(string platform); 
### Parameters
Parameter | Description  
---|---  
platform | Platform name.  
### Returns
**VideoImporterTargetSettings** The platform-specific import settings. Throws an exception if the platform is unknown. 
### Description
Returns the platform-specific import settings for the specified platform.
The options for the `platform` string are as follows: 
  * Standalone
  * Web
  * iPhone
  * Android
  * WSA
  * tvOS


* * *
