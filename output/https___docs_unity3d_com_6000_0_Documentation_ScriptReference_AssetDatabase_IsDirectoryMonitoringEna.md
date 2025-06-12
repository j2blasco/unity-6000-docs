* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsDirectoryMonitoringEnabled.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsDirectoryMonitoringEnabled
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
public static bool IsDirectoryMonitoringEnabled(); 
### Returns
**bool** Returns true when Directory Monitoring is enabled. Returns false otherwise. 
### Description
Reports whether Directory Monitoring is enabled.
Turn Directory Monitoring on or off in Preferences settings or in script with EditorPrefs.SetBool("DirectoryMonitoring", boolValue).  
Directory Monitoring can be disabled with command line flag [[-DisableDirectoryMonitor]] and Directory Monitoring is automatically disabled when Unity detects symlinks in the project.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.Profiling;
using System.IO;  
  
public class DirectoryMonitoringTest
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Directory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html) Monitoring Test")]
    static void DirectoryMonitoringBenchmark()
    {
        var BenchmarkCount = 1;  
  
        //Disabling the Directory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html) Monitoring will use a brute force scanning method to evaluate which files in the project have been changed, and is much slower
        EditorPrefs.SetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html)("DirectoryMonitoring", false);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Is Directory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html) Monitoring Enabled? - " + AssetDatabase.IsDirectoryMonitoringEnabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsDirectoryMonitoringEnabled.html)());  
  
        Benchmark(BenchmarkCount);
        BenchmarkCount++;  
  
        EditorPrefs.SetBool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetBool.html)("DirectoryMonitoring", true);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Is Directory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html) Monitoring Enabled? - " + AssetDatabase.IsDirectoryMonitoringEnabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsDirectoryMonitoringEnabled.html)());
        Benchmark(BenchmarkCount);
    }  
  
    //This test will show faster scan time when using Directory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html) Monitoring
    static void Benchmark(int BenchmarkCount)
    {
        var relativePath = "Assets/test_file01.txt";
        if (!File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(relativePath))
        {
            using (StreamWriter sw = File.CreateText(relativePath))
            {
                sw.WriteLine("Hello");
                sw.WriteLine("And");
                sw.WriteLine("Welcome");
            }
        }  
  
        Profiler.BeginSample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginSample.html)("Benchmark " + BenchmarkCount); ;
        AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(relativePath);
        Profiler.EndSample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EndSample.html)();  
  
        AssetDatabase.DeleteAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAsset.html)(relativePath);
        AssetDatabase.Refresh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html)();
    }
}
```

* * *
