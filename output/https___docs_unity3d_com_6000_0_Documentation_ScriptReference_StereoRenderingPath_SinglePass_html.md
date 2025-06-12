* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.SinglePass.html

#  [StereoRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.html).SinglePass
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
Single pass VR rendering ( via double-wide render texture ).
This is a faster rendering path for VR compared to the [StereoRenderingPath.MultiPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.MultiPass.html). The speed is achieved by traversing the Scene graph only once while issuing two draw calls for each render node.  
  
The main render target has to be a double wide render target. Scene culling & shadow map rendering is shared between the eyes.  
  
Additional resources: [PlayerSettings.stereoRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-stereoRenderingPath.html).
* * *
