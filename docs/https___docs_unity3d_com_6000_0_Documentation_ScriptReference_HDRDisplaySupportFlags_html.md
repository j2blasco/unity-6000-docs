* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplaySupportFlags.html

# HDRDisplaySupportFlags
enumeration
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
A set of flags that describe the level of HDR display support available on the GPU and driver.
See [SystemInfo.hdrDisplaySupportFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hdrDisplaySupportFlags.html) for more details.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplaySupportFlags.None.html) | Denotes that support for HDR displays is not available for the GPU and the driver. It doesn't indicate HDR compatibility for your monitor's display.  
[Supported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplaySupportFlags.Supported.html) | Denotes that support for HDR displays is available for the GPU and the driver. It doesn't indicate HDR compatibility for your monitor's display.  
[RuntimeSwitchable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplaySupportFlags.RuntimeSwitchable.html) | Denotes that the GPU and driver can change whether the output is performed in HDR or SDR ranges at runtime when connected to a HDR display.  
[AutomaticTonemapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplaySupportFlags.AutomaticTonemapping.html) | Denotes if the GPU and driver support automatic tone mapping to HDR displays.  
* * *
