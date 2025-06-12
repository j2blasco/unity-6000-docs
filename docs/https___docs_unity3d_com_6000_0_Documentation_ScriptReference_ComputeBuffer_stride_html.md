* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer-stride.html

#  [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html).stride
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
stride; 
### Description
Size of one element in the buffer in bytes (Read Only).
Must be a multiple of 4 and less than 2048, and match the size of the buffer type in the shader. See [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) for cross-platform compatibility information.  
  
The stride you declare for your compute buffer must match the stride in the buffer declaration of the shader you use it with. If the two stride values do not match, Unity may crash without warning.  
  
Compute Buffers in Unity use Unit Stride. Additional resources: [count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer-count.html).
* * *
