* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FormatBytes.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).FormatBytes
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
public static string FormatBytes(int bytes); 
### Description
Returns a text for a number of bytes.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class FormatBytesExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints "100 bytes"
        print(EditorUtility.FormatBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FormatBytes.html)(100));  
  
        // prints "2.0 KB"
        print(EditorUtility.FormatBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FormatBytes.html)(2048));
    }
}

```

* * *
