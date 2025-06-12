* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport.html

# CrashReport
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Holds data for a single application crash event and provides access to all gathered crash reports.
If compiled with appropriate settings, Unity will try to gather useful information, like location and thread stack traces, when your application crashes. Upon the next application start, if the data gathering was successful, all crash information will be accessible using this API.  
  
To enable crash report generation, in iOS player settings set "Script Call Optimization" option to "Fast but no Exceptions". After you build your Xcode project in Unity, open it and edit trampoline file: Classes/CrashReporter.h. Change ENABLE_CUSTOM_CRASH_REPORTER define from 0 to 1. Note that the iOS Player Settings has a Crash Reporting setting with an "Enable CrashReport API".  
  
Note: this API currently is available only for iOS targets.  
  
Additional resources: [CrashReport.reports](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport-reports.html).
```
using UnityEngine;  
  

// This example shows a list of crash reports (if available),
// and allows you to output crash data to console, or
// delete them.
public class Crashes : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        var reports = CrashReport.reports[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport-reports.html);
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Crash reports:");
        foreach (var r in reports)
        {
            GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Crash: " + r.time);
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Log"))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(r.text);
            }
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Remove"))
            {
                r.Remove();
            }
            GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
        }
    }
}

```

### Static Properties
Property | Description  
---|---  
[lastReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport-lastReport.html) | Returns last crash report, or null if no reports are available.  
[reports](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport-reports.html) | Returns all currently available reports in a new array.  
### Properties
Property | Description  
---|---  
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport-text.html) | Crash report data as formatted text.  
[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport-time.html) | Time, when the crash occured.  
### Public Methods
Method | Description  
---|---  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport.Remove.html) | Remove report from available reports list.  
### Static Methods
Method | Description  
---|---  
[RemoveAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport.RemoveAll.html) | Remove all reports from available reports list.  
* * *
