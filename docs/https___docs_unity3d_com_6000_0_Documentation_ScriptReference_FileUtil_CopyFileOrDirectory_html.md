* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.CopyFileOrDirectory.html

#  [FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html).CopyFileOrDirectory
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
public static void CopyFileOrDirectory(string source, string dest); 
### Description
Copies a file or a directory.
This function's path can be relative to the project root folder or be an absolute path.  
  
All file separators should be forward ones "/".  
  
Make sure to include the name of the files or directories at the end of the `dest` argument.  
  

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CopyFile : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Copy Something")]
    static void CopySomething()
    {
        FileUtil.CopyFileOrDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.CopyFileOrDirectory.html)("sourcepath/YourFileOrFolder", "destpath/YourFileOrFolder");
    }
}

```

* * *
