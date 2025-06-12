* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SinglePassStereoMode.SideBySide.html

#  [SinglePassStereoMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SinglePassStereoMode.html).SideBySide
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
Render stereo to the left and right halves of a single, double-width render target.
In side-by-side single-pass stereo rendering, the rendering pipeline traverses the scene graph only once while issuing two draw calls for each render node. Each eye is rendered to one side of the render target. The main render target must be a twice as wide as a single-eye target. Scene culling and shadow map rendering is shared between both eyes. Side-by-side rendering is significantly faster than multi-pass rendering for VR, but is a little slower than instancing or multiview modes. 
* * *
