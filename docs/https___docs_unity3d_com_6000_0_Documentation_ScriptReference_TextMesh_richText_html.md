* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh-richText.html

#  [TextMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html).richText
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
richText; 
### Description
Enable HTML-style tags for Text Formatting Markup.
Supported tags are:  
<color="htmlcolor">colored text</color>, where "htmlcolor" is a html color string, like "#ff0000" or "red".  
<b>bold text</b>  
<i>italic text</i>  
<size=20>sized text</size>  
<material=1>render using custom material index</material>  
<quad material=1 size=20 x=0.1 y=0.1 width=0.5 height=0.5/>, to render a single quad using the given material and UVs, used for embedding images in text.  
These are only supported for fonts set to use dynamic font rendering, except for the 'color', 'material' and 'quad' tags.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        GetComponent<TextMesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html)>().richText = true;
    }
}

```

* * *
