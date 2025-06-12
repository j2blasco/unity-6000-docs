* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage-enabled.html

#  [Coverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html).enabled
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
enabled; 
### Returns
**bool** Returns true if code coverage is enabled; otherwise, returns false. 
### Description
Enables or disables code coverage. Note that Code Coverage can affect the performance.
```
// Create a new C# script called _CodeCoverageMenuItem_ and place it under the _Editor_ folder.  
  
// This class creates a toggle menu item under **Code Coverage > Enable Code Coverage**.
// Use it to enable/disable Code Coverage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html).  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.TestTools;  
  
class CodeCoverageMenuItem
{
    const string EnableCodeCoverageItemName = "Code Coverage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html)/Enable Code Coverage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html)";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)(EnableCodeCoverageItemName, false)]
    static void EnableCodeCoverage()
    {
        Coverage.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage-enabled.html) = !Coverage.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage-enabled.html);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)(EnableCodeCoverageItemName, true)]
    static bool EnableCodeCoverageValidate()
    {
        Menu.SetChecked[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.SetChecked.html)(EnableCodeCoverageItemName, Coverage.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage-enabled.html));
        return true;
    }
}

```

* * *
