* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Clone.html

#  [ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html).Clone
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
public [ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html) Clone([Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
allocator | The allocator to use to allocate the memory for the copy.  
### Returns
**ObjectChangeEventStream** A copy of the stream that contains the same events, but in a separate memory lcoation. 
### Description
Creates a copy of this stream with the specified allocator.
Depending on the allocator used, the resulting copy needs to be manually disposed by the caller.
* * *
