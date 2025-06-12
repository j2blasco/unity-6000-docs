* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Pack.html

#  [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html).Pack
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html "Go to PackageManager Component in the Manual")
## Declaration
public static [PackageManager.Requests.PackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.PackRequest.html) Pack(string packageFolder, string targetFolder); 
### Parameters
Parameter | Description  
---|---  
packageFolder | Folder containing the package. `ArgumentException` is thrown if `packageFolder` is `null` or empty.  
targetFolder | Folder where the Package Manager will write the GZip tarball file. The Package Manager will create this folder if it does not already exist. `ArgumentException` is thrown if `targetFolder` is `null` or empty.  
### Returns
**PackRequest** A [PackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.PackRequest.html) instance, which you can use to get the [PackOperationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackOperationResult.html) representing the path of the generated tarball from the `PackRequest.Result` property. 
### Description
Creates a GZip tarball file from a package folder. The format and content of the file is the same as if the package was published to a package registry.
`Pack()` is an asynchronous operation. Before the operation is complete, you can use the `PackRequest` instance to monitor the asynchronous operation.  
  
**Note:** Make sure any other Client operations have completed before calling this method. For more information, see the note on the [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class reference page.
* * *
