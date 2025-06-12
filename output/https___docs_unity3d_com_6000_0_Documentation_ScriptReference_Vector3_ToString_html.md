* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ToString.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).ToString
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
Returns a formatted string for this vector.
Defaults to two digits displayed (format="F2"). For more information, see Microsoft's documentation on [Standard numeric format strings](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings#FFormatString).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // let Unity show these as (1.00, 2.00, 3.00)
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 2, 3);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(vector.ToString());  
  
        // unity displays by default (1.23, 5.68, 9.01)
        vector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.234f, 5.678f, 9.012f);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(vector.ToString());  
  
        // but we can show this using format - 3 numbers after the decimal point
        // (1.234, 5.678, 9.012)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(vector.ToString("F3"));  
  
        // now let's create some longer numbers
        vector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f / 3.0f, -Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html), Mathf.Exp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Exp.html)(-2.0f));  
  
        // we get (0.333333, -3.141593, 0.135335)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("fractional part is 6: " + vector.ToString("F6"));  
  
        // note how F8 cannot display these numbers as we want
        // (0.33333330, -3.14159300, 0.13533530)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("fractional part is 8: " + vector.ToString("F8"));
    }
}

```

* * *
