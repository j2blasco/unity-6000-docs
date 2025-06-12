* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.html

# XcScheme
class in UnityEditor.iOS.Xcode
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
Represents an Xcode scheme (xcscheme file).
```
#if UNITY_IOS
string schemePath = pathToBuiltProject + "/Unity-iPhone.xcodeproj/xcshareddata/xcschemes/Unity-iPhone.xcscheme";  
  
var xcscheme = new XcScheme[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.html)();
xcscheme.ReadFromFile(schemePath);  
  
xcscheme.SetMetalValidationOnRun(XcScheme.MetalValidation.Extended[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.MetalValidation.Extended.html));
xcscheme.SetFrameCaptureModeOnRun(XcScheme.FrameCaptureMode.Metal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.FrameCaptureMode.Metal.html));
xcscheme.AddArgumentPassedOnLaunch("--myarg = 1");  
  
xcscheme.WriteToFile(schemePath);
#endif

```

### Constructors
Constructor | Description  
---|---  
[XcScheme](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme-ctor.html) | Creates a new instance of the XcScheme class.  
### Public Methods
Method | Description  
---|---  
[AddArgumentPassedOnLaunch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.AddArgumentPassedOnLaunch.html) | Adds command line arguments to be passed on launch.  
[GetBuildConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.GetBuildConfiguration.html) | Returns the build configuration used for running.  
[ReadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.ReadFromFile.html) | Reads the scheme from a file identified by the given path.  
[ReadFromStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.ReadFromStream.html) | Reads the scheme from the given text reader.  
[ReadFromString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.ReadFromString.html) | Reads the scheme from the given string.  
[SetBuildConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.SetBuildConfiguration.html) | Sets the build configuration to be used for running.  
[SetDebugExecutable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.SetDebugExecutable.html) | Sets the **Debug executable** toggle in the scheme.  
[SetFrameCaptureModeOnRun](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.SetFrameCaptureModeOnRun.html) | Sets whether frame capture should be enabled.  
[SetMetalValidationOnRun](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.SetMetalValidationOnRun.html) | Sets the **Metal API Validation** option in the scheme.  
[WriteToFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.WriteToFile.html) | Writes the scheme contents to the specified file.  
[WriteToStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.WriteToStream.html) | Writes the scheme contents to the specified text writer.  
[WriteToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Xcode.XcScheme.WriteToString.html) | Writes the contents of the scheme to a string.  
* * *
