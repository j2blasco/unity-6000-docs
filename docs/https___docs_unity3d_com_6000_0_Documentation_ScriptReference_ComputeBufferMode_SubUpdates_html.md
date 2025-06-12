* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.SubUpdates.html

#  [ComputeBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.html).SubUpdates
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
Dynamic, unsynchronized access to the buffer.
Same as [ComputeBufferMode.Dynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.Dynamic.html) except Unity does not perform any CPU-GPU synchronization; if the user modifies an area of the buffer where the GPU is currently reading from, the results are undefined. For example, this mode together with [GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html) can be used to implement circular buffers.
* * *
