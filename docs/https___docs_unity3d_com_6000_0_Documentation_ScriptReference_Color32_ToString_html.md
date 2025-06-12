* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.ToString.html

#  [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html).ToString
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
public string ToString(); 
## Declaration
public string ToString(string format); 
## Declaration
public string ToString(string format, IFormatProvider formatProvider); 
### Parameters
Parameter | Description  
---|---  
format | A numeric format string.  
formatProvider | An object that specifies culture-specific formatting.  
### Description
Returns a formatted string for this color.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) color = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        print(color.ToString("x"));
    }
}

```

* * *
