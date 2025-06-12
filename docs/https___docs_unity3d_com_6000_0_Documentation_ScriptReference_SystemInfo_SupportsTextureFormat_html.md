* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsTextureFormat.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).SupportsTextureFormat
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
public static bool SupportsTextureFormat([TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format); 
### Parameters
Parameter | Description  
---|---  
format | The [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) format to look up.  
### Returns
**bool** True if the format is supported. 
### Description
Is texture format supported on this device?
It is good practice to check that the device supports a texture format before using it.  
  
Additional resources: [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) enum.
* * *
