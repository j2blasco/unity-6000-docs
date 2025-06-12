* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.VirtualFileSystem.GetLocalFileSystemName.html

#  [VirtualFileSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.VirtualFileSystem.html).GetLocalFileSystemName
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
public static bool GetLocalFileSystemName(string vfsFileName, out string localFileName, out ulong localFileOffset, out ulong localFileSize); 
### Parameters
Parameter | Description  
---|---  
vfsFileName | Virtual file entry to find.  
localFileName | Out parameter containing the file on the local filesystem.  
localFileOffset | Out parameter containing the offset inside of file on the local filesystem.  
localFileSize | Out parameter containing the size inside of file on the local filesystem.  
### Returns
**bool** Details were successfully found. 
### Description
This method looks up the virtual file entry specified, and returns the details of that file within the file on the local filesystem.
It populates the localFileName, localFileOffset, and localFileSize parameters with the path of the file on the local filesystem that contains the virtual file, and the offset and size of the virtual file within it. This method returns true if the details were successfully found. It returns false if it was not possible. This can happen if the virtual file is contained in a memory filesystem, or in a compressed file.
* * *
