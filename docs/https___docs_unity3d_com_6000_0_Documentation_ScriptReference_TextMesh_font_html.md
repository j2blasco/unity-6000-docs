* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-font.html

#  [TextMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html).font
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
[Font](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html) font; 
### Description
The [Font](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html) used.
Additional resources: [text mesh component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextMesh.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set the text of the attached Text mesh
        Font[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html) newFont = new Font[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Font.html)();
        GetComponent<TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)>().font = newFont;
    }
}

```

* * *
