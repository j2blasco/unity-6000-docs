* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.ToString.html

#  [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).ToString
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
Returns a formatted string for the bounds.
Defaults to two digits displayed (format="F2"). For more information, see Microsoft's documentation on [Standard numeric format strings](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings#FFormatString).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(bounds.ToString()); // output displayed as: "Center: (0.00, 0.00, 0.00), Extents: (0.00, 0.00, 0.00)"
    }
}

```

* * *
