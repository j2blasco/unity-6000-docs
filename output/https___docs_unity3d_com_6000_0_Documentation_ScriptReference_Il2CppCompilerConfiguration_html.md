* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.html

# Il2CppCompilerConfiguration
enumeration
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
C++ compiler configuration used when compiling IL2CPP generated code.
### Properties
Property | Description  
---|---  
[Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.Debug.html) | Debug configuration turns off all optimizations, which makes the code quicker to build but slower to run.  
[Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.Release.html) | Release configuration enables optimizations, so the compiled code runs faster and the binary size is smaller but it takes longer to compile.  
[Master](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.Master.html) | Master configuration enables all possible optimizations, squeezing every bit of performance possible. For instance, on platforms that use the MSVC++ compiler, this option enables link-time code generation. Compiling code using this configuration can take significantly longer than it does using the Release configuration. Unity recommends building the shipping version of your game using the Master configuration if the increase in build time is acceptable.  
* * *
