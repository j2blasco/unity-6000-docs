* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.ReplaceDirectory.html

#  [FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html).ReplaceDirectory
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
public static void ReplaceDirectory(string src, string dst); 
### Description
Replaces a directory.
Replaces the directory located at **dst** with the directory located at **src**. if **dst** doesnt exists it copies the file. If **dst** exists then it deletes it and copies the directory at **src** to **dst** Additional resources: [FileUtil.ReplaceFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.ReplaceFile.html).  
  

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ReplaceDir : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Replace Directory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html)")]
    static void ReplaceDirectory()
    {
        FileUtil.ReplaceDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.ReplaceDirectory.html)("sourcepath/YourFolder", "destpath/YourNewFolder");
    }
}

```

* * *
