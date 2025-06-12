* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html

# ILogHandler
interface in UnityEngine
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
Interface for custom log handler implementation.
ILogHandler interface to ease unit-testing and mocking of loggers.
```
using UnityEngine;
using System.Collections;
using System.IO;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
public class MyFileLogHandler : ILogHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html)
{
    private FileStream m_FileStream;
    private StreamWriter m_StreamWriter;
    private ILogHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.html) m_DefaultLogHandler = Debug.unityLogger.logHandler;  
  
    public MyFileLogHandler()
    {
        string filePath = Application.persistentDataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html) + "/MyLogs.txt";  
  
        m_FileStream = new FileStream(filePath, FileMode.OpenOrCreate, FileAccess.ReadWrite);
        m_StreamWriter = new StreamWriter(m_FileStream);  
  
        // Replace the default debug log handler
        Debug.unityLogger.logHandler = this;
    }  
  
    public void LogFormat(LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) logType, UnityEngine.Object context, string format, params object[] args)
    {
        m_StreamWriter.WriteLine(String.Format(format, args));
        m_StreamWriter.Flush();
        m_DefaultLogHandler.LogFormat(logType, context, format, args);
    }  
  
    public void LogException(Exception exception, UnityEngine.Object context)
    {
        m_DefaultLogHandler.LogException(exception, context);
    }
}  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private static ILogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogger.html) logger = Debug.unityLogger[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug-unityLogger.html);
    private static string kTAG = "MyGameTag";
    private MyFileLogHandler myFileLogHandler;  
  
    void Start()
    {
        myFileLogHandler = new MyFileLogHandler();  
  
        logger.Log(kTAG, "MyGameClass Start.");
    }
}

```

### Public Methods
Method | Description  
---|---  
[LogException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.LogException.html) | A variant of ILogHandler.LogFormat that logs an exception message.  
[LogFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ILogHandler.LogFormat.html) | Logs a formatted message.  
* * *
