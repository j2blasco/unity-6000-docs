* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConsoleWindowUtility.GetConsoleLogCounts.html

#  [ConsoleWindowUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConsoleWindowUtility.html).GetConsoleLogCounts(out int, out int, out int)
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
### Description
Retrieve the current counts of messages in the Console Window.
Returns the current number of Error, Warning, and Log messages that are currently present in the Console Window.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Print Log Counts")]
    static void PrintLogCounts()
    {
        ConsoleWindowUtility.GetConsoleLogCounts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConsoleWindowUtility.GetConsoleLogCounts.html)(out int error, out int warning, out int log);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Errors: {error}, Warnings: {warning}, Info: {log}");
    }
}

```

* * *
