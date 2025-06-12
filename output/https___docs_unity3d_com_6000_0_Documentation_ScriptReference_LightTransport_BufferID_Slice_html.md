* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.Slice.html

#  [BufferID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html).Slice
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
public BufferSlice<T> Slice(ulong offset); 
### Parameters
Parameter | Description  
---|---  
offset | The offset to use for the slice, measured in elements of the passed the type.  
### Returns
**BufferSlice <T>** A typed slice aliasing the BufferID. 
### Description
Constructs a typed slice from the BufferID.
* * *
