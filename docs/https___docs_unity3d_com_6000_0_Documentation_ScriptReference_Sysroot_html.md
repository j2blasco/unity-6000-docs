* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.html

# Sysroot
class in UnityEditor
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
Base class for implementing sysroots and toolchains for IL2CPP
### Properties
Property | Description  
---|---  
[HostArch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.HostArch.html) | Returns name of the host architecture  
[HostPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.HostPlatform.html) | Returns name of the host platform  
[Name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.Name.html) | Returns name of the sysroot  
[TargetArch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.TargetArch.html) | Returns name of the target architecture  
[TargetPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.TargetPlatform.html) | Returns name of the target platform  
### Public Methods
Method | Description  
---|---  
[GetIl2CppAdditionalDefines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppAdditionalDefines.html) | Returns an array of additional defines.  
[GetIl2CppAdditionalIncludeDirectories](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppAdditionalIncludeDirectories.html) | Returns an array of additional include directories.  
[GetIl2CppAdditionalLibraries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppAdditionalLibraries.html) | Returns an array of additional static libraries.  
[GetIl2CppAdditionalLinkDirectories](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppAdditionalLinkDirectories.html) | Returns an array of additional link directories.  
[GetIl2CppArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppArguments.html) | Returns the next Il2Cpp argument on each call  
[GetIl2CppCompilerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppCompilerFlags.html) | Returns compiler flags string to pass to Il2Cpp  
[GetIl2CppLinkerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppLinkerFlags.html) | Returns linker flags string to pass to Il2Cpp  
[GetIl2CppLinkerFlagsFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetIl2CppLinkerFlagsFile.html) | Returns linker flags file string to pass to Il2Cpp.  
[GetSysrootPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetSysrootPath.html) | Returns path to sysroot  
[GetToolchainPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.GetToolchainPath.html) | Returns path to toolchain  
[Initialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.Initialize.html) | Initializes sysroot  
* * *
