* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.ReplaceFile.html

#  [FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html).ReplaceFile
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
public static void ReplaceFile(string src, string dst); 
### Description
Replaces a file.
Replaces the file located at **dst** with the file located at **src**. if **dst** doesnt exists it just copies the file. If **dst** exists then it deletes it and copies the file at **src** to **dst** Additional resources: [FileUtil.ReplaceDirectory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.ReplaceDirectory.html).  
  

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ReplaceFile : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Replace Something")]
    static void ReplaceSomething()
    {
        FileUtil.ReplaceFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.ReplaceFile.html)("sourcepath/YourFileOrFolder", "destpath/YourReplacedFileOrFolder");
    }
}

```

* * *
