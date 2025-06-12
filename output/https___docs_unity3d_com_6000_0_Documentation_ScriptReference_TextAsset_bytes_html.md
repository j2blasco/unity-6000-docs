* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html

#  [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html).bytes
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
bytes; 
### Description
The raw bytes of the text asset. (Read Only)
This returns an array containing all the data in a file, including invisible characters such as byte-order marks for Unicode text files.  
  
This property returns a new C# array with a copy of the asset data every time it's called. To get access the original asset data without creating an additional copy, use [GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Drag a .jpg or .png file onto the image variable.
    TextAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) image;  
  
    void Start()
    {
        var tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(4, 4);
        tex.LoadImage(image.bytes);
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = tex;
    }
}

```

Additional resources: [text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html), [GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html), [Text Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html).
* * *
