* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.CrashReporting-crashReportFolder.html

#  [CrashReporting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.CrashReporting.html).crashReportFolder
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
crashReportFolder; 
### Description
Contains the path to the crash report folder on Windows.
Crash reports are stored in the following location:  
  
`%TMP%\CompanyName\ProductName\Crashes`  
  
Crash reports are assigned a unique path on startup allowing you to determine in advance where a crash report will be stored if one occurs.  
  
Additional resources: [PlayerSettings.companyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-companyName.html), [PlayerSettings.productName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-productName.html). 
```
// Required namespaces
using System.IO;                // For working with file system operations, such as directories and files.
using UnityEngine;  
  
public class CrashReportExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Get the folder path where crash reports are stored
        string crashReportPath = UnityEngine.Windows.CrashReporting.crashReportFolder;
        
        // Log the path to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Crash reports are stored in: " + crashReportPath);
        
        // Check if the folder exists, and if it does, list crash reports
        if (Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)(crashReportPath))
        {
            string[] crashReports = Directory.GetFiles(crashReportPath);
            foreach (string report in crashReports)
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Found crash report: " + report);
            }
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Crash report folder does not exist.");
        }
    }
}

```

* * *
