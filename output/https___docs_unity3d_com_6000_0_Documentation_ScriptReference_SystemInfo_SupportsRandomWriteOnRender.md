* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRandomWriteOnRenderTextureFormat.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).SupportsRandomWriteOnRenderTextureFormat
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
public static bool SupportsRandomWriteOnRenderTextureFormat([RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) format); 
### Parameters
Parameter | Description  
---|---  
format | The format to look up.  
### Returns
**bool** True if the format can be used for random access writes. 
### Description
Tests if a RenderTextureFormat can be used with [RenderTexture.enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html).
Random access write might not be supported on all [RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) as this is API/driver/hardware dependent.
* * *
