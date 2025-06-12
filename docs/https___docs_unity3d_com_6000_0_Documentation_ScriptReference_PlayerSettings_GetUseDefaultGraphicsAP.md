* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetUseDefaultGraphicsAPIs.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetUseDefaultGraphicsAPIs
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
## Declaration
public static bool GetUseDefaultGraphicsAPIs([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform); 
### Parameters
Parameter | Description  
---|---  
platform | Platform to get the flag for.  
### Returns
**bool** Should best available graphics API be used. 
### Description
Is a build platform using automatic graphics API choice?
By default each platform is using "automatic" graphics API detection and picks the best available one. However it is possible to change that to explicitly limit the graphics APIs used, see [SetGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetGraphicsAPIs.html).  
  
Additional resources: [SetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetUseDefaultGraphicsAPIs.html), [GetGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetGraphicsAPIs.html), [SetGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetGraphicsAPIs.html).
* * *
