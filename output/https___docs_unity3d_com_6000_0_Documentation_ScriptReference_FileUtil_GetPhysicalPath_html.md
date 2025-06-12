* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.GetPhysicalPath.html

#  [FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html).GetPhysicalPath
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
public static string GetPhysicalPath(string path); 
### Parameters
Parameter | Description  
---|---  
path | Logical path.  
### Returns
**string** Physical path. 
### Description
Converts a logical path to a physical path.
Logical paths in Unity are virtual paths which point to real (or "physical") file and directory paths on disk. They're designed to be shorter and simpler, making them easier to work with than the real file paths. For example in Unity you might see a logical path such as:  
  
**Packages/MyPackage/MyFile.txt**  
  
Which points to a physical file at:  
  
**C:/Users/SomeUser/MyProject/Library/PackageCache/MyPackage@fingerprint/MyFile.txt**  
  
When working inside Unity, these mappings occur automatically, so in most situations you do not need to call these methods to convert from logical to physical paths. However in certain situations if you are working with external tools that are unaware of Unity's logical paths, you may need to use these methods to provide the mapping between logical and physical paths.  
  
Additional resources: [FileUtil.GetLogicalPath]
* * *
