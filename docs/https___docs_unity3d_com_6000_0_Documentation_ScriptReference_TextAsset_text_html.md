* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html

#  [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html).text
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html "Go to TextAsset Component in the Manual")
text; 
### Description
The text contents of the file as a string. (Read Only)
Encodings are detected and interpreted automatically. Supported encodings are: 
  * UTF-32 Big or Little Endian with a byte order mark,
  * UTF-16 Big or Little Endian with a byte order mark,
  * UTF-8 with a byte order mark,
  * UTF-8 without a byte order mark. This encoding is used as a fallback, if the above encodings can't decode the file without missing characters.


To use a specific encoding to decode a file, use [TextAsset.bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html) and C# encoding classes.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) asset;  
  
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(asset.text);
    }
}

```

Additional resources: [bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html), [GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html), [Text Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html).
* * *
