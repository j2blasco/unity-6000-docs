* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html

#  [ObjectNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.html).NicifyVariableName
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
public static string NicifyVariableName(string name); 
### Description
Make a displayable name for a variable.
This function will insert spaces before capital letters and remove optional `m_`, `_` or `k` followed by uppercase letter in front of the name.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        // prints "My Variable"
        print(ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)("MyVariable"));
        // prints "The Other Variable"
        print(ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)("m_TheOtherVariable"));
        // prints "Some Constant"
        print(ObjectNames.NicifyVariableName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.NicifyVariableName.html)("kSomeConstant"));
    }
}

```

* * *
