* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-fontStyle.html

#  [TextMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html).fontStyle
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextMesh.html "Go to TextMesh Component in the Manual")
[FontStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FontStyle.html) fontStyle; 
### Description
The font style to use (for dynamic fonts).
If this is set to a value other then normal, the font style set in the font importer is overriden with a custom style. This is only supported for fonts set to use dynamic font rendering. Other fonts will always render in normal style.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GetComponent<TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)>().fontStyle = FontStyle.Bold[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FontStyle.Bold.html);
    }
}

```

* * *
