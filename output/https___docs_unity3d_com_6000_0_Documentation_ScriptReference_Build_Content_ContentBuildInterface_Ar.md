* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.ArchiveAndCompress.html

#  [ContentBuildInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.html).ArchiveAndCompress
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
public static uint ArchiveAndCompress(ResourceFile[] resourceFiles, string outputBundlePath, [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) compression); 
## Declaration
public static uint ArchiveAndCompress(ResourceFile[] resourceFiles, string outputBundlePath, [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) compression, bool stripUnityVersion); 
### Parameters
Parameter | Description  
---|---  
resourceFiles |  Array of [ResourceFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ResourceFile.html) structs pointing to the files that should be copied into the Archive.   
outputBundlePath |  File path of the output Archive file.   
compression |  Type of compression to apply to the content of the Archive.   
stripUnityVersion |  By default the Archive file will record the version of the Unity Editor that created the Archive. When true is passed for this parameter the version will not be recorded in the Archive header. This can be useful when rebuilding AssetBundles after a minor upgrade of the Unity Editor, to make sure otherwise identical AssetBundles generate the exact same full-file content. Note: The CRC and hash values calculated by Unity for AssetBundles ignore the Archive Header. So it is not necessary to strip the Unity Version in the Archive Header when using those for integrity and version tracking.   
### Description
Create a Unity archive file, containing the content of one or more resource files.
Generate a Unity Archive file. This low level API is exposed primarily for use by the **Scriptable Build Pipeline** package. For example, when building AssetBundles using [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) it is not necessary to call this API because the AssetBundle Archive files are created automatically.  
  
Additional resources: [ArchiveFileInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInterface.html). 
* * *
