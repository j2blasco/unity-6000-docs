* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.UnregisterCustomDependencyPrefixFilter.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).UnregisterCustomDependencyPrefixFilter
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
public static uint UnregisterCustomDependencyPrefixFilter(string prefixFilter); 
### Parameters
Parameter | Description  
---|---  
prefixFilter | Prefix filter for the custom dependencies to unregister.  
### Returns
**uint** Number of custom dependencies removed. 
### Description
Removes custom dependencies that match the prefixFilter.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.Assertions;
public class CustomDependenciesExample
{
    public static void AddAndRemoveCustomDependencies()
    {
        // Example to to illustrate how UnregisterCustomDependencyPrefixFilter works. Not a useful scenario.
        AssetDatabase.RegisterCustomDependency[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RegisterCustomDependency.html)("MyDependencySystem/DepA", Hash128.Compute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Compute.html)("Hello"));
        AssetDatabase.RegisterCustomDependency[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RegisterCustomDependency.html)("MyDependencySystem/DepB", Hash128.Compute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.Compute.html)("World"));  
  
        var unregistered = AssetDatabase.UnregisterCustomDependencyPrefixFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.UnregisterCustomDependencyPrefixFilter.html)("MyDependencySystem/");
        Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)(2, unregistered);
    }
}
```

* * *
