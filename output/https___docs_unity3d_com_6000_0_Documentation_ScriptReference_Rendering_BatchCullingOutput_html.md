* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput.html

# BatchCullingOutput
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Contains the output data where OnPerformCulling will write draw commands into.
### Properties
Property | Description  
---|---  
[customCullingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput-customCullingResult.html) | Optional pointer to custom culling result data.  
[drawCommands](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput-drawCommands.html) | A single-element array of BatchCullingOutputDrawCommands that OnPerformCulling can write into without unnecessary copying.  
* * *
