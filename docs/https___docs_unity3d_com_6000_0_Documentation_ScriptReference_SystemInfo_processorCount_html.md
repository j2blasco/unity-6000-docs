* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorCount.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).processorCount
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
processorCount; 
### Description
Number of processors present (Read Only).
This is number of "logical processors" as reported by the operating system, also commonly called as "number of hardware threads". Note that some CPUs have different amounts of "physical cores" and "logical cores" (for example, many Intel CPUs have 4 physical cores and 8 logical cores in so called "hyper threaded" fashion). This method reports the latter. On Android, it reports the number of active processors.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Prints using the following format - "4" on a quad-core CPU.
        print(SystemInfo.processorCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorCount.html));
    }
}

```

Additional resources: [SystemInfo.processorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorType.html), [SystemInfo.processorFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorFrequency.html).
* * *
