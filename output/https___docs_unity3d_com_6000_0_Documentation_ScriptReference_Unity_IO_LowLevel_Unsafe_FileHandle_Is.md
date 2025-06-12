* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.IsValid.html

#  [FileHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.html).IsValid
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
public bool IsValid(); 
### Returns
**bool** True, if this FileHandle represents an open file; otherwise, false. 
### Description
Reports whether this FileHandle instance is valid.
A FileHandle is invalid if the open operation failed or the FileHandle has been closed. (Creating a new FileHandle object is also invalid.)
* * *
