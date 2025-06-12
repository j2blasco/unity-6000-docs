* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.CopyFileOrDirectoryFollowSymlinks.html

#  [FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html).CopyFileOrDirectoryFollowSymlinks
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
public static void CopyFileOrDirectoryFollowSymlinks(string source, string dest); 
### Description
Copies the file or directory.
Copies from the path suppplied as the `source` parameter to the path supplied as the `dest` parameter.  
  
In presence of symbolic links (macOS only), the actual files to which symbolic links point to are copied, not the symbolic links themselves.  
  
Additional resources: [FileUtil.CopyFileOrDirectory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.CopyFileOrDirectory.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CopyFileSymLink : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Copy Something SymLink")]
    static void CopySomethingSymLink()
    {
        FileUtil.CopyFileOrDirectoryFollowSymlinks[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.CopyFileOrDirectoryFollowSymlinks.html)("sourcepath/YourFileOrFolder", "destpath/YourFileOrFolder");
    }
}

```

* * *
