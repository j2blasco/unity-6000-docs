* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-localBounds.html

#  [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html).localBounds
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html "Go to AnimationClip Component in the Manual")
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) localBounds; 
### Description
AABB of this Animation Clip in local space of Animation component that it is attached too.
It is precomputed on import for imported models/animations based on the meshes that this animation clip affects. This bounding box is specific to the mesh(es) that this clip is attached to during import, i.e. this means that it is calculated based on the file that is part of and on the "Model" file if you're using Model@Animation notation.
* * *
