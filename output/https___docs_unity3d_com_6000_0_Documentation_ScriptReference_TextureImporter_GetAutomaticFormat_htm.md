* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetAutomaticFormat.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).GetAutomaticFormat
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
## Declaration
public [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) GetAutomaticFormat(string platform); 
### Parameters
Parameter | Description  
---|---  
platform | Accepts the following platform strings; `Standalone`, `Web`, `iPhone`, `Android`, `Windows Store Apps`, and `tvOS`.  
### Returns
**TextureImporterFormat** Format chosen by the system for the provided platform, TextureImporterFormat.Automatic if the platform does not exist. 
### Description
Returns the TextureImporterFormat that would be automatically chosen for this platform.
* * *
