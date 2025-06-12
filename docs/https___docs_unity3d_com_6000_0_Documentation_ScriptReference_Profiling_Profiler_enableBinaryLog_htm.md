* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableBinaryLog.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).enableBinaryLog
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
enableBinaryLog; 
### Description
Enables the logging of profiling data to a file.
When enabled, the Unity player saves profiling data to the file specified in the [Profiler.logFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-logFile.html) file. The player automatically assigns the file extension, “.raw” to this log file. You can load this file in the Unity Editor using the Profiler window to view the data.  
  
You must also set [Profiler.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) to `true`. If the buffer is too small to output the profiler data you will see a message in the debug log "Skipping profile frame. Receiver can not keep up with the amount of data sent". Use [Profiler.maxUsedMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-maxUsedMemory.html) to raise the buffer memory.  
  
**Note:** In the following example, on the WebGL platform, the log file is outputted to a path like the following: `/idbfs/some-hash/profiler.raw`. To find this file, use your browser's developer tools. You can also use `File.Open` with the same path that you used to load the data, and use [UnityWebRequest.Post](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html) to send it to a web server. 
```
using UnityEngine;
using System.Collections;
using UnityEngine.Profiling;
using System.IO;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        StartCoroutine(RunProfiler());
    }  
  
    IEnumerator RunProfiler()
    {
        // Specify the profiler output file
        Profiler.logFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-logFile.html) = Path.Join(Application.persistentDataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html), "mylog.raw");
        Profiler.enableBinaryLog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableBinaryLog.html) = true;
        // Start profiler
        Profiler.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) = true;
        // Optional, if more memory is needed for the buffer
        Profiler.maxUsedMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-maxUsedMemory.html) = 256 * 1024 * 1024;  
  
        // Run profiling for 5 seconds
        yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(5.0f);  
  
        // Stop profiler
        Profiler.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) = false;
        // It is important to change the log file so it can be opened
        Profiler.logFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-logFile.html) = "";
    }
}

```

* * *
