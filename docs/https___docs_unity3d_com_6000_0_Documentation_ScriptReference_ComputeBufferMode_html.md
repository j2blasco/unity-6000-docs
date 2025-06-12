* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.html

# ComputeBufferMode
enumeration
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
Intended usage of the buffer.
Use this enum to convey the intended usage of the buffer to the engine, so that Unity can decide where and how to store the buffer contents.
### Properties
Property | Description  
---|---  
[Immutable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.Immutable.html) | Static buffer, only initial upload allowed by the CPU  
[Dynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.Dynamic.html) | Dynamic buffer.  
[SubUpdates](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.SubUpdates.html) | Dynamic, unsynchronized access to the buffer.  
* * *
