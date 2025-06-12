* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.ExtractStackTraceNoAlloc.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).ExtractStackTraceNoAlloc
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
## Declaration
public static int ExtractStackTraceNoAlloc(byte* buffer, int bufferMax, string projectFolder); 
### Parameters
Parameter | Description  
---|---  
buffer | Target buffer to receive the callstack text  
bufferMax | Max number of bytes to write  
projectFolder | Project folder path, to clean up path names  
### Description
Populate an unmanaged buffer with the current managed call stack as a sequence of UTF-8 bytes, without allocating GC memory. Returns the number of bytes written into the buffer.
* * *
