* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceModel.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).deviceModel
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
deviceModel; 
### Description
The model of the device (Read Only).
Exact format of model name is operating system dependent, for example iOS device names typically look like "iPhone6,1", whereas Android device names are often in "manufacturer model" format (e.g. "LGE Nexus 5" or "SAMSUNG-SM-G900A"). The returned model can also be a very generic name (e.g. "PC") if the actual model name is not available or relevant on the current platform. The returned value will usually be similar to the one shown in the operating system's "About Device" or "System Information" screen (or equivalent). This information will often also include the manufacturer.  
  
Will return [SystemInfo.unsupportedIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-unsupportedIdentifier.html) on platforms which don't support this property.  
  
Additional resources: [deviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html).
* * *
