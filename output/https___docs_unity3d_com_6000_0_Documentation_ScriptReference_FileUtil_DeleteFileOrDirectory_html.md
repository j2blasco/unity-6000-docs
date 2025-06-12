* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.DeleteFileOrDirectory.html

#  [FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html).DeleteFileOrDirectory
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
public static bool DeleteFileOrDirectory(string path); 
### Description
Deletes a file or a directory given a path.
This function's path is relative to the project root folder but it can also accept absolute paths.  
  
All file separators should be forward ones "/" (Unix style).  
  

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class DeleteFile : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Delete Something")]
    static void DeleteSomething()
    {
        FileUtil.DeleteFileOrDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.DeleteFileOrDirectory.html)("yourPath/YourFileOrFolder");
    }
}

```

* * *
