* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UnlockBufferAfterWrite.html

#  [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).UnlockBufferAfterWrite
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
public void UnlockBufferAfterWrite(int countWritten); 
### Parameters
Parameter | Description  
---|---  
countWritten | Number of elements written to the buffer. Counted from the first element.  
### Description
Ends a write operation to the buffer
This call ends a write operation on the buffer. When you call this method, Unity marks the native array returned by the corresponding [GraphicsBuffer.LockBufferForWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.LockBufferForWrite.html) call as unusable, you don't need to call the Dispose method on the array.
* * *
