* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.Instancing.html

#  [StereoRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.html).Instancing
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
Single pass VR rendering ( via instanced rendering ).
This is an optimization over the [StereoRenderingPath.SinglePass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.SinglePass.html) method. The Scene graph is traversed only once and there will be only one instanced draw call issued for each render node thus reducing the bandwidth required to render the Scene.  
  
This method is compatible with the regular instanced. Special hardware support is required for this to run. The main render target has to be an array render target. Scene culling & shadow map rendering is shared between the eyes.  
  
Additional resources: [PlayerSettings.stereoRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-stereoRenderingPath.html).
* * *
