* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCulling.Compute.html

#  [StaticOcclusionCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCulling.html).Compute
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
public static bool Compute(); 
### Description
Used to generate static occlusion culling data.
This function will run asynchronously until the data is generated but you can check the status of the computation using the [isRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCulling-isRunning.html) property.  
  
The memory limit (specified in bytes) is a hint to the PVS baking system about the likely memory requirements.  
  
Additional resources: [GenerateInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCulling.GenerateInBackground.html), [isRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCulling-isRunning.html).
* * *
