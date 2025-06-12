* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-skinnedMotionVectors.html

#  [SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html).skinnedMotionVectors
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html "Go to SkinnedMeshRenderer Component in the Manual")
skinnedMotionVectors; 
### Description
Specifies whether skinned motion vectors should be used for this renderer.
If set to true, the SkinnedMeshRenderer generates vectors using skinning data from the current and last frame to calculate the per-pixel object movement. This means that the motion vector buffer captures small object movements. (For example; a character moving an arm.)  
  
Skinned motion vectors are important for characters with animation. There is a cost to skinned motion vectors, though; they require twice as much memory per skinned mesh because the graphics memory on the GPU becomes double buffered (one buffer for the current frame and one buffer for the previous frame). The buffers track motion between frames; the velocity is the current frame's position minus the last frame's position.  
  
Additional resources: [DepthTextureMode.MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DepthTextureMode.MotionVectors.html), [Renderer.motionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-motionVectorGenerationMode.html), [PassType.MotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.MotionVectors.html), [SystemInfo.supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMotionVectors.html).
* * *
