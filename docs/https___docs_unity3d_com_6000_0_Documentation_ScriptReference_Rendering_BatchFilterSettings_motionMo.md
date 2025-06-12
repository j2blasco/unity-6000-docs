* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings-motionMode.html

#  [BatchFilterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html).motionMode
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
[MotionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MotionVectorGenerationMode.html) motionMode; 
### Description
Specifies how to generate motion vectors in this draw range.
This corresponds to [Renderer.motionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-motionVectorGenerationMode.html). 
  * If you set this to [MotionVectorGenerationMode.Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MotionVectorGenerationMode.Camera.html), Unity doesn't render the draw commands in per-object motion vector passes, regardless of each draw command's [BatchDrawCommand.flags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand-flags.html).
  * If you set this to [MotionVectorGenerationMode.Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MotionVectorGenerationMode.Object.html), Unity renders the draw commands in per-object motion vector passes if the draw command has [BatchDrawCommandFlags.HasMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.HasMotion.html) set.
  * If you set this to [MotionVectorGenerationMode.ForceNoMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MotionVectorGenerationMode.ForceNoMotion.html), Unity renders the draw commands in per-object motion vector passes if the draw command has [BatchDrawCommandFlags.HasMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.HasMotion.html) set, and it should output a zero motion vector. This behavior relies on the used shader being implemented correctly.


* * *
