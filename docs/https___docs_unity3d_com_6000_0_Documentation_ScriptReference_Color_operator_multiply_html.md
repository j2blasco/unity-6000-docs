* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_multiply.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).operator *
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) operator *([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) a, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) b); 
### Description
Multiplies two colors together. Each component is multiplied separately.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) grayColor = Color.gray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gray.html) * Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
    }
}

```

* * *
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) operator *([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) a, float b); 
### Description
Multiplies color `a` by the float `b`. Each color component is scaled separately.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) whiteColor = Color.gray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gray.html) * 2;
    }
}

```

* * *
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) operator *(float b, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) a); 
### Description
Multiplies color `a` by the float `b`. Each color component is scaled separately.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) whiteColor = 2 * Color.gray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gray.html);
    }
}

```

* * *
